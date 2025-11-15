# Write an O(n)-time procedure that prints all the keys of an arbitrary rooted tree with 
# n nodes, where the tree is stored using the left-child, right-sibling representation.

# PRINT-LCRS-TREE(T)
#     PRINT-LCRS-NODE(T.root)

# PRINT-LCRS-NODE(x)
#     if x != NIL
#         print x.key
#         PRINT-LCRS-NODE(x.left-child)
#         PRINT-LCRS-NODE(x.right-sibling)

class LCRSNode:
    """Left-Child, Right-Sibling Tree Node"""
    def __init__(self, key):
        self.key = key
        self.left_child = None      # First child
        self.right_sibling = None   # Next sibling
    
    def __repr__(self):
        return f"Node({self.key})"


def print_lcrs_tree(node):
    """
    Print all keys in a left-child, right-sibling tree.
    Time Complexity: O(n) - visits each node exactly once
    """
    if node is not None:
        print(node.key, end=' ')
        print_lcrs_tree(node.left_child)      # Visit all descendants
        print_lcrs_tree(node.right_sibling)   # Visit all siblings


def print_lcrs_tree_verbose(node, depth=0, is_sibling=False):
    """
    Print tree with indentation to show structure
    """
    if node is not None:
        prefix = "  " * depth
        if is_sibling:
            print(f"{prefix}└─ Sibling: {node.key}")
        else:
            print(f"{prefix}└─ Child: {node.key}" if depth > 0 else f"Root: {node.key}")
        
        # Visit first child (go deeper)
        print_lcrs_tree_verbose(node.left_child, depth + 1, False)
        # Visit next sibling (same level)
        print_lcrs_tree_verbose(node.right_sibling, depth, True)


# Example 1: Simple tree
#       A
#      /|\
#     B C D
#    /|
#   E F

def create_example_tree1():
    """
    Tree structure:
           A
          /|\
         B C D
        /|
       E F
    """
    A = LCRSNode('A')
    B = LCRSNode('B')
    C = LCRSNode('C')
    D = LCRSNode('D')
    E = LCRSNode('E')
    F = LCRSNode('F')
    
    # A's children: B, C, D
    A.left_child = B
    B.right_sibling = C
    C.right_sibling = D
    
    # B's children: E, F
    B.left_child = E
    E.right_sibling = F
    
    return A


# Example 2: More complex tree
#           1
#        /  |  \
#       2   3   4
#      /|   |   |\
#     5 6   7   8 9
#               |
#              10

def create_example_tree2():
    """
    More complex tree to demonstrate O(n) complexity
    """
    nodes = {i: LCRSNode(i) for i in range(1, 11)}
    
    # Level 1: root
    root = nodes[1]
    
    # Level 2: 1's children are 2, 3, 4
    root.left_child = nodes[2]
    nodes[2].right_sibling = nodes[3]
    nodes[3].right_sibling = nodes[4]
    
    # Level 3: 2's children are 5, 6
    nodes[2].left_child = nodes[5]
    nodes[5].right_sibling = nodes[6]
    
    # Level 3: 3's child is 7
    nodes[3].left_child = nodes[7]
    
    # Level 3: 4's children are 8, 9
    nodes[4].left_child = nodes[8]
    nodes[8].right_sibling = nodes[9]
    
    # Level 4: 8's child is 10
    nodes[8].left_child = nodes[10]
    
    return root


# Example 3: Convert from the problem's binary tree representation
def convert_binary_to_lcrs(nodes_dict, root_index):
    """
    Convert the binary tree from your problem to LCRS representation.
    In a binary tree, left and right children become:
    - left child → left_child
    - right child → left_child's right_sibling
    """
    class BinaryNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    
    # Create binary nodes
    binary_nodes = {}
    for idx, (key, left, right) in nodes_dict.items():
        binary_nodes[idx] = BinaryNode(key)
    
    # Connect binary tree
    for idx, (key, left, right) in nodes_dict.items():
        if left:
            binary_nodes[idx].left = binary_nodes[left]
        if right:
            binary_nodes[idx].right = binary_nodes[right]
    
    # Convert to LCRS
    def binary_to_lcrs(binary_node):
        if not binary_node:
            return None
        
        lcrs_node = LCRSNode(binary_node.key)
        
        # Left child of binary becomes left_child of LCRS
        if binary_node.left:
            lcrs_node.left_child = binary_to_lcrs(binary_node.left)
            
            # Right child of binary becomes right_sibling of left child
            if binary_node.right:
                lcrs_node.left_child.right_sibling = binary_to_lcrs(binary_node.right)
        elif binary_node.right:
            # If only right child exists, it becomes the left_child
            lcrs_node.left_child = binary_to_lcrs(binary_node.right)
        
        return lcrs_node
    
    return binary_to_lcrs(binary_nodes[root_index])


# Testing
if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Simple Tree")
    print("=" * 50)
    tree1 = create_example_tree1()
    print("\nSimple print:")
    print_lcrs_tree(tree1)
    print("\n\nVerbose print:")
    print_lcrs_tree_verbose(tree1)
    
    print("\n" + "=" * 50)
    print("Example 2: Complex Tree")
    print("=" * 50)
    tree2 = create_example_tree2()
    print("\nSimple print:")
    print_lcrs_tree(tree2)
    print("\n\nVerbose print:")
    print_lcrs_tree_verbose(tree2)
    
    print("\n" + "=" * 50)
    print("Example 3: Your Binary Tree Converted to LCRS")
    print("=" * 50)
    nodes_data = {
        1: (17, 8, 9),
        2: (14, None, None),
        3: (12, None, None),
        4: (20, 10, None),
        5: (33, 2, None),
        6: (15, 1, 4),
        7: (28, None, None),
        8: (22, None, None),
        9: (13, 3, 7),
        10: (25, None, 5)
    }
    tree3 = convert_binary_to_lcrs(nodes_data, 6)
    print("\nSimple print:")
    print_lcrs_tree(tree3)
    print("\n\nVerbose print:")
    print_lcrs_tree_verbose(tree3)