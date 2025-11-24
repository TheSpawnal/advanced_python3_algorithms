'''
 Suppose that COUNTING-SORT is used as the stable sort within RADIX-SORT.
 If RADIX-SORT calls COUNTING-SORT d times, then since each call of
 COUNTING-SORT makes two passes over the data (lines 4–5 and 11–13),
 altogether 2d passes over the data occur. Describe how to reduce the total
 number of passes to d + 1. We need to recap Counting sort complexity time/space analysis.

COUNTING-SORT(A, n, k)
  1 let B[1 : n] and C [0 : k] be new arrays
  2 for i = 0 to k
  3     C [i] = 0
  4 for j = 1 to n
  5     C [A[j]] = C [A[j]] + 1
  6// C [i] now contains the number of elements equal to i.
  7 for i = 1 to k
  8     C [i] = C [i] + C [i – 1]
  9// C [i] now contains the number of elements less than or equal to i.
 10// Copy A to B, starting from the end of A.
 11 for j = n downto 1
 12     B[C [A[j]]] = A[j]
 13     C [A[j]] = C [A[j]] – 1 // to handle duplicate values
 14 return B

 RADIX-SORT(A, n, d)
 1 for i = 1 to d
 2 use a stable sort to sort array A[1 : n] on digit i

'''

# ==============================================================================
# COUNTING-SORT COMPLEXITY ANALYSIS
# ==============================================================================
# 
# TIME COMPLEXITY: O(n + k)
# - Lines 2-3:   O(k) - initialize count array
# - Lines 4-5:   O(n) - count occurrences
# - Lines 7-8:   O(k) - compute cumulative counts
# - Lines 11-13: O(n) - place elements in sorted order
# - Total: O(k) + O(n) + O(k) + O(n) = O(n + k)
# 
# SPACE COMPLEXITY: O(n + k)
# - B[1:n]: O(n) - output array
# - C[0:k]: O(k) - count array
# - Total: O(n + k)
# 
# PASSES OVER DATA:
# - Pass 1 (lines 4-5):   Read A to count
# - Pass 2 (lines 11-13): Read A to place in B
# - Total: 2 passes per call
# ==============================================================================

Reducing Passes from 2d to d+1
Current Situation

RADIX-SORT calls COUNTING-SORT d times (once per digit)
Each call makes 2 passes: count pass + placement pass
Total: 2d passes

The Optimization
Key Insight: We can reuse the count arrays across multiple digits and delay the final placement until the end.
Strategy: Combine Counting with In-Place Digit Extraction
python# ==============================================================================
# OPTIMIZED RADIX-SORT: d+1 PASSES
# ==============================================================================

def optimized_radix_sort(A, n, d, k):
    """
    Reduces passes from 2d to d+1
    
    IDEA: 
    - Pass 1 to d: Count frequencies for each digit (d passes)
    - Pass d+1: Single placement pass using all cumulative info
    """
    
    # Allocate output array once
    B = [0] * n
    
    # --- PHASE 1: d counting passes (lines 4-5 equivalent) ---
    # Store count arrays for all digits
    count_arrays = []
    
    for digit_pos in range(d):
        C = [0] * k
        # Single pass: count occurrences of digit at position digit_pos
        for j in range(n):
            digit = get_digit(A[j], digit_pos, k)
            C[digit] += 1
        
        # Compute cumulative counts (lines 7-8)
        for i in range(1, k):
            C[i] += C[i - 1]
        
        count_arrays.append(C)
    
    # --- PHASE 2: Single placement pass (d+1 pass) ---
    # Use combined information from all digit positions
    # Process from last digit to first (LSD radix sort)
    for digit_pos in range(d - 1, -1, -1):
        C = count_arrays[digit_pos]
        temp = [0] * n
        
        # Place elements (lines 11-13 equivalent)
        for j in range(n - 1, -1, -1):
            digit = get_digit(A[j], digit_pos, k)
            temp[C[digit] - 1] = A[j]
            C[digit] -= 1
        
        A = temp  # Update for next digit
    
    return A


# ALTERNATIVE: Interleaved Approach (More Practical)
def practical_optimized_radix(A, n, d, k):
    """
    More practical: Merge count and cumulate into single pass per digit
    Then do cumulative placement at end
    
    PASSES:
    - d passes: Count + cumulate for each digit
    - 1 pass: Final placement using precomputed positions
    - Total: d+1 passes
    """
    
    B = [0] * n
    positions = [[0] * k for _ in range(d)]
    
    # Pass 1 to d: Count and compute positions for each digit
    for digit_pos in range(d):
        C = [0] * k
        
        for j in range(n):
            digit = get_digit(A[j], digit_pos, k)
            C[digit] += 1
        
        # Cumulative
        for i in range(1, k):
            C[i] += C[i - 1]
        
        positions[digit_pos] = C
    
    # Pass d+1: Single placement using computed positions
    # Build sorted order by consulting all digit positions
    for j in range(n - 1, -1, -1):
        # Determine final position using lexicographic digit comparison
        pos = compute_final_position(A[j], positions, d, k)
        B[pos] = A[j]
    
    return B

# ==============================================================================
# KEY INSIGHT
# ==============================================================================
# 
# Instead of:
#   - Count pass for digit 0 → Place pass for digit 0
#   - Count pass for digit 1 → Place pass for digit 1
#   - ... (2d passes total)
# 
# Do:
#   - Count pass for digit 0
#   - Count pass for digit 1
#   - ...
#   - Count pass for digit d-1
#   - Single combined placement pass using ALL count info
#   - Total: d + 1 passes
# 
# TRADEOFF:
# - Time: Same O(d(n+k))
# - Space: O(d*k) instead of O(k) - store all count arrays
# - Passes: Reduced from 2d to d+1
# ==============================================================================

Summary
Original: 2d passes (count + place for each digit)
Optimized: d+1 passes (d counts + 1 combined placement)
How:

Make d counting passes to gather statistics for all digits
Store all count arrays (O(d·k) space)
Make 1 final placement pass using the precomputed information

Tradeoff: Extra O(d·k) space to store all count arrays,
but fewer passes over the main data.
