#  Write an O(n)-time nonrecursive procedure that, given an n-node binary
#  tree, prints out the key of each node in the tree. Use a stack as an auxiliary
#  data structure.

# PRINT-BINARY-TREE(T, S)
#     PUSH(S, T.root)
#     while !STACK-EMPTY(S)
#         x = S[S.top]
#         while x != NIL      // store all nodes on the path towards the leftmost leaf
#             PUSH(S, x.left)
#             x = S[S.top]
#         POP(S)              // S has NIL on its top, so pop it
#         if !STACK-EMPTY(S)  // print this nodes, leap to its in-order successor
#             x = POP(S)
#             print x.key
#             PUSH(S, x.right)

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def print_preorder(root):
    #simpler iterative preorder- also O(n)
    if not root:
        return
    
    stack =[root]
    while stack:
        node = stack.pop()
        print(node.key, end = ' ')

        #push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def print_binary_tree(root):
    """Iterative in-order traversal using stack - O(n) time, O(h) space"""
    stack = [root]
    
    while stack:
        x = stack[-1]
        
        # Push all left children
        while x is not None:
            stack.append(x.left)
            x = stack[-1]
        
        stack.pop()  # Remove NIL
        
        if stack:
            x = stack.pop()
            print(x.key, end=' ')
            stack.append(x.right)

# Test with your tree from earlier (rooted at 6)
nodes = {i: Node(key) for i, (key, _, _) in {
    1: (17, 8, 9), 4: (20, 10, None), 6: (15, 1, 4),
    8: (22, None, None), 9: (13, 3, 7), 10: (25, None, 5),
    3: (12, None, None), 7: (28, None, None), 5: (33, 2, None),
    2: (14, None, None)
}.items()}

# Connect nodes
for i, (_, l, r) in {1: (17, 8, 9), 4: (20, 10, None), 6: (15, 1, 4),
                      8: (22, None, None), 9: (13, 3, 7), 10: (25, None, 5),
                      3: (12, None, None), 7: (28, None, None), 5: (33, 2, None),
                      2: (14, None, None)}.items():
    nodes[i].left = nodes[l] if l else None
    nodes[i].right = nodes[r] if r else None

print_binary_tree(nodes[6])  # Output: 22 17 12 13 28 15 25 14 33 20
print("\n")
print_preorder(nodes[6]) 