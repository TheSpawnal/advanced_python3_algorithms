class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def heapify_up(self, i):
        """Fix heap property upwards - O(log n)"""
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap with parent
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
    
    def heapify_down(self, i):
        """Fix heap property downwards - O(log n)"""
        size = len(self.heap)
        largest = i
        l = self.left(i)
        r = self.right(i)
        
        if l < size and self.heap[l] > self.heap[largest]:
            largest = l
        if r < size and self.heap[r] > self.heap[largest]:
            largest = r
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)
    
    def insert(self, key):
        """Insert element - O(log n)"""
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        """Remove and return max - O(log n)"""
        if not self.heap:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self.heapify_down(0)
        
        return max_val
    
    def build_heap(self, arr):
        """Build heap from array - O(n)"""
        self.heap = arr.copy()
        # Start from last non-leaf and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
## Heap Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Extract-Max/Min | O(log n) |
| Get-Max/Min | O(1) |
| Build-Heap | O(n) |
| Heapify | O(log n) |
