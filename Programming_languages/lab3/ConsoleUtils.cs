// Rider (Jetbrains)
// Visual Studio Comunity (.NET)
// Visual Studio Code

// C code => gcc (compile) => binary (asm)
// C# code => dotnet (compile) => binary (IL code — Intermediate Language) => CLR (.net runtime)
// C# code => dotnet (AOT (ahead of time) compile) => binary (asm)
// dotnet new console  => для создания проекта
// dotnet run => компиляция + запуск проекта

// OOP






// heroes[] = 



public static class ConsoleUtils
{
    public static void Log(string data, ConsoleColor color)
    {
        Console.ForegroundColor = color;
        Console.WriteLine(data);
        Console.ResetColor();
    }
}

// TODO:
// 1. Создать класс Wizard (наследник Hero)
// 2. Реализовать SpecialAbility (на выбор. Например, игнорировать Defense)
// 3. Написать AutoBattler (класс или метод)
// 4. Бесконечная битва пока у кого-то не останется HP
//    (можно между двумя, можно между некоторы количество Hero)
// 5. Случайным образом выбирается кто ходит
// 6. SpecialAbility каджый 3 ход.
// 7. Вывод в консоль хода битвы (цветным)
// 8. Также вывод в файл.
// 