# Consider the searching problem:
#  Input: A sequence of n numbers 〈a1, a2, … , an〉 stored in array A[1 : n] and
#  a value x.
#  Output: An index i such that x equals A[i] or the special value NIL if x does
#  not appear in A.
#  Write pseudocode for linear search, which scans through the array from
#  beginning to end, looking for x. Using a loop invariant, prove that your
#  algorithm is correct. Make sure that your loop invariant fulfills the three
#  necessary properties.

# LINEAR-SEARCH(A, n, x)
# for i = 1 to n
#     if A[i] == x
#         return i
# return NIL

def linear_search(A, x):
    """
    Linear search algorithm
    
    Args:
        A: List of elements
        x: Value to search for
    
    Returns:
        Index i where A[i] == x, or None if x not found
    """
    for i in range(len(A)):
        if A[i] == x:
            return i
    return None


def linear_search_verbose(A, x):
    """
    Linear search with detailed output for demonstration
    """
    print(f"Searching for {x} in array: {A}")
    print(f"Loop Invariant: At each step i, x is not in A[0:i]\n")
    
    for i in range(len(A)):
        print(f"Step {i+1}: Checking A[{i}] = {A[i]}")
        print(f"  Invariant holds: {x} not found in A[0:{i}]")
        
        if A[i] == x:
            print(f"  ✓ Found! A[{i}] == {x}")
            print(f"\nResult: Index {i}")
            return i
        else:
            print(f"  A[{i}] ≠ {x}, continue...")
    
    print(f"\n✗ Not found. {x} not in array A[0:{len(A)}]")
    print(f"Result: None")
    return None


# Test cases
print("="*60)
print("LINEAR SEARCH EXAMPLES")
print("="*60)

# Example 1: Value exists
print("\n### Example 1: Search for 26 ###")
array1 = [31, 41, 59, 26, 41, 58]
result1 = linear_search_verbose(array1, 26)

print("\n" + "="*60)

# Example 2: Value doesn't exist
print("\n### Example 2: Search for 100 ###")
array2 = [31, 41, 59, 26, 41, 58]
result2 = linear_search_verbose(array2, 100)

print("\n" + "="*60)

# Example 3: Multiple occurrences (returns first)
print("\n### Example 3: Search for 41 (multiple occurrences) ###")
array3 = [31, 41, 59, 26, 41, 58]
result3 = linear_search_verbose(array3, 41)

print("\n" + "="*60)

# Simple usage examples
print("\n### Simple Usage ###")
test_array = [10, 20, 30, 40, 50]
print(f"Array: {test_array}")
print(f"Search for 30: {linear_search(test_array, 30)}")  # Returns 2
print(f"Search for 25: {linear_search(test_array, 25)}")  # Returns None
print(f"Search for 50: {linear_search(test_array, 50)}")  # Returns 4