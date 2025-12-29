
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
