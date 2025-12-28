'''pseudocode
QUEUE-EMPTY(Q)
    if Q.head == Q.tail
        return true
    else return false

QUEUE-FULL(Q)
    if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length)
        return true
    else return false

ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
        error "overflow"
    else
        Q[Q.tail] = x
        if Q.tail == Q.length
            Q.tail = 1
        else Q.tail = Q.tail + 1

DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
        error "underflow"
    else
        x = Q[Q.head]
        if Q.head == Q.length
            Q.head = 1
        else Q.head = Q.head + 1
        return x
'''

# - Implement queue using 2 stacks
# - ENQUEUE must be more expensive
# - Provide precise runtime analysis

# - ENQUEUE O(n), DEQUEUE O(1)
# - Must maintain FIFO order
# - DO not miss pseudocode or engage vague runtime discussion

class QueueWithTwoStacks:
    """
    Queue implementation using two stacks.
    ENQUEUE: O(n) - transfers all elements
    DEQUEUE: O(1) - direct pop from main stack
    """
    def __init__(self):
        self.main_stack = []      # Holds elements in FIFO order (top = front)
        self.temp_stack = []      # Temporary storage during enqueue
    
    def is_empty(self):
        return len(self.main_stack) == 0
    
    def enqueue(self, x):
        """O(n) operation - transfers all elements twice"""
        # Transfer all from main to temp: O(n)
        while self.main_stack:
            self.temp_stack.append(self.main_stack.pop())
        
        # Push new element to temp: O(1)
        self.temp_stack.append(x)
        
        # Transfer all back to main: O(n)
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
    
    def dequeue(self):
        """O(1) operation - single pop"""
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self.main_stack.pop()
    
    def peek(self):
        """O(1) operation"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.main_stack[-1]


# Test
if __name__ == "__main__":
    q = QueueWithTwoStacks()
    
    operations = [
        ("enqueue", 1),
        ("enqueue", 2),
        ("enqueue", 3),
        ("dequeue", None),
        ("enqueue", 4),
        ("dequeue", None),
        ("dequeue", None),
        ("dequeue", None)
    ]
    
    for op, val in operations:
        if op == "enqueue":
            q.enqueue(val)
            print(f"ENQUEUE({val}): main={q.main_stack}")
        else:
            result = q.dequeue()
            print(f"DEQUEUE() = {result}: main={q.main_stack}")

'''
**PSEUDOCODE:**
STRUCTURE QueueWithTwoStacks
    main_stack: Stack
    temp_stack: Stack
END STRUCTURE

FUNCTION IS-EMPTY(Q)
    RETURN SIZE(Q.main_stack) == 0
END FUNCTION

FUNCTION ENQUEUE(Q, x)
    // Transfer all elements from main to temp: O(n)
    WHILE NOT IS-EMPTY(Q.main_stack) DO
        element = POP(Q.main_stack)
        PUSH(Q.temp_stack, element)
    END WHILE
    
    // Push new element to temp: O(1)
    PUSH(Q.temp_stack, x)
    
    // Transfer all elements back to main: O(n)
    WHILE NOT IS-EMPTY(Q.temp_stack) DO
        element = POP(Q.temp_stack)
        PUSH(Q.main_stack, element)
    END WHILE
END FUNCTION

FUNCTION DEQUEUE(Q)
    // Single pop operation: O(1)
    IF IS-EMPTY(Q.main_stack) THEN
        ERROR "Queue underflow"
    END IF
    RETURN POP(Q.main_stack)
END FUNCTION
'''


'''
RUNTIME ANALYSIS:
ENQUEUE(Q, x) - O(n) where n = current queue size:

Transfer main → temp: n POP + n PUSH operations = 2n operations
Push new element: 1 PUSH operation = 1 operation
Transfer temp → main: (n+1) POP + (n+1) PUSH operations = 2(n+1) operations
Total: 2n + 1 + 2n + 2 = 4n + 3 = O(n)

DEQUEUE(Q) - O(1):

Single POP from main_stack
Total: 1 operation = O(1)

INVARIANT:

main_stack always maintains FIFO order with front at top (index -1)
After each ENQUEUE, newest element is at bottom of main_stack
DEQUEUE always removes from top of main_stack (oldest element)

CORRECTNESS:

Element enqueued at time t₁ before element at time t₂ will be deeper in main_stack
DEQUEUE pops from top, ensuring FIFO order preserved

'''
