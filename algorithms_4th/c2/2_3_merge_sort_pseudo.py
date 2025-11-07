
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


def merge(A, p, q, r):
    """
    Merge two sorted subarrays A[p:q+1] and A[q+1:r+1] into A[p:r+1].
    """
    nL = q - p + 1  # Length of left subarray
    nR = r - q      # Length of right subarray
    
    # Create temporary arrays
    L = [0] * nL
    R = [0] * nR
    
    # Copy data to temp arrays L and R
    for i in range(nL):
        L[i] = A[p + i]
    
    for j in range(nR):
        R[j] = A[q + 1 + j]
    
    # Merge the temp arrays back into A[p:r+1]
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = p  # Initial index of merged subarray
    
    # Merge while both subarrays have elements
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements of L, if any
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    
    # Copy remaining elements of R, if any
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    """
    Sort array A[p:r+1] using merge sort algorithm.
    
    Args:
        A: List to sort
        p: Starting index
        r: Ending index
    """
    if p >= r:  # Base case: 0 or 1 element
        return
    
    q = (p + r) // 2  # Find the middle point
    
    merge_sort(A, p, q)      # Sort first half
    merge_sort(A, q + 1, r)  # Sort second half
    merge(A, p, q, r)        # Merge the sorted halves


# Example usage
if __name__ == "__main__":
    array = [3, 41, 52, 26, 38, 57, 9,49]
    print(f"Original array: {array}")
    
    merge_sort(array, 0, len(array) - 1)
    print(f"Sorted array: {array}")
    
    # Test with edge cases
    test_cases = [
        [5],           # Single element
        [2, 1],        # Two elements
        [],            # Empty
        [1, 2, 3, 4],  # Already sorted
        [4, 3, 2, 1]   # Reverse sorted
    ]
    
    for test in test_cases:
        original = test.copy()
        if test:
            merge_sort(test, 0, len(test) - 1)
        print(f"{original} → {test}")




#alternative with slicing
# def merge_sort_pythonic(A):
#     """Pythonic merge sort using slicing."""
#     if len(A) <= 1:
#         return A
    
#     mid = len(A) // 2
#     left = merge_sort_pythonic(A[:mid])
#     right = merge_sort_pythonic(A[mid:])
    
#     # Merge
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result


# # Usage
# array = [38, 27, 43, 3, 9, 82, 10]
# sorted_array = merge_sort_pythonic(array)
# print(sorted_array)
