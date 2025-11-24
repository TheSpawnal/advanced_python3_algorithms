
# Which of the following sorting algorithms are stable: insertion sort, merge sort, 
# heapsort, and quicksort? Give a simple scheme that makes any comparison sort stable. 
# How much additional time and space does your scheme entail?


# ==============================================================================
# SORTING ALGORITHM COMPLEXITY CHEAT SHEET
# ==============================================================================
# 
# | Algorithm        | Best      | Average   | Worst     | Space    | Stable? |
# |------------------|-----------|-----------|-----------|----------|---------|
# | Insertion Sort   | O(n)      | O(n²)     | O(n²)     | O(1)     | YES     |
# | Merge Sort       | O(n logn) | O(n logn) | O(n logn) | O(n)     | YES     |
# | Heapsort         | O(n logn) | O(n logn) | O(n logn) | O(1)     | NO      |
# | Quicksort        | O(n logn) | O(n logn) | O(n²)     | O(log n) | NO      |
# 
# NOTES:
# - Insertion Sort: Best for small/nearly-sorted data, adaptive, online
# - Merge Sort: Consistent performance, parallelizable, external sort champion
# - Heapsort: In-place, guaranteed O(n log n), poor cache locality
# - Quicksort: Fast average case, cache-friendly, needs good pivot strategy
# 
# DEFINITIONS:
# - Stable: Preserves relative order of equal elements
# - In-place: Uses O(1) extra space (excluding recursion stack)
# - Space for Quicksort: O(log n) recursion stack in balanced case
# 
# MAKING ANY SORT STABLE:
# - Attach original index as tie-breaker: (value, index)
# - Cost: +O(n) space, +O(1) per comparison
# ==============================================================================
'''
Stability Analysis
Stable: Insertion Sort, Merge Sort
Unstable: Heapsort, Quicksort
Making ANY Comparison Sort Stable
Scheme: Attach the original index to each element as a tie-breaker.
python# Transform: [5, 3, 5, 1] → [(5,0), (3,1), (5,2), (1,3)]
# Compare: if values equal, compare indices
# After sort: [(1,3), (3,1), (5,0), (5,2)] → [1, 3, 5, 5]
Cost:

Time: O(1) per comparison (index check is constant)
Space: O(n) extra for storing indices



Key Characteristics
Insertion Sort
Shifts elements one-by-one to insert in correct position
Adaptive: blazing fast on nearly-sorted data
Online: can sort as data arrives

Merge Sort
Divide-and-conquer: split, sort halves, merge
Guaranteed O(n log n) - no bad inputs
External sort champion (works great on disk)

Heapsort
Build max-heap, repeatedly extract maximum
In-place with guaranteed O(n log n)
Poor cache locality, not adaptive

Quicksort
Partition around pivot, recursively sort partitions
Average case kills it: low constant factors, cache-friendly
Degenerates to O(n²) on sorted/reverse-sorted without good pivot selection
Randomized pivot or median-of-three helps


Bottom Line: Need stability? Merge sort. 
Need in-place + guaranteed? Heapsort. 
Need speed? Quicksort (with good pivot strategy). 
Need simplicity for small n? Insertion sort.

Definitions
Stable Sort: Preserves the relative order of equal elements.
python# Input:  [(5,A), (3,B), (5,C), (1,D)]  # same value, different tags
# Stable: [(1,D), (3,B), (5,A), (5,C)]  # A still before C ✓
# Unstable: [(1,D), (3,B), (5,C), (5,A)]  # C jumped before A ✗
In-place Sort: Uses O(1) extra space (excluding input array).
python# In-place: modifies original array, no significant extra memory
# Out-of-place: creates new arrays/structures (e.g., merge sort needs O(n))

'''
