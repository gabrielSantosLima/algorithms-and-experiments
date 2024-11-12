#include "graph.h"
#include "bfs.h"
#include "dfs.h"
#include "dijkstra.h"

int main()
{
    GRAPH *graph = create_graph();
    add_vertex(graph, 0);
    add_vertex(graph, 1);
    add_vertex(graph, 2);
    add_vertex(graph, 3);
    add_vertex(graph, 4);
    add_vertex(graph, 5);
    add_vertex(graph, 6);

    add_edge(graph, 0, 1, 1);
    add_edge(graph, 1, 0, 1);
    add_edge(graph, 1, 2, 1);
    add_edge(graph, 1, 3, 1);
    add_edge(graph, 2, 1, 1);
    add_edge(graph, 2, 3, 1);
    add_edge(graph, 2, 4, 1);
    add_edge(graph, 3, 1, 1);
    add_edge(graph, 3, 2, 1);
    add_edge(graph, 4, 2, 1);
    add_edge(graph, 4, 6, 1);
    add_edge(graph, 5, 6, 1);
    add_edge(graph, 6, 5, 1);

    add_edge(graph, 3, 6, 1);

    print_graph(graph);
    // remove_vertex(graph, 0);
    // printf("\n");
    // print_graph(graph);
    // printf("\n");

    // printf("FOUND: %d\n", find_vertex(graph, 1)->index);
    // printf("NOT FOUND: %s\n", find_vertex(graph, 0));

    printf("\n==== BFS ====\n");
    PATH *path = BFS(graph, 0, 6);
    printf("MENOR CAMINHO: %d passos.\n", length_path(path));
    print_path(path);

    printf("\n\n==== DFS ====\n");
    PATH *path_dfs = DFS(graph, 0, 6);
    printf("MENOR CAMINHO: %d passos.\n", length_path(path_dfs));
    print_path(path_dfs);

    printf("\n\n==== DIJKSTRA ====\n");
    GRAPH *graph2 = create_graph();
    add_vertex(graph2, 0);
    add_vertex(graph2, 1);
    add_vertex(graph2, 2);
    add_vertex(graph2, 3);

    add_edge(graph2, 0, 1, 50);
    add_edge(graph2, 0, 2, 8);
    add_edge(graph2, 1, 0, 50);
    add_edge(graph2, 1, 2, 9);
    add_edge(graph2, 1, 3, 2);
    add_edge(graph2, 2, 0, 8);
    add_edge(graph2, 2, 1, 9);
    add_edge(graph2, 2, 3, 40);
    add_edge(graph2, 3, 1, 2);
    add_edge(graph2, 3, 2, 6);

    print_graph(graph2);

    PATH *path_dks = dijkstra(graph2, 0, 3);
    print_path(path_dks);

    return 0;
}