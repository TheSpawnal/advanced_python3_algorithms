# The code for MAX-HEAPIFY is quite efficient in terms of constant factors, 
# except possibly for the recursive call in line 10, which might cause some 
# compilers to produce inefficient code. Write an efficient MAX-HEAPIFY
# that uses an iterative control construct (a loop) instead of recursion.


MAX-HEAPIFY(A, i)
    while true
        l = LEFT(i)
        r = RIGHT(i)
        if l ≤ A.heap-size and A[l] > A[i]
            largest = l
        else largest = i
        if r ≤ A.heap-size and A[r] > A[largest]
            largest = r
        if largest == i
            return
        exchange A[i] with A[largest]
        i = largest
