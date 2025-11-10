
Whereas a stack allows insertion and deletion of elements at only one end, 
and a queue allows insertion at one end and deletion at the other end, 
a deque (double-ended queue) allows insertion and deletion at both ends. 
Write four O(1)-time procedures to insert elements into and delete elements 
from both ends of a deque implemented by an array.

HEAD-ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
        error "overflow"
    else
        if Q.head == 1
            Q.head = Q.length
        else Q.head = Q.head - 1
        Q[Q.head] = x

TAIL-ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
        error "overflow"
    else
        Q[Q.tail] = x
        if Q.tail == Q.length
            Q.tail = 1
        else Q.tail = Q.tail + 1

HEAD-DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
        error "underflow"
    else
        x = Q[Q.head]
        if Q.head == Q.length
            Q.head = 1
        else Q.head = Q.head + 1
        return x

TAIL-DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
        error "underflow"
    else
        if Q.tail == 1
            Q.tail = Q.length
        else Q.tail = Q.tail - 1
        x = Q[Q.tail]
        return x