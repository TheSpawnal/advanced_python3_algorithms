#  illustrate the operation of HEAPSORT on the
#  array A = 〈5, 13, 2, 25, 7, 17, 20, 8, 4〉

# HEAPSORT(A,n)
#     BUILD-MAX-HEAP(A,n)
#     for i = n downto 2
#         exchange A[l] with A[i]
#         A.heap-size = A.heap-size -1
#         MAX-HEAPIFY(A,l)

# MAX-HEAPIFY(A,i)
#   l = LEFT(i)
#   r = RIGHT(i)
#   if l <= A.heap-size and A[l] > A[i]
#     largest = l
#   else largest = i
#   if r <= A.heap-size and A[r] > A[largest]
#     largest = r
#   if largest != i
#     exchange A[i] with A[largest]
#     MAX-HEAPIFY(A, largest)

# BUILD-MAX-HEAP(A, n)
#   A.heap-size = n
#   for i = ⌊n/2⌋ downto 1
#     MAX-HEAPIFY(A, i)

class HeapArray:
    def __init__(self, data):
        self.data = data
        self.heap_size = len(data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __repr__(self):
        return str(self.data)


def LEFT(i):
    """Return left child index (1-indexed)"""
    return 2 * i


def RIGHT(i):
    """Return right child index (1-indexed)"""
    return 2 * i + 1


def MAX_HEAPIFY(A, i, step_counter=[0]):
    """Maintain max-heap property at node i (1-indexed)"""
    step_counter[0] += 1
    print(f"\n  MAX-HEAPIFY called on index {i}")
    
    l = LEFT(i)
    r = RIGHT(i)
    
    # Find largest among node, left child, and right child
    if l <= A.heap_size and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    
    if r <= A.heap_size and A[r-1] > A[largest-1]:
        largest = r
    
    print(f"    Node {i}: {A[i-1]}, Left {l}: {A[l-1] if l <= A.heap_size else 'N/A'}, " +
          f"Right {r}: {A[r-1] if r <= A.heap_size else 'N/A'}, Largest: {largest}")
    
    # If largest is not the current node, swap and recurse
    if largest != i:
        print(f"    Swapping A[{i}]={A[i-1]} with A[{largest}]={A[largest-1]}")
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        print(f"    Array after swap: {A}")
        MAX_HEAPIFY(A, largest, step_counter)


def BUILD_MAX_HEAP(A, n):
    """Build a max heap from unordered array"""
    print("\n=== BUILD-MAX-HEAP ===")
    A.heap_size = n
    print(f"Initial array: {A}")
    print(f"Heap size: {A.heap_size}")
    
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2, 0, -1):
        print(f"\nHeapifying subtree rooted at index {i}:")
        MAX_HEAPIFY(A, i)
    
    print(f"\nMax heap built: {A}")


def HEAPSORT(A, n):
    """Sort array using heapsort algorithm"""
    print("=" * 60)
    print("HEAPSORT ALGORITHM")
    print("=" * 60)
    print(f"Original array: {A}")
    
    BUILD_MAX_HEAP(A, n)
    
    print("\n=== SORTING PHASE ===")
    original_size = A.heap_size
    
    for i in range(n, 1, -1):
        print(f"\n--- Iteration: i = {i} ---")
        print(f"Current heap: {A.data[:A.heap_size]}")
        print(f"Sorted portion: {A.data[A.heap_size:]}")
        
        # Move current root (maximum) to end
        print(f"Swapping A[1]={A[0]} with A[{i}]={A[i-1]}")
        A[0], A[i-1] = A[i-1], A[0]
        
        # Reduce heap size
        A.heap_size = A.heap_size - 1
        print(f"Heap size reduced to: {A.heap_size}")
        print(f"Array after swap: {A}")
        
        # Heapify the root
        if A.heap_size > 0:
            MAX_HEAPIFY(A, 1)
    
    print("\n" + "=" * 60)
    print(f"FINAL SORTED ARRAY: {A}")
    print("=" * 60)


# Main execution
if __name__ == "__main__":
    # Input array (Note: pseudocode uses 1-indexing, Python uses 0-indexing)
    # We'll handle this by adjusting indices in the functions
    data = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    A = HeapArray(data.copy())
    n = len(A)
    
    HEAPSORT(A, n)
    
    # Verification
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    print(f"Original: {data}")
    print(f"Sorted:   {A.data}")
    print(f"Is sorted: {A.data == sorted(data)}")