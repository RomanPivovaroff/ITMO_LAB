import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
import os
import subprocess
import shutil
import json
import sys


def force_rmtree(path):
    """shutil.rmtree с обходом read-only файлов на Windows."""
    import stat
    def on_error(func, fpath, exc_info):
        try:
            os.chmod(fpath, stat.S_IWRITE)
            func(fpath)
        except Exception:
            pass
    shutil.rmtree(path, onerror=on_error)

VARIANT    = 880309
BASE_URL   = "https://se.ifmo.ru/courses/software-engineering-basics"
WORK_DIR   = os.path.expanduser("~/lab2")
CACHE_DIR  = os.path.join(WORK_DIR, "cache")
SVN_REPO   = os.path.join(WORK_DIR, "svn_repo")       # голый репозиторий
SVN_WC0    = os.path.join(WORK_DIR, "svn_wc_user0")   # рабочая копия user0
SVN_WC1    = os.path.join(WORK_DIR, "svn_wc_user1")   # рабочая копия user1
GIT_REPO   = os.path.join(WORK_DIR, "git_repo")       # голый репозиторий
GIT_WC0    = os.path.join(WORK_DIR, "git_wc_user0")
GIT_WC1    = os.path.join(WORK_DIR, "git_wc_user1")

USER0_NAME  = "user0"
USER0_EMAIL = "user0@lab2.local"
USER1_NAME  = "user1"
USER1_EMAIL = "user1@lab2.local"

LOG_FILE = os.path.join(WORK_DIR, "commands.log")
_log_fh  = None

def log(msg):
    print(msg)
    if _log_fh:
        _log_fh.write(msg + "\n")
        _log_fh.flush()

def log_cmd(cmd, cwd=None):
    prefix = f"[{cwd}]" if cwd else ""
    log(f"  $ {prefix} {cmd if isinstance(cmd, str) else ' '.join(cmd)}")

def run(cmd, cwd=None, check=True, capture=False, env=None):
    log_cmd(cmd, cwd)
    kwargs = dict(cwd=cwd, check=check)
    if capture:
        kwargs["capture_output"] = True
        kwargs["text"] = True
    if env:
        merged = os.environ.copy()
        merged.update(env)
        kwargs["env"] = merged
    if isinstance(cmd, str):
        kwargs["shell"] = True
    return subprocess.run(cmd, **kwargs)

def run_out(cmd, cwd=None, env=None):
    r = run(cmd, cwd=cwd, capture=True, check=False, env=env)
    return r.stdout.strip()

class PortalClient:
    def __init__(self):
        self._session = requests.Session()
        self._session.verify = False
        self._p_auth  = None

    def init(self):
        log(f"[portal] GET {BASE_URL}")
        r = self._session.get(BASE_URL, timeout=20)
        r.raise_for_status()
        m = re.search(r'p_auth=([^&"\']+)', r.text)
        if not m:
            raise RuntimeError("p_auth not found")
        self._p_auth = m.group(1)
        log(f"[portal] p_auth={self._p_auth}")

    def _params(self, extra):
        p = {"p_p_id": "selab2_WAR_seportlet",
             "p_p_state": "normal", "p_p_mode": "view",
             "p_auth": self._p_auth}
        p.update(extra)
        return p

    def get_branches(self):
        r = self._session.post(BASE_URL,
            params=self._params({"p_p_lifecycle": "1",
                "_selab2_WAR_seportlet_javax.portlet.action": "getBranches"}),
            data={"variant": str(VARIANT)}, timeout=20)
        r.raise_for_status()
        return r.json()

    def download_commit(self, commit_id):
        """
        Скачивает архив коммита, распаковывает в CACHE_DIR/<commit_id>/.
        Возвращает (extract_dir, is_empty):
          - is_empty=True  если zip сломан / пуст — коммит пропускаем,
                           но ветку/мердж всё равно обрабатываем.
          - is_empty=False если всё ок.
        """
        extract_dir = os.path.join(CACHE_DIR, str(commit_id))
        sentinel_empty = os.path.join(CACHE_DIR, f"{commit_id}.empty")

        # Уже в кэше
        if os.path.isdir(extract_dir):
            is_empty = os.path.exists(sentinel_empty)
            return extract_dir, is_empty

        log(f"[portal] download commit {commit_id}")
        r = self._session.post(BASE_URL,
            params=self._params({"p_p_lifecycle": "2",
                "p_p_cacheability": "cacheLevelPage"}),
            data={"variant": str(VARIANT), "commit": str(commit_id)},
            stream=True, timeout=30)
        r.raise_for_status()

        zip_path = os.path.join(CACHE_DIR, f"{commit_id}.zip")
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)

        os.makedirs(extract_dir, exist_ok=True)
        import zipfile
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(extract_dir)
            real_files = [f for f in os.listdir(extract_dir)
                          if os.path.isfile(os.path.join(extract_dir, f))]
            if not real_files:
                log(f"  [warn] commit {commit_id}: zip распакован, но файлов нет — пустой коммит")
                open(sentinel_empty, 'w').close()
                os.remove(zip_path)
                return extract_dir, True
        except (zipfile.BadZipFile, Exception) as e:
            log(f"  [warn] commit {commit_id}: zip сломан ({e}) — пустой коммит, пропускаем")
            open(sentinel_empty, 'w').close()
            os.remove(zip_path)
            return extract_dir, True

        os.remove(zip_path)
        return extract_dir, False


