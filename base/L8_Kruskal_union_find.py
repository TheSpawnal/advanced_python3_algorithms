

How could we check if adding an edge {u, v} in T would create a cycle?
Remember: We create a cycle if u and v are already in the same connected 
component (or set).
IDEA: we keep track of the so far connected components, so we can quickly check 
if they belong to the same
-We start with a component for each node.
-Components merge when we add an edge in T.
-Need a way to check if u and v are in same component and to merge two components into one.

Kruskal’s algorithm with Union-Find 
The Union-Find abstract data type supports the following operations:
-Initialize(V): given an array V of objects, create a union-find data structure 
with each object v ∈ V in its own set.-> O(n)
-Find(U,x): given a union-find data structure and an object x in it, return the 
name of the set that contains x.->O(log n)
-Union(U,x,y): given a union-find data structure and two objects x, y ∈ V in it, 
merge the sets that contain x and y into a single set-> O(log n)


Input: G = (V, E)   // G is a connected and undirected graph
       a cost ce
 for each edge e ∈ E
Output: the edges of a minimum spanning tree of G
// Initialization
T := ∅              // the edges that span G
U := Initialize(V)  // union-find data structure
sort edges of E by cost
// main loop
for each (v,w) ∈ E in increasing order of cost do
    if Find(U,v) ≠ Find(U,w) then   // no v-w path in T 
        T := T ∪ {(v,w)}
        Union(U,v,w)
return T

Complexity:
Initialize + sorting: O(n) + O(m log n)
2*m Find operations:   O(m log n)
n-1 Union operations:  O(n log n)
Total: O((m+n) log n)
