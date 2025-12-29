
Input: G = (V, E)   // G is a connected and undirected graph
       a cost ce
 for each edge e ∈ E
Output: the edges of a minimum spanning tree of G
// Initialization
T := ∅              // the edges that span G
// Preprocessing
sort edges of E by cost
// main loop
for each e ∈ E in increasing order of cost do
    if T ∪ {e} is acyclic then
        T := T ∪ {e}
return T

"""
Complexity:
It depends a lot on sorting and acyclic checking!
"Naive" implementation:
Assuming the usage of Merge Sort for sorting and DFS for acyclic checking, 
that would result in O(m*n)
"""