def sync_files(src_dir, dst_dir, tracked_by_vcs="svn", wc=None):
    """
    Синхронизирует файлы из src_dir в dst_dir.
    Добавляет новые, обновляет существующие, удаляет исчезнувшие.
    Возвращает (added, modified, deleted).
    """
    src_files = set()
    for f in os.listdir(src_dir):
        if os.path.isfile(os.path.join(src_dir, f)):
            src_files.add(f)

    dst_files = set()
    for f in os.listdir(dst_dir):
        if os.path.isfile(os.path.join(dst_dir, f)) and not f.startswith("."):
            dst_files.add(f)

    added    = src_files - dst_files
    deleted  = dst_files - src_files
    modified = set()

    for f in src_files & dst_files:
        with open(os.path.join(src_dir, f), "rb") as fh:
            sc = fh.read()
        with open(os.path.join(dst_dir, f), "rb") as fh:
            dc = fh.read()
        if sc != dc:
            modified.add(f)

    for f in added:
        shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, f))
        if tracked_by_vcs == "svn" and wc:
            run(["svn", "add", f], cwd=wc)

    for f in modified:
        shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, f))

    for f in deleted:
        if tracked_by_vcs == "svn" and wc:
            run(["svn", "delete", f], cwd=wc)
        else:
            os.remove(os.path.join(dst_dir, f))

    return list(added), list(modified), list(deleted)


def build_graph(branches):
    """
    Возвращает список событий в хронологическом порядке (по номеру коммита):
    [
      {"commit": N, "branch": "br_X", "user": U,
       "type": "commit"|"branch_start"|"merge"},
      ...
    ]
    """
    commit_branch = {}
    for br_name, br in branches.items():
        for c in br["commits"]:
            commit_branch[c] = br_name

    all_commits = sorted(commit_branch.keys())

    events = []
    for c in all_commits:
        br_name = commit_branch[c]
        br = branches[br_name]
        user = br["user"]
        events.append({
            "commit": c,
            "branch": br_name,
            "user": user,
        })

    return events


def svn_setup():
    log("\n=== SVN: инициализация репозитория ===")
    if os.path.exists(SVN_REPO):
        force_rmtree(SVN_REPO)
    if os.path.exists(SVN_WC0):
        force_rmtree(SVN_WC0)
    if os.path.exists(SVN_WC1):
        force_rmtree(SVN_WC1)

    run(["svnadmin", "create", SVN_REPO])
    svn_path = SVN_REPO.replace("\\", "/").replace("\\", "/")
    import pathlib
    svn_path = pathlib.Path(SVN_REPO).as_posix()
    if svn_path[1] == ":":  # Windows absolute path like C:/...
        repo_url = f"file:///{svn_path}"
    else:
        repo_url = f"file://{svn_path}"

    run(["svn", "mkdir", "--parents", "-m", "init structure",
         f"{repo_url}/br_0", f"{repo_url}/br_1", f"{repo_url}/br_2"])

    os.makedirs(SVN_WC0, exist_ok=True)
    os.makedirs(SVN_WC1, exist_ok=True)

    run(["svn", "checkout", f"{repo_url}/br_0", SVN_WC0])

    return repo_url


def svn_user_env(user):
    """Возвращает env с именем пользователя для svn (через config)."""
    if user == 0:
        return USER0_NAME
    return USER1_NAME


def svn_commit(wc, msg, username):
    """Делает svn commit от имени username."""
    run(["svn", "commit", "-m", msg, "--username", username], cwd=wc)
    r = run_out(["svn", "info", "--show-item", "last-changed-revision"], cwd=wc)
    return r


