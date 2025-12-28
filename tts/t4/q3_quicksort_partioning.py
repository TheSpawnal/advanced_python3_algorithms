

# 1/Modify PARTITION to use median-of-three pivot (pseudocode)
# 2/Part B: Explain why median-of-three avoids worst-case scenarios
#3/according to python3 code provided, implement median of three pivots

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
 1 x = A[r]     // the pivot
 2 i = p – 1    // highest index into the low side
 3 for j = p to r – 1   // process each element other than the pivot
 4  if A[j] ≤ x // does this element belong on the low side ? 
 #flip the condition to sort into nonincreasing order
 5      i = i + 1   // index of a new slot in the low side
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

def median_of_three(arr, p, r):
    mid = (p + r) // 2
    
    if arr[p] > arr[mid]:
        arr[p], arr[mid] = arr[mid], arr[p]
    if arr[p] > arr[r]:
        arr[p], arr[r] = arr[r], arr[p]
    if arr[mid] > arr[r]:
        arr[mid], arr[r] = arr[r], arr[mid]
    
    arr[mid], arr[r] = arr[r], arr[mid]
    return arr[r]

def partition(arr, p, r):
    pivot = median_of_three(arr, p, r)
    i = p - 1
    
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)

def sort(arr):
    if len(arr) > 1:
        quicksort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    tests = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [1, 2, 3, 4, 5],           # sorted
        [5, 4, 3, 2, 1],           # reverse sorted
        [1],
        [],
        [2, 2, 2, 2],              # duplicates
    ]
    
    for t in tests:
        original = t.copy()
        sort(t)
        print(f"{original} -> {t}")
```

**Output:**
```
[3, 1, 4, 1, 5, 9, 2, 6] -> [1, 1, 2, 3, 4, 5, 6, 9]
[1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
[5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]
[1] -> [1]
[] -> []
[2, 2, 2, 2] -> [2, 2, 2, 2]


  
'''
Corrected Hoare Partition Pseudocode
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
        
        If i >= j:
            return j                 // partition boundary
        
        swap(arr[i], arr[j])

Define quicksort(arr, lo, hi)
    If lo >= 0 AND hi >= 0 AND lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)        // NOTE: includes p (Hoare-specific)
        quicksort(arr, p + 1, hi)
'''


Critical Hoare Detail: The recursive call is quicksort(arr, lo, p) not quicksort(arr, lo, p-1). This is because Hoare's partition returns a boundary index, not the pivot's final position.

Median-of-Three Hoare Variant
Define median_of_three(arr, lo, hi)
    mid = (lo + hi) / 2
    
    // Sort the three elements in place
    If arr[lo] > arr[mid]:
        swap(arr, lo, mid)
    If arr[lo] > arr[hi]:
        swap(arr, lo, hi)
    If arr[mid] > arr[hi]:
        swap(arr, mid, hi)
    
    // arr[lo] <= arr[mid] <= arr[hi]
    // Return median VALUE (not index)
    return arr[mid]

Define partition_hoare_median(arr, lo, hi)
    pivot = median_of_three(arr, lo, hi)
    i = lo - 1
    j = hi + 1
    
    Loop forever:
        Do:
            i = i + 1
        While arr[i] < pivot
        
        Do:
            j = j - 1
        While arr[j] > pivot
        
        If i >= j:
            return j
        
        swap(arr[i], arr[j])

Define quicksort(arr, lo, hi)
    If lo >= 0 AND hi >= 0 AND lo < hi:
        p = partition_hoare_median(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)

Define sort(arr)
    If length(arr) > 1:
        quicksort(arr, 0, length(arr) - 1)
    return arr
  '''

#Python Implementation (Hoare + Median-of-Three)
median_of_three(arr, lo, hi):
    mid = (lo + hi) // 2
    
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    
    return arr[mid]

def partition_hoare(arr, lo, hi):
    pivot = median_of_three(arr, lo, hi)
    i = lo - 1
    j = hi + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition_hoare(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)

def sort(arr):
    if len(arr) > 1:
        quicksort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    tests = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
        [2, 2, 2, 2],
        [10, 7, 8, 9, 1, 5],
    ]
    
    for t in tests:
        original = t.copy()
        sort(t)
        print(f"{original} -> {t}")


# **Output:**

# [3, 1, 4, 1, 5, 9, 2, 6] -> [1, 1, 2, 3, 4, 5, 6, 9]
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5]
# [1] -> [1]
# [] -> []
# [2, 2, 2, 2] -> [2, 2, 2, 2]
# [10, 7, 8, 9, 1, 5] -> [1, 5, 7, 8, 9, 10]



  
