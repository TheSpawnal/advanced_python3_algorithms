

'''
Due to a predicted long term effect of smart working, the US local government of California has decided 
to reduce road infrastructure maintenance costs by investing in long term infrastructural changes.
They opened a competition innovation project, the winner will be hired for this urban planning project. 
Intersections and endpoints are represented by nodes and the roads connecting these intersections or road 
endpoints are represented by edges. Each edge has a cost associated to it and each node has a weight.

 Given a grid-like graph, find the shortest path using A* between the two nodes with the maximum weight. 
 Where the starting node is the highest and the end node is the 2nd highest. 
 Use the Euclidean  as heuristic function, which is calculated between two points in 
 a coordinate system(x1,y1) and (x2,y2) as follows:

sqrt((x2-x1)^2 + (y2-y1)^2)

where, the nodes of the graph are represented as such points (see the data format below). 
You can assume that there exists a path between the two nodes with the maximum weight, 
and, that all nodes have a unique weight.

Dataformat1. The shortest_path function takes two parameters:
• nodes_l (list[node:tuple[tuple[x:int, y:int], weight:int]])
A tuple list of thenodes, where each node is represented by a tuple of its grid coordinates, and, the node weight.

• edges_l (list[edge:tuple[n1:tuple[int,int], n2:tuple[int,int], cost:int]]):  
A tuple list of the edges, where each edge is represented by the coordinates (as tuples) of the two nodes, and, the cost of the undirected edge.
nodes_l: [((<x1>, <y1>), <weight1>), ..., ((<xn>, <yn>), <weightn>)]
edges_l: [((<x1>,<y1>), (<x2>,<y2>),<edgecost1>), ..., ((<xs>,<ys>), (<xe>,<ye>),<edgecostm>)]

'''


from typing import List, Tuple, Dict, Callable
from math import sqrt
import heapq

class Graph:
    def __init__(self):
        self.nodes: Dict[Tuple[int, int], int] = {}
        self.edges: Dict[Tuple[int, int], Dict[Tuple[int, int], int]] = {}
        self.max_nodes: List[Tuple[Tuple[int, int], int]] = [
            ((-1, -1), float('-inf')),
            ((-1, -1), float('-inf'))
]

    def add_node(self, node_id: Tuple[int, int], weight: int):
        self.nodes[node_id] = weight
        self.edges[node_id] = {}
        
        # Update max_nodes if necessary
        if weight > self.max_nodes[0][1]:
            self.max_nodes[1] = self.max_nodes[0]
            self.max_nodes[0] = (node_id, weight)
        elif weight > self.max_nodes[1][1]:
            self.max_nodes[1] = (node_id, weight)

    def add_edge(self, source_id: Tuple[int, int], end_id: Tuple[int, int], cost: int):
        # Add edge in both directions to create an undirected graph
        self.edges[source_id][end_id] = cost
        self.edges[end_id][source_id] = cost

    def astar_shortest_path(self, source_id: Tuple[int, int], end_id: Tuple[int, int], heuristic: Callable):
        def reconstruct_path(came_from, current):
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        open_set = []
        heapq.heappush(open_set, (0, source_id))
        came_from = {}
        g_score = {source_id: 0}
        f_score = {source_id: heuristic(source_id, end_id)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == end_id:
                return reconstruct_path(came_from, current)

            for neighbor in self.edges[current]:
                tentative_g_score = g_score[current] + self.edges[current][neighbor]

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end_id)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []  # No path found

def build_Graph(nodes_l: List[Tuple[Tuple[int, int], int]],
                edges_l: List[Tuple[Tuple[int, int], Tuple[int, int], int]]) -> Graph:
    G = Graph()

    for node, weight in nodes_l:
        G.add_node(node, weight)

    for node1, node2, cost in edges_l:
        G.add_edge(node1, node2, cost)

    return G

def heuristic(u: Tuple[int, int], v: Tuple[int, int]) -> float:
    return sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)

def shortest_path(nodes_l: List[Tuple[Tuple[int, int], int]],
                  edges_l: List[Tuple[Tuple[int, int], Tuple[int, int], int]]) -> List[Tuple[int, int]]:
    G = build_Graph(nodes_l, edges_l)

    source_id, _ = G.max_nodes[0]
    end_id, _ = G.max_nodes[1]

    return G.astar_shortest_path(source_id, end_id, heuristic)



