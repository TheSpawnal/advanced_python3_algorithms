# Timing Tools Overview

# time module - Simple, built-in, good for basic timing
# timeit module - Most accurate for benchmarking, runs multiple iterations
# cProfile/profile - Detailed profiling with function-level statistics
# perf_counter - High-resolution timer (best for performance measurement)
# @profile decorators - Third-party like line_profiler and memory_profiler

# MERGE-SORT IMPLEMENTATIONS WITH TIMING METRICS

import time
import timeit
from functools import wraps

# ============= TIMING DECORATORS =============

def timing_decorator(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = (end - start) * 1000  # Convert to milliseconds
        print(f"⏱️  {func.__name__} took: {elapsed:.4f} ms")
        return result
    return wrapper


# ============= VERSION 1: CLASSIC MERGE SORT =============

def merge(A, p, q, r):
    """
    Merge two sorted subarrays A[p:q+1] and A[q+1:r+1] into A[p:r+1].
    """
    nL = q - p + 1  # Length of left subarray
    nR = r - q      # Length of right subarray
    
    # Create temporary arrays
    L = [0] * nL
    R = [0] * nR
    
    # Copy data to temp arrays L and R
    for i in range(nL):
        L[i] = A[p + i]
    
    for j in range(nR):
        R[j] = A[q + 1 + j]
    
    # Merge the temp arrays back into A[p:r+1]
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = p  # Initial index of merged subarray
    
    # Merge while both subarrays have elements
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements of L, if any
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    
    # Copy remaining elements of R, if any
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort_classic(A, p, r):
    """
    Sort array A[p:r+1] using merge sort algorithm (classic in-place version).
    """
    if p >= r:  # Base case: 0 or 1 element
        return
    
    q = (p + r) // 2  # Find the middle point
    
    merge_sort_classic(A, p, q)      # Sort first half
    merge_sort_classic(A, q + 1, r)  # Sort second half
    merge(A, p, q, r)                # Merge the sorted halves


# ============= VERSION 2: PYTHONIC MERGE SORT =============

def merge_sort_pythonic(A):
    """Pythonic merge sort using slicing (returns new list)."""
    if len(A) <= 1:
        return A
    
    mid = len(A) // 2
    left = merge_sort_pythonic(A[:mid])
    right = merge_sort_pythonic(A[mid:])
    
    # Merge
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


# ============= TIMING WRAPPERS =============

@timing_decorator
def timed_merge_sort_classic(array):
    """Timed version of classic merge sort."""
    merge_sort_classic(array, 0, len(array) - 1)
    return array


@timing_decorator
def timed_merge_sort_pythonic(array):
    """Timed version of pythonic merge sort."""
    return merge_sort_pythonic(array)


# ============= MAIN EXECUTION =============

if __name__ == "__main__":
    print("=" * 70)
    print("MERGE SORT TIMING COMPARISON")
    print("=" * 70)
    
    # Test array
    test_array = [3, 41, 52, 26, 38, 57, 9, 49]
    
    print("\n📊 TEST 1: Small Array (8 elements)")
    print(f"Original: {test_array}")
    
    # Version 1: Classic
    array_v1 = test_array.copy()
    result_v1 = timed_merge_sort_classic(array_v1)
    print(f"Classic Result: {result_v1}")
    
    # Version 2: Pythonic
    array_v2 = test_array.copy()
    result_v2 = timed_merge_sort_pythonic(array_v2)
    print(f"Pythonic Result: {result_v2}")
    
    # ============= LARGER ARRAY TESTS =============
    
    import random
    
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        print(f"\n📊 TEST: Array with {size} elements")
        large_array = [random.randint(1, 10000) for _ in range(size)]
        
        # Classic version
        array_classic = large_array.copy()
        timed_merge_sort_classic(array_classic)
        
        # Pythonic version
        array_pythonic = large_array.copy()
        timed_merge_sort_pythonic(array_pythonic)
    
    # ============= USING TIMEIT FOR PRECISE BENCHMARKING =============
    
    print("\n" + "=" * 70)
    print("PRECISE BENCHMARKING WITH TIMEIT (1000 runs)")
    print("=" * 70)
    
    test_size = 100
    test_data = [random.randint(1, 1000) for _ in range(test_size)]
    
    # Benchmark classic version
    classic_time = timeit.timeit(
        lambda: merge_sort_classic(test_data.copy(), 0, len(test_data) - 1),
        number=1000
    )
    print(f"⏱️  Classic merge sort (avg): {(classic_time / 1000) * 1000:.4f} ms")
    
    # Benchmark pythonic version
    pythonic_time = timeit.timeit(
        lambda: merge_sort_pythonic(test_data.copy()),
        number=1000
    )
    print(f"⏱️  Pythonic merge sort (avg): {(pythonic_time / 1000) * 1000:.4f} ms")
    
    # Calculate difference
    if classic_time < pythonic_time:
        speedup = pythonic_time / classic_time
        print(f"\n✅ Classic version is {speedup:.2f}x faster")
    else:
        speedup = classic_time / pythonic_time
        print(f"\n✅ Pythonic version is {speedup:.2f}x faster")
    
    # ============= EDGE CASES =============
    
    print("\n" + "=" * 70)
    print("EDGE CASES TESTING")
    print("=" * 70)
    
    test_cases = [
        ([5], "Single element"),
        ([2, 1], "Two elements"),
        ([], "Empty array"),
        ([1, 2, 3, 4], "Already sorted"),
        ([4, 3, 2, 1], "Reverse sorted"),
    ]
    
    for test, description in test_cases:
        if test:
            print(f"\n🧪 {description}: {test}")
            array_test = test.copy()
            result = timed_merge_sort_classic(array_test)
            print(f"   Result: {result}")


# ============= PROFILING WITH cProfile (Optional) =============
"""
To run with detailed profiling, use:

    python -m cProfile -s cumtime merge_sort.py

Or programmatically:
"""

def profile_merge_sort():
    import cProfile
    import pstats
    
    test_array = [random.randint(1, 1000) for _ in range(1000)]
    
    profiler = cProfile.Profile()
    profiler.enable()
    
    merge_sort_classic(test_array, 0, len(test_array) - 1)
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumtime')
    print("\n" + "=" * 70)
    print("cProfile DETAILED PROFILING")
    print("=" * 70)
    stats.print_stats(10)  # Top 10 functions

# Uncomment to run profiling
# profile_merge_sort()
