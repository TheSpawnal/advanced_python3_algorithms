
# STACK-EMPTY(L)
#     if L.head == NIL
#         return true
#     else return false

# PUSH(L, x)
#     x.next = L.head
#     L.head = x

# POP(L)
#     if STACK-EMPTY(L)
#         error "underflow"
#     else
#         x = L.head
#         L.head = L.head.next
#         return x


class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    """
    Stack implementation using singly linked list.
    
    Attributes needed:
    - head: Points to the top of the stack (most recent element)
    
    Optional:
    - size: Track number of elements for O(1) size queries
    """
    
    def __init__(self):
        self.head = None  # Top of stack (required)
        self.size = 0     # Optional: for O(1) size queries
    
    def is_empty(self):
        """
        Check if stack is empty.
        Time: O(1)
        """
        return self.head is None
    
    def push(self, x):
        """
        Push element onto stack.
        Time: O(1)
        
        Pseudocode:
            x.next = L.head
            L.head = x
        """
        new_node = Node(x)
        new_node.next = self.head  # Point new node to current top
        self.head = new_node       # Update head to new node
        self.size += 1
        print(f"PUSH({x})")
    
    def pop(self):
        """
        Pop and return top element.
        Time: O(1)
        
        Pseudocode:
            if STACK-EMPTY(L)
                error "underflow"
            else
                x = L.head
                L.head = L.head.next
                return x
        """
        if self.is_empty():
            raise IndexError("Stack underflow - cannot pop from empty stack")
        
        x = self.head              # Save top node
        self.head = self.head.next # Move head to next node
        self.size -= 1
        print(f"POP() -> {x.data}")
        return x.data
    
    def peek(self):
        """
        Return top element without removing.
        Time: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.data
    
    def get_size(self):
        """Return number of elements. Time: O(1) if we track size."""
        return self.size
    
    def display(self):
        """Display stack contents (top to bottom)."""
        if self.is_empty():
            print("Stack: []")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(f"Stack: {' -> '.join(elements)} (top -> bottom)")


# Demonstration
def demonstrate():
    """Demonstrate stack operations with visualization."""
    print("=== Stack Using Singly Linked List ===\n")
    
    stack = StackLinkedList()
    
    print("Initial state:")
    stack.display()
    print(f"Empty? {stack.is_empty()}\n")
    
    # Push operations
    print("--- Push Operations ---")
    stack.push(4)
    stack.display()
    print()
    
    stack.push(1)
    stack.display()
    print()
    
    stack.push(3)
    stack.display()
    print()
    
    # Pop operation
    print("--- Pop Operations ---")
    stack.pop()
    stack.display()
    print()
    
    # More operations
    stack.push(8)
    stack.display()
    print()
    
    stack.pop()
    stack.display()
    print()
    
    # Peek
    print(f"Peek: {stack.peek()}")
    stack.display()
    print()
    
    # Empty the stack
    print("--- Emptying Stack ---")
    while not stack.is_empty():
        stack.pop()
        stack.display()
    
    print(f"\nFinal state - Empty? {stack.is_empty()}")
    
    # Try to pop from empty stack
    print("\n--- Error Handling ---")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    demonstrate()
