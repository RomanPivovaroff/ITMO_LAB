public static class AutoBattler
{
    public static void battle(Hero[] heroes)
    {
        var random = new Random();
        int[] motion_massive = new int[heroes.Length];
        var file_output = "";
        var str = "";
        while (true)
        {
            int active_hero_num = (int)random.NextInt64(heroes.Length);
            int defence_hero_num = (int)random.NextInt64(heroes.Length);
            while (active_hero_num == defence_hero_num)
            {
                defence_hero_num = (int)random.NextInt64(heroes.Length);
            }
            int hp_before_act = heroes[active_hero_num].HP;
            int hp_before_def = heroes[defence_hero_num].HP;
            if (motion_massive[active_hero_num] % 5 == 4)
            {
                Console.Beep(500, 500);
                heroes[active_hero_num].UseArtifact(heroes[defence_hero_num]);
                str = $"{heroes[active_hero_num]} использует артефакт {heroes[active_hero_num].Artifact}";
                file_output += str + "\n";
                ConsoleUtils.Log(str, ConsoleColor.Cyan);
            }
            if (motion_massive[active_hero_num] % 3 == 2)
            {
                Console.Beep(500, 500);
                heroes[active_hero_num].SpecialAbility(heroes[defence_hero_num]);
                str = $"{heroes[active_hero_num]} использует особую способность";
                file_output += str + "\n";
                ConsoleUtils.Log(str, ConsoleColor.DarkMagenta);
            }
            else
            {
                heroes[defence_hero_num].TakeDamage(heroes[active_hero_num].Attack);
            }
            int hp_after_act = heroes[active_hero_num].HP;
            int hp_after_def = heroes[defence_hero_num].HP;
            str = $"{heroes[defence_hero_num]} теряет {hp_before_def - hp_after_def} HP";
            file_output += str + "\n";
            ConsoleUtils.Log(str, ConsoleColor.Red);
            str = $"{heroes[active_hero_num]} восстанваливет {hp_after_act - hp_before_act} HP";
            file_output += str + Environment.NewLine;
            ConsoleUtils.Log(str, ConsoleColor.Green);
            if (hp_after_def <= 0)
            {
                str = $"{heroes[defence_hero_num]} умирает";
                file_output += str + "\n";
                ConsoleUtils.Log($"{heroes[defence_hero_num]} умирает", ConsoleColor.DarkRed);
                break;
            }
            motion_massive[active_hero_num] += 1;
        }
    File.AppendAllText(Path.Combine(Environment.CurrentDirectory, "log.txt"), file_output);
    }
}