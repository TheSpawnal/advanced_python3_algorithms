
# Explain how to implement doubly linked lists using only one pointer value
#  x.np per item instead of the usual two (next and prev). Assume that all
#  pointer values can be interpreted as k-bit integers, and define x.np = x.next
#  XOR x.prev, the k-bit “exclusive-or” of x.next and x.prev. The value NIL is
#  represented by 0. Be sure to describe what information you need to access
#  the head of the list. Show how to implement the SEARCH, INSERT, and
#  DELETE operations on such a list. Also show how to reverse such a list in
#  O(1) time


# LIST-SEARCH(L, k)
#     prev = NIL
#     x = L.head
#     while x != NIL and x.key != k
#         next = prev XOR x.np
#         prev = x
#         x = next
#     return x

# LIST-INSERT(L, x)
#     x.np = NIL XOR L.tail
#     if L.tail != NIL
#         L.tail.np = (L.tail.np XOR NIL) XOR x   // tail.prev XOR x
#     if L.head == NIL
#         L.head = x
#     L.tail = x

# LIST-DELETE(L, x)
#     y = L.head
#     prev = NIL
#     while y != NIL
#         next = prev XOR y.np
#         if y != x
#             prev = y
#             y = next
#         else
#             if prev != NIL
#                 prev.np = (prev.np XOR y) XOR next  // prev.prev XOR next
#             else L.head = next
#             if next != NIL
#                 next.np = prev XOR (y XOR next.np)  // prev XOR next.next
#             else L.tail = prev

# LIST-REVERSE(L)
#     tmp = L.head
#     L.head = L.tail
#     L.tail = tmp


class Node:
    """Node for XOR linked list."""
    def __init__(self, data):
        self.data = data
        self.np = 0  # XOR of next and prev (stored as integers)
    
    def __repr__(self):
        return f"Node({self.data})"


