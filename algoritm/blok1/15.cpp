#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int N, M, t1, t2, pos;
  cin >> N >> M;
  vector<vector<int>> graph(N);
  vector<int> visited(N, 0);
  for (int i = 0; i < M; i++) {
    cin >> t1 >> t2;
    graph[t1 - 1].push_back(t2 - 1);
    graph[t2 - 1].push_back(t1 - 1);
  }
  bool flag = true;
  for (int i = 0; i < N; i++) {
    if (visited[i] == 0) {
      queue<int> q;
      q.push(i);
      visited[i] = 1;
      while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int to : graph[v]) {
          if (visited[to] == 0) {
            visited[to] = 3 - visited[v];
            q.push(to);
          } else if (visited[to] == visited[v]) {
            flag = false;
            break;
          }
        }
        if (!flag)
          break;
      }
      if (!flag)
        break;
    }
    }
    cout << (flag ? "YES" : "NO") << endl;
    return 0;
  }