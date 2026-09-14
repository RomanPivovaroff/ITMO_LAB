#include <stdio.h>
#include<stdlib.h>

void foo(int a) {
    // a - копия
    a = 10;
}

void bar(int* a) {
    // a - копия адреса
    printf("\nint*a = %d", a);
    *a = 10;
    printf("\n*a = %d", *a);
}

int main() {
    int a = 1;
    foo(a);
    printf("a = %d", a);

    // int* указатель на тип инт
    // *a разименование указателя(обратная операция, берет по адресу значение)
    // &a - взятие адрема
    bar(&a);

    int* b;
    void* untyped = b;
    char* c;
    untyped = c;
    b = untyped; // в инт(4 байта) записываем начало чара(1 байт)
    // b = c; выведет ощибку

    // 1. отсутсвие типизации при работы с void*
    // 2. отсутсвии арифметики указателей

    int * arr = malloc(10 * sizeof(int));
    if (arr == NULL) {
        return -1;
    }
    arr[0] = 1;
    arr[1] = 2;
    printf("arr[0] = %d\n", arr[0]);
    printf("arr[1] = %d\n", arr[1]);

    int s_arr[10];
    // arr - указатель на 1 элемент массива
    printf("arr = %d\n", *arr);
    printf("arr + 1 = %d\n", *(arr +1));
    // arr[n] == *(arr + n)
    // *(n + arr) == n[arr]
    for (int i = 0; i < 10; i++) {
        printf("arr[%d] = %d", i, arr[i]);
    }
    // realloc при успехе сам сделает free(arr)
    int * temp = realloc(arr, 5);
    if (temp != NULL) {
        arr = temp;
    }
    free(arr);
    arr = NULL;

    printf(-20 % 2);
    // malloc(size) -берет случайный участок памяти и возврашает указатель на начало
    // calloc(size) - дополнительно инициализирует элементы
    // realloc(arr, new_size) - уменьшает или увеличивает размер выделенной памяти(выделяет новых блок памяти и копирует)
}