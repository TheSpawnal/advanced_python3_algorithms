
'''
Include Past Data with one Warehouse and Sort by Job Priority 
Covid happens and IKEA is in turmoil, as the way they were calculating the job priority 
(the constant selection time) does not work anymore. 
You have a bunch of jobs to schedule on a single ‘machine’.
Job j requires p j units of processing time and has a positive weight w j which represents its relative importance 
- think of it as the inventory cost of storing the raw materials for job j for 1 unit of time. 
If job j finishes being processed at time t, then it costs t * w j dollars. 
The goal is to sequence the jobs so as to minimize the sum of the weighted completion times of each job. 
You should expect between 10*10K - 20*20K elements.
Use Smith’s rule, that is, schedule the jobs in the order of their ratio of processing time to weight.
This greedy rule turns out to be optimal.

Example 3. The sort() function takes a data list of tuples (list[tuple[id:int, p:int, w:int]])
as a parameter representing the data-set of jobs. Where, id, p, w are of type unsigned int, and, n is the number of orders.

<(i d1>, <p1>, <w1>), ..., (<i dn >,<pn >, <wn >)]

The function returns a list of integers of the job ids, sorted using Smith’s rule.
Hint: The Merge or Bubble sort may not work for this input size, consider Quick sort
'''

from typing import Optional, List, Tuple, Union

class Job:
    def __init__(self, id: int, p: int, w: int, next: Optional["Job"] = None):
        self.id: int = id
        self.p: int = p
        self.w: int = w
        # We don't need next pointer for quicksort
    
    def __lt__(self, other):
        # Smith's rule: lower ratio of p/w should come first
        return (self.p / self.w) < (other.p / other.w)
    
    def __gt__(self, other):
        return (self.p / self.w) > (other.p / other.w)

def swap(arr: List[Job], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr: List[Job], low: int, high: int) -> int:
    # Use median-of-three for pivot selection to handle partially sorted data better
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        swap(arr, low, mid)
    if arr[low] > arr[high]:
        swap(arr, low, high)
    if arr[mid] > arr[high]:
        swap(arr, mid, high)
    
    pivot = arr[mid]
    
    # Move pivot to end
    swap(arr, mid, high - 1)
    
    left = low
    right = high - 1
    
    while True:
        left += 1
        while arr[left] < pivot:
            left += 1
            
        right -= 1
        while right >= low and arr[right] > pivot:
            right -= 1
            
        if left >= right:
            break
        swap(arr, left, right)
    
    # Restore pivot
    swap(arr, left, high - 1)
    return left

def quicksort(arr: List[Job], low: int, high: int):
    if low < high:
        # Only use quicksort for larger segments
        if high - low <= 10:
            # Use insertion sort for small arrays
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        else:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    # Create array of Job objects
    jobs: List[Job] = []
    for id, p, w in data:
        jobs.append(Job(id, p, w))
    
    # Sort using quicksort
    quicksort(jobs, 0, len(jobs) - 1)
    
    # Return sorted job IDs
    return [job.id for job in jobs]
