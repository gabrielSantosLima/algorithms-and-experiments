#include "dijkstra.h"

PATH *dijkstra(GRAPH *graph, int source, int target)
{
    if (graph == NULL || graph->v == 0)
        return NULL;
    int length = graph->v;
    int distance[length];
    int visited[length];
    int parent[length];

    for (int i = 0; i < length; i++)
    {
        distance[i] = INT_MAX;
        visited[i] = 0;
        parent[i] = -1;
    }
    distance[source] = 0;

    VERTEX *aux = find_vertex(graph, source);

    if (aux == NULL)
        return NULL;

    for (int i = 0; i < length; i++)
    {
        int v = -1;
        while (aux != NULL && (v == -1 || distance[aux->index] < distance[v]))
        {
            if (visited[v] == 0)
                v = aux->index;
            aux = aux->next;
        }
        ADJ_VERTEX *aux2 = aux->adjacents;
        while (aux2 != NULL)
        {
            int u = aux2->index;
            if (distance[v] + aux2->weight < distance[u])
            {
                distance[u] = distance[v] + aux2->weight;
                parent[u] = v;
            }
            aux2 = aux2->next;
        }
        visited[v] = 1;
    }

    for (int i = 0; i < length; i++)
        printf("INDEX: %d, DISTANCE = %d, PARENT = %d, VISITED = %d\n", i, distance[i], parent[i], visited[i]);

    return NULL;
}