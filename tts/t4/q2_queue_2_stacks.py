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


'''
**PSEUDOCODE:**

INIT()
    A = empty stack    // "ready" stack, front of queue on top
    B = empty stack    // temporary transfer stack

ENQUEUE(Q, x)
    // Move all from A to B
    while not STACK-EMPTY(A)
        PUSH(B, POP(A))
    
    // Push new element at bottom
    PUSH(A, x)
    
    // Move all back from B to A
    while not STACK-EMPTY(B)
        PUSH(A, POP(B))

DEQUEUE(Q)
    if STACK-EMPTY(A)
        error "underflow"
    return POP(A)

PEEK(Q)
    if STACK-EMPTY(A)
        error "underflow"
    return TOP(A)


Runtime Analysis
ENQUEUE(x): Given n elements currently in queue:
First while loop: n pops + n pushes = 2n
Middle push: 1
Second while loop: n pops + n pushes = 2n
Total: 4n + 1 = O(n)

DEQUEUE: Single pop from A = O(1)
PEEK: Single read from A = O(1)

'''


"""
alternative

Show how to implement a queue using two stacks. 
Analyze the running time of the queue operations.


ENQUEUE: Θ(1).
DEQUEUE: worst O(n), amortized Θ(1).

Let the two stacks be A and B.

ENQUEUE pushes elements on B. DEQUEUE pops elements from A.
If A is empty, the contents of B are transfered to 
A by popping them out of B and pushing them to A. 
That way they appear in reverse order and are popped in the original.

A DEQUEUE operation can perform in Θ(n) time, 
but that will happen only when A is empty. If many 
ENQUEUEs and DEQUEUEs are performed, the total time will be linear 
to the number of elements, not to the largest length of the queue.

"""