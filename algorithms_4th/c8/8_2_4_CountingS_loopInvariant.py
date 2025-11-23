 # 4/Prove the following loop invariant for COUNTING-SORT:
 # At the start of each iteration of the for loop of lines 11–13, the last
 # element in A with value i that has not yet been copied into B
 # belongs in B[C [i]].



def demonstrate_loop_invariant():
    """
    Demonstrates the loop invariant for lines 11-13
    """
    print("LOOP INVARIANT DEMONSTRATION")
    print("="*60)
    print("\nLoop Invariant:")
    print("At the start of each iteration of the for loop of lines 11-13,")
    print("the LAST element in A with value i that has not yet been copied")
    print("into B belongs in B[C[i]].")
    print()
    
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    k = max(A)
    n = len(A)
    B = [None] * n
    C = [0] * (k + 1)
    
    # Setup
    for val in A:
        C[val] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    print(f"Initial A: {A}")
    print(f"After setup, C: {C}")
    print(f"C[i] = number of elements ≤ i (ending position)\n")
    
    # Track which elements have been processed
    processed = [False] * n
    
    for iteration, j in enumerate(range(n - 1, -1, -1)):
        print(f"--- Iteration {iteration + 1}: j = {j} ---")
        
        # Show invariant BEFORE processing
        print(f"BEFORE processing A[{j}]:")
        print(f"  B: {B}")
        print(f"  C: {C}")
        
        # Find last unprocessed element with each value
        print("\n  Last unprocessed element for each value:")
        for val in range(k + 1):
            last_unprocessed_idx = None
            for idx in range(n - 1, -1, -1):
                if A[idx] == val and not processed[idx]:
                    last_unprocessed_idx = idx
                    break
            if last_unprocessed_idx is not None:
                expected_pos = C[val] - 1  # -1 for 0-indexing
                print(f"    Value {val}: last unprocessed at A[{last_unprocessed_idx}]")
                print(f"              should go to B[{expected_pos}] (C[{val}]={C[val]})")
        
        # Process current element
        value = A[j]
        position = C[value] - 1
        B[position] = value
        processed[j] = True
        C[value] -= 1
        
        print(f"\n  Processing A[{j}] = {value}:")
        print(f"    Placed at B[{position}]")
        print(f"    Decremented C[{value}]: {C[value] + 1} → {C[value]}")
        print()
    
    print("="*60)
    print(f"\nFinal B: {B}")

demonstrate_loop_invariant()



# Formal Proof of Loop Invariant:
# Loop Invariant: At the start of each iteration of the for loop (lines 11-13), for each value i, the last element in A with value i that has not yet been copied into B belongs in position B[C[i]].
# Proof by Induction:
# Initialization: Before the first iteration (j = n):

# No elements have been copied to B yet
# After line 8, C[i] contains the count of elements ≤ i
# For any value i, C[i] points to where the last occurrence of i should be placed
# The last unprocessed element with value i (which is ALL elements with value i) belongs at B[C[i]]
# ✓ Invariant holds

# Maintenance: Assume the invariant holds at the start of iteration j.

# Let v = A[j] (the current element being processed)
# By the invariant, the last unprocessed element with value v belongs at B[C[v]]
# Since we're processing from right to left, A[j] IS the last unprocessed element with value v
# Line 12: We place A[j] at B[C[v]] ✓
# Line 13: We decrement C[v]
# Now A[j] is processed, so the "last unprocessed" element with value v is the next occurrence to the left
# C[v] now correctly points to where that next occurrence should go
# For all other values i ≠ v, the invariant is unchanged
# ✓ Invariant holds for next iteration

# Termination: When j = 0 (loop completes):

# All elements have been processed
# Each element was placed in its correct sorted position
# B contains the sorted array
# ✓ Algorithm is correct
