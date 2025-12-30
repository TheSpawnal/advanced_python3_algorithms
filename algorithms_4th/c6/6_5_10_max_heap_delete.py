 

# The operation MAX-HEAP-DELETE(A, x) deletes the object x from max-heap
#  A. Give an implementation of MAX-HEAP-DELETE for an n-element max
# heap that runs in O(lg n) time plus the overhead for mapping priority queue
#  objects to array indices.

MAX-HEAP-DELETE(A, x)
    find index i where x occurs
    if i == A.heap-size
        A.heap-size = A.heap-size - 1
        return
    A[i] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    if A[i] > A[PARENT(i)]
        MAX-HEAP-INCREASE-KEY(A, i, A[i].key)
    else
        MAX-HEAPIFY(A, i)
        
Running time: O(lg n)

Replace deleted element with last element
Restore heap property by either bubbling up or down
Both operations are O(lg n)