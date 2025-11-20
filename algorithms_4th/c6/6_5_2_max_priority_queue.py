

MAX-HEAP-MAXIMUM(A)
    if A.heap-size < 1
        error “heap underflow”
    return A[1]

MAX-HEAP-EXTRACT-MAX(A)
    max = MAX-HEAP-MAXIMUM(A)
    A[1] = A[A.heap-size]
    A.heap-size = A.heap-size – 1
    MAX-HEAPIFY(A, 1)
    return max

MAX-HEAP-INCREASE-KEY(A, x, k)
    if k < x.key
        error “new key is smaller than current key”
    x.key = k
    find the index i in array A where object x occurs
    while i > 1 and A[PARENT(i)].key < A[i].key
        exchange A[i] with A[PARENT(i)], updating the information that
            maps priority queue objects to array indices
        i = PARENT(i)

MAX-HEAP-INSERT(A, x, n)
    if A.heap-size == n
        error “heap overflow”
    A.heap-size = A.heap-size + 1
    k = x.key
    x.key = –∞
    A[A.heap-size] = x
    map x to index heap-size in the array
    MAX-HEAP-INCREASE-KEY(A, x, k)