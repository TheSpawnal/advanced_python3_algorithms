
# Each exchange operation on line 6 of MAX-HEAP-INCREASE-KEY typically
#  requires three assignments, not counting the updating of the mapping from
#  objects to array indices. Show how to use the idea of the inner loop of
#  INSERTION-SORT to reduce the three assignments to just one assignment.

 MAX-HEAP-INCREASE-KEY(A, x, k)
 1 if k < x.key
 2 error “new key is smaller than current key”
 3 x.key = k
 4 find the index i in array A where object x occurs
 5while i > 1 and A[PARENT(i)].key < A[i].key
 6 exchange A[i] with A[PARENT(i)], updating the information that maps priority queue objects to array indices
 7 i = PARENT(i)

#Current approach (3 assignments per exchange):

temp = A[i]
A[i] = A[PARENT(i)]
A[PARENT(i)] = temp

#Optimized approach (like INSERTION-SORT):

MAX-HEAP-INCREASE-KEY(A, i, key)
    if key < A[i]
        error "new key is smaller than current key"
    A[i] = key
    while i > 1 and A[PARENT(i)] < key
        A[i] = A[PARENT(i)]  // Only 1 assignment per iteration
        i = PARENT(i)
    A[i] = key  // Final placement
#Key idea: Hold the increased key in a variable and shift parent values down. Place the key once at the end.
