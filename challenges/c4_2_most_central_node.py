

"""
Find the most central node. Betweenness centrality (CB) is based on the idea that a node is central if 
it lies between manyothernodes. It is defined as the total number of shortest paths connecting couple of nodes, 
which pass through the given node. Betweenness centrality of a node v is the sum of the fraction
of all-pairs shortest paths that pass through v: 

CB(v) = 2 / ((n-1)(n-2)) * sum(sigma(s,t|v) / sigma(s,t) for s,t in V)

where V is the set of nodes, n is the number of nodes in the graph, 
σ(s,t) is the number of shortest (s,t)-paths, 
and σ(s,t|v) is the number of those paths passing through some node v other than s,t. 
If s =t,σ(s,t)=1, andif v ∈s,t, σ(s,t|v)=0


Dataformat2. The most_centralfunctiontakestwoparameters:
 • nodes_l(list[int]): Alist of all the nodes ids of the graph.
 • edges_l (list[tuple[node1:int,node2:int,cost:int]]): A tuple list of the edges, where
 each edge is represented by the two node ids, and, the cost of the undirected edge.
 nodes_l: [<id1>, ..., <idn>]
 edges_l: [(<id1,1>, <id1,2>, <cost1>), ..., (<idm,1>, <idm,2>, <costm>)]

 The function returns the integer id of the most central node.
"""


from typing import List, Tuple, Dict
from collections import deque

class Graph:
    def __init__(self):
        self.nodes: List[int] = []
        self.edges: Dict[int, Dict[int, int]] = {}

    def add_node(self, node_id: int):
        if node_id not in self.nodes:
            self.nodes.append(node_id)
            self.edges[node_id] = {}

    def add_edge(self, source_id: int, end_id: int, cost: int):
        self.edges[source_id][end_id] = cost
        self.edges[end_id][source_id] = cost

def build_Graph(nodes_l: List[int], edges_l: List[Tuple[int, int, int]]) -> Graph:
    G = Graph()
    for node in nodes_l:
        G.add_node(node)
    for node1, node2, cost in edges_l:
        G.add_edge(node1, node2, cost)
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

def most_central(nodes_l: List[int], edges_l: List[Tuple[int, int, int]]) -> int:
    G = build_Graph(nodes_l, edges_l)
    betweenness = brandes_betweenness_centrality(G)
    return max(betweenness, key=betweenness.get)




