#include "path.h"

int length_path(PATH *path)
{
    if (path == NULL)
        return 0;
    int count = 0;
    path = path->next;
    while (path != NULL)
    {

        count++;
        path = path->next;
    }
    return count;
}

PATH *create_path()
{
    PATH *path = (PATH *)malloc(sizeof(PATH));
    path->index = -1;
    path->weight = -1;
    path->next = NULL;
    return path;
}

void add_path(PATH *path, int index, int weight)
{
    if (path == NULL)
        return;
    PATH *aux = path;
    while (aux->next != NULL)
        aux = aux->next;
    aux->next = create_path(index, weight);
    aux->index = index;
    aux->weight = weight;
}

void print_path(PATH *path)
{
    while (path != NULL)
    {
        if (path->next != NULL)
        {
            printf("%d (w=%d) -> ", path->index, path->weight);
            path = path->next;
        }
        else
            path = NULL;
    }
}
