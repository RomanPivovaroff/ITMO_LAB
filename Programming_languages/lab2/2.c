#include <stdio.h>
#include <stdlib.h>
 
typedef struct {
  int x;
  int y;
} Point;
 
typedef enum {
    Circle,
    Square,
    Triangle
} ShapeType;
 
typedef struct {
    Point p;
    char* name;
    ShapeType type;
} Shape;
 
typedef struct {
    Shape* shapes;
    int size;
} Container;
 
Container* create_container(){
    Container* ct = malloc(sizeof(Container));
    if (ct != NULL) {
        ct->size = 0;
        ct->shapes = calloc(0, sizeof(Shape));
    }
    return ct;
}
 
int add_new_shape(Container*, char*, Point, ShapeType);
int remove_shape_by_index(Container*, int);
void print(Container*);
 
int main() {
    Container* container = create_container();
    Point* p = malloc(sizeof(Point));
    p->x = 1;
    p->y = 2;
    ShapeType type = Square;
    printf("code_add_new_shape = %d\n", add_new_shape(container, "Igor", *p, type));
    free(p); p = NULL;
    printf("coderemove_shape_by_index = %d\n", remove_shape_by_index(container, 0));
    print(container);
    if (container != NULL) {
        free(container->shapes);
        free(container);
    }
} 

int add_new_shape(Container* ct, char* name, Point p, ShapeType type) {
    if (ct == NULL) {
        return -1;
    }
    Shape* sp = malloc(sizeof(Shape));
    sp->name = name;
    sp->p = p;
    sp->type = type;
    if (ct->shapes == NULL) {
        free(sp);
        return -1;
    }
    Shape* temp = (Shape*) realloc(ct->shapes, ++ct->size * sizeof(Shape));
    if (temp == NULL) {
        free(sp);
        return -1;
    }
    temp[ct->size - 1] = *sp;
    ct->shapes = temp;
    free(sp); sp = NULL;
    return 0;
};

int remove_shape_by_index(Container* ct, int ind) {
    if (ct == NULL) {
        return -1;
    }
    if (ct->shapes == NULL) {
        return -1;
    }
    for (int i = ind + 1; i < ct->size; i++) {
        ct->shapes[i - 1] = ct->shapes[i]; 
    }
    if (ct->size == 1) {
        free(ct->shapes);
        ct->shapes = NULL;
        return 0;
    }
    Shape* temp = realloc(ct->shapes, --ct->size);
    if (temp == NULL) {
        return -1;
    }
    ct->shapes = temp;
    return 0;
};

void print(Container*ct) {
    if (ct == NULL) {
        printf("NULL");
    }
    for (int i = 0; i < ct->size; i++) {
        printf("Shapes[%d] = %d\n", i, ct->shapes[i]);
        printf("name = %s, type = %d, Point.x = %d, Point.y = %d\n", ct->shapes[i].name, ct->shapes[i].type, ct->shapes[i].p.x, ct->shapes[i].p.y);
    }
}

