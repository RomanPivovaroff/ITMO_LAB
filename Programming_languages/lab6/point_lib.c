#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct Point {
   int x;
   int y;
} Point;


int* process_point(Point* points, int size)  {
    int* res = calloc(size, sizeof(int));
    for (int i = 0; i < size; i++) {
        Point p = (points[i]);
        int dist = 0;
        if ((p.y > 0 & p.x > 0) | (p.y < 0 & p.x < 0)) {
            dist = abs(p.x - p.y);
        }
        else {dist = abs(p.x) + abs(p.y) + 1;};
        res[i] = dist;
    }
    //free(points);
    return res;
}

void free_res(Point* res) {free(res);}