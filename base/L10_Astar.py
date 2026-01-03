

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