class XORLinkedList:
    """
    XOR Linked List - uses only one pointer per node.
    Each node stores: np = prev XOR next
    
    Why we need head AND tail:
    - head: to start traversal forward
    - tail: to start traversal backward OR to insert at end in O(1)
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._nodes = {}  # id(node) -> node (for memory simulation)
    
    def _xor(self, a, b):
        """XOR two node references (using their ids)."""
        id_a = id(a) if a else 0
        id_b = id(b) if b else 0
        return id_a ^ id_b
    
    def _get_node(self, xor_id):
        """Convert XOR result back to node reference."""
        if xor_id == 0:
            return None
        return self._nodes.get(xor_id)
    
    def _register_node(self, node):
        """Register node in our lookup table."""
        if node:
            self._nodes[id(node)] = node
    
    def insert(self, data):
        """
        Insert at the end of the list.
        
        Pseudocode:
            x.np = NIL XOR L.tail
            if L.tail != NIL
                L.tail.np = (L.tail.np XOR NIL) XOR x
            if L.head == NIL
                L.head = x
            L.tail = x
        """
        new_node = Node(data)
        self._register_node(new_node)
        
        # x.np = NIL XOR L.tail
        new_node.np = self._xor(None, self.tail)
        
        # if L.tail != NIL
        if self.tail is not None:
            # L.tail.np = (L.tail.np XOR NIL) XOR x
            # This updates old tail's np to point to new node
            # Old tail had: np = prev XOR NIL
            # New should be: np = prev XOR new_node
            tail_prev = self._get_node(self.tail.np ^ 0)  # tail.np XOR NIL
            self.tail.np = self._xor(tail_prev, new_node)
        
        # if L.head == NIL
        if self.head is None:
            self.head = new_node
        
        # L.tail = x
        self.tail = new_node
        
        print(f"Inserted {data}")
    
    def search(self, key):
        """
        Search for a node with given key.
        
        Pseudocode:
            prev = NIL
            x = L.head
            while x != NIL and x.key != k
                next = prev XOR x.np
                prev = x
                x = next
            return x
        """
        print(f"\nSearching for {key}...")
        
        prev = None
        x = self.head
        
        while x is not None and x.data != key:
            # next = prev XOR x.np
            next_node = self._get_node(self._xor(prev, None) ^ x.np)
            print(f"  Current: {x.data}, moving to next...")
            prev = x
            x = next_node
        
        if x:
            print(f"  Found: {x.data}")
        else:
            print(f"  Not found")
        return x
    
    def delete(self, key):
        """
        Delete node with given key.
        
        Pseudocode:
            y = L.head
            prev = NIL
            while y != NIL
                next = prev XOR y.np
                if y != x
                    prev = y
                    y = next
                else
                    if prev != NIL
                        prev.np = (prev.np XOR y) XOR next
                    else L.head = next
                    if next != NIL
                        next.np = prev XOR (y XOR next.np)
                    else L.tail = prev
        """
        print(f"\nDeleting {key}...")
        
        y = self.head
        prev = None
        
        while y is not None:
            # next = prev XOR y.np
            next_node = self._get_node(self._xor(prev, None) ^ y.np)
            
            if y.data != key:
                prev = y
                y = next_node
            else:
                # Found the node to delete
                # if prev != NIL
                if prev is not None:
                    # prev.np = (prev.np XOR y) XOR next
                    prev_prev = self._get_node(prev.np ^ id(y))
                    prev.np = self._xor(prev_prev, next_node)
                else:
                    # L.head = next
                    self.head = next_node
                
                # if next != NIL
                if next_node is not None:
                    # next.np = prev XOR (y XOR next.np)
                    next_next = self._get_node(next_node.np ^ id(y))
                    next_node.np = self._xor(prev, next_next)
                else:
                    # L.tail = prev
                    self.tail = prev
                
                # Clean up
                del self._nodes[id(y)]
                print(f"  Deleted {key}")
                return
        
        print(f"  {key} not found")
    
    def reverse(self):
        """
        Reverse the list in O(1) time!
        
        Pseudocode:
            tmp = L.head
            L.head = L.tail
            L.tail = tmp
        """
        print("\nReversing list...")
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        print("  Reversed!")
    
    def traverse_forward(self):
        """Traverse from head to tail."""
        print("\nTraverse Forward:")
        if self.head is None:
            print("  (empty)")
            return
        
        elements = []
        prev = None
        current = self.head
        
        while current is not None:
            elements.append(str(current.data))
            # next = prev XOR current.np
            next_node = self._get_node(self._xor(prev, None) ^ current.np)
            prev = current
            current = next_node
        
        print(f"  {' -> '.join(elements)}")
    
    def traverse_backward(self):
        """Traverse from tail to head."""
        print("\nTraverse Backward:")
        if self.tail is None:
            print("  (empty)")
            return
        
        elements = []
        next_node = None
        current = self.tail
        
        while current is not None:
            elements.append(str(current.data))
            # prev = next XOR current.np
            prev = self._get_node(self._xor(None, next_node) ^ current.np)
            next_node = current
            current = prev
        
        print(f"  {' -> '.join(elements)}")


# Demonstration
def main():
    print("="*60)
    print("XOR LINKED LIST DEMONSTRATION")
    print("="*60)
    
    xor_list = XORLinkedList()
    
    print("\n--- INSERT OPERATIONS ---")
    xor_list.insert(10)
    xor_list.insert(20)
    xor_list.insert(30)
    xor_list.insert(40)
    xor_list.insert(50)
    
    xor_list.traverse_forward()
    xor_list.traverse_backward()
    
    print("\n--- SEARCH OPERATIONS ---")
    xor_list.search(30)
    xor_list.search(99)
    
    print("\n--- DELETE OPERATIONS ---")
    xor_list.delete(30)  # Delete middle
    xor_list.traverse_forward()
    
    xor_list.delete(10)  # Delete head
    xor_list.traverse_forward()
    
    xor_list.delete(50)  # Delete tail
    xor_list.traverse_forward()
    
    print("\n--- REVERSE OPERATION (O(1)!) ---")
    xor_list.reverse()
    xor_list.traverse_forward()
    xor_list.traverse_backward()
    
    print("\n--- MORE OPERATIONS ---")
    xor_list.insert(100)
    xor_list.traverse_forward()
    
    xor_list.reverse()
    xor_list.traverse_forward()


if __name__ == "__main__":
    main()


# Why Reverse is O(1)
# In a normal doubly linked list, reversing requires O(n) time to swap all prev/next pointers.
# In XOR list:
# python# Before: head → [A] ⊕ [B] ⊕ [C] ← tail
# # After:  head → [C] ⊕ [B] ⊕ [A] ← tail

# # Just swap head and tail pointers!
# tmp = head
# head = tail  
# tail = tmp
# The XOR values don't change! Node B still has np = A XOR C, which works for both directions.
# Key Insights

# Need both head AND tail - for bidirectional traversal and O(1) operations
# Must track previous node during traversal - this "unlocks" the XOR
# Space savings: 1 pointer vs 2 (50% reduction)
# Trade-off: More complex logic, can't directly access prev/next
# Reverse is free: O(1) by swapping head/tail

# Run this code and observe how the XOR magic works! 🐉✨