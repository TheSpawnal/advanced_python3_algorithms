# In the following code the path from start to end is going to be searched with a depth-first
#  algorithm. The graph passed to the function is an edge list, represented by a dictionary where
#  the key is the vertex and its value is a list of the vertices it is connected to.

# Define dfs(graph, start, end)
#     Create the stack to track nodes and their paths
#     Put the start node in the stack with itself as the first node of the path
#     While there are values in the stack
#         Pop the stack, returning the starting node and the path
#         If the most recently extracted node is the end node, then return the
#             path that was just returned
#         For every neighbour of the most recently returned node
#             If the neighbour is not in the path that was just returned, then
#                 append the neighbour node to the current path, and append the
#                     node and the updated path to the top of the stack
#     Return None


def dfs(graph, start, end):
    stack = [(start, [start])]
    while stack:
        node, path = stack[-1]
        del stack[-1]
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                new_index = len(stack)
                stack[new_index] = (neighbor, path + [neighbor])
    return None

""""
Which of the following statement(s) about the implementation above are true:

-The pop " node, path = stack[-1]" is not correctly implemented, we must use the pop() method instead. 
That code will prevent the correct popping. False

-On line :
        node, path = stack[-1]
        del stack[-1]
we cannot return and delete the index-1 since it will raise an IndexError not having the index-1 in the list. False

-On line :
stack[new_index] = (neighbor, path + [neighbor])
we cannot append to the list by using the index, we should use the append() method instead.True

-This is not a depth-first search but a breadth-first search. In order to make it a DFS we should
start from the bottom, which in this case is the end node. False

solutions:
• The pop consists in returning the last item of a list and deleting it from the list itself. The
pop() does it all in one method, in this case it’s simply been re-implemented.

• You can indeed get negative indices out of an array, a negative index means that the index
count should start from the end of the list. [-1] means the last item, [-2] means the second
last, and so on.

• We cannot refer a position in the list that has never been initialized, since the stack didn’t
have the new index position assigned (because it was new 0, meaning the last index is new
index but indexing starts fromindex-1). Therefore we need to use the append() method
to add an item at the end of the list.

• This is indeed a DFS algorithm since we always look at the current node’s children first. We
do not need to ”start from the bottom” in order to have a DFS.
"""


#corrected version:
def dfs(graph, start, end):
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    return None