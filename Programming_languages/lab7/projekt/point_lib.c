#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Point {
   int x;
   int y;
} Point;


void process(Point* points, Point* res, int size, bool (*MyFunc) (Point))  {
    int res_size = 0;
    for (int i = 0; i < size; i++) {
        Point p = (points[i]);
        if (MyFunc(p)) {
            res[res_size] = p;
            res_size += 1;
        }
    }
}

int find_res_size(Point* points, int size, bool (*MyFunc) (Point))  {
    int res_size = 0;
    for (int i = 0; i < size; i++) {
        Point p = (points[i]);
        if (MyFunc(p)) {
            res_size += 1;
        }
    }
    return res_size;
}