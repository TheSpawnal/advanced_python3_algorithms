
'''
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
 

 Using Figure the provided pseudocode as a model, illustrate the operation of 
BUCKET-SORT on the array A = 〈.79, .13, .16, .64, .39, .20, .89, .53, .71, .42〉 through python3.
two clever strategies expected. 
'''

#calssic
def bucket_sort_verbose(A, n):
    """Classic bucket sort with detailed visualization"""
    print(f"Input: {A}\n")
    
    # 1: Create n empty buckets
    B = [[] for _ in range(n)]
    print(f"Step 1: Created {n} empty buckets")
    print(f"Buckets: {B}\n")
    
    #  2: Distribute elements into buckets
    print("Step 2: Distribute elements into buckets")
    for i in range(n):
        bucket_index = int(n * A[i])  # ⌊n · A[i]⌋
        B[bucket_index].append(A[i])
        print(f"  A[{i}] = {A[i]:.2f} → Bucket[{bucket_index}] (because ⌊{n} × {A[i]:.2f}⌋ = {bucket_index})")
    
    print(f"\nBuckets after distribution:")
    for i, bucket in enumerate(B):
        if bucket:
            print(f"  B[{i}]: {[f'{x:.2f}' for x in bucket]}")
        else:
            print(f"  B[{i}]: []")
    
    #3: Sort each bucket with insertion sort
    print("\nStep 3: Sort each non-empty bucket with insertion sort")
    for i in range(n):
        if B[i]:
            print(f"  Before: B[{i}] = {[f'{x:.2f}' for x in B[i]]}")
            B[i] = insertion_sort(B[i])
            print(f"  After:  B[{i}] = {[f'{x:.2f}' for x in B[i]]}")
    
    #4: Concatenate buckets
    print("\nStep 4: Concatenate all buckets in order")
    result = []
    for i in range(n):
        result.extend(B[i])
        if B[i]:
            print(f"  Added B[{i}]: {[f'{x:.2f}' for x in B[i]]}")
    
    print(f"\nFinal sorted array: {[f'{x:.2f}' for x in result]}")
    return result

