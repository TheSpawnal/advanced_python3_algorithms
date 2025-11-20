
# The left-child, right-sibling representation of an arbitrary rooted tree uses 
# three pointers in each node: left-child, right-sibling, and parent. 
# From any node, its parent can be reached and identified in constant time and 
# all its children can be reached and identified in time linear in the number of 
# children. Show how to use only two pointers and one boolean value in each node 
# so that the parent of a node or all of its children can be reached and identified 
# in time linear in the number of children.

class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_sibling = None  # Overloaded: sibling OR parent
        self.is_leftmost = False

class TwoPointerTree:
    def __init__(self, root_key):
        self.root = Node(root_key)
        self.root.is_leftmost = True  # Root has no siblings
    
    def add_children(self, parent, *child_keys):
        """Add children to a parent node - maintains the invariant"""
        if not child_keys:
            return []
        
        children = [Node(key) for key in child_keys]
        
        # First child is leftmost
        children[0].is_leftmost = True
        children[0].right_sibling = parent  # Points to parent!
        parent.left_child = children[0]
        
        # Other children point to next sibling
        for i in range(1, len(children)):
            children[i].is_leftmost = False
            children[i-1].right_sibling = children[i]  # Previous points to current
            
        # Last child points to parent
        children[-1].right_sibling = parent
        
        return children
    
    def get_parent(self, node):
        """O(k) where k = number of siblings"""
        if node == self.root:
            return None
        
        if node.is_leftmost:
            # Easy: right_sibling IS the parent
            return node.right_sibling
        
        # Traverse sibling chain backwards to leftmost
        # The rightmost sibling's right_sibling is parent
        current = node
        while current.right_sibling:
            if current.right_sibling.is_leftmost or \
               current.right_sibling.left_child is not None:
                # Found parent
                return current.right_sibling
            current = current.right_sibling
        
        return current.right_sibling
    
    def get_children(self, node):
        """O(k) where k = number of children"""
        children = []
        child = node.left_child
        
        if child is None:
            return children
        
        # Traverse sibling chain
        while child:
            children.append(child)
            
            # Stop when we loop back to parent
            if child.right_sibling == node:
                break
            
            # If not leftmost, continue to next sibling
            if not child.is_leftmost:
                child = child.right_sibling
            else:
                # Leftmost has only one "next" if there are siblings
                # Actually, we need to reconsider...
                break
        
        # Better implementation:
        children = []
        child = node.left_child
        if child:
            children.append(child)
            # Follow sibling chain until we hit parent again
            while child.right_sibling != node:
                child = child.right_sibling
                children.append(child)
        
        return children


# Example: Build tree
#       A
#      /|\
#     B C D
#    /|
#   E F

# tree = TwoPointerTree('A')

# # Add children to A: B, C, D
# B, C, D = tree.add_children(tree.root, 'B', 'C', 'D')

# # Add children to B: E, F
# E, F = tree.add_children(B, 'E', 'F')

# # Test get_parent
# print("Parent of B:", tree.get_parent(B).key)  # Should be A
# print("Parent of C:", tree.get_parent(C).key)  # Should be A
# print("Parent of E:", tree.get_parent(E).key)  # Should be B

# # Test get_children
# print("Children of A:", [n.key for n in tree.get_children(tree.root)])  # [B, C, D]
# print("Children of B:", [n.key for n in tree.get_children(B)])  # [E, F]
# print("Children of D:", [n.key for n in tree.get_children(D)])  # []

# # Verify structure
# print("\nStructure verification:")
# print(f"B.is_leftmost: {B.is_leftmost}")  # True
# print(f"C.is_leftmost: {C.is_leftmost}")  # False
# print(f"B.right_sibling == A: {B.right_sibling == tree.root}")  # True (points to parent!)
# print(f"C.right_sibling == D: {C.right_sibling == D}")  # True (points to sibling)
# ```

# ## Complexity Analysis

# | Operation | Time Complexity |
# |-----------|----------------|
# | Get parent | O(k) where k = # of siblings |
# | Get children | O(k) where k = # of children |
# | Space per node | 2 pointers + 1 boolean |

## Key Insight Visualization
# ```
# Normal LCRS:          Our 2-pointer version:
#     A                     A
#    ↙ ↘                   ↙
#   B → C → D             B ⟲ (is_leftmost=T, points back to A)
#                          ↓
#                         C (is_leftmost=F, points to D)
#                          ↓
#                         D ⟲ (points back to A)