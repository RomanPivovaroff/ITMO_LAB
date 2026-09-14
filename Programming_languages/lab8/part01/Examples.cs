using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace part01
{
    public static class Examples
    {

        public static Func<int, int, int> Division()
        {
            // 1. Создаем "Метод-призрак" (DynamicMethod)
            // Имя: "FastCalc"
            // Возвращает: double
            // Аргументы: double, double, double
            var dynamicMethod = new DynamicMethod("Division", typeof(int), [typeof(int), typeof(int)]);



            // 2. Получаем ILGenerator — это наш "ассемблер" для .NET
            // IL — Intermediate Language
            ILGenerator il = dynamicMethod.GetILGenerator();

            // Пишем программу на стековой машине:

            // Загружаем аргумент 0 (a) в стек
            il.Emit(OpCodes.Ldarg_0);

            // Загружаем аргумент 1 (c) в стек
            il.Emit(OpCodes.Ldarg_1);

            // Умножаем (result / c) -> результат в стеке
            il.Emit(OpCodes.Div);

            // Возвращаем то, что лежит на вершине стека
            il.Emit(OpCodes.Ret);

            // 3. "Компилируем" это в делегат C#
            return (Func<int, int, int>)dynamicMethod.CreateDelegate(typeof(Func<int, int, int>));
        }

         public static Func<int, int, int> Minus()
        {
            // 1. Создаем "Метод-призрак" (DynamicMethod)
            var dynamicMethod = new DynamicMethod("Minus", typeof(int), [typeof(int), typeof(int)]);



            // 2. Получаем ILGenerator — это наш "ассемблер" для .NET
            // IL — Intermediate Language
            ILGenerator il = dynamicMethod.GetILGenerator();

            // Пишем программу на стековой машине:

            // Загружаем аргумент 0 (a) в стек
            il.Emit(OpCodes.Ldarg_0);

            // Загружаем аргумент 1 (b) в стек
            il.Emit(OpCodes.Ldarg_1);

            // Складываем два верхних числа в стеке (a - b) -> результат падает в стек
            il.Emit(OpCodes.Sub);

            // Возвращаем то, что лежит на вершине стека
            il.Emit(OpCodes.Ret);

            // 3. "Компилируем" это в делегат C#
            return (Func<int, int, int>)dynamicMethod.CreateDelegate(typeof(Func<int, int, int>));
        }
    }
}
