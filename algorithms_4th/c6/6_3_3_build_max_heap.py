BUILD-MAX-HEAP(A, n)
  A.heap-size = n
  for i = ⌊n/2⌋ downto 1
    MAX-HEAPIFY(A, i)

# Why does the loop index i in line 2 of BUILD-MAX-HEAP decrease from
#  ⌊n/2⌋ to 1 rather than increase from 1 to ⌊n/2⌋?

Otherwise we won't be allowed to call MAX-HEAPIFY, 
since it will fail the condition of having the subtrees be max-heaps. 
That is, if we start with 1, there is no guarantee that A[2] and A[3] 
are roots of max-heaps.
