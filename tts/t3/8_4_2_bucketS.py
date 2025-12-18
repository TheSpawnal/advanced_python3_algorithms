

'''
Explain why the worst-case running time for bucket sort is Θ(n2). What
 simple change to the algorithm preserves its linear average-case running
 time and makes its worst-case running time O(n lg n)?
Recap the also best case time, with conditions and characteristics of the algorithm. 

BUCKET-SORT(A, n)
 1 let B[0 : n – 1] be a new array
 2 for i = 0 to n – 1
 3   make B[i] an empty list
 4 for i = 1 to n
 5   insert A[i] into list B[⌊n · A[i]⌋]
 6 for i = 0 to n – 1
 7   sort list B[i] with insertion sort
 8 concatenate the lists B[0], B[1], … , B[n – 1] together in order
 9 return the concatenated lists



SOLUTION:
If all the keys fall in the same bucket and they happen to be in reverse order, we have
to sort a single bucket with n items in reversed order with insertion sort. this is O(n^2).

We can use merge sort or heapsort to improve the worst-case running time. Insertion sort was 
chosen besause it operates well on linked lists, which has optimal time and requires only 
constant extra space for short linked lists. If we use another sorting algorithm, we have 
to convert each list to an array, whcih might slow down the algorithm in practice.
 '''


# ==============================================================================
# WORST-CASE SCENARIO: All Elements Land in ONE Bucket
# ==============================================================================

# Example: A = [0.01, 0.02, 0.03, 0.04, 0.05, ..., 0.09]
# All elements map to B[0] since ⌊10 × 0.0x⌋ = 0

def demonstrate_worst_case():
    """Show worst-case scenario"""
    n = 10
    # All values between [0.00, 0.10) → all go to bucket 0
    A = [i/100 for i in range(1, n+1)]  # [0.01, 0.02, ..., 0.10]
    
    print("Worst-case input:")
    print(f"A = {[f'{x:.2f}' for x in A]}\n")
    
    B = [[] for _ in range(n)]
    
    for val in A:
        bucket_idx = int(n * val)
        B[bucket_idx].append(val)
        print(f"{val:.2f} → B[{bucket_idx}]")
    
    print("\nBucket distribution:")
    for i, bucket in enumerate(B):
        if bucket:
            print(f"B[{i}]: {len(bucket)} elements")
    
    print(f"\nInsertion sort on B[0] with {len(B[0])} elements: O({len(B[0])}²) = O(n²)")

demonstrate_worst_case()

# ==============================================================================
# WHY Θ(n²)?
# ==============================================================================
# 
# TIME BREAKDOWN:
# - Lines 2-3:   O(n) - create buckets
# - Lines 4-5:   O(n) - distribute elements
# - Lines 6-7:   O(?) - sort each bucket ← THE PROBLEM
# - Line 8:      O(n) - concatenate
# 
# WORST CASE: All n elements in ONE bucket
# - Insertion sort on n elements: Θ(n²)
# - Only one bucket has work: Θ(n²)
# - Total: Θ(n) + Θ(n²) = Θ(n²)
# 
# WHEN DOES THIS HAPPEN?
# - Non-uniform distribution (all values clustered)
# - Adversarial input (sorted/reverse-sorted in narrow range)
# - Poor bucket distribution function
# ==============================================================================

# ==============================================================================
# SOLUTION: Replace Insertion Sort with O(n log n) Sort
# ==============================================================================

import heapq

def bucket_sort_improved(A, n):
    """
    Bucket sort with O(n log n) worst-case guarantee
    
    CHANGE: Line 7 - Use merge sort or heap sort instead of insertion sort
    """
    # Lines 1-3: Create buckets
    B = [[] for _ in range(n)]
    
    # Lines 4-5: Distribute
    for i in range(n):
        bucket_idx = int(n * A[i])
        if bucket_idx == n:  # Handle edge case for A[i] = 1.0
            bucket_idx = n - 1
        B[bucket_idx].append(A[i])
    
    # Lines 6-7: Sort each bucket with O(k log k) sort
    for i in range(n):
        if B[i]:
            # OPTION 1: Use built-in sort (Timsort - O(k log k))
            B[i].sort()
            
            # OPTION 2: Use merge sort
            # B[i] = merge_sort(B[i])
            
            # OPTION 3: Use heap sort
            # B[i] = heap_sort(B[i])
    
    # Line 8-9: Concatenate and return
    result = []
    for bucket in B:
        result.extend(bucket)
    
    return result

