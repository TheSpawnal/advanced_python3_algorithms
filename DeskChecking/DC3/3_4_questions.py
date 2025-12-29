'''
 Which of the following statement(s) are true:

 When looking for an element in a tree we must perform both a BFS and a DFS since the BFS
 will look for the items at the same level of the starting point and the DFS will look for the
 items on the branch starting from the starting point. Using only one of them may exclude
 some items from the search.FALSE

 Dijkstra’s algorithm can find the shortest path only for acyclical graphs, if cycles are in the
 graph then we need to use A* that will instead follow its heuristic without being tricked into
 the cycles. FALSE

√ Dijkstra’s algorithm runs on an unweighted graph (every edge has the same weight), works
 just like a classic BFS search. TRUE
 
 • BFS and DFS look for items within a tree. The way they operate is similar but they simply
 follow different paths, DFS explores the tree vertically first while BFS explores it breadth
 first. Regardless of the order they’ll both check out every element, so using one of them is
 totally fine, we do not need to use both at the same time.
 
 • Dijkstra’s algorithm works also in cyclical graphs, since it will not revisit the exact same
 path twice. But it could visit the same node multiple times to try find a shorter path to it.
 
 • Dijkstra’s algorithm works just like BFS when no difference in weights between the edges
 is found. This is because Dijkstra is going to take the next node with the shortest distance
 from the source. Dijkstra is essentially a BFS with respect to the edge weights rather than
 the topology (BFS is guided by topology, not edge weights).

 '''
