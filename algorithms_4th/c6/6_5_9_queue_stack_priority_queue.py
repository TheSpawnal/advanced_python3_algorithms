

#  Show how to implement a first-in, first-out queue with a priority queue.
#  Show how to implement a stack with a priority queue. 

#FIFO Queue with Priority Queue
#Use a min-heap with timestamps as keys:
    
ENQUEUE(Q, x)
    timestamp = timestamp + 1
    x.key = timestamp
    MIN-HEAP-INSERT(Q, x)

DEQUEUE(Q)
    return MIN-HEAP-EXTRACT-MIN(Q)
#Logic: Smaller timestamps = inserted earlier = dequeued first.


#Stack with Priority Queue
#Use a max-heap with timestamps as keys:
    
PUSH(S, x)
    timestamp = timestamp + 1
    x.key = timestamp
    MAX-HEAP-INSERT(S, x)

POP(S)
    return MAX-HEAP-EXTRACT-MAX(S)