def svn_do_branch(repo_url, from_branch, to_branch, from_rev=None):
    """Создаёт ветку в SVN через svn copy."""
    src = f"{repo_url}/{from_branch}"
    if from_rev:
        src += f"@{from_rev}"
    dst = f"{repo_url}/{to_branch}"
    run(["svn", "copy", "-m", f"branch {to_branch} from {from_branch}", src, dst])


def svn_do_merge(wc, repo_url, from_branch, username):
    """Делает svn merge из from_branch в текущую рабочую копию."""
    src = f"{repo_url}/{from_branch}"
    run(["svn", "merge", "--ignore-ancestry", "-r", "1:HEAD", src], cwd=wc)
    result = run_out(["svn", "status"], cwd=wc)
    if "C" in result:
        log("  [svn] обнаружены конфликты, разрешаем (theirs-full)")
        run(["svn", "resolve", "--accept", "theirs-full", "-R", "."], cwd=wc)
    run(["svn", "commit", "-m", f"merge {from_branch}", "--username", username], cwd=wc)


def git_setup():
    log("\n=== GIT: инициализация репозитория ===")
    if os.path.exists(GIT_REPO):
        force_rmtree(GIT_REPO)
    if os.path.exists(GIT_WC0):
        force_rmtree(GIT_WC0)
    if os.path.exists(GIT_WC1):
        force_rmtree(GIT_WC1)

    run(["git", "init", "--bare", GIT_REPO])

    run(["git", "clone", GIT_REPO, GIT_WC0])
    run(["git", "config", "user.name",  USER0_NAME],  cwd=GIT_WC0)
    run(["git", "config", "user.email", USER0_EMAIL], cwd=GIT_WC0)

    run(["git", "clone", GIT_REPO, GIT_WC1])
    run(["git", "config", "user.name",  USER1_NAME],  cwd=GIT_WC1)
    run(["git", "config", "user.email", USER1_EMAIL], cwd=GIT_WC1)


def git_user_env(user):
    if user == 0:
        return {"GIT_AUTHOR_NAME": USER0_NAME, "GIT_AUTHOR_EMAIL": USER0_EMAIL,
                "GIT_COMMITTER_NAME": USER0_NAME, "GIT_COMMITTER_EMAIL": USER0_EMAIL}
    return {"GIT_AUTHOR_NAME": USER1_NAME, "GIT_AUTHOR_EMAIL": USER1_EMAIL,
            "GIT_COMMITTER_NAME": USER1_NAME, "GIT_COMMITTER_EMAIL": USER1_EMAIL}


def git_commit(wc, msg, user):
    env = git_user_env(user)
    run(["git", "add", "-A"], cwd=wc)
    status = run_out(["git", "status", "--porcelain"], cwd=wc)
    if not status:
        log("  [git] нечего коммитить, пропускаем")
        return None
    run(["git", "commit", "-m", msg], cwd=wc, env=env)
    sha = run_out(["git", "rev-parse", "--short", "HEAD"], cwd=wc)
    return sha


def git_push(wc, branch):
    run(["git", "push", "-u", "origin", branch], cwd=wc)


def git_pull(wc):
    run(["git", "pull", "--rebase"], cwd=wc, check=False)


def git_checkout_branch(wc, branch, create=False, from_branch=None):
    if create:
        if from_branch:
            run(["git", "checkout", "-b", branch, from_branch], cwd=wc)
        else:
            run(["git", "checkout", "-b", branch], cwd=wc)
    else:
        run(["git", "fetch", "origin"], cwd=wc)
        branches_local = run_out(["git", "branch"], cwd=wc)
        if branch in branches_local:
            run(["git", "checkout", branch], cwd=wc)
        else:
            run(["git", "checkout", "-b", branch, f"origin/{branch}"], cwd=wc)


def git_merge(wc, from_branch, user, commit_msg=None):
    env = git_user_env(user)
    msg = commit_msg or f"merge {from_branch}"
    result = run(["git", "merge", "--no-ff", from_branch, "-m", msg],
                 cwd=wc, check=False, env=env)
    if result.returncode != 0:
        log("  [git] конфликты при merge, принимаем theirs")
        run(["git", "checkout", "--theirs", "."], cwd=wc)
        run(["git", "add", "-A"], cwd=wc)
        run(["git", "commit", "-m", msg], cwd=wc, env=env)


