


"""
The following code computes the most central edge, meant as the edge that is part of the highest
number of shortest paths, in this case, computed with Dijkstra's algorithm, 
which we can consider correct.
The dijkstra method returns the shortest path to every node in the graph starting from startid. 
The method return two dictionaries:

the distance dictionary encodes the shortest path length, but we will not need it.

The second dictionary encodes the parent of every node 
(the node before the last node in the shortest path starting from start id).

The graph edges is a dictionary where the key is the start id. 
Its values are a dictionary: its key is the endid and the value is the weight of the edge.


Define class Graph
    Define constructor
        Initialize node field as list of integers
        Initialize edges field as dictionary with integer keys and dictionary values with integer key and value

Define mostcentral(G)
    Initialize dictionary central d as the counter for the number of paths through every node

    For every node (start id) in the graph
        Get the distances and the last node parent for every shortest path in G from starting node start id
        For every node (end id) in graph
            Initialize path list with end id
            Reconstruct the shortest path backwards from end id to start id 
                (stops at−1 because if there is no parent then we are at node start id)
 
            If the path is a single edge then do not reconstruct it and go to next node
 
            For every edge int he path but the last
                Increase its value in central d (the counter dictionary)
 
    Return the key of the highest value in central 
"""    

class Graph:
    def __init__ (self) :
        self.nodes: List[int] = []
        self.edges: Dict[int, Dict[int, int]] = {}

def mostcentral(G: Graphs)−>int:
    central_d: Dict[int,int] = {}
    for e in G.edges:
        central_d[e] = 0

    for start_id in G.nodes:
        _, p = dijkstra(G, start_id) #line 12
        for end_id in G.nodes:
            path = [end_id]
            while path[-1] != -1:
                path.append(p[path[-1]])

            if path[-2] != start_id:
                continue#line 19

            for q in path[:-1]:
                central_d[q] ++ 1 #line 22

 return max(central_d, key=lambda key: central_d[key])

"""
which are true: 

-The return statement using max will not work since it does not correctly return the node with
 the most shortest paths passing through it.

-At line 22 using ++ will not increase the intended value by 1. TRUE

-At line 12 with _  we are effectively discarding the first of the two objects returned from
dijkstra. The first object is the length of every shortest path, and the second is the list of
parents for every node. Discarding the first will simply let us read the second return object
without saving the first. TRUE

-Thecontinue at line 19 will terminate the method too early by exiting most_central and
 continuing to the following code. This prevents all the paths from being analyzed, and
 consequently prevents getting a correct result.

explan:
+The return statement is a correct python expression that will return the key in central_d
 that has the highest result of the lambda expression, and the lambda expression returns the
 central_d value. It represents the number of shortest paths the edge is in.

• Using ++ as the postfix increment available in many languages does not represent a correct
 syntax for python. The correct syntax would instead be central_d[q] += 1.

• The _ is a discard operator, which indeed does not save the value assigned to it. It is often
used when we only care about saving some items of a tuple or only some of the values
returned by a function. It is not a way to effectively store the variable.

• The continue does not terminate the function by exiting it, it simply skips to the next value
 in the for loop that loops through G.nodes. We do not exit the loop but just skip to the
 next value without increasing the node count in central_d

 """



