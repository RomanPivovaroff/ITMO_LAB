// Rider (Jetbrains)
// Visual Studio Comunity (.NET)
// Visual Studio Code

// C code => gcc (compile) => binary (asm)
// C# code => dotnet (compile) => binary (IL code — Intermediate Language) => CLR (.net runtime)
// C# code => dotnet (AOT (ahead of time) compile) => binary (asm)
// dotnet new console  => для создания проекта
// dotnet run => компиляция + запуск проекта

Hero hero = new Warrior("Warrior", 10, 40, 5, new HealingPotion(20));
//Console.WriteLine(hero);
// hero.TakeDamage(10);
// hero.SpecialAbility(hero);
// Console.WriteLine(hero);
// hero.Method();
Hero[] heroes = new Hero[] {
hero,
new Wizard("Wizard", 15, 40, 0, new HealingPotion(10)),
new Wizard("Bolwanchik", 1, 100, 0)
};
AutoBattler.battle(heroes);
// heroes[] = 

// Вывод в файл
// File.AppendAllText(Path.Combine(Environment.CurrentDirectory, "log.txt"), "text in file");


// TODO:
// 1. Создать класс Wizard (наследник Hero)
// 2. Реализовать SpecialAbility (на выбор. Например, игнорировать Defense)
// 3. Написать AutoBattler (класс или метод)
// 4. Бесконечная битва пока у кого-то не останется HP
//    (можно между двумя, можно между некоторы количество Hero)
// 5. Случайным образом выбирается кто ходит
// 6. SpecialAbility каджый 3 ход. (либо каждый третий ход в общем, либо персонажа)
// 7. Вывод в консоль хода битвы (цветным)
// 8. Также вывод в файл.
// 9*. Реализация и использование IArtifact (каждый 5 ход)
// 10*. Консольный звук.