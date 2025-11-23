

# 1/illustrate the operation of COUNTING-SORT on
#  the array A = 〈6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2〉 with pyhton3 implementation.

def counting_sort_illustrated(A, k):
    """
    Counting sort with detailed step-by-step illustration.
    A: input array (0-indexed in Python)
    k: maximum value in A
    """
    n = len(A)
    B = [0] * n  # Output array
    C = [0] * (k + 1)  # Count array
    
    print(f"Input array A: {A}")
    print(f"n = {n}, k = {k}")
    print("\n" + "="*60)
    
    # Step 1: Count occurrences (lines 2-5)
    print("\nSTEP 1: Counting occurrences")
    for i in range(len(A)):
        C[A[i]] += 1
    print(f"C after counting: {C}")
    print("Interpretation: C[i] = number of elements equal to i")
    for i in range(k + 1):
        if C[i] > 0:
            print(f"  Value {i} appears {C[i]} time(s)")
    
    # Step 2: Cumulative sum (lines 7-8)
    print("\n" + "="*60)
    print("\nSTEP 2: Computing cumulative sums")
    print(f"C before cumulative: {C}")
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    print(f"C after cumulative:  {C}")
    print("Interpretation: C[i] = number of elements ≤ i")
    for i in range(k + 1):
        print(f"  C[{i}] = {C[i]} (position where value {i} should end)")
    
    # Step 3: Place elements (lines 11-13)
    print("\n" + "="*60)
    print("\nSTEP 3: Placing elements (right to left)")
    print(f"Processing A from right to left: {A[::-1]}")
    print()
    
    for j in range(n - 1, -1, -1):
        value = A[j]
        position = C[value] - 1  # -1 because arrays are 0-indexed
        B[position] = value
        C[value] -= 1
        
        print(f"j={j}: A[{j}]={value}")
        print(f"  → Place at B[{position}]")
        print(f"  → Decrement C[{value}]: {C[value] + 1} → {C[value]}")
        print(f"  B so far: {B}")
        print(f"  C so far: {C}")
        print()
    
    print("="*60)
    print(f"\nFinal sorted array B: {B}")
    return B


# Test with the given array
A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
k = max(A)
result = counting_sort_illustrated(A, k)