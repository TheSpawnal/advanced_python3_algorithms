def insertion_sort_decreasing(A):
    """
    INSERTION-SORT for decreasing order
    Sorts array A in place from largest to smallest
    """
    n = len(A)
    print(f"Initial array: {A}\n")
    
    for i in range(1, n):  # for i = 2 to n
        key = A[i]
        print(f"Step {i}: key = A[{i}] = {key}")
        print(f"  Before: {A}")
        
        # Insert A[i] into the sorted subarray A[0 : i-1]
        j = i - 1
        while j >= 0 and A[j] < key:  # Changed from > to 
            A[j + 1] = A[j]
            j = j - 1
            print(f"    Shifting: {A}")
        
        A[j + 1] = key
        print(f"  After:  {A}")
        print()
    
    return A

# Test with the same sequence
array = [31, 41, 59, 26, 41, 58]
print("="*50)
print("INSERTION SORT - DECREASING ORDER")
print("="*50)
sorted_array = insertion_sort_decreasing(array)
print("="*50)
print(f"Final sorted array: {sorted_array}")

## Pseudocode Version
# ```
# INSERTION-SORT-DECREASING(A, n)
# for i = 2 to n
#     key = A[i]
#     // Insert A[i] into the sorted subarray A[1 : i – 1]
#     j = i – 1
#     while j > 0 and A[j] < key    // Changed from > to 
#         A[j + 1] = A[j]
#         j = j – 1
#     A[j + 1] = key
