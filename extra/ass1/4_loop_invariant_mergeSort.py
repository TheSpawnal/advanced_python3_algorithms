


# Find a loop invariant for the first while loop of the 
# MERGE pseudocode, and use it to show the algorithm 
# is correct.


# MERGE(a,p,q,r)
# nL = q - p + 1 //length of A[p:q]
# nR = r - q //length of A[q+1 : r]
# let L[0 : nL -1] & R[0: nR - 1] be new arrays
# for i = 0 to nL - 1 //copy A[p:q] into L[0: nL -1 ]
#     L[i] = A[p+i]
# for j = 0 to nR - 1 //copy A[q+1:r] into R[0:nR -1]

#     R[j] = A[q + j + 1]
# i = 0 // i indexes the smallest remaining element in L
# j = 0 // j indexes the smallest remaining element in R
# k = p // k indexes the location in A to fill
# // As long as each of the arrays L and R contains an unmerged element,
# //copy the smallest unmerged element back into A[p : r].
# while i < nL and j < nR
#     if L[i] ≤ R[j]
#         A[k] = L[i]
#         i = i + 1
#     else A[k] = R[j]
#         j = j + 1
#     k = k + 1
# // Having gone through one of L and R entirely, copy the
# //  remainder of the other to the end of A[p : r].
# while i < nL
#     A[k] = L[i]
#     i = i + 1
#     k = k + 1
# while j < nR
#     A[k] = R[j]
#     j = j + 1
#     k = k + 1

# MERGE-SORT(A,p,r)
# if p >= r   //zero or one element?
#     return
# q = [(p+r)/2] //midpoint of A[p:r]
# MERGE-SORT(A,p,q) //recursively sort A[p:q]
# MERGE-SORT(A,q+1,r) //recursively sort A[q+1:r]
# //MERGE A[p:q] and A[q+1: r] into A[p:r]
# MERGE(A,p,q,r)

'''
MERGE Algorithm - Loop Invariant Analysis
Loop Invariant for First While Loop
Invariant: At the start of each iteration of the first while loop (line while i < nL and j < nR):

The subarray A[p:k-1] contains the (k-p) smallest elements from L[0:nL-1] and R[0:nR-1] in sorted order.
L[i] and R[j] are the smallest elements in their respective arrays that have not been copied back into A.
k = p + i + j

Proof of Correctness
Initialization
Before the first iteration:

i = 0, j = 0, k = p
A[p:k-1] = A[p:p-1] is empty (contains 0 elements)
L[0] and R[0] are the smallest elements of L and R respectively (not yet copied)
k = p + 0 + 0 ✓

The invariant holds.
Maintenance
Assume the invariant holds at the start of iteration with indices (i, j, k).
Case 1: L[i] ≤ R[j]

We set A[k] = L[i], then increment i and k
A[p:k-1] now contains (k-p) smallest elements: the previous (k-p-1) elements plus L[i] (which is ≤ all remaining elements in both L and R)
L[i+1] is now the smallest uncopied element in L
R[j] remains the smallest uncopied element in R
k' = k+1 = p + (i+1) + j ✓

Case 2: L[i] > R[j]

We set A[k] = R[j], then increment j and k
Similar reasoning: A[p:k-1] contains (k-p) smallest elements in sorted order
k' = k+1 = p + i + (j+1) ✓

The invariant holds for the next iteration.
Termination
The loop terminates when i ≥ nL or j ≥ nR.
Case 1: i = nL (L exhausted)

All elements of L have been copied
A[p:k-1] contains all nL elements from L and the j smallest elements from R, in sorted order
The second cleanup loop copies remaining R[j:nR-1] to A[k:r]
Since R was already sorted and R[j] ≥ A[k-1], the final array A[p:r] is sorted ✓

Case 2: j = nR (R exhausted)

All elements of R have been copied
A[p:k-1] contains the i smallest elements from L and all nR elements from R, in sorted order
The third cleanup loop copies remaining L[i:nL-1] to A[k:r]
Since L was already sorted and L[i] ≥ A[k-1], the final array A[p:r] is sorted ✓


Complexity
Time: Θ(n) for MERGE where n = r - p + 1

Each element copied once to L or R: Θ(n)
Each element copied once back to A: Θ(n)
Total: Θ(n)

Space: Θ(n) auxiliary space for L and R arrays
MERGE-SORT overall: Θ(n log n) in all cases
'''

def merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q
    
    L = [0] * nL
    R = [0] * nR
    
    for i in range(nL):
        L[i] = A[p + i]
    
    for j in range(nR):
        R[j] = A[q + j + 1]
    
    i = 0
    j = 0
    k = p
    
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)


test_cases = [
    [38, 27, 43, 3, 9, 82, 10],
    [5, 2, 4, 7, 1, 3, 2, 6],
    [1],
    [2, 1],
    []
]

for arr in test_cases:
    original = arr.copy()
    if len(arr) > 0:
        merge_sort(arr, 0, len(arr) - 1)
    print(f"{original} -> {arr}")
