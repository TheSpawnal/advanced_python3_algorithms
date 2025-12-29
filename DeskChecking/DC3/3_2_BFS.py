#Breadth-FirstSearch, it simply looks whether it is possible to reach the destination node starting from the source node.

# Pseudocode

# Define bfs(graph, start, target)
#     Create a set for the visited nodes
#     Create a queue with the start node
#     While there are nodes in the queue
#         Set the current node to the first node in the queue
#         If the current node is the target then return true
#         Add the current node to the visited set
#         For every neighbour of the current node
#             If the neighbour is not in the visited set add it to the queue
#     Return false


def bfs(graph, start, target):
    visited = set()
    queue = [start]

    while queue:
        currentnode = queue.pop(0)
        if currentnode == target:
            return True

        visited.add(currentnode)
        for neighbor in graph[currentnode]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
'''
which are true:

-the code will not work in case the graph is cyclical

-the pop method does not have parameter, it can just pop the last element.

-the method correctly implements a BFS . TRUE

- the method would work only for directed graphs and not for undirected graphs.

solutions:

• The code works in both cyclical and acyclical graphs, nodes in cycles will not be visited
twice since they are stored in the visited set and filtered at line 28.

• Even though the pop concept is derived from stacks where only the last element can be
popped, in Python lists the pop method can take a parameter, which is the index of the
element to remove and then delete. If no parameter is passed, the last item will be deleted
just like in the classic pop concept.

• It does implement a BFS, it checks all nodes at the same depth before moving onto the
deeper layer.

• Being directed or non directed is irrelevant since the edges would be represented in the edge
list. In non directed graphs there will be an item in the list of two vertices instead of just
one
'''
