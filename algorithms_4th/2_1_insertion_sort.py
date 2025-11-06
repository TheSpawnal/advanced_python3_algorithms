# INSERTION-SORT(A, n) 
# for i = 2 to n
#     key = A[i]
#     // Insert A[i] into the sorted subarray A[1 : i – 1].
#     j = i – 1
#     while j > 0 and A[j] > key
#         A[j + 1] = A[j]
#         j = j – 1
#     A[j + 1] = 

# illustrate the operation of INSERTION-SORT on an array 
# initially containing the sequence 〈31, 41, 59, 26, 41, 58〉 in python3

def insertion_sort(A):
    """
    INSERTION-SORT(A, n)
    Sorts array A in place
    """
    n = len(A)
    print(f"Initial array: {A}\n")
    
    for i in range(1, n):  # for i = 2 to n (adjusting for 0-indexed)
        key = A[i]
        print(f"Step {i}: key = A[{i}] = {key}")
        print(f"  Before: {A}")
        
        # Insert A[i] into the sorted subarray A[0 : i-1]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
            print(f"    Shifting: {A}")
        
        A[j + 1] = key
        print(f"  After:  {A}")
        print()
    
    return A

# Test with the given sequence
array = [31, 41, 59, 26, 41, 58]
print("="*50)
print("INSERTION SORT ILLUSTRATION")
print("="*50)
sorted_array = insertion_sort(array)
print("="*50)
print(f"Final sorted array: {sorted_array}")
