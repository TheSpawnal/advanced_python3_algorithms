

# 1/Modify PARTITION to use median-of-three pivot (pseudocode)
# 2/Part B: Explain why median-of-three avoids worst-case scenarios,


# critera: 
# Implementation: finding median, using it as pivot
# Performance explanation: must mention sorted/reverse sorted arrays
# Common errors: forgetting to swap pivot or explain performance



'''
basic quicksort pseudo code

QUICKSORT(A, p, r)
 1 if p < r
 2 // Partition the subarray around the pivot, which ends up in A[q].
 3 q = PARTITION(A, p, r)
 4 QUICKSORT(A, p, q – 1) // recursively sort the low side
 5 QUICKSORT(A, q + 1, r) // recursively sort the high side

PARTITION(A, p, r)
 1 x = A[r]             // the pivot
 2 i = p – 1            // highest index into the low side
 3 for j = p to r – 1   // process each element other than the pivot
 4  if A[j] ≤ x         // does this element belong on the low side ? 
 #flip the condition to sort into nonincreasing order
 5      i = i + 1       // index of a new slot in the low side
 6      exchange A[i] with A[j] // put this element there
 7 exchange A[i + 1] with A[r]  // pivot goes just to the right of the low side
 8 return i + 1     // new index of the pivot

'''

'''
MEDIAN-OF-THREE(A, p, r)
 1  mid = ⌊(p + r) / 2⌋
 2  // Sort A[p], A[mid], A[r] to find median
 3  if A[p] > A[mid]
 4      exchange A[p] with A[mid]
 5  if A[p] > A[r]
 6      exchange A[p] with A[r]
 7  if A[mid] > A[r]
 8      exchange A[mid] with A[r]
 9  // Now: A[p] ≤ A[mid] ≤ A[r], median is at mid
10  exchange A[mid] with A[r]    // move pivot to end for standard partition
11  return A[r]

PARTITION-MEDIAN(A, p, r)
 1  x = MEDIAN-OF-THREE(A, p, r)   // pivot is now median of three
 2  i = p – 1
 3  for j = p to r – 1
 4      if A[j] ≤ x
 5          i = i + 1
 6          exchange A[i] with A[j]
 7  exchange A[i + 1] with A[r]
 8  return i + 1

QUICKSORT(A, p, r)
 1  if p < r
 2      q = PARTITION-MEDIAN(A, p, r)
 3      QUICKSORT(A, p, q – 1)
 4      QUICKSORT(A, q + 1, r)
'''

  
'''
Hoare Partition Pseudocode

Define partition(arr, lo, hi)
    pivot = arr[(lo + hi) / 2]       // pivot VALUE (not index)
    i = lo - 1
    j = hi + 1    
    Loop forever:
        Do:
            i = i + 1                // move right
        While arr[i] < pivot
        
        Do:
            j = j - 1                // move left
        While arr[j] > pivot
        
        if i >= j:
            return j                 // partition boundary
        
        swap(arr[i], arr[j])

Define quicksort(arr, lo, hi)
    If lo >= 0 AND hi >= 0 AND lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)        // NOTE: includes p (Hoare-specific)
        quicksort(arr, p + 1, hi)



+-------------------+------------------+---------------------+-------------------+
| Aspect            | Lomuto (Classic) | Hoare               | Median-of-Three   |
+-------------------+------------------+---------------------+-------------------+
| Pivot choice      | Last element     | Middle element      | Median of 3       |
| Scan direction    | Single L->R      | Two pointers inward | Single L->R       |
| Pivot placed?     | Yes, exactly     | No, in left part    | Yes, exactly      |
| Recursive calls   | (p,q-1), (q+1,r) | (p,j), (j+1,r)      | (p,q-1), (q+1,r)  |
| Swaps (random)    | ~n/2             | ~n/6                | ~n/2              |
| Sorted input      | O(n^2)           | O(n^2)*             | O(n log n)        |
| Reverse sorted    | O(n^2)           | O(n^2)*             | O(n log n)        |
| All equal         | O(n^2)           | O(n^2)              | O(n^2)            |
+-------------------+------------------+---------------------+-------------------+

* Hoare with middle pivot handles sorted better than with first/last pivot.

Core Trade-offs
Lomuto: Simple, predictable, but vulnerable to common inputs.

Hoare: Fewest swaps, fastest in practice on random data, 
but tricky boundary handling and pivot not isolated.

Median-of-Three: Robust against sorted/reverse inputs with minimal 
overhead (3 comparisons, 2-3 swaps). Best practical default.


Why Median-of-Three Avoids Worst Case
Classic (Lomuto) problem: Picks last element blindly. 
On sorted/reverse-sorted input, pivot is always min or max → splits of (0, n-1) → Θ(n²).

Median-of-three solution: Examines A[p], A[mid], A[r] and picks the middle value. 
This guarantees:
On sorted input: median of (smallest, middle, largest) = middle element → balanced split
On reverse-sorted: same logic applies
Cannot pick the absolute min or max from those three positions

Result: Sorted/reverse-sorted inputs become O(n log n) instead of O(n²).
Still vulnerable to: Adversarial inputs specifically crafted against 
median-of-three (rare in practice).



'''