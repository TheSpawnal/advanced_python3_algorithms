'''
FindAllPaths
Our task is to find all the possible paths from which a (TwitterID-A) could have
seen a post by a user (TwitterID-B). For each path a vertice should be visited
only once as the graph may contain cycles.

Allowed data structures 2: tuple, dict, list, set

Dataformat2. Thefind_paths()function takes the same parameters and data format as 
our fist task mentioned earlier. 
But,  returns a list of lists (list[list[int]]) of all possible paths from start to end.

[ [idstart>, ..., <idend>], [<idstart>, ..., <idend>], ...]

Call: find_paths(1, 3, [(1, [2, 3]), (2, [3, 1]), (3, [2])])

Returns (list[list[int]]): [[1, 3], [1, 2, 3]]

'''


from typing import List, Tuple, Dict
from collections import deque

class Graph:
    '''Class to represent a Graph, as a list of weighted nodes and edges.'''
    def __init__(self):
        '''Function to initialize a Graph object
        TODO: You can modify it to suite your needs
        '''
        self.nodes: List[int] = []
        self.edges: Dict[int, Dict[int, int]] = {}

    def add_node(self, node_id: int):
        '''Function to add a node to a Graph object.

        ### Parameters
        `node_id` : `int` representing the ID of a node in the graph.

        You are free to choose your own way to represent nodes and edges.
        '''
        if node_id not in self.nodes:
            self.nodes.append(node_id)
            self.edges[node_id] = {}

    def add_edge(self, source_id: int, end_id: int, cost: int):
        '''Function to add an edge to a Graph object.

        ### Parameters
        `source_id` : `int` representing the ID of the source node of the edge.

        `end_id` : `int` representing the ID of the end node of the edge.

        `cost` : `int` representing the cost of an edge in the graph.

        You are free to choose your own way to represent nodes and edges.

        !! Notice: Take appropriate measures to create an undirected graph
        '''
        self.edges[source_id][end_id] = cost
        self.edges[end_id][source_id] = cost


def build_Graph(nodes_l: List[int],edges_l: List[Tuple[int, int, int]])->Graph:
    '''Function to build a grid-like Graph object from the input data.

    ### Parameters
    `nodes_l` : list of nodes ids.

    `edges_l` : list of edges, each represented as source and end nodes,
        and edge cost.
        i.e. [(u, v, cost),(u1, v1, cost), ...]

    !! Notice: Take appropriate measures to create an undirected graph

    ### Return
    A Graph object.
    '''
    G = Graph()

    for node in nodes_l:
        G.add_node(node)

    for node1, node2, c in edges_l:
        G.add_edge(node1, node2, cost=c)

    return G

def brandes_betweenness_centrality(G: Graph) -> Dict[int, float]:
    betweenness = {node: 0.0 for node in G.nodes}
    
    for s in G.nodes:
        S = []
        P = {w: [] for w in G.nodes}
        sigma = {w: 0 for w in G.nodes}
        sigma[s] = 1
        d = {w: -1 for w in G.nodes}
        d[s] = 0
        Q = deque([s])

        while Q:
            v = Q.popleft()
            S.append(v)
            for w in G.edges[v]:
                if d[w] < 0:
                    Q.append(w)
                    d[w] = d[v] + 1
                if d[w] == d[v] + 1:
                    sigma[w] += sigma[v]
                    P[w].append(v)

        delta = {w: 0 for w in G.nodes}
        while S:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                betweenness[w] += delta[w]

    n = len(G.nodes)
    for v in betweenness:
        betweenness[v] *= 2 / ((n - 1) * (n - 2))

    return betweenness

def most_central(nodes_l: List[int],
                 edges_l: List[Tuple[int, int, int]]
                 ) -> int:
    '''
    Find the most central node of the provided graph

    ### Parameters
    `nodes_l` : list of nodes ids.

    `edges_l` : list of edges, each represented as source and end nodes,
        and edge cost.
        i.e. [((u, v, cost),(u1, v1), cost), ...]

    ### Return
    The most central node id
    '''

    G = build_Graph(nodes_l, edges_l)
    betweenness = brandes_betweenness_centrality(G)
    return max(betweenness, key=betweenness.get)
