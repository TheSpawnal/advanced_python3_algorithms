

# Write pseudocode for the procedure MAX-HEAP-DECREASE-KEY(A, x, k) in a
#  max-heap. What is the running time of your procedure?



MAX-HEAP-DECREASE-KEY(A, x, k)
    if k > x.key
        error "new key is larger than current key"
    x.key = k
    find the index i in array A where object x occurs
    MAX-HEAPIFY(A, i)


# MAX-HEAP-DECREASE-KEY uses MAX-HEAPIFY because 
# decreasing a key might make it smaller than its children 
# (violating max-heap property downward)

# MAX-HEAP-INCREASE-KEY bubbles up because increasing a key might make 
# it larger than its parent (violating max-heap property upward)

# Running Time: O(lg n) due to MAX-HEAPIFY, which traverses at most the height of the tree

# Symmetry: MIN-HEAP-DECREASE-KEY bubbles up (opposite of MAX-HEAP-INCREASE-KEY)