def insertion_sort(arr):
    """Standard insertion sort for bucket contents"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Test
A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
n = len(A)
print("="*50)
print("STRATEGY 1: CLASSIC VERBOSE BUCKET SORT")
print("="*70)



#ascii representation
def bucket_sort_visual(A, n  ):
    """Bucket sort with visual ASCII representation"""
    print(f"Input array: {[f'{x:.2f}' for x in A]}")
    print(f"Range: [0.00, 1.00) divided into {n} buckets\n")
    
    # Create buckets
    B = [[] for _ in range(n)]
    
    # Distribution phase with visual
    print("="*70)
    print("DISTRIBUTION PHASE: Mapping elements to buckets")
    print("="*70)
    
    for i in range(n):
        bucket_idx = int(n * A[i])
        B[bucket_idx].append(A[i])
        
        # Visual number line
        print(f"\nElement: {A[i]:.2f}")
        print(f"Bucket index: ⌊{n} × {A[i]:.2f}⌋ = ⌊{n * A[i]:.2f}⌋ = {bucket_idx}")
        print("Number line: ", end="")
        print("".join(["[X]" if j == bucket_idx else "[ ]" for j in range(n)]))
        print(f"Buckets:     {' '.join([f'{i:2d}' for i in range(n)])}")
    
    # Show bucket contents
    print("\n" + "="*70)
    print("BUCKET CONTENTS (Before Sorting)")
    print("="*70)
    print_buckets_ascii(B)
    
    # Sort each bucket
    print("\n" + "="*70)
    print("SORTING PHASE: Insertion sort on each bucket")
    print("="*70)
    for i in range(n):
        if B[i]:
            print(f"\nBucket[{i}] before: {[f'{x:.2f}' for x in B[i]]}")
            B[i] = insertion_sort(B[i])
            print(f"Bucket[{i}] after:  {[f'{x:.2f}' for x in B[i]]}")
    
    # Show sorted buckets
    print("\n" + "="*70)
    print("BUCKET CONTENTS (After Sorting)")
    print("="*70)
    print_buckets_ascii(B)
    
    # Concatenate
    result = []
    for bucket in B:
        result.extend(bucket)
    
    print("\n" + "="*70)
    print("CONCATENATION: Merge all buckets in order")
    print("="*70)
    print(f"Final result: {[f'{x:.2f}' for x in result]}")
    
    return result

def print_buckets_ascii(B):
    """Pretty print buckets as ASCII art"""
    for i, bucket in enumerate(B):
        print(f"B[{i}] |", end=" ")
        if bucket:
            for val in bucket:
                print(f"[{val:.2f}]", end=" ")
        else:
            print("(empty)", end="")
        print()

# Test
print("\n\n")
print("="*70)
print("STRATEGY 2: VISUAL ASCII ART BUCKET SORT")
print("="*70)
A2 = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
bucket_sort_visual(A2, len(A2))


# ==============================================================================
# BUCKET-SORT COMPLEXITY ANALYSIS
# ==============================================================================
# 
# ASSUMPTIONS:
# - Input: n numbers uniformly distributed in [0, 1)
# - n buckets covering equal ranges
# - Insertion sort used for each bucket
# 
# TIME COMPLEXITY:
# - Lines 2-3:   O(n) - initialize n empty buckets
# - Lines 4-5:   O(n) - distribute n elements into buckets
# - Lines 6-7:   O(n) average case - sort all buckets
#                * Expected elements per bucket: n/n = 1
#                * Insertion sort on bucket of size k: O(k²)
#                * Expected total: n × O(1)² = O(n)
#                * Worst case: O(n²) if all elements in one bucket
# - Line 8:      O(n) - concatenate all elements
# 
# AVERAGE CASE: O(n) [with uniform distribution]
# WORST CASE:   O(n²) [all elements in one bucket]
# 
# SPACE COMPLEXITY: O(n)
# - B[0:n-1]: O(n) - bucket array
# - Total stored elements: O(n)
# 
# KEY INSIGHT:
# - Works best when input is uniformly distributed
# - Each bucket gets ~1 element → insertion sort is O(1)
# - Linear time sorting! (average case)
# 
# BUCKET RANGES for n=10:
# - B[0]: [0.0, 0.1)
# - B[1]: [0.1, 0.2)
# - B[2]: [0.2, 0.3)
# - ...
# - B[9]: [0.9, 1.0)
# ==============================================================================
```

---

## Quick Output Preview
```
A = [.79, .13, .16, .64, .39, .20, .89, .53, .71, .42]

Distribution:
  .79 → B[7]  (⌊10 × .79⌋ = 7)
  .13 → B[1]  (⌊10 × .13⌋ = 1)
  .16 → B[1]  (⌊10 × .16⌋ = 1)
  .64 → B[6]  (⌊10 × .64⌋ = 6)
  .39 → B[3]  (⌊10 × .39⌋ = 3)
  .20 → B[2]  (⌊10 × .20⌋ = 2)
  .89 → B[8]  (⌊10 × .89⌋ = 8)
  .53 → B[5]  (⌊10 × .53⌋ = 5)
  .71 → B[7]  (⌊10 × .71⌋ = 7)
  .42 → B[4]  (⌊10 × .42⌋ = 4)

Buckets before sort:
  B[1]: [.13, .16]
  B[2]: [.20]
  B[3]: [.39]
  B[4]: [.42]
  B[5]: [.53]
  B[6]: [.64]
  B[7]: [.79, .71]
  B[8]: [.89]

After sorting B[1]: [.13, .16]
After sorting B[7]: [.71, .79]

Final: [.13, .16, .20, .39, .42, .53, .64, .71, .79, .89]














bucket_sort_verbose(A, n)
