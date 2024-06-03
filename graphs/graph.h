#include <stdio.h>
#include <stdlib.h>
#ifndef GRAPH_FILE
#define GRAPH_FILE

typedef struct ADJ_VERTEX
{
    int index;
    int weight;
    struct ADJ_VERTEX *next;
} ADJ_VERTEX;

typedef struct VERTEX
{
    int index;
    ADJ_VERTEX *adjacents;
    struct VERTEX *next;
} VERTEX;

typedef struct GRAPH
{
    int v;
    int e;
    VERTEX *vertex;
} GRAPH;

GRAPH *create_graph();
void add_vertex(GRAPH *graph, int index);
void add_edge(GRAPH *graph, int source, int target, int weight);
void remove_vertex(GRAPH *graph, int index);
void remove_edge(GRAPH *graph, VERTEX *source, int target);
VERTEX *find_vertex(GRAPH *graph, int index);
ADJ_VERTEX *find_edge(GRAPH *graph, int source, int target);
void print_graph(GRAPH *graph);

#endif