def main():
    global _log_fh
    os.makedirs(WORK_DIR, exist_ok=True)
    _log_fh = open(LOG_FILE, "w", encoding="utf-8")
    log(f"Вариант: {VARIANT}")
    log(f"Рабочий каталог: {WORK_DIR}\n")

    portal = PortalClient()
    portal.init()

    log("\n=== Получение графа веток ===")
    branches = portal.get_branches()
    log(json.dumps(branches, indent=2, ensure_ascii=False))

    events = build_graph(branches)
    log(f"\nВсего событий: {len(events)}")

    log("\n=== Скачивание архивов коммитов ===")
    all_commit_ids = sorted(set(e["commit"] for e in events))
    for cid in all_commit_ids:
        portal.download_commit(cid)
    log(f"Скачано: {len(all_commit_ids)} коммитов")

    repo_url = svn_setup()

    git_setup()

    br_info = branches  

    log("SVN WORKFLOW")

    run(["svn", "checkout", f"{repo_url}/br_0", SVN_WC0])

    os.makedirs(SVN_WC1, exist_ok=True)

    svn_wc_current_branch = {0: "br_0", 1: None}
    svn_wc_path           = {0: SVN_WC0, 1: SVN_WC1}

    def svn_switch_user1(branch):
        """Переключает/создаёт рабочую копию user1 на нужную ветку."""
        if svn_wc_current_branch[1] is None:
            run(["svn", "checkout", f"{repo_url}/{branch}", SVN_WC1])
        else:
            run(["svn", "switch", "--ignore-ancestry", f"{repo_url}/{branch}"], cwd=SVN_WC1)
        svn_wc_current_branch[1] = branch

    for ev in events:
        cid    = ev["commit"]
        branch = ev["branch"]
        user   = ev["user"]
        wc     = svn_wc_path[user]
        uname  = svn_user_env(user)

        log(f"\n[SVN] commit={cid} branch={branch} user={user}")

        if branch == "br_2" and cid == br_info["br_2"]["commits"][0]:
            log(f"  → создаём ветку br_2 от br_0 (после коммита {br_info['br_2']['parent']['commit']})")
            svn_do_branch(repo_url, "br_0", "br_2")
            svn_switch_user1("br_2")

        if branch == "br_1" and cid == br_info["br_1"]["commits"][0]:
            log(f"  → создаём ветку br_1 от br_2 (после коммита {br_info['br_1']['parent']['commit']})")
            svn_do_branch(repo_url, "br_2", "br_1")
            svn_switch_user1("br_1")

        if user == 1 and svn_wc_current_branch.get(1) != branch:
            svn_switch_user1(branch)

        run(["svn", "update", "--username", uname], cwd=wc, check=False)

        src, is_empty = portal.download_commit(cid)
        is_merge_commit = (
            (branch == "br_2" and br_info.get("br_1", {}).get("merge", {}).get("commit") == cid) or
            (branch == "br_0" and br_info.get("br_2", {}).get("merge", {}).get("commit") == cid)
        )
        if is_empty and not is_merge_commit:
            log(f"  [skip] commit {cid} пустой — пропускаем sync+commit, ветку/мердж обрабатываем")
        elif not is_empty:
            sync_files(src, wc, tracked_by_vcs="svn", wc=wc)
            svn_rev = svn_commit(wc, f"commit {cid}", uname)
            log(f"  SVN revision: {svn_rev}")

        if branch == "br_2" and "merge" in br_info["br_1"] and \
                br_info["br_1"]["merge"]["commit"] == cid:
            log(f"  → merge br_1 → br_2 @ commit {cid}")
            svn_switch_user1("br_2")
            run(["svn", "update", "--username", uname], cwd=SVN_WC1, check=False)
            svn_do_merge(SVN_WC1, repo_url, "br_1", uname)

        if branch == "br_0" and "merge" in br_info["br_2"] and \
                br_info["br_2"]["merge"]["commit"] == cid:
            log(f"  → merge br_2 → br_0 @ commit {cid}")
            run(["svn", "update", "--username", uname], cwd=SVN_WC0, check=False)
            svn_do_merge(SVN_WC0, repo_url, "br_2", uname)

    log("\n[SVN] Готово!")
    svn_log = run_out(["svn", "log", f"{repo_url}/br_0", "--limit", "10"])
    log(f"SVN log (последние 10):\n{svn_log}")
    
    log("GIT WORKFLOW")

    git_branches_created = set()
    git_branch_wc = {}

    def git_ensure_branch(wc, branch, user, from_branch=None):
        """Создаёт ветку если не существует, иначе переключается."""
        if branch not in git_branches_created:
            git_checkout_branch(wc, branch, create=True,
                                from_branch=f"origin/{from_branch}" if from_branch else None)
            git_branches_created.add(branch)
        else:
            git_checkout_branch(wc, branch)
        git_branch_wc[branch] = wc

    first_ev = events[0]
    assert first_ev["branch"] == "br_0"

    src, is_empty = portal.download_commit(first_ev["commit"])
    run(["git", "checkout", "-b", "br_0"], cwd=GIT_WC0)
    git_branches_created.add("br_0")
    git_branch_wc["br_0"] = GIT_WC0
    if not is_empty:
        for f in os.listdir(src):
            full = os.path.join(src, f)
            if os.path.isfile(full):
                shutil.copy2(full, os.path.join(GIT_WC0, f))
        sha = git_commit(GIT_WC0, f"commit {first_ev['commit']}", first_ev["user"])
        if sha:
            git_push(GIT_WC0, "br_0")
            log(f"[GIT] commit={first_ev['commit']} branch=br_0 sha={sha}")
        else:
            log(f"[GIT][warn] commit {first_ev['commit']} — нечего коммитить")
    else:
        log(f"[GIT][skip] commit {first_ev['commit']} пустой")

    for ev in events[1:]:
        cid    = ev["commit"]
        branch = ev["branch"]
        user   = ev["user"]
        env    = git_user_env(user)
        uname  = USER0_NAME if user == 0 else USER1_NAME

        log(f"\n[GIT] commit={cid} branch={branch} user={user}")

        wc = GIT_WC0 if user == 0 else GIT_WC1

        if branch not in git_branches_created:
            if branch == "br_2":
                parent_commit = br_info["br_2"]["parent"]["commit"]
                run(["git", "fetch", "origin"], cwd=wc)
                git_ensure_branch(wc, "br_2", user, from_branch="br_0")
                git_push(wc, "br_2")
                run(["git", "fetch", "origin"], cwd=GIT_WC1)
            elif branch == "br_1":
                run(["git", "fetch", "origin"], cwd=wc)
                git_ensure_branch(wc, "br_1", user, from_branch="br_2")
                git_push(wc, "br_1")
                run(["git", "fetch", "origin"], cwd=GIT_WC0)
        else:
            git_checkout_branch(wc, branch)

        merge_br1_into_br2_at = br_info.get("br_1", {}).get("merge", {}).get("commit")
        merge_br2_into_br0_at = br_info.get("br_2", {}).get("merge", {}).get("commit")

        run(["git", "pull", "--rebase", "origin", branch], cwd=wc, check=False)

        src, is_empty = portal.download_commit(cid)
        merge_br1_into_br2_at = br_info.get("br_1", {}).get("merge", {}).get("commit")
        merge_br2_into_br0_at = br_info.get("br_2", {}).get("merge", {}).get("commit")
        is_merge_commit = (cid == merge_br1_into_br2_at or cid == merge_br2_into_br0_at)
        if is_empty and not is_merge_commit:
            log(f"  [skip] commit {cid} пустой — пропускаем sync+commit, ветку/мердж обрабатываем")
        elif not is_empty:
            added, modified, deleted = sync_files(src, wc, tracked_by_vcs="git")
            for f in deleted:
                if os.path.exists(os.path.join(wc, f)):
                    run(["git", "rm", "-f", f], cwd=wc, check=False)
            sha = git_commit(wc, f"commit {cid}", user)
            git_push(wc, branch)
            log(f"  sha={sha}")

        if branch == "br_2" and cid == merge_br1_into_br2_at:
            log(f"  → git merge br_1 → br_2")
            run(["git", "fetch", "origin"], cwd=wc)
            git_merge(wc, "origin/br_1", user, f"merge br_1 into br_2 @ {cid}")
            git_push(wc, "br_2")

        if branch == "br_0" and cid == merge_br2_into_br0_at:
            log(f"  → git merge br_2 → br_0")
            wc0 = GIT_WC0
            git_checkout_branch(wc0, "br_0")
            run(["git", "pull", "--rebase", "origin", "br_0"], cwd=wc0, check=False)
            run(["git", "fetch", "origin"], cwd=wc0)
            git_merge(wc0, "origin/br_2", user, f"merge br_2 into br_0 @ {cid}")
            git_push(wc0, "br_0")

    log("\n[GIT] Готово!")
    git_log = run_out(["git", "log", "--oneline", "--graph", "--all", "--decorate",
                        "--max-count=20"], cwd=GIT_WC0)
    log(f"GIT log:\n{git_log}")

    log("КОМАНДЫ СОХРАНЕНЫ В: " + LOG_FILE)
    _log_fh.close()


if __name__ == "__main__":
    main()