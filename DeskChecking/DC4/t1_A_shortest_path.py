

'''
The following code implements an A* shortest path algorithm. 
The used heuristic is the Euclidean distance (the standard 2-D plane distance). 
The Graph object is created accordingly to the reported init method.
The parameters of the method are rather intricate so let's go through them:

-Graph: the object that represents the graph, contains a dictionary nodes whose keys are Tuples 
(x and y coordinates of the nodes) and whose values are the the weights of the nodes. 
The object also contains a dictionary edges that consists of a dictionary within a dictionary
(edges[source][end] 
returns the cost of the edge between source and end). Every entry represents a undirected graph. 
We will not use the weight of nodes.

-source_id: the x and y coordinates of the source point.

-end_id: the x and y coordinates of the end point.
h: the function that computes the distance between 2 nodes. 
It simply computes the Euclidean distance between the nodes, in our case the second node will always be end_id. 
You can assume it is correct.

The function then returns a list of tuples, which represent the shortest path just found. 
The function reconstruct path is a utility function that reconstructs the path in the correct output format, 
you can assume it is correct.
Just a reminder: in A* algorithms, the g function usually refers to the distance from the source, 
the h function refers to the heuristic score of a node and the f function is the sum of the g-score and the h-score.
'''


""" PSEUDOCODE

Define class Graph
    Define __init__
        Create dictionary for nodes (key: coordinates, value: weight)
        Create dictionary for edges (key: source coordinates, value: destination coordinates and cost)
 
Define astar shortest path(Graph, sourceid, end id)
    Create open set dictionary and put starting node in it
    Create came from dictionary
    Create f_score dictionary
    Create g_score dictionary
    For every node in the graph
        Set the f and g_score to infinite for every node
    Set the g_score of the starting node to 0
    Compute and set the h_score for the starting node

    As long as there are nodes in the open set dictionary
        Set the current_score to infinite
        For every node in the open set
            If the current node f_score is lower than the current_score then
                set the current node as the best node and the current_score to the best node f_score

        If the best node is the end id node then return the path so far

        Remove the current node from the open set

        For every neighbour of the current node
            Compute potential g_score
            If the potential g_score is lower than the neighbour g_score (if we have just found a shortest path)
                Then set the current node as the parent node for the neighbour
                Update its g_score
                Compute and update its f_score
                If the neighbour is not in the open set then add it

    Return an empty list
"""


class Graph:
    def __init__ (self):
        self.nodes: dict[Tuple, int] = {}
        self.edges: dict[Tuple, dict[Tuple, int]] = {}

def astar shortest path(G: Graph, source_id: Tuple, end_id: Tuple, h):
    open_set = {source_id}
    came_from = {}
    g_score = dict()#line 9
    f_score = dict()#line 10
    for node in G.nodes:
        g_score[node] = float('inf')
        f_score[node] = float('inf')
    g_score[source_id] = 0
    f_score[source_id] = h(source_id, end_id)
 
    while open set:
        current = (-1,-1)
        current_score = 0
      #corrdction
        #current_score = float('inf')
            for node in open set:
                if f_score[node]<current_score:
                    current = node
                    current_score = f_score[node]
 
        if current == end_id:
        return reconstruct_path(came_from, current)
 
        open set.remove(current)
        for neighbor in G.edges[current]:
            tentative_g_score = g_score[current] + G.edges[current][neighbor]
            if tentative_g_score<g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score - h(neighbor, end_id) #line34
              #correction
                #f_score[neighbor] = tentative_g_score + h(neighbor, end_id) #line34
                if neighbor not in open set:
                    open set.add(neighbor)
    return []


"""
which are true:

-On line 34, the f score is wrongly computed, it should be the sum of the g and h functions.  TRUE

-On lines 9 and 10, the dictionaries will behave differently from the ones created with {}, using
 dict() is indeed an incorrect way of creating a dictionary. 

-The current score initialization to 0 will prevent any new path from being found, it should 
instead be set to float('inf'). TRUE

-On line 34 when using h(neighbor, end) we should also take into consideration the path
 that has been taken so far before computing the heuristic score.


• It is true, the f score is the sum of the distance from the score and the heuristic score of a
given point, subtracting one from the other makes no sense. We want to sum them to take
into consideration both the distance from the source and the distance from the destination.

• Both methods are correct methods for initializing a dictionary in python. The dict() way
is a built-in function that makes the initialization more clear. The dictionary will behave in
the same manner once created.
 
• The current_score set to 0 will prevent any node with a better score from being picked.
 The current_score should be set to infinite since any new score value should be picked in
 the first place, and of course no node will have an f score of 0, unless the source node = end
 node, but in that case it would not make any sense to use this algorithm.

• The whole point of a heuristic is to give a rough estimation of how good a node is with
 respect to its closeness to the destination. The heuristic value has to do only with the
 current point and the final destination, not with the path, it is a score that measures the
 closeness of a node with respect to another node.

 """
