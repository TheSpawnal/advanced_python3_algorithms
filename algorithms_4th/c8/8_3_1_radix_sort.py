# Using pseudocode as a model, illustrate the operation of 
# RADIX-SORT on the following list of English words: 
# COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.

# RADIX-SORT(A, n, d)
#  1 for i = 1 to d
#  2 use a stable sort to sort array A[1 : n] on digit i

#classic LSD(least significant digit)
def radix_sort_lsd(words):
    """Radix sort - Least Significant Digit first (right to left)"""
    if not words:
        return words
    
    # All words are length 3
    d = 3
    result = words[:]
    
    # Sort from rightmost digit (position 2) to leftmost (position 0)
    for pos in range(d - 1, -1, -1):
        result = counting_sort_stable(result, pos)
        print(f"After sorting position {pos} ({['1st', '2nd', '3rd'][pos]} char): {result}")
    
    return result

def counting_sort_stable(arr, pos):
    """Stable counting sort on character at position 'pos'"""
    # Create buckets for a-z
    buckets = [[] for _ in range(26)]
    
    # Distribute into buckets
    for word in arr:
        char_index = ord(word[pos].lower()) - ord('a')
        buckets[char_index].append(word)
    
    # Collect back in order (stable - preserves order within buckets)
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

# Test
words = ["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]
print("Original:", words)
print("\n--- LSD Radix Sort ---")
sorted_lsd = radix_sort_lsd(words)
print(f"\nFinal: {sorted_lsd}")

# LSD is simpler: just d passes of counting sort, no recursion.
# MSD is clever: can terminate early for buckets, more cache-friendly for strings of varying length (though not relevant here with fixed length).
# Both run in Θ(d(n + k)) where d=3 characters, n=16 words, k=26 alphabet size.

# **LSD (Right to Left):**
# Position 2 (3rd char): Group by last letter
# Position 1 (2nd char): Group by middle letter (stable!)
# Position 0 (1st char): Group by first letter (stable!)

# **MSD (Left to Right):**
# Position 0: Split into B-bucket, C-bucket, D-bucket, etc.
#   → Then recursively sort each bucket on position 1, then 2
#MSD
# def radix_sort_msd(words, pos=0, depth=0):
#     """Radix sort - Most Significant Digit first (left to right, recursive)"""
#     if not words or len(words) <= 1 or pos >= 3:
#         return words
    
#     indent = "  " * depth
#     print(f"{indent}Sorting at position {pos} ({['1st', '2nd', '3rd'][pos]} char): {words}")
    
#     # Create buckets
#     buckets = [[] for _ in range(26)]
    
#     # Distribute
#     for word in words:
#         char_index = ord(word[pos].lower()) - ord('a')
#         buckets[char_index].append(word)
    
#     # Recursively sort each non-empty bucket on next position
#     result = []
#     for bucket in buckets:
#         if bucket:
#             sorted_bucket = radix_sort_msd(bucket, pos + 1, depth + 1)
#             result.extend(sorted_bucket)
    
#     return result

# # Test it
# print("\n\n--- MSD Radix Sort ---")
# sorted_msd = radix_sort_msd(words[:])
# print(f"\nFinal: {sorted_msd}")



