

Complexity ("naive" implementation):
Iterations: O(|V|) = O(n)
Edge search: O(|E|) = O(m)
O(n*m)


Input: G = (V, E)   // G is a connected and undirected graph
       a cost ce for each edge e ∈ E
Output: the edges of a minimum spanning tree of G
// Initialization
X := {s}            // s is a randomly chosen vertex
T := ∅              // the edges in T that span X
// main loop
while X ≠ V do
    find (v, w) that has the least cost edge such that 
        v ∈ X and w ∈ V-X
    X := X ∪ {w}
    T := T ∪ {(v, w)}
return T
