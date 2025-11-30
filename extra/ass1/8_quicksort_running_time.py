'''
What is the running time of QUICK SORT when all 
elements of the array have the same value?


QuickSort with All Equal Elements Analysis
Running Time Analysis
When all elements have the same value:
Lomuto Partition (Standard PARTITION)

Running Time: Θ(n²) - WORST CASE

Why?

Pivot x = A[r] equals all other elements
Condition A[j] ≤ x is always true (all elements equal pivot)
Every element goes to the "low side"
Partition always splits as: [n-1 elements] | [pivot]
Recursion tree: n + (n-1) + (n-2) + ... + 1 = Θ(n²)

Hoare Partition (HOARE-PARTITION)

Running Time: Θ(n log n) - MUCH BETTER

Why?

Two-pointer approach from both ends
When all equal: i and j meet near the middle
Splits roughly in half: [n/2] | [n/2]
Recursion depth: O(log n)
Total work: Θ(n log n)

'''

class QuickSortVisualizer:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.partitions = 0
        self.recursion_depth = 0
        self.max_depth = 0
    
    def lomuto_partition(self, A, p, r, depth):
        """Standard partition - poor on equal elements"""
        print(f"{'  '*depth}PARTITION[{p}:{r}] pivot={A[r]} array={A[p:r+1]}")
        self.partitions += 1
        
        x = A[r]
        i = p - 1
        
        for j in range(p, r):
            self.comparisons += 1
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
                self.swaps += 1
        
        A[i + 1], A[r] = A[r], A[i + 1]
        self.swaps += 1
        
        print(f"{'  '*depth}RESULT: pivot_idx={i+1} array={A[p:r+1]}")
        return i + 1
    
    def quicksort_lomuto(self, A, p, r, depth=0):
        """Lomuto QuickSort"""
        self.max_depth = max(self.max_depth, depth)
        
        if p < r:
            q = self.lomuto_partition(A, p, r, depth)
            self.quicksort_lomuto(A, p, q - 1, depth + 1)
            self.quicksort_lomuto(A, q + 1, r, depth + 1)
    
    def hoare_partition(self, A, p, r, depth):
        """Hoare partition - good on equal elements"""
        print(f"{'  '*depth}HOARE-PARTITION[{p}:{r}] pivot={A[p]} array={A[p:r+1]}")
        self.partitions += 1
        
        x = A[p]
        i = p - 1
        j = r + 1
        
        while True:
            while True:
                j -= 1
                self.comparisons += 1
                if A[j] <= x:
                    break
            
            while True:
                i += 1
                self.comparisons += 1
                if A[i] >= x:
                    break
            
            if i < j:
                A[i], A[j] = A[j], A[i]
                self.swaps += 1
                print(f"{'  '*depth}SWAP: i={i} j={j} array={A[p:r+1]}")
            else:
                print(f"{'  '*depth}RESULT: split_idx={j} array={A[p:r+1]}")
                return j
    
    def quicksort_hoare(self, A, p, r, depth=0):
        """Hoare QuickSort"""
        self.max_depth = max(self.max_depth, depth)
        
        if p < r:
            q = self.hoare_partition(A, p, r, depth)
            self.quicksort_hoare(A, p, q, depth + 1)
            self.quicksort_hoare(A, q + 1, r, depth + 1)
    
    def reset_stats(self):
        self.comparisons = 0
        self.swaps = 0
        self.partitions = 0
        self.max_depth = 0
    
    def print_stats(self, label):
        print(f"\n{label} STATS:")
        print(f"Comparisons: {self.comparisons}")
        print(f"Swaps: {self.swaps}")
        print(f"Partitions: {self.partitions}")
        print(f"Max Recursion Depth: {self.max_depth}")
        print(f"Estimated Time Complexity: O(n²)" if self.max_depth > 10 else f"O(n log n)")


def demonstrate_equal_elements():
    """Demonstrate behavior on all equal elements"""
    
    print("="*70)
    print("SCENARIO: ALL EQUAL ELEMENTS [5, 5, 5, 5, 5, 5]")
    print("="*70)
    
    # Test Lomuto
    print("\n" + "="*70)
    print("LOMUTO PARTITION (Standard)")
    print("="*70)
    arr1 = [5, 5, 5, 5, 5, 5]
    viz = QuickSortVisualizer()
    viz.quicksort_lomuto(arr1, 0, len(arr1) - 1)
    print(f"\nFinal: {arr1}")
    viz.print_stats("LOMUTO")
    
    # Test Hoare
    print("\n" + "="*70)
    print("HOARE PARTITION")
    print("="*70)
    arr2 = [5, 5, 5, 5, 5, 5]
    viz.reset_stats()
    viz.quicksort_hoare(arr2, 0, len(arr2) - 1)
    print(f"\nFinal: {arr2}")
    viz.print_stats("HOARE")


def demonstrate_varied_input():
    """Demonstrate on varied input for comparison"""
    
    print("\n\n" + "="*70)
    print("SCENARIO: VARIED ELEMENTS [3, 7, 1, 9, 2, 5]")
    print("="*70)
    
    # Test Lomuto
    print("\n" + "="*70)
    print("LOMUTO PARTITION")
    print("="*70)
    arr1 = [3, 7, 1, 9, 2, 5]
    viz = QuickSortVisualizer()
    viz.quicksort_lomuto(arr1, 0, len(arr1) - 1)
    print(f"\nFinal: {arr1}")
    viz.print_stats("LOMUTO")


if __name__ == "__main__":
    demonstrate_equal_elements()
    demonstrate_varied_input()


'''
## Key Insights from Output

### Lomuto with All Equal Elements:

Recursion depth: n-1
Each partition: [n-1] | [1]
Comparisons: n(n-1)/2 ≈ Θ(n²)


### Hoare with All Equal Elements:

Recursion depth: log n
Each partition: [n/2] | [n/2]
Comparisons: n log n ≈ Θ(n log n)

Summary Table
Partition Scheme  All Equal Elements  Average Case  Best Case
Lomuto              Θ(n²) ❌            Θ(n log n)  Θ(n log n)
Hoare            Θ(n log n) ✓        Θ(n log n)      Θ(n log n)
Conclusion: Lomuto partition degrades to worst-case quadratic time when all elements are equal. 
Hoare partition handles this gracefully with balanced splits.Claude can make mistakes. 
Please double-check responses.
'''
  



'''

