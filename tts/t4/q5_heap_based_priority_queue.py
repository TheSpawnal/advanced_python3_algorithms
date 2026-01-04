
'''
Write HEAP-INCREASE-KEY and MAX-HEAP-INSERT
•Must maintain max-heap property

• HEAP-INCREASE-KEY: must bubble up correctly
• MAX-HEAP-INSERT: must use increase-key
• Points lost for logical errors (not checking parent, wrong 
dummy value)

PARENT(i)
1  return ⌊i/2⌋
LEFT(i)
1  return 2i
RIGHT(i)
1  return 2i + 1

MAX-HEAPIFY(A, i)
1  l = LEFT(i)
2  r = RIGHT(i)
3  if l ≤ A.heap-size and A[l] > A[i]
4    largest = l
5  else largest = i
6  if r ≤ A.heap-size and A[r] > A[largest]
7    largest = r
8  if largest ≠ i


BUILD-MAX-HEAP(A, n)
1 A.heap-size = n
2 for i = ⌊n/2⌋ downto 1
3   MAX-HEAPIFY(A, i)


HEAPSORT(A, n)
1 BUILD-MAX-HEAP(A, n)
2 for i = n downto 2
3    exchange A[1] with A[i]
4    A.heap-size = A.heap-size – 1
5    MAX-HEAPIFY(A, 1)

MAX-HEAP-MAXIMUM(A)
1 if A.heap-size < 1
2    error “heap underflow”
3 return A[1]

MAX-HEAP-EXTRACT-MAX(A)
1 max = MAX-HEAP-MAXIMUM(A)
2 A[1] = A[A.heap-size]
3 A.heap-size = A.heap-size – 1
4 MAX-HEAPIFY(A, 1)
5 return max



MAX-HEAP-INCREASE-KEY(A, x, k)
1 if k < x.key
2   error “new key is smaller than current key”
3 x.key = k
4 find the index i in array A where object x occurs
5 while i > 1 and A[PARENT(i)].key < A[i].key
6   exchange A[i] with A[PARENT(i)], updating the information that
      maps priority queue objects to array indices
7    i = PARENT(i)

MAX-HEAP-INSERT(A, x, n)
1 if A.heap-size == n
2   error “heap overflow”
3 A.heap-size = A.heap-size + 1
4 k = x.key
5 x.key = –∞
6 A[A.heap-size] = x
7 map x to index heap-size in the array
8 MAX-HEAP-INCREASE-KEY(A, x, k)




ops: 
HEAP-INCREASE-key time O(log n) space O(1)
MAX-HEAP-INSERT O(log n) O(1)amortized


Why O(log n)? 
Bubble-up traverses at most the height of the tree = ⌊log₂ n⌋ levels.


Common Pitfalls

Mistake

ConsequenceFix

Dummy value = 0
Fails for negative keys
Use -∞ 

Not checking new_key < A[i]
Violates heap property silently
Explicit check + error

Loop condition i >= 0
Off-by-one at root
Use i > 0

Forget to update i after swap
Infinite loop
i ← PARENT(i)

Compare with wrong parent formula
Incorrect swaps
(i-1)//2 for 0-indexed

'''