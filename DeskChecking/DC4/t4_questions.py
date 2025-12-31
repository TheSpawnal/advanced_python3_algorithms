
In A*shortest path algorithm, the heuristic function is just a minor improvement and it is not
 really relevant to finding the correct graph. Therefore the heuristic function can be anything
 and does not significantly affect the running time.

In somegraphs there may be several equally correct minimum spanning trees. TRUE

Kruksal’s and Prim’s algorithms have the same complexity regardless of how they are implemented 
since the steps they have to take to get to the result are always the same, regardless
of the data structure used


expl:

• The heuristic function is the main difference between Dijkstra and A* star. It is important
 for it to be consistent or monotone in order to find a correct solution. The quality of the
 heuristic then makes the A* search shorter or longer.

• Graphs with cycles, parallel edges, many edges with the same weight, are all cases where we
 may have multiple correct MSTs with the same weight.

• Using some data structures rather than others may avoid some long operations (think about
 the complexity of finding an item in a list O(n) vs finding an item in a hashmap O(1)). The
 complexity lies not only in the loops but also in the complexity it takes to interact with
 the data structures. The Prim’s naive implementation takes O(v) to iterate over all nodes
 times O(e) to search the correct edge to expand, getting to a total of O(v∗e). On the other
 hand, a Prim’s implementation using a heap costs O(v log(v)) for the heap initialization and
 O(v log(v) + e log(v)), for a total of O((v+e)log(v) which is definitely lower than the O(v∗e)
 of the naive implementation.
