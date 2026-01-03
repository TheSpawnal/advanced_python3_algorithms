

BUCKET-SORT(A,n) 
1 let B[0:n-1] be a new array 
2 for i = 0 to n - 1    
3   make B[i] an empty list 
4 for i = 1 to n  
5   insert A[i] into list B[floor(n*A[i])]    
6 for i = 0 to n -1     
7   sort list B[i] with insertion sort 
8 concatenate the lists B[0], B[1], ..., B[n-1] together in order 
9 return the concatenated lists 





Modified Bucket Sort
Analysis of Distribution
floor(10x_i)/10 ∈ {0, 0.1, 0.2, ..., 0.9} — 10 discrete values
y_i/n ∈ [0, 1/n) — uniform perturbation within each group

Each element falls in range [k/10, k/10 + 1/n) for some k ∈ {0,...,9}.

Modified Algorithm
MODIFIED-BUCKET-SORT(A, n)
 1  let B[0:9] be a new array           // only 10 buckets
 2  for i = 0 to 9
 3      make B[i] an empty list
 4  for i = 1 to n
 5      k = floor(A[i] * 10)            // extract first decimal digit
 6      insert A[i] into list B[k]
 7  for i = 0 to 9
 8      sort list B[i] with insertion sort
 9  concatenate B[0], B[1], ..., B[9] together in order
10  return the concatenated lists

Why O(n) Expected

Lines 1-3: O(1)
Lines 4-6: O(n)
Lines 7-8: Each bucket has ~n/10 elements; 
            within each bucket, y_i/n is uniform over [0, 1/n), 
              so insertion sort runs in O(n/10) expected per bucket → O(n) total
Line 9: O(n)

Total: O(n) expected
