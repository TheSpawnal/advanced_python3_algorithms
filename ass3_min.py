"""

1/Prove that in a heap, with nodes indexed by 1,...,n, starting with
the root, the node with largest index to have children, has index
⌊n/2⌋.


Proof:

Node floor(n/2)+1 has no children:
left child index = 2(floor(n/2)+1) = 2(floor(n/2))+2 > n
index exceeds heap size -> no children -> it's a leaf. 
Same for all higher indices

Node floor(n/2) has children:
left child index = 2(floor(n/2)) <= n
    -n even : left child at index n
    - n odd : left child at n-1, right child at n

therefore last internal node is at index floor(n/2)

==================================================================
2/Is the operation of deletion in a binary search tree ”commuta
tive”? That is, would deleting x and then y, yield the same tree
as deleting y and then x? Argue why it is commutative, or give a
counterexample.


No, the operation delete in a binary tree is not commutative. 
ex: 

tree: 1,2,4,3
delete 1 then 2
tree: 3,4(right child)

tree array representation: 1,2,4,3
delete 2 then 1
tree:4,3(left child)

==================================================================
3/Suppose that you construct a binary search tree by repeatedly
inserting distinct values into the tree. Argue that the number of
nodes examined in searching for a value in the tree is 1 plus the
number of nodes examined when the value was first inserted into
the tree.

Inserting a value and searching for it == same strategy, we know 
that they do must examine at least the same number of nodes.
Searching for a node will include on additional node : the node being
search for.Then searching for a node will look at one more node than 
the number analyzed when inserting a node.

==================================================================
4/The square of a directed graph G = (V,E) is the graph G2 = (V,E2)
such that (u,v) ∈ E2 if and only if contains a walk with two edges
between and.
Describe an efficient algorithm for computing G2 from the ad
jacency matrix of G, and analyze the running time.


COMPUTE-G-SQUARE
init adj2 as empty adjacency lists
for each vertex u E V do 
    create a set S to track unique neighbors
    //add 1-hop neigbors
    for each v E adj[u] do
        S.add(v)
        //add 2-hop neighbors
        for each w E adj[v] do
            S.add(w)
        end for
    end for
    adj2[u] = S.toList()
end for
return adj2

time O(V E)
space : O(V^2) for storing G^2 in the worst case. 

==================================================================
5/Most graph algorithms that take an adjacency-matrix representa
tion as input require time Ω(V^2), but there are some exceptions.
Show how to determine whether a directed graph G contains a
universal sink– a vertex with in-degree |V|−1 and out-degree 0
in time O(V), given an adjacency matrix for G.


We can eliminate at least one candidate vertex per step by walking
diagonally through the adjacency matrix.
Logic:
Start at (1,1):
-if M[i, j] = 1: vertex i has an outgoing edge to j->i cannot be a 
sink -> eliminate i, move to (i+1, j)
-if M[i,j] = 0: No edge from i to j -> either j cannot be a sink
(missing edge from i), or i might be a sink -> eliminate j, move to (i, j+1)

Each step eliminates exactly one vertex as a potential sink, so after at
most |V| steps, we have at most one candidate remaining.

==================================================================
7/GiveanexampleofadirectedgraphG=(V,E), asourcevertex
s∈V, andasetof treeedgesEπ⊆Esuchthat foreachvertex
v∈V, theuniquesimplepathinthegraph(V,Eπ) fromstov is
ashortestpathinG,yetthesetofedgesEπcannotbeproduced
byrunningBFSonG,nomatterhowtheverticesareorderedin
eachadjacencylist.

Solution:
GraphG: V ={s,x,y,a,b}withedges{(s,x),(s,y),(x,a),(x,b),(y,a),(y,b)}
Source: s
Tree Edges: Eπ = {(s,x),(x,a),(s,y),(y,b)}
Edges: (s,x), (s,y) (x,a), (x,b) (y,a), (y,b)
Chosen Eπ ={(s,x),(x,a),(s,y),(y,b)}
Eπ contains shortest paths:
• s to x: dist= 1
• s to a: dist= 2 (via s → x → a)
• s to y: dist= 1
• s to b: dist=2 2 (via s → y → b)
BFS cannot produce Eπ:
If Adj[s] = [x, y]:
• x is dequeued before y
• x discovers both a and b first
• Tree: {(s,x),(x,a),(x,b),(s,y)}
• Missing (y,b) ×
If Adj[s] = [y, x]:
• y is dequeued before x
• y discovers both a and b first
• Tree: {(s,y),(y,a),(y,b),(s,x)}
• Missing (x,a) ×
Conclusion: No adjacency list ordering produces both (x,a) and (y,b)
simultaneously! This Eπ contains only shortest paths but cannot be pro
duced by any BFS execution on G.
==================================================================
8/The diameter of a tree is defined as the largest of all distances in
the tree. Give an efficient algorithm to compute the diameter of
a tree, and analyze the running time of your algorithm.


This works on the principle that any farthest node from an arbitrary
starting point must be one endpoint of a diameter, and, the farthest node
from that endpoint is the other endpoint of the diameter.


First BFS/DFS: O(V +E) where V = number of vertices, E = number of edges.
Second BFS/DFS: O(V +E).
Total: O(V +E).
Since a tree with V vertices has exactly V − 1 edges, the complexity is
O(V) or O(n) where n is the number of nodes.
Space complexity: O(V) for the distance array and queue.


COMPUTE-TREE-DIAMETER()
input: tree represented as adjacency-list
output: diamter of the tree(longest path between any two nodes)
if tree is empty then
    return 0
end if
Select a node(root or node 0) as start_node
//first BFS/DFS; find the farthest node from start_node
farthest_node_1, distance_1 = SearchFarthestNode(tree, start_node)
//second BFS/DFS; find the farthest node from farthest_node_1
farthest_node_2, diameter= = SearchFarthestNode(tree, farthest_node_1)
return diameter 


SearchFarthestNode()
Input: tree (adjacency list), source node
Output: (farthest node, max distance)

Initialize distances array with-1 (unvisited)
Initialize queue with source node
Set distance[source] = 0
// BFS traversal
while queue is not empty do
    current = queue.dequeue()
    for each neighbor in tree[current] do
        if distances[neighbor] ==-1 then // unvisited
            distances[neighbor] = distances[current] + 1
            queue.enqueue(neighbor)
        end if
    end for
end while
// Find node with maximum distance
farthest node = node with maximum distance
max distance = distances[farthest node]
return (farthest node, max distance)

==================================================================


"""