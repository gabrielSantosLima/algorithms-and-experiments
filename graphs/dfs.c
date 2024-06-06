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

int time_dfs = 0;

void DFS_visit(GRAPH *graph,
               VERTEX *source,
               int *colors,
               int *s_time,
               int *f_time,
               int *parents)
{
    int u = source->index;
    time_dfs++;
    s_time[u] = time_dfs;
    colors[u] = GRAY;
    ADJ_VERTEX *aux = source->adjacents;
    printf("> u=%d\n", u);
    while (aux != NULL)
    {
        int v = aux->index;
        if (colors[v] == WHITE)
        {
            printf("> v=%d\n", v);
            parents[v] = u;
            DFS_visit(graph,
                      find_vertex(graph, v),
                      colors,
                      s_time,
                      f_time,
                      parents);
        }
        aux = aux->next;
    }
    colors[u] = BLACK;
    time_dfs++;
    f_time[u] = time_dfs;
}

PATH *DFS(GRAPH *graph, int source, int target)
{
    if (graph == NULL || graph->v == 0)
        return NULL;

    int length = graph->v;
    int colors[length];
    int s_time[length], f_time[length];
    int parents[length];

    for (int i = 0; i < length; i++)
    {
        colors[i] = WHITE;
        parents[i] = -1;
    }

    VERTEX *aux = find_vertex(graph, source);
    while (aux != NULL)
    {
        int u = aux->index;
        if (colors[u] == WHITE)
            DFS_visit(graph, aux, colors, s_time, f_time, parents);
        aux = aux->next;
    }

    for (int i = 0; i < length; i++)
        printf("[i=%d] COLOR=%d, PARENT=%d, TIME=%d/%d\n", i, colors[i], parents[i], s_time[i], f_time[i]);

    PATH *path = create_path();
    add_path_recursive_dfs(path, parents, target);
    return path;
}
