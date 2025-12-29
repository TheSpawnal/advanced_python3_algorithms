

Input: G = (V, E)
       a cost ce
 for each edge e ∈ E
Output: the edges of a minimum spanning tree of G
// Initialization
X := {s}
T := ∅
H := empty heap
for every v ∈ V, v ≠ s do
    if there is an edge (s, v) ∈ E then
        key(v) := csv
        cheapestEdge(v) := (s, v)
    else
        key(v) := +∞
        cheapestEdge(v) := null
    Insert v into H
 (cont)
// main loop
while H is non-empty do
    w := ExtractMin(H)
    X := X ∪ {w}
    T := T ∪ {cheapestEdge(w)}
    // update keys
    for every edge (w, y) with y ∈ V-X do
        if cwy
 < key(y) then
            Delete y from H
            key(y) := cwy
            cheapestEdge(y) := (w, y)
            Insert y into H
return T

Initialization: O(|V|) * O(log|V|)
Main loop: O(|V|) * O(log|V|) + O(|E|) * O(log|V|)
Total: O((|V|+|E|) * log|V|) = O((n+m) * logn)
