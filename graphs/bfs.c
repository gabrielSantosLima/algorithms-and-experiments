#include "bfs.h"
#define WHITE 0
#define BLACK 1
#define GRAY -1

void add_path_recursive(PATH *path, int *parents, int index)
{
    if (index == -1)
        return;
    add_path_recursive(path, parents, parents[index]);
    add_path(path, index, 1);
}

PATH *BFS(GRAPH *graph, int source, int target)
{
    VERTEX *s = find_vertex(graph, source);
    if (s == NULL || graph == NULL || graph->v == 0)
        return NULL;

    int length = graph->v;
    int visited[length];
    int parents[length];
    int distance[length];
    int queue[length];

    int end = 0;

    for (int i = 0; i < length; i++)
    {
        visited[i] = 0;
        parents[i] = -1;
        distance[i] = 0;
    }

    visited[source] = GRAY;
    parents[source] = -1;
    distance[source] = 0;

    queue[0] = source;
    end++;

    while (end != 0)
    {
        int u = queue[end - 1];
        end--;
        VERTEX *vs = find_vertex(graph, u);
        ADJ_VERTEX *aux = vs->adjacents;
        while (aux != NULL)
        {
            int v = aux->index;
            if (visited[v] == WHITE)
            {
                visited[v] = GRAY;
                parents[v] = u;
                distance[v] = distance[u] + 1;
                queue[end] = v;
                end++;
            }
            aux = aux->next;
        }
        visited[u] = BLACK;
    }

    for (int i = 0; i < length; i++)
        printf("[i=%d] COLOR=%d, PARENT=%d\n", i, visited[i], parents[i]);

    PATH *path = create_path();
    add_path_recursive(path, parents, target);
    return path;
}
