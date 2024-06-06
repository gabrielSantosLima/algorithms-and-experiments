#include "dfs.h"
#define WHITE 0
#define BLACK 1
#define GRAY -1

void add_path_recursive_dfs(PATH *path, int *parents, int index)
{
    if (index == -1)
        return;
    add_path_recursive_dfs(path, parents, parents[index]);
    add_path(path, index, 1);
}

void DFS_visit(GRAPH *graph,
               VERTEX *source,
               int target,
               int _time,
               int *colors,
               int *initial_time,
               int *final_time,
               int *parents)
{
    int u = source->index;
    int time = _time + 1;
    initial_time[u] = time;
    colors[u] = GRAY;
    ADJ_VERTEX *aux = source->adjacents;
    while (aux != NULL)
    {
        int v = aux->index;
        if (colors[v] == WHITE)
        {
            parents[v] = u;
            DFS_visit(graph,
                      find_vertex(graph, v),
                      target,
                      time,
                      colors,
                      initial_time,
                      final_time,
                      parents);
        }
        aux = aux->next;
    }
    colors[u] = BLACK;
    time++;
    final_time[u] = time;
}

PATH *DFS(GRAPH *graph, int source, int target)
{
    if (graph == NULL || graph->v == 0)
        return NULL;

    int length = graph->v;
    int time = 0;
    int colors[length];
    int initial_time[length], final_time[length];
    int parents[length];

    for (int i = 0; i < length; i++)
    {
        colors[i] = WHITE;
        parents[i] = -1;
    }

    VERTEX *aux = graph->vertex;
    while (aux != NULL)
    {
        int u = aux->index;
        if (colors[u] == WHITE)
            DFS_visit(graph, aux, target, time, colors, initial_time, final_time, parents);
        aux = aux->next;
    }

    for (int i = 0; i < length; i++)
        printf("[i=%d] COLOR=%d, PARENT=%d\n", i, colors[i], parents[i]);

    PATH *path = create_path();
    add_path_recursive_dfs(path, parents, target);
    return path;
}
