#include "graph.h"

ADJ_VERTEX *create_adj_vertex(int index, int weight)
{
    ADJ_VERTEX *vertex = (ADJ_VERTEX *)malloc(sizeof(ADJ_VERTEX));
    vertex->index = index;
    vertex->weight = weight;
    vertex->next = NULL;
    return vertex;
}

VERTEX *create_vertex(int index)
{
    VERTEX *vertex = (VERTEX *)malloc(sizeof(VERTEX));
    vertex->index = index;
    vertex->adjacents = NULL;
    vertex->next = NULL;
    return vertex;
}

GRAPH *create_graph()
{
    GRAPH *graph = (GRAPH *)malloc(sizeof(GRAPH));
    graph->e = 0;
    graph->v = 0;
    graph->vertex = NULL;
    return graph;
}

void add_vertex(GRAPH *graph, int index)
{
    VERTEX *vertex = create_vertex(index);
    if (graph->vertex == NULL)
    {
        graph->vertex = vertex;
        graph->v++;
        return;
    }
    VERTEX *aux = graph->vertex;
    while (aux->next != NULL)
        aux = aux->next;
    aux->next = vertex;
    graph->v++;
}

void add_edge(GRAPH *graph, int source, int target, int weight)
{
    if (graph->v == 0)
        return;
    VERTEX *aux = graph->vertex;
    while (aux != NULL && aux->index != source)
        aux = aux->next;
    if (aux == NULL)
        return;
    ADJ_VERTEX *vertex = create_adj_vertex(target, weight);
    if (aux->adjacents == NULL)
    {
        aux->adjacents = vertex;
        return;
    }
    ADJ_VERTEX *aux2 = aux->adjacents;
    while (aux2->next != NULL)
        aux2 = aux2->next;
    aux2->next = vertex;
    graph->e++;
}

void remove_vertex(GRAPH *graph, int index)
{
    if (graph->v == 0)
        return;
    VERTEX *aux = graph->vertex;
    if (aux->index == index)
    {
        graph->vertex = aux->next;
        graph->v--;
        free(aux);
    }
    else
    {
        VERTEX *last = NULL;
        while (aux != NULL && aux->index != index)
        {
            last = aux;
            aux = aux->next;
        }
        if (aux == NULL)
            return;
        last->next = aux->next;
        graph->v--;
        free(aux);
    }
    aux = graph->vertex;
    while (aux != NULL)
    {
        remove_edge(graph, aux, index);
        aux = aux->next;
    }
}

void remove_edge(GRAPH *graph, VERTEX *source, int target)
{
    if (source->adjacents == NULL)
        return;
    ADJ_VERTEX *aux = source->adjacents;
    if (aux->index == target)
    {
        source->adjacents = aux->next;
        free(aux);
    }
    else
    {
        ADJ_VERTEX *last = aux;
        while (aux != NULL && aux->index != target)
        {
            last = aux;
            aux = aux->next;
        }
        if (aux == NULL)
            return;
        last->next = aux->next;
        free(aux);
    }
}

VERTEX *find_vertex(GRAPH *graph, int index)
{
    if (graph->v == 0)
        return NULL;
    VERTEX *aux = graph->vertex;
    while (aux != NULL && aux->index != index)
        aux = aux->next;
    return aux;
}

ADJ_VERTEX *find_edge(GRAPH *graph, int source, int target)
{
    if (graph->v == 0)
        return NULL;
    VERTEX *aux = find_vertex(graph, source);
    if (aux == NULL)
        return NULL;
    ADJ_VERTEX *aux2 = aux->adjacents;
    while (aux2 != NULL && aux2->index != target)
        aux2 = aux2->next;
    return aux2;
}

void print_graph(GRAPH *graph)
{
    if (graph->v == 0)
        return;

    VERTEX *aux = graph->vertex;
    ADJ_VERTEX *aux2 = NULL;

    while (aux != NULL)
    {
        printf("%d -> ", aux->index);
        aux2 = aux->adjacents;
        while (aux2 != NULL)
        {
            printf("%d (w=%d) ", aux2->index, aux2->weight);
            aux2 = aux2->next;
        }
        printf("\n");
        aux = aux->next;
    }
}
