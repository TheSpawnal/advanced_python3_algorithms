
'''
Consider sorting n numbers stored in array A[1 : n] by first finding the
smallest element of A[1 : n] and exchanging it with the element in A[1].
Then find the smallest element of A[2 : n], and exchange it with A[2]. 
Then find the smallest element of A[3 : n], and exchange it with A[3]. 
Continue in this manner for the first n – 1 elements of A. 
Write pseudocode for this algorithm, which is known as selection sort. 
What loop invariant does this algorithm maintain Why does it need to run for only the first n – 1
elements, rather than for all n elements Give the worst-case running time of selection sort in Θ-notation. 
Is the best-case running time any better
'''


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

'''
solution:

SELECTION-SORT(A,n)
  for i = 1 to n - 1
    smallest = i
    for j = i + 1 to n
      if A[j] < A[smallest]
        smallest = j
    exchange A[i] with A[smallest]

  The algo maintains loop invariant that at the start of each iteration of the outer
  for loop, the subarray A[1:i-1]consists of the i-1 smallest elements in the array
  A[1:n], and this subarray is in sorted order. After the first n-1 elemnts, the subarray A[1:n-1]
  contains the smallest n-1 elements, sorted, and therefore element A[n] must be the largest element.
  the running time is O(n^2) for all cases.
'''
