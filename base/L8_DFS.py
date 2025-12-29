
DFS(G)
1for each vertex u ∈ G.V
2  u.c l r = WHITE
3  u.π = NIL
4time = 0
5for each vertex u ∈ G.V
6  if u.c l r == WHITE
7    DFS-VISIT(G, u)
DFS-VISIT(G, u)
1time = time + 1 // white vertex u has just been discovered
2u.d = time
3u.c l r = GRAY
4for each vertex v in G.Adj[u]// explore each edge (u, v)
5  if v.c l r == WHITE
6    v.π = u
7    DFS-VISIT(G, v)
8time = time + 1
9u.f = time
10u.c l r = BLACK // blacken u; it is finished



# dfs iterative pseudocode
# input: graph G = (V,E) in adjacency-list
#     representation, and a vertex s∈V
# Postcondition: a vertex is reachable from s if and only if it
#     is marked as explored.

# Mark all vertices as unexplored
# S := a stack data structure, initialized with s
# while S is not empty do
#     remove("pop") the vertex v from the front of S
#     if v is unexplored then
#         mark v as explored
#         for each edge (v,w) in v's adjacency list do
#             add("push") w to the front of S


def dfs_iterative(graph, start):
    #mark all vertices as unexplored
    explored = {v : False for v in graph}
    #initialize the stack with the starting vertex
    stack = [start]
    #while the stack is not empty
    while stack:
        #pop the vertex from the top of the stack
        v = stack.pop()
        #if v is unexplored
        if not explored[v]:
            #Mark v as explored
            explored[v] = True
            print(f"Exploring vertex: {v}")
            #for each neighbor w of v
            for w in graph[v]:
                #push w onto the stack
                stack.append(w)
    return explored

# Example usage:
graph = {
    'S': ['A', 'B'],
    'A': ['C','S'],
    'B': ['C', 'D','S'],
    'C': ['A','B','D','E'],
    'D': ['B','C','E'],
    'E': ['C','D']
}

dfs_iterative(graph, 'A')









#  DFS(RecursiveVersion)

#  Input: graphG=(V,E) inadjacency-list
#  representation,and a vertex s2V.
#  Postcondition: a vertex is reachable from s if and
#  onlyif it is marked as “explored.”

#  // all vertices unexplored before outer call
#  marksasexplored
#  foreachedge(s,v) in s’s adjacency list do
#       if v is unexplored then
#           DFS(G,v)

def dfs_recursive(graph, s, explored=None, traversal_order=None):
    if explored is None:
        explored = {v: False for v in graph}
    if traversal_order is None:
        traversal_order = []
    
    explored[s] = True
    traversal_order.append(s)
    
    for v in graph[s]:
        if not explored[v]:
            dfs_recursive(graph, v, explored, traversal_order)
    
    return traversal_order

# Example usage:
traversal_order = dfs_recursive(graph, 'A')
print("Traversal Order:", traversal_order)
