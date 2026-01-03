

QUICKSORT(A,p,r) 
1  if p < r
2    // Partition the subarray around the pivot, which ends up in A[q]. 
3     q = PARTITION(A,p,r) 
4     QUICKSORT(A,p,q-1)   // recursively sort the low side 
5     QUICKSORT(A,q-1, r)   // recursively sort the high side 

PARTITION(A,p,r)
1  x = A[r]    // the pivot 
2  i = p - 1    // highest index into the low side 
3  for j = p to r - 1    // process each element other than the pivot 
4    if A[j] <= x    // does this element belong on the low side? 
5      i = i + 1// index of a new slot in the low side 
6      exchange A[i] with A[j]  // put this element there 
7  exchange A[i+1] with A[r]  // pivot goes just to the right of the low side 
8  return i + 1    // new index of the pivot

The partition procedure admits the following loop invariant: 
• If p≤ k ≤ i then A[k]≤x
• If i+1 <= k <= j-1 then A[k] > x     
• If k = r then A[k] = x 

Partition operation: theta(n)
worst case : theta(n^2)
best case : theta(n log(n))

#RANDOMIZED QS
RANDOMIZED-PARTITION(A,p,r)
1  i = RANDOM(p,r)
2  exchange A[r] with A[i]
3  return PARTITION(A,p,r)

#HOARE
HOARE-PARTITION  
1  x = A[p]    
2  i = p - 1    
3  j = r + 1    
4  while TRUE 
5    repeat 
6      j = j - 1  
7     until A[j] <= x   
8     repeat 
9       i = i + 1 
10    until A[i] >= x   
11    if i < j   
12       exchange A[i] with A[j]  
13     else return j  

Hoare does ~3× fewer swaps — better cache/memory performance.

Trade-offs
Lomuto: Simpler logic, easier to understand, pivot lands in final position.
Hoare: Fewer swaps, faster in practice, but trickier bounds and pivot not isolated.
