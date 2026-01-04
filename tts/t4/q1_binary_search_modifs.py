

"""

• Modify binary search to count elements < x
• Must be iterative, recursive only gets partial
• Part B: Loop invariant proof 



ITERATIVE-BINARY-SEARCH(A,x,low,high)
    while low <= high
        mid = floor((low+high)/2)
        if x == A[mid]
            return mid
        elseif x > A[mid]
            low = mid + 1
        else high = mid -1
    return NIL

    

RECURSIVE-BINARY-SEARCH(A,x,low, high)
    if low > high
        return NIL
    mid = floor((low + high)/2)
    if x == A[mid]
        return mid
    elseif x > A[mid]
        return RECURSIVE-BINARY-SEARCH(A,x,mid + 1, high)
    else return RECURSIVE-BINARY-SEARCH(A,x,low, mid -1)
"""

"""
Solution:

iterative: 
COUNT-LESS-THAN-ITERATIVE(A, x, low, high)
    while low <= high
        mid = floor((low + high) / 2)
        if A[mid] < x
            low = mid + 1
        else
            high = mid - 1
    return low - 1

recursive:
COUNT-LESS-THAN-RECURSIVE(A, x, low, high)
    if low > high
        return low - 1
    mid = floor((low + high) / 2)
    if A[mid] < x
        return COUNT-LESS-THAN-RECURSIVE(A, x, mid + 1, high)
    else
        return COUNT-LESS-THAN-RECURSIVE(A, x, low, mid - 1)

        
Part B: Loop invariant proof:

Loop invariant: at the start of each iteration, all elements
in A[1...low-1] are < x, and all elements in A[high+1,...,n] are >= x.

Initialization: Before first iteration, low = 1 and high = n.
A[1..0] is empty and A[n+1..n] is empty. Invariant holds trivially.

Maintenance:
    -If A[mid] < x : we set low = mid + 1. all elements in A[1..mid]
    are < x, so A[1..low-1] still contains only elements < x.

    -If A[mid] >= x : we set high = mid -1. 
    A[mid..n] contains elements >= x, so A[high+1..n] still contains 
    only elements >= x.

Termination: Loop ends when low > high. 
By invariant, A[1..low-1] contains all elements < x. Count = low - 1.
"""

