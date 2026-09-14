import ctypes
import os
import random

# TODO
# 1. Создать на питоне скрипт, который генерирует файл, содержащий 1000+ пар чисел
# Пример
# 0,1 1,20 —> расстояние между ними
# 1,20 1,20 
# 3,10 3,10
# 1,0 1,0
# 2. Читаем файл и записываем в массив(ы)
# 3. Массив(ы) содержит класс Point
# 4. Передаём массив(ы) в фунцию написанную на C
# 5. Функция на C для каждой пары считаем расстояние и возвращаем массив с результатами
# 6. Результаты выводим из кода питона
# gcc -shared .\point_lib.c -o point_lib.dll — Windows
# gcc -fPIC -shared .\point_lib.c -o point_lib.so — Linux & MacOS


class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


def generate_points(num, filename):
    points = []
    for i in range(num):
        points.append(" ".join((str(random.randint(-10000, 10000)), str(random.randint(-10000, 10000)))))
    f = open(filename, 'w')
    f.write("\n".join(points))
    f.close()


def read_points(filename):
    f = open(filename, 'r')
    points = []
    for line in f.readlines():
        line = line.strip().split(" ")
        points.append(Point(x=int(line[0]), y=int(line[1])))
    f.close()
    return points


if __name__ == "__main__":
    print("Start program")
    filename = "points.txt"
    generate_points(1000, filename)
    points = read_points(filename)
    # --- Загрузка библиотеки ---
    # Определение имени файла библиотеки в зависимости от ОС
    lib_name = "point_lib.dll" if os.name == 'nt' else "point_lib.so"
    lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

    try:
        # Загрузка C-библиотеки
        c_lib = ctypes.CDLL(lib_path)
        print(f"Библиотека успешно загружена: {lib_path}")
    except Exception as e:
        print(f"ОШИБКА: Не удалось загрузить библиотеку '{lib_path}'")
        print(f"Детали ошибки: {e}")
        exit()

    ArrayType = Point * len(points)
    c_array = ArrayType(*points)
    c_lib.process_point.argtypes = [ctypes.POINTER(Point), ctypes.c_int]
    c_lib.process_point.restype = ctypes.POINTER(ctypes.c_int)
    lst = c_lib.process_point(c_array, len(points))
    C_ArrayType = ctypes.c_int * len(points)
    res = list(C_ArrayType.from_address(ctypes.addressof(lst.contents)))
    print(res)

    c_lib.free_res.argtypes = [ctypes.POINTER(ctypes.c_int)]
    c_lib.free_res.restype = None
    c_lib.free_res(lst)
