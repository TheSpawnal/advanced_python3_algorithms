
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# Build the tree
n5 = Node(5)
n10 = Node(10, n5)
n20 = Node(20, n10)
n40 = Node(40)
n30 = Node(30, n20, n40)

n55 = Node(55)
n60 = Node(60, n55)
n90 = Node(90)
n80 = Node(80, n60, n90)
n70 = Node(70, None, n80)

root = Node(50, n30, n70)


#visit root, then left subtree, then right subtree
def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)

#visit left subtree, then root, then right subtree
def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)

#visit left subtree, then right subtree, then root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')


#BFS level order
#visit nodes level by level, left to right.
from collections import deque

def levelorder(root):
    if not root:
        return
    queue = deque([root])
    while queue: 
        node = queue.popleft()
        print(node.key, end =' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
#purpose: find shortest path, serialize tree



# Comparison & Memory Aid

# | Traversal    | When to process root | Use case |
# |-----------    |---------------------|----------|
# | **Pre-order** | **Before** children | Copy tree, prefix notation |
# | **In-order**  | **Between** children| BST → sorted, infix notation |
# | **Post-order** | **After** children | Delete tree, postfix notation |
# | **Level-order** | **By level**      | BFS, serialization |