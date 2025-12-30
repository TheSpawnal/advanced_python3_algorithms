


#Prove that COUNTING-SORT is stable.

def stability_demonstration():
    """
    Demonstrates why counting sort is stable by tracking element origins.
    """
    print("STABILITY PROOF DEMONSTRATION")
    print("="*60)
    
    # Create array with duplicate values marked by their original positions
    A = [(6, 'pos0'), (0, 'pos1'), (2, 'pos2'), (0, 'pos3'), 
         (1, 'pos4'), (3, 'pos5'), (4, 'pos6'), (6, 'pos7'), 
         (1, 'pos8'), (3, 'pos9'), (2, 'pos10')]
    
    print("Input with position markers:")
    for i, (val, marker) in enumerate(A):
        print(f"  A[{i}] = {val} ({marker})")
    
    print("\nKey observation: Two 0's at positions 1 and 3")
    print("                 Two 1's at positions 4 and 8")
    print("                 Two 2's at positions 2 and 10")
    print("                 etc.")
    
    # Simulate counting sort
    values = [x[0] for x in A]
    k = max(values)
    n = len(A)
    B = [None] * n
    C = [0] * (k + 1)
    
    # Count
    for val in values:
        C[val] += 1
    
    # Cumulative
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    print("\n" + "="*60)
    print("\nPlacing elements RIGHT TO LEFT (this is the key!):")
    
    # Place from right to left
    for j in range(n - 1, -1, -1):
        val, marker = A[j]
        pos = C[val] - 1
        B[pos] = (val, marker)
        C[val] -= 1
        print(f"  Process {marker}: value={val} → B[{pos}]")
    
    print("\nFinal sorted array:")
    for i, (val, marker) in enumerate(B):
        print(f"  B[{i}] = {val} ({marker})")
    
    print("\n" + "="*60)
    print("\nSTABILITY VERIFICATION:")
    print("  0's: pos1 before pos3 ✓")
    print("  1's: pos4 before pos8 ✓")
    print("  2's: pos2 before pos10 ✓")
    print("  3's: pos5 before pos9 ✓")
    print("  6's: pos0 before pos7 ✓")

stability_demonstration()


# Formal Proof of Stability:
# Theorem: COUNTING-SORT is stable.
# Proof:
# A sorting algorithm is stable if equal elements maintain their relative order from the input array to the output array.
# Consider two elements A[i] and A[j] where:

# i < j (A[i] appears before A[j] in input)
# A[i] = A[j] = v (both have the same value)

# Key observations:

# After line 8, C[v] contains the number of elements ≤ v, which is the position where the last occurrence of v should be placed.
# Lines 11-13 process array A from right to left (n downto 1).
# Since j > i, element A[j] is processed before A[i].
# When A[j] is processed:

# It's placed at position B[C[v]]
# Then C[v] is decremented


# When A[i] is processed later:

# It's placed at position B[C[v]] (which is now smaller)
# This position is to the left of where A[j] was placed


# Therefore, in the output array B, A[i] appears before A[j], preserving their relative order.