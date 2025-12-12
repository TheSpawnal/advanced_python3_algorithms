
'''
Heaps are commonly implemented with an array, 
the positioning in the array determines the positioning in the tree, 
here's an example: [A,B,C,D,E,F] A has 2 leaves (B and C), 
B has 2 leaves (D and E), C has 1 leaf(F). 
Considering the lexicographical order this would be a min-heap since 
the children are always greater than the parent. 
Here's an implementation of min-heap and some of its main methods

Define class MinHeap
    Define init()
        Initialize heap field to an empty list
    
    Define parent(i)
        Return the index of the parent of the node at the i−th position
    
    Define left child(i)
        Return the index of the left child of the node at the i−th position
    
    Define right child(i)
        Return the index of the right child of the node at the i−th position
    
    Define insert(value)
        Append the new value at the end of the heap
        Starting from the last element of the heap
        While the element index is greater than 0 and the current element is less than its parent
            Swap the values of the current element and its parent

    Define get min()
        If the heap has elements, then return the element of the heap field at index 0
        else return None
'''


class MinHeap:
    def __init__ (self):
        self.heap = []

    def parent(self, i):
        return (i-1) / 2
    
    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap)
        while i>0 and self.heap[i]<self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # def insert(self, value):
    #     """
    #     Insert a value into the min heap and maintain the heap property
    #     by bubbling up the value to its correct position.
    #     """
    #     # 1. Add the new value to the end of the heap
    #     self.heap.append(value)
    #     # 2. Get the index of the newly added value
    #     i = len(self.heap) - 1
        
    #     # 3. Bubble up: While we're not at root and parent is greater than current
    #     while current > 0:
    #         parent_idx = self.parent(i)
            
    #         # If parent is greater than current value, swap them
    #         if self.heap[parent_idx] > self.heap[i]:
    #             self.swap(i, parent_idx)
    #             i = parent_idx  # Move up to the parent position
    #         else:
    #             break  # Heap property is satisfied, we can stop


    def get_min(self):
        if len(self.heap)>0:
            return self.heap[0]
        else:
            return None

'''
which are true:

A: the parent method is wrong, since it may return a non integer value TRUE
The parent function could return a float value, which is definitely wrong since it needs to
return the index of the parent of the i-th item, and indexes must be integer values. The
correct operator is // which would truncate decimal division results, leading to the correct
index being returned.

B: while at line 51:
self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
stops as soon as the parent is greater than the child, but it should instead continue to verify that it is true
throughout the whole hierachy.FALSE
There is no need for the while at line 18 to continue looping after having found that the
 parent is greater than the child. Since we are in a min-heap we know that before adding a
 new element the min-heap is already correctly ordered. For this reason, once we have that
 the new item becomes greater than its parent, we are assured that the parent, the grand
 parent and so on will be already correctly ordered.

C: the get_min method doesn't take into consideration lists with a negative number of values, it could 
break because of this FALSE
 Lists cannot contain a negative number of values; we cannot have less than 0 items in a list.

D: the insert method will break raising IndexError:index out of range TRUE
 Setting i to the length of the list after having appended the new element will cause us to
 subsequently look for an item that doesn’t exist at line 17 when we use self.heap[i]. List
 indexes are zero-based, therefore the last index will be equal to the list length minus one. In
 order to fix the issue we should have done i = len(self.heap)-1 or swapped line 50 with
 line 51.
'''
#recall mainstrean implementation:
class MinHeap:
    def __init__(self):
        # Initialize with empty list
        self.heap = []
    
    def parent(self, i):
        # Get parent index
        return (i - 1) // 2
    
    def left_child(self, i):
        # Get left child index
        return 2 * i + 1
    
    def right_child(self, i):
        # Get right child index
        return 2 * i + 2
        
    def swap(self, i, j):
        # Helper to swap elements
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        # Add the new key at the end
        self.heap.append(key)
        # Fix the min heap property if violated
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        # Move the element up until heap property is satisfied
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
            
        # Store the minimum value
        min_val = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Fix the min heap property if violated
        if len(self.heap) > 0:
            self._sift_down(0)
            
        return min_val
    
    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Compare with left child
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
            
        # Compare with right child
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
            
        # If min_index changed, we need to swap and continue sifting down
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)
    
    def get_min(self):
        # Return minimum element without removing it
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Example usage:
if __name__ == "__main__":
    heap = MinHeap()
    # Insert example from your description: [A,B,C,D,E,F]
    for char in ['A', 'B', 'C', 'D', 'E', 'F']:
        heap.insert(char)
    
    print("Initial heap:", heap.heap)
    print("Min element:", heap.get_min())
    print("Extracting elements in order:")
    while heap.heap:
        print(heap.extract_min(), end=' ')
