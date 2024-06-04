#ifndef PATH_FILE
#define PATH_FILE
#include <stdio.h>
#include <stdlib.h>

typedef struct PATH
{
    int index;
    int weight;
    struct PATH *next;
} PATH;

int length_path(PATH *path);
PATH *create_path();
void add_path(PATH *path, int index, int weight);
void print_path(PATH *path);

#endif