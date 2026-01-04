"""
-You are given a directed acyclic graph with real-valued edge 
weights and two distinguished vertices s and t. Describe a 
dynamic-programming approach for finding a longest weighted 
simple path from s to t.  
- What is the running time of your algorithm?


LONGEST-PATH-DAG(G, s, t) 
    Perform topological sort on G to get ordering v₁, v₂, ..., vn 
    Let d[v] = length of longest path from s to v 
    Let π[v] = predecessor of v on longest path from s 
    for each vertex v in G 
        d[v] = -∞ 
        π[v] = NIL 
    d[s] = 0 
    for each vertex u in topological order 
        if d[u] ≠ -∞ 
            for each edge (u, v) with weight w(u, v) 
                if d[u] + w(u, v) > d[v] 
                    d[v] = d[u] + w(u, v) 
                    π[v] = u 
    if d[t] = -∞ 
        print "No path from s to t" 
    else 
        print "Longest path has weight " + d[t] 
        PRINT-PATH(π, s, t)


PRINT-PATH(π, s, t) 
    if t = s 
        print s 
    else if π[t] = NIL 
        print "No path exists" 
    else 
        PRINT-PATH(π, s, π[t]) 
        print t

Topological ordering ensures that when we 
process vertex v, we've already computed optimal solutions for 
all vertices that can reach v

"""
#==================================================================================
"""
Problem 1: DFS Cycle Detection
Write pseudocode for an algorithm that uses DFS to detect if an 
undirected graph contains a cycle.

Algorithm: DFS(graph, start)
Input: graph, starting node
Output: visits all reachable nodes from start
visited ← empty set
function DFS_Visit(node):
    add node to visited
    for each neighbor of node do
        if neighbor not in visited then
            DFS_Visit(neighbor)
        end if
    end for
// Start DFS from the given node
DFS_Visit(start)

-idea:
we track each node's parent in the DFS recursion. 
When we encounter a visited neighbor:
- If it's our parent, we're just seeing the undirected edge from the
other direction (neighbor→node), so ignore it.
- If it's NOT our parent, we've found a path back to a previously
visited node through a different route, which means a cycle exists.




Has_Cycle_DFS(graph)
Input: undirected graph
Output: true if cycle exists, false otherwise
visited ← empty set
function DFS(node, parent):
    add node to visited
    for each neighbor of node do
        if neighbor not in visited then
            if DFS(neighbor, node) = true then
                return true
            end if
        else if neighbor ≠ parent then
            return true // Found cycle: visiting a visited node that's not our parent
        end if
    end for
return false
for each vertex v in graph do
// Ensures we check all components
    if v not in visited then
        if DFS(v, null) = true then
            return true
        end if
    end if
end for
return false


"""
#==================================================================================



#==================================================================================
"""
Problem 2: Heap Operations for Streaming Data.
You're receiving a stream of integers and need to maintain the median
at all times. Design a solution which uses two heaps, write pseudocode
and analyze the time complexity for:
1. Adding a number to your data structure
2. Retrieving the current median


How it works:
◦ Max-heap stores the smaller half; its maximum is the largest of the small 
numbers
◦ Min-heap stores the larger half; its minimum is the smallest of the large 
numbers
◦ Median is either the max of max-heap, min of min-heap, or their average


Algorithm: MedianTracker

Algorithm: MedianTracker
Data structures:
◦ maxHeap: max-heap for smaller half of numbers
◦ minHeap: min-heap for larger half of numbers
Need to maintain:
◦ maxHeap.size() ≈ minHeap.size() (differ by at most 1)
◦ maxHeap.max() ≤ minHeap.min()

function addNumber(num):
// Add to appropriate heap
    if maxHeap is empty OR num ≤ maxHeap.max() then
        maxHeap.insert(num)
    else
        minHeap.insert(num)
    end if
// Rebalance to maintain size invariant
if maxHeap.size() > minHeap.size() + 1 then
    val ← maxHeap.extractMax()
    minHeap.insert(val)
else if minHeap.size() > maxHeap.size() + 1 then
    val ← minHeap.extractMin()
    maxHeap.insert(val)
end if
function getMedian():
    if maxHeap.size() = minHeap.size() then
        return (maxHeap.max() + minHeap.min()) / 2
    else if maxHeap.size() > minHeap.size() then
        return maxHeap.max()
    else
        return minHeap.min()
    end if


Time complexity:
◦ addNumber: O(log n) where n is total numbers seen
◦ Insert into heap: O(log n)
◦ Possible rebalance (extract + insert): O(log n)
◦ getMedian: O(1) (just peek at heap roots)


"""
#==================================================================================

#==================================================================================
"""
Problem 3: Prim's with Distance Constraints
You're designing a network where each connection has a cost (edge weight) and you want to 
minimize total cost, but with a constraint: no node can be more than D hops (edges) away from a 
designated center node. Modify Prim’s algorithm to build a minimum spanning tree rooted at a 
center node where every node is at most D edges away from the center. Provide pseudocode for 
your modification. What is the time complexity?

Key ideas:
1. Track depth of each node from center
2. Only add edges to PQ if target node would be within depth D
3. Skip edges during extraction if they violate depth constraint
4. Start from specified center node (not arbitrary node)


Algorithm: Prim_DepthConstrained(graph, center, D)
Input: weighted graph, center node, max depth D
Output: MST with depth ≤ D from center, or "IMPOSSIBLE“
MST ← empty set
inMST ← {center}
depth[center] ← 0
PQ ← priority queue of (edge, targetNode, depthOfTarget)
// Initialize with edges from center
for each neighbor v of center do
    depth[v] ← 1
    PQ.insert((weight(center, v), v, 1), priority = weight(center, v))
end for
while PQ is not empty AND inMST.size() < V do
    (edge (u, v), targetDepth) ← PQ.extractMin()
    if v in inMST then
        continue // Already added
    end if
if targetDepth > D then
    continue // Violates depth constraint, skip this edge
end if
add v to inMST
add edge (u, v) to MST
depth[v] ← targetDepth
// Add edges from newly added node v
for each neighbor w of v where w not in inMST do
    if depth[v] + 1 ≤ D then // Only add if within depth limit
        PQ.insert((weight(v, w), w, depth[v] + 1),
        priority = weight(v, w))
    end if
end for
end while
if inMST.size() = V then
    return MST
else
    return "IMPOSSIBLE"
end if

Time complexity: O((E + V) log V) with heap
◦ Same as standard Prim's—the depth checks are O(1)
◦ Each edge considered at most once, each vertex added once


"""
#==================================================================================

#==================================================================================
"""
Problem 4
How can the number of strongly connected components of a graph 
change if a new edge is added?


Adding an edge cannot increase the number of strongly connected components.
◦ Strongly connected components are maximal sets of mutually reachable vertices. Adding a new edge can only create 
new paths, not destroy existing ones. So components cannot split into more parts.
The number of strongly connected components can either:
◦ Stay the same, if the new edge does not create any new cycles between different strongly connected components.
Example
: If you add an edge from a vertex in the strongly connected component A to a vertex in the strongly 
connected component B, but there is no path from B back to A, then the strongly connected components remain 
unchanged.
◦ Decrease, if the new edge connects two or more strongly connected components in such a way that they become 
mutually reachable.
Example
: If you add an edge from a vertex in the strongly connected component A to a vertex in the strongly 
connected component B, and there is already a path from B back to A, then A and B merge into a single strongly 
connected component. More generally, several strongly connected components could merge along a chain, so the count 
decreases by at least 1
"""
#==================================================================================

#==================================================================================
"""
"""
#==================================================================================