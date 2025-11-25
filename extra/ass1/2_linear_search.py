

# Write an algorithm for a linear search of array A[1:n] 
# looking for element x.  
# The algorithm should scan through the array, starting at 
# the first element, and return the index of element x, or the 
# special value NIL if the element is not found. 
# Describe a loop invariant, and use it to show your 
# algorithm is correct.

LINEAR-SEARCH(A, n, x)
    for i = 1 to n
        if A[i] == x
            return i
    return NIL

'''
Loop Invariant
Invariant: At the start of each iteration of the for loop, the subarray A[1:i-1] 
contains no element equal to x.
Proof of Correctness:
Initialization: Before the first iteration (i = 1), 
the subarray A[1:0] is empty, so trivially contains no element equal to x. The invariant holds.
Maintenance: Assume the invariant holds at the start of iteration i. 
If A[i] == x, we return i immediately. Otherwise, A[i] ≠ x, and we increment i. 
Now A[1:i] contains no element equal to x (since A[1:i-1] contained no x by the invariant, 
and A[i] ≠ x). The invariant holds for the next iteration.
Termination: The loop terminates when either:
We find A[i] == x for some i ∈ [1:n], and return i (correct)
i > n, meaning we've checked all n elements. 
By the invariant, A[1:n] contains no element equal to x, so returning NIL is correct.
'''


def linear_search(A, x):
    n = len(A)
    for i in range(n):
        if A[i] == x:
            return i
    return None

A = [5, 2, 4, 6, 1, 3]
print(linear_search(A, 6))
print(linear_search(A, 7))

A = [10, 20, 30, 40, 50]
print(linear_search(A, 30))
print(linear_search(A, 25))

A = [7]
print(linear_search(A, 7))
print(linear_search(A, 3))
```

**Output:**
```
3
None
2
None
0
None