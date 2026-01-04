
'''
Show how to implement a stack using two queues. 
Analyze the running time of the stack operations.


PUSH: Θ(1).
POP: Θ(n).
We have two queues and mark one of them as active. 
PUSH queues an element on the active queue. 
POP should dequeue all but one element of the active queue and 
queue them on the inactive. 
The roles of the queues are then reversed, 
and the final element left in the (now) inactive queue is returned.

The PUSH operation is Θ(1), but the POP operation is 
Θ(n) where n is the number of elements in the stack.

'''







"""
INIT()
    A = empty queue    // main queue, top of stack at front
    B = empty queue    // temporary transfer queue

PUSH(S, x)
    // Put new element in empty B
    ENQUEUE(B, x)
    
    // Move all from A to B (behind x)
    while not QUEUE-EMPTY(A)
        ENQUEUE(B, DEQUEUE(A))
    
    // Swap A and B
    swap(A, B)

POP(S)
    if QUEUE-EMPTY(A)
        error "underflow"
    return DEQUEUE(A)

TOP(S)
    if QUEUE-EMPTY(A)
        error "underflow"
    return FRONT(A)




Runtime:
PUSH: n transfers + 1 enqueue = O(n)
POP: O(1)   
"""