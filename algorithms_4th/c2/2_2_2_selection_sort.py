# pseudocode selection sort:

# for i = 1 to n-1 do
#     min = i
#     for j = i + 1 to n do
#         //find index of the ith smallest element
#         if A[j] < A[min] then
#             min = j
#         end if
#     end for
#     Swap A[min] and A[i]
# end for

def selection_sort(A):
    """
    Sorts array A in-place using selection sort algorithm.
    
    Args:
        A: List of comparable elements
    """
    n = len(A)
    
    for i in range(n - 1):
        min_idx = i
        
        # Find index of the smallest element in remaining array
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        A[i], A[min_idx] = A[min_idx], A[i]


# Example usage
if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    print(f"Original array: {array}")
    
    selection_sort(array)
    print(f"Sorted array: {array}")