using System.Diagnostics;
using Microsoft.VisualBasic.FileIO;

static Task NewMethod(String name)
{
    var task = Task.Run(() => {
        var parser = new TextFieldParser(name);
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(" ", ",");
        parser.HasFieldsEnclosedInQuotes = true;
        int count = 0;
        while (!parser.EndOfData)
        {
            string[] fields = parser.ReadFields();
            count += fields.Length;
        }
        Console.WriteLine(count);
        Console.WriteLine(Environment.CurrentManagedThreadId);
        });
    return task;
}


var st = new Stopwatch();
st.Start();

Console.WriteLine(Environment.CurrentManagedThreadId);
String[] names = ["logx5.txt", "1.txt", "2.txt", "logx5.txt", "3.txt", "log.txt", "logx5.txt"];
List<Task> tasks = new List<Task>();
foreach (var name in names)
{
    tasks.Add(NewMethod(name));
}
await Task.WhenAll(tasks);
Console.WriteLine(st.Elapsed);
 
// TODO
// Написать программу, которая принимает названия текстовых файлов (можно брать с консоли, аргументов, хардкодить)
// Создаёт на каждый файл таску, которая читает файл и считает количество слов в файле
// Как только таска заканчивается, то нужно вывести сколько слов в файле
// Замерить время выполнение программы