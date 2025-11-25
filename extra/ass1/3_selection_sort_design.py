
# Design a sorting algorithm (selection sort) which 
# follows the following procedure. First find the smallest 
# element of A[1:n] and exchange it with the element in 
# A[1]. Then find the smallest element of A[2:n], and 
# exchange it with A[2]. Continue in this manner for the 
# first n-1 elements of A.  
# What loop invariant does this algorithm maintain?  
# Give the worst-case running time of selection sort in theta 
# notation. Compare with the best scenario running time.


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
Loop Invariant
Invariant: At the start of each iteration of the outer for loop (with index i), the subarray A[1:i-1] contains the (i-1) smallest elements of the original array in sorted order, and A[i:n] contains the remaining elements.
Proof:
Initialization: Before first iteration (i = 1), A[1:0] is empty and trivially sorted. Invariant holds.
Maintenance: Assume invariant holds at start of iteration i. The inner loop finds the smallest element in A[i:n] and swaps it with A[i]. Now A[1:i] contains the i smallest elements in sorted order. Invariant holds for next iteration.
Termination: Loop terminates when i = n. By invariant, A[1:n-1] contains (n-1) smallest elements sorted, and A[n] contains the largest element. Thus A[1:n] is sorted.
Time Complexity Analysis
Worst-case: Θ(n²)

Outer loop: (n-1) iterations
Inner loop iteration i: (n-i) comparisons
Total comparisons: Σ(n-i) for i=1 to n-1 = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = Θ(n²)

Best-case: Θ(n²)

Algorithm always performs same number of comparisons regardless of input
Even if array is already sorted, inner loop still executes fully
No early termination possible

Key observation: Selection sort is NOT input-sensitive. Best = Worst = Average = Θ(n²)


Algorithm        Best Case    Worst Case   Stable?   In-place?
Selection Sort   Θ(n²)        Θ(n²)        No        Yes
Insertion Sort   Θ(n)         Θ(n²)        Yes       Yes
Merge Sort       Θ(n log n)   Θ(n log n)   Yes       No
Quick Sort       Θ(n log n)   Θ(n²)        No        Yes
Heap Sort        Θ(n log n)   Θ(n log n)   No        Yes