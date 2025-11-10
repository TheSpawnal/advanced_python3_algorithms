//Implement a queue by a singly linked list 

QUEUE-EMPTY(L)
    if L.head == NIL
        return true
    else return false

ENQUEUE: inserts an element at the end of the list. 
In this case we need to keep track of the last element of the list. 
We can do that with a sentinel.

ENQUEUE(L, x)
    if QUEUE-EMPTY(L)
        L.head = x
    else L.tail.next = x
    L.tail = x
    x.next = NIL

DEQUEUE: removes an element from the beginning of the list.

DEQUEUE(L)
    if QUEUE-EMPTY(L)
        error "underflow"
    else
        x = L.head
        if L.head == L.tail
            L.tail = NIL
        L.head = L.head.next
        return x


class Node:
    """Node for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    """
    Queue implementation using singly linked list.
    
    Required Attributes:
    - head: Points to front of queue (for dequeue)
    - tail: Points to rear of queue (for enqueue)
    
    Optional:
    - size: Track number of elements
    """
    
    def __init__(self):
        self.head = None  # Front of queue (required)
        self.tail = None  # Rear of queue (required)
        self.size = 0     # Optional: for O(1) size queries
    
    def is_empty(self):
        """
        Check if queue is empty.
        Time: O(1)
        
        Pseudocode:
            if L.head == NIL
                return true
            else return false
        """
        return self.head is None
    
    def enqueue(self, x):
        """
        Insert element at the rear of the queue.
        Time: O(1)
        
        Pseudocode:
            if QUEUE-EMPTY(L)
                L.head = x
            else L.tail.next = x
            L.tail = x
            x.next = NIL
        """
        new_node = Node(x)
        new_node.next = None  # Explicitly set to None
        
        if self.is_empty():
            # First element - both head and tail point to it
            self.head = new_node
        else:
            # Link current tail to new node
            self.tail.next = new_node
        
        # Update tail to new node
        self.tail = new_node
        self.size += 1
        print(f"ENQUEUE({x})")
    
    def dequeue(self):
        """
        Remove and return element from front of queue.
        Time: O(1)
        
        Pseudocode:
            if QUEUE-EMPTY(L)
                error "underflow"
            else
                x = L.head
                if L.head == L.tail
                    L.tail = NIL
                L.head = L.head.next
                return x
        """
        if self.is_empty():
            raise IndexError("Queue underflow - cannot dequeue from empty queue")
        
        x = self.head  # Save front node
        
        # Special case: if this is the last element
        if self.head == self.tail:
            self.tail = None  # Queue will be empty
        
        # Move head to next node
        self.head = self.head.next
        self.size -= 1
        
        print(f"DEQUEUE() -> {x.data}")
        return x.data
    
    def peek(self):
        """
        Return front element without removing.
        Time: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data
    
    def get_size(self):
        """Return number of elements. Time: O(1)"""
        return self.size
    
    def display(self):
        """Display queue contents (front to rear)."""
        if self.is_empty():
            print("Queue: [] (empty)")
            print("head -> None, tail -> None")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(f"Queue: {' -> '.join(elements)} (front -> rear)")
        print(f"head -> {self.head.data}, tail -> {self.tail.data}")


# Demonstration
def demonstrate():
    """Demonstrate queue operations with visualization."""
    print("=== Queue Using Singly Linked List ===\n")
    
    q = QueueLinkedList()
    
    print("Initial state:")
    q.display()
    print(f"Empty? {q.is_empty()}\n")
    
    # Enqueue operations
    print("--- Enqueue Operations ---")
    q.enqueue(4)
    q.display()
    print()
    
    q.enqueue(1)
    q.display()
    print()
    
    q.enqueue(3)
    q.display()
    print()
    
    # Dequeue operation
    print("--- Dequeue Operations ---")
    q.dequeue()
    q.display()
    print()
    
    # More operations
    q.enqueue(8)
    q.display()
    print()
    
    q.dequeue()
    q.display()
    print()
    
    # Peek
    print(f"Peek (front element): {q.peek()}")
    q.display()
    print()
    
    # Dequeue until one element remains
    print("--- More Dequeues ---")
    q.dequeue()
    q.display()
    print()
    
    # Dequeue last element (special case: head == tail)
    print("--- Dequeue Last Element (head == tail case) ---")
    q.dequeue()
    q.display()
    print()
    
    # Try operations on empty queue
    print("--- Error Handling ---")
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}\n")
    
    # Rebuild queue
    print("--- Rebuild Queue ---")
    q.enqueue(10)
    q.display()
    print()
    
    q.enqueue(20)
    q.display()
    print()
    
    q.enqueue(30)
    q.display()


def test_edge_cases():
    """Test important edge cases."""
    print("\n\n=== Testing Edge Cases ===\n")
    
    q = QueueLinkedList()
    
    # Test 1: Single element
    print("Test 1: Single element enqueue/dequeue")
    q.enqueue(100)
    print(f"After enqueue(100): size={q.get_size()}")
    q.display()
    result = q.dequeue()
    print(f"Dequeued: {result}, size={q.get_size()}")
    q.display()
    print()
    
    # Test 2: Alternating enqueue/dequeue
    print("Test 2: Alternating operations")
    q.enqueue(1)
    q.enqueue(2)
    q.display()
    q.dequeue()
    q.display()
    q.enqueue(3)
    q.display()
    q.dequeue()
    q.display()


if __name__ == "__main__":
    demonstrate()
    test_edge_cases()