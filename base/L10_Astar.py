
"""
A* search algorithm. 

A-STAR(Graph, start, goal, h)
────────────────────────────────────────────────────────────
Input:
    Graph       : weighted graph with vertices and edges
    start       : source vertex
    goal        : target vertex
    h(v)        : heuristic function estimating cost from v to goal

Output:
    Shortest path from start to goal, or failure if none exists

────────────────────────────────────────────────────────────
1.  openSet <- EMPTY MIN-PRIORITY QUEUE      // Frontier nodes

2.  prev    <- EMPTY MAP                     // Predecessor pointers
3.  gScore  <- EMPTY MAP                     // Cost from start to v
4.  fScore  <- EMPTY MAP                     // Estimated total cost

5.  // Initialize all vertices
6.  for each vertex v in Graph.Vertices:
7.      gScore[v] <- INFINITY
8.      fScore[v] <- INFINITY
9.      prev[v]   <- UNDEFINED

10. // Initialize start vertex
11. gScore[start] <- 0
12. fScore[start] <- h(start)
13. openSet.add(start)

14. // Main loop
15. while openSet is not empty:
16.     current <- node in openSet with lowest fScore[]
17.     
18.     if current = goal:
19.         return gScore[], prev[]           // Success: path found
20.     
21.     openSet.Remove(current)
22.     
23.     // Relax all neighbors
24.     for each edge (current, neighbor) with weight w:
25.         tentative_gScore <- gScore[current] + w
26.         
27.         if tentative_gScore < gScore[neighbor]:
28.             // Found a better path to neighbor
29.             prev[neighbor]   <- current
30.             gScore[neighbor] <- tentative_gScore
31.             fScore[neighbor] <- tentative_gScore + h(neighbor)
32.             
33.             if neighbor not in openSet:
34.                 openSet.add(neighbor)

35. return failure                            // No path exists
"""




class Graph:
    def __init__ (self):
        self.nodes: dict[Tuple, int] = {}
        self.edges: dict[Tuple, dict[Tuple, int]] = {}

def astar shortest path(G: Graph, source_id: Tuple, end_id: Tuple, h):
    open_set = {source_id}
    came_from = {}
    g_score = dict()
    f_score = dict()
    for node in G.nodes:
        g_score[node] = float('inf')
        f_score[node] = float('inf')
    g_score[source_id] = 0
    f_score[source_id] = h(source_id, end_id)
 
    while open set:
        current = (-1,-1)
        current_score = float('inf')
            for node in open set:
                if f_score[node]<current_score:
                    current = node
                    current_score = f_score[node]
 
        if current == end_id:
        return reconstruct_path(came_from, current)
 
        open set.remove(current)
        for neighbor in G.edges[current]:
            tentative_g_score = g_score[current] + G.edges[current][neighbor]
            if tentative_g_score<g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, end_id)
                if neighbor not in open set:
                    open set.add(neighbor)
    return []
