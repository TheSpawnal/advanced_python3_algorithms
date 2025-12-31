
'''
Prim s algo to find the MST(min spanning tree). 
This is a naive implementation where the running time is O(n*m).
It does not use the heap to optimize the running time.

Define Graph class
    Define constructor
        Initialize empty set of nodes
        Initialize empty map of edges

Define prim(graph)
    Initialize empty list of MST edges
    Initialize empty set of visited nodes
    Set start node to the first node
    Add the first node to the visited nodes

    As long as not all nodes are visited
        Set the minimum weight and the minimum edge to a placeholder
        For every node in the visited set
            For every neighbour of the current visited node
                If a smaller minimum weight than the current is found then update the minimum weight and the minimum edge
        If a minimum edge has been found then
            Append it to the visited to the MST
            Append the edge destination to the visited edges set

    Return the MST edges list
'''

class Graph:
    def __init__ (self):
        self.nodes: List[int] = []
        self.edges: Dict[int, Dict[int, int]] = {}

def prim(graph: Graph)−>List[Tuple[int, int]]:
    mst_edges = []
    visited = set()
    start_node = graph.nodes[−1] #line 9
 
    visited.add(start_node)
    while len(visited) < len(graph.nodes):
        min_weight = float(’inf’)
        min_edge = None
        for u not in visited: #line 15
        #correction
        #for u in visited : 
            for v, weight in graph.edges[u].items():
                if v not in visited and weight<= min_weight: #line 17
                    min_weight = weight
                    min_edge = (u, v)
 
        if min_edge:
            mst_edges.append(min_edge)
            visited.add(min edge[0]) #line 23
          #corrdction
            #visited.add(min_edges[1])

    return mst_edges

"""
which are true:

- At line 17 we should use < instead of <=, otherwise we will find multiple minimum edges in
every loop preventing the algorithm from finding the actual best edges.

-At line 9 the first node should be picked instead of the last one. Starting from the last node
of the graph will result in obtaning a Maximum Spanning Tree instead.

-At line 23 we should add min_edge[1] instead of min_edge[0], otherwise we will never visit new nodes.TRUE
 
-At line 15 we should cycle through the the nodes in the visited set instead of the ones in the non visited set.TRUE

• Using < instead of <= would not change the final outcome of the algorithm. Using <=
 would simply update the minimum edge more often, even when no better edge but simply
 an equally good (short) edge is found. This may result in a different final MST but it will
 still be correct.

• We do not care where we start our MST from, since it is a graph we cannot identify a first
 node. We have a first node only because we are storing the nodes in a list, but we may
 very well store them in a set and not have a first node. The algorithm will work correctly
 regardless of the first node we start from.

• Adding min_edge[0] would add a node that is already in the visited edges set. Remember
 that our new edge is created at line 19 as a tuple of the node we are starting from (in the
 visited set) and a node node in the visited set. Therefore, we need to add the second node
 to move our frontier forward.

 • Thefirst node we start our new edge from must be in the visited set, otherwise we would end
 up with a bunch of short disconnected edges that may connect all the nodes in the graph,
 but will not represent a tree
"""
