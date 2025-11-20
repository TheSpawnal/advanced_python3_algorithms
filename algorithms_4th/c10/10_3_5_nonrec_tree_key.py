#  Write an O(n)-time nonrecursive procedure that, given an n-node binary
#  tree, prints out the key of each node. Use no more than constant extra space
#  outside of the tree itself and do not modify the tree, even temporarily,
#  during the procedure.

#Morris-like traversal variant that uses parent pointer instead of a stack or tree modification.
# o(1) space solution.

# Strategy
# Core Idea: Track where we came from (prev) to decide where to go next:

# Coming from parent → print node, go left (or right if no left, or back up)
# Coming from left child → go right (if exists, else back up)
# Coming from right child → go back up to parent

# This creates a pre-order traversal (root-left-right) without extra space.
# Corrected Algorithm (original has typos)

# PRINT-KEY(T)
#     prev = NIL
#     x = T.root
#     while x != NIL
#         if prev == x.parent              # Coming down from parent
#             print x.key
#             prev = x
#             if x.left != NIL
#                 x = x.left
#             elif x.right != NIL
#                 x = x.right
#             else
#                 x = x.parent
#         elif prev == x.left              # Coming up from left
#             prev = x
#             if x.right != NIL
#                 x = x.right
#             else
#                 x = x.parent
#         else                             # Coming up from right
#             prev = x
#             x = x.parent


class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def print_key(root):
    """O(n) time, O(1) space - uses parent pointers"""
    prev = None
    x = root
    
    while x is not None:
        if prev == x.parent:  # Coming down from parent
            print(x.key, end=' ')
            prev = x
            if x.left:
                x = x.left
            elif x.right:
                x = x.right
            else:
                x = x.parent
        
        elif prev == x.left:  # Coming up from left subtree
            prev = x
            if x.right:
                x = x.right
            else:
                x = x.parent
        
        else:  # Coming up from right subtree (or right is None)
            prev = x
            x = x.parent

# Build example tree with parent pointers
#       15
#      /  \
#    17    20
#   /  \   /
#  22  13 25
#     / \   \
#    12 28  33
#            /
#           14

def build_tree():
    n15 = Node(15)
    n17 = Node(17, n15)
    n20 = Node(20, n15)
    n22 = Node(22, n17)
    n13 = Node(13, n17)
    n25 = Node(25, n20)
    n12 = Node(12, n13)
    n28 = Node(28, n13)
    n33 = Node(33, n25)
    n14 = Node(14, n33)
    
    n15.left, n15.right = n17, n20
    n17.left, n17.right = n22, n13
    n20.left = n25
    n13.left, n13.right = n12, n28
    n25.right = n33
    n33.left = n14
    
    return n15

root = build_tree()
print("Pre-order traversal (O(1) space):")
print_key(root)  # Output: 15 17 22 13 12 28 20 25 33 14



# ## Trace Example
# Tree:     15
#          /  \
#        17    20
#        /
#       22

# Start: prev=None, x=15

# Step 1: prev==parent(None) → print 15, go left to 17
# Step 2: prev==parent(15) → print 17, go left to 22  
# Step 3: prev==parent(17) → print 22, no children → go up to 17
# Step 4: prev==left(22) → no right → go up to 15
# Step 5: prev==left(17) → go right to 20
# Step 6: prev==parent(15) → print 20, no children → go up to 15
# Step 7: prev==right(20) → go up to None → DONE