def merge_sort(arr):
    """O(k log k) merge sort"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ==============================================================================
# WHY THIS FIXES WORST-CASE
# ==============================================================================
# 
# WORST CASE: All n elements still in one bucket
# - But now: Merge sort on n elements = O(n log n)
# - Total: O(n) + O(n log n) + O(n) = O(n log n)
# 
# AVERAGE CASE: Still O(n) with uniform distribution
# - Each bucket gets ~1 element
# - n buckets × O(1 log 1) = O(n)
# - Linear time preserved!
# 
# TRADE-OFF:
# - Slightly more overhead for small buckets
# - But guaranteed O(n log n) worst-case protection
# ==============================================================================

# ==============================================================================
# BUCKET-SORT COMPLETE TIME COMPLEXITY ANALYSIS
# ==============================================================================
# 
# ORIGINAL (with Insertion Sort):
# --------------------------------
# BEST CASE:    Θ(n)
#   Condition: Each bucket gets exactly 0 or 1 element
#   Why: No sorting needed, just distribution and concatenation
#   Example: Perfectly uniform distribution with n buckets for n elements
# 
# AVERAGE CASE: Θ(n)
#   Condition: Uniform distribution, ~n/n = 1 element per bucket
#   Why: Expected O(1) elements per bucket → n × O(1²) = O(n)
#   Math: E[sort time] = Σ E[bucket_i²] = n × (1 + 1/n)² ≈ O(n)
# 
# WORST CASE:   Θ(n²)
#   Condition: All n elements in one bucket
#   Why: Insertion sort on n elements = Θ(n²)
#   Example: A = [0.01, 0.02, ..., 0.09] all map to B[0]
# 
# 
# IMPROVED (with Merge/Heap Sort):
# ---------------------------------
# BEST CASE:    Θ(n)
#   Condition: Same as above (each bucket ≤ 1 element)
#   Why: O(k log k) = O(1 log 1) = O(1) per bucket
# 
# AVERAGE CASE: Θ(n)
#   Condition: Uniform distribution
#   Why: n buckets × O(1 log 1) = O(n)
#   Preserved! Linear average case maintained
# 
# WORST CASE:   O(n log n)
#   Condition: All n elements in one bucket
#   Why: Merge sort on n elements = O(n log n)
#   Fixed! No more quadratic blowup
# 
# ==============================================================================
# SPACE COMPLEXITY
# ==============================================================================
# 
# SPACE: O(n) for both versions
# - B[0:n-1]: O(n) bucket array
# - Elements stored: O(n)
# - Recursion (merge sort): O(log n) stack
# - Total: O(n)
# 
# ==============================================================================
# KEY CHARACTERISTICS
# ==============================================================================
# 
# STABLE: YES (if using stable sort for buckets)
# - Insertion sort is stable
# - Merge sort is stable
# - Heap sort is NOT stable (use merge sort for stability)
# 
# IN-PLACE: NO
# - Requires O(n) auxiliary space for buckets
# 
# ADAPTIVE: YES (in average case)
# - Better performance with uniform distribution
# - Degrades gracefully with clustering
# 
# ONLINE: NO
# - Needs all data upfront to determine bucket ranges
# 
# CACHE-FRIENDLY: Moderate
# - Good: Sequential access within buckets
# - Bad: Scattered access during distribution
# 
# PARALLEL-FRIENDLY: YES
# - Buckets can be sorted independently
# - Easy to parallelize sorting phase
# 
# ==============================================================================
# WHEN TO USE BUCKET SORT
# ==============================================================================
# 
# IDEAL FOR:
# - Uniformly distributed floating-point numbers in [0, 1)
# - Known input range that can be divided evenly
# - External sorting (disk-based) with range partitioning
# 
# AVOID WHEN:
# - Unknown or skewed distribution
# - Integer sorting (use counting/radix sort instead)
# - Small n (overhead not worth it)
# 
# ==============================================================================


