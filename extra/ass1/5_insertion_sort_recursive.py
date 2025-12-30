'''
Describe (with pseudocode) a recursive algorithm for insertion sort, 
which calls on itself to sort the sub-array A[1:n-1] and the inserts A[1].

RECURSIVE-INSERTION-SORT(A, n)
    if n <= 1
        return
    RECURSIVE-INSERTION-SORT(A, n-1)
    INSERT(A, n)

INSERT(A, n)
    key = A[n]
    i = n - 1
    while i >= 1 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

Alternative with single function:
RECURSIVE-INSERTION-SORT(A, n)
    if n <= 1
        return
    RECURSIVE-INSERTION-SORT(A, n-1)
    
    key = A[n]
    i = n - 1
    while i >= 1 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

How It Works

Base case: If n ≤ 1, array is already sorted
Recursive case:

Recursively sort A[1:n-1]
Insert A[n] into the sorted subarray A[1:n-1]
Recurrence Analysis
Recurrence relation:
T(n) = T(n-1) + Θ(n)
Where:

T(n-1): time to recursively sort first n-1 elements
Θ(n): worst-case time to insert A[n] into sorted portion

Solving the recurrence:
T(n) = T(n-1) + cn
     = T(n-2) + c(n-1) + cn
     = T(n-3) + c(n-2) + c(n-1) + cn
     = ...
     = T(1) + c(2 + 3 + ... + n)
     = Θ(1) + c · Σ(i=2 to n) i
     = Θ(1) + c · [n(n+1)/2 - 1]
     = Θ(n²)
Worst-case running time: Θ(n²)
'''

def recursive_insertion_sort(A, n=None):
    if n is None:
        n = len(A)
    
    if n <= 1:
        return
    
    recursive_insertion_sort(A, n - 1)
    
    key = A[n - 1]
    i = n - 2
    
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    
    A[i + 1] = key


test_cases = [
    [5, 2, 4, 6, 1, 3],
    [31, 41, 59, 26, 41, 58],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [1],
    []
]

for arr in test_cases:
    original = arr.copy()
    recursive_insertion_sort(arr)
    print(f"{original} -> {arr}")




