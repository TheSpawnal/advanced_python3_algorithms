

class QueueWithStacks:
    """
    Queue implementation using two stacks.
    
    Strategy:
    - stack1: Used for enqueue operations (inbox)
    - stack2: Used for dequeue operations (outbox)
    """
    
    def __init__(self):
        self.stack1 = []  # Enqueue stack (inbox)
        self.stack2 = []  # Dequeue stack (outbox)
    
    def enqueue(self, x):
        """
        Add element to the rear of the queue.
        Time Complexity: O(1)
        """
        self.stack1.append(x)
    
    def dequeue(self):
        """
        Remove and return element from the front of the queue.
        Time Complexity: O(1) amortized
        """
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Dequeue from empty queue")
            
            # Transfer all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    
    def is_empty(self):
        """Check if queue is empty. Time: O(1)"""
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def size(self):
        """Return the number of elements. Time: O(1)"""
        return len(self.stack1) + len(self.stack2)
    
    def peek(self):
        """
        Return front element without removing it.
        Time Complexity: O(1) amortized
        """
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Peek from empty queue")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]


# Demonstration
def demonstrate():
    """Show how the queue works step by step."""
    q = QueueWithStacks()
    
    print("=== Queue Operations Demo ===\n")
    
    # Enqueue operations
    print("ENQUEUE(1):")
    q.enqueue(1)
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("ENQUEUE(2):")
    q.enqueue(2)
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("ENQUEUE(3):")
    q.enqueue(3)
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    # First dequeue - triggers transfer
    print("DEQUEUE():")
    result = q.dequeue()
    print(f"  Returned: {result}")
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("ENQUEUE(4):")
    q.enqueue(4)
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("DEQUEUE():")
    result = q.dequeue()
    print(f"  Returned: {result}")
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("DEQUEUE():")
    result = q.dequeue()
    print(f"  Returned: {result}")
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")
    
    print("DEQUEUE():")
    result = q.dequeue()
    print(f"  Returned: {result}")
    print(f"  stack1: {q.stack1}, stack2: {q.stack2}\n")


if __name__ == "__main__":
    demonstrate()

## Time Complexity Analysis

# ### ENQUEUE Operation
# - **Time:** **O(1)** worst-case
# - Simply pushes onto stack1
# - No transfer needed

# ### DEQUEUE Operation
# - **Worst-case:** **O(n)** - when stack2 is empty and we transfer all n elements from stack1
# - **Amortized:** **O(1)** ⭐

# #### Amortized Analysis (Accounting Method)

# **Key insight:** Each element is moved at most twice:
# 1. Once when pushed to stack1 (enqueue)
# 2. Once when transferred from stack1 to stack2 (before first dequeue)

# **Cost assignment:**
# - Assign cost = 2 to each ENQUEUE operation
#   - 1 for the actual push to stack1
#   - 1 stored as credit for future transfer to stack2

# When DEQUEUE transfers elements:
# - Use the stored credits to pay for the transfers
# - The actual pop from stack2 costs 1

# **Therefore:** 
# - Total cost for n operations = O(n)
# - Amortized cost per operation = O(n)/n = **O(1)**

# ### Space Complexity
# - **O(n)** where n is the number of elements in the queue
