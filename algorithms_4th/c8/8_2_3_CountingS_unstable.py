# 3/Suppose that we were to rewrite the for loop header in line 11 of the
#  COUNTING-SORT as
#  11for j = 1 to n
#  Show that the algorithm still works properly, but that it is not stable. Then
#  rewrite the pseudocode for counting sort so that elements with the same
#  value are written into the output array in order of increasing index and the
#  algorithm is stable.

# COUNTING-SORT-STABLE-FORWARD(A, n, k)
#  1 let B[1 : n] and C[0 : k] be new arrays
#  2 for i = 0 to k
#  3     C[i] = 0
#  4 for j = 1 to n
#  5     C[A[j]] = C[A[j]] + 1
#  6 // C[i] now contains the number of elements equal to i.
#  7 for i = 1 to k
#  8     C[i] = C[i] + C[i - 1]
#  9 // C[i] now contains the number of elements less than or equal to i.
# 10 // Adjust C to contain starting positions instead of ending positions
# 11 for i = k downto 1
# 12     C[i] = C[i - 1]
# 13 C[0] = 0
# 14 // Now C[i] contains the starting position for value i
# 15 // Copy A to B, starting from the beginning of A
# 16 for j = 1 to n
# 17     B[C[A[j]]] = A[j]
# 18     C[A[j]] = C[A[j]] + 1  // INCREMENT to handle duplicates


def counting_sort_forward_unstable(A, k):
    """
    Processing from left to right - UNSTABLE version
    """
    n = len(A)
    B = [0] * n
    C = [0] * (k + 1)
    
    # Count
    for val in A:
        C[val] += 1
    
    # Cumulative
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    print("UNSTABLE VERSION (left to right):")
    print(f"Input: {A}")
    
    # Process LEFT TO RIGHT - this breaks stability!
    for j in range(n):  # Line 11: for j = 1 to n
        value = A[j]
        position = C[value] - 1
        B[position] = value
        C[value] -= 1
        print(f"  A[{j}]={value} → B[{position}]")
    
    print(f"Output: {B}")
    return B


def counting_sort_forward_stable(A, k):
    """
    Processing from left to right - STABLE version
    The key: use C[i] as the starting position, not ending position
    """
    n = len(A)
    B = [0] * n
    C = [0] * (k + 1)
    
    # Count
    for val in A:
        C[val] += 1
    
    # Cumulative - but now C[i] is the STARTING position for value i
    # We compute where each value STARTS instead of where it ENDS
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    # Shift C right: C[i] now holds where value i should START
    for i in range(k, 0, -1):
        C[i] = C[i - 1]
    C[0] = 0
    
    print("\nSTABLE VERSION (left to right with modified C):")
    print(f"Input: {A}")
    print(f"C (starting positions): {C}")
    
    # Process LEFT TO RIGHT - now stable!
    for j in range(n):  # for j = 1 to n
        value = A[j]
        position = C[value]  # Use current position
        B[position] = value
        C[value] += 1  # Increment (not decrement!)
        print(f"  A[{j}]={value} → B[{position}]")
    
    print(f"Output: {B}")
    return B


# Demonstration
print("="*60)
A_demo = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
counting_sort_forward_unstable(A_demo.copy(), max(A_demo))
print()
counting_sort_forward_stable(A_demo.copy(), max(A_demo))



