using System.Runtime.InteropServices;
using Microsoft.VisualBasic.FileIO;

[DllImport("point_lib.dll", CallingConvention = CallingConvention.Cdecl)]
static extern void process([In] Point[] p, [Out] Point[] result, [In] int len, [In] MyFunc f);
[DllImport("point_lib.dll", CallingConvention = CallingConvention.Cdecl)]
static extern int find_res_size([In] Point[] p, [In] int len, [In] MyFunc f);

static Point[] NewMethod(String name)
{
    var parser = new TextFieldParser(name);
    parser.TextFieldType = FieldType.Delimited;
    parser.SetDelimiters(" ");
    parser.HasFieldsEnclosedInQuotes = true;
    List<Point> list_points = new List<Point>();
    while (!parser.EndOfData)
    {
        string[] fields = parser.ReadFields();
        var p = new Point
        {
            x = int.Parse(fields[0]),
            y = int.Parse(fields[1])
        };
        list_points.Add(p);
    }
    Point[] arr_points = new Point[list_points.Count];
    list_points.CopyTo(arr_points);
    return arr_points;
}
 

Point[] points = NewMethod("points.txt");
Console.WriteLine($" points.Length {points.Length}");

var res_size = find_res_size(points, points.Length, x => x.x > 0 && x.y > 0);
Point[] res = new Point[res_size];
process(points, res, points.Length, x => x.x > 0 && x.y > 0);
Console.WriteLine($" res.Length x > 0 y > 0 {res.Length}");

res_size = find_res_size(points, points.Length, x => x.x > 0 && x.y < 0);
res = new Point[res_size];
process(points, res, points.Length, x => x.x > 0 && x.y < 0);
Console.WriteLine($" res.Length x > 0 y < 0 {res.Length}");

res_size = find_res_size(points, points.Length, x => x.x < 0 && x.y > 0);
res = new Point[res_size];
process(points, res, points.Length, x => x.x < 0 && x.y > 0);
Console.WriteLine($" res.Length x < 0 y > 0 {res.Length}");

res_size = find_res_size(points, points.Length, x => x.x < 0 && x.y < 0);
res = new Point[res_size];
process(points, res, points.Length, x => x.x < 0 && x.y < 0);
Console.WriteLine($" res.Length x < 0 y < 0 {res.Length}");
 
// TODO:
// 1. Возьмём файл с 1000+ точек (x, y) (можно взять с прошлого занятия)
// 2. Прочитать в С# файл с точками
// 3. Написать функцию filter на C,
// которая принимает массив точек, 
// количество точек,
// функцию фильтрации(Point -> bool),
// выходный аргумент отфильтрованный массив точек
// 4. Вызываем функцию filter из C# для точек с функциями фильтрациями, 
// чтобы разделить их на коориднатные четверти
// 5. Вывести для каждой четверти список точек
 
// var p = new Point
// {
//     x = 42,
//     y = 42
// };
// Console.WriteLine($" p.x {p.x} p.y {p.y}");
// Console.WriteLine($" p.x {p.x} p.y {p.y}");
// process(arr_points, arr_points.Length);
// foreach (var item in arr_points)
// {
//     Console.WriteLine($" p.x {item.x} p.y {item.y}");
// }
 
// MyFunc f;
// f = x => x * 2;
// f = bar;

 
// int bar(int a)
// {
//     return a;
// }
// [StructLayout(LayoutKind.Sequential)]
struct Point
{
    public int x;
    public int y;
}
 
 
 
delegate bool MyFunc(Point a);
 
// /*
// typedef int (*MyFunc)(int);
 
// int foo(int a, MyFunc f) {
//     //qsort()
//     return f(a);
// }
// */
