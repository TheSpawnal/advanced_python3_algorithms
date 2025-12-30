'''
Our sorting program is successful, IKEA asks for your solution to run for several IKEA warehouses. 
Weshould expect between 10*10K - 20*20K elements.
Hint: Bubble sort may not work anymore, consider Merge sort.
The sort() function has the same parameter/return format as:
Example2:
The sort() function takes a data list of tuples 
(list[tuple[id:int, t_selection:int, t_shipping:int]]) as a parameter representing the data-set of orders. 
Where, id, t_selection and t_shipping are of type unsigned int, and, n is the number of orders.
[(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.

hints
1/Consider the format of the data for each task. 
Ask yourself the following questions by looking at the sample tests and task descriptions.
• Is the data ordered? partially ordered? or unordered?
• Does the task require the algorithm to be stable?
2/Perform floating point operations/comparisons to find the proper ordering.
'''

#!/usr/bin/env python3
from typing import List, Tuple

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time: int = shipping_time
    
    def total_time(self) -> int:
        return self.selection_time + self.shipping_time

    def __lt__(self, other: "Order") -> bool:
        # If total times are equal, we keep the original order-> stability !
        if self.total_time() == other.total_time():
            return self.id < other.id
        return self.total_time() < other.total_time()

def merge_sort(orders: List[Order]) -> List[Order]:
    if len(orders) <= 1:
        return orders
    
    # split the list inhalf
    mid = len(orders) // 2
    left_half = merge_sort(orders[:mid])
    right_half = merge_sort(orders[mid:])
    
    #merge the two halves
    return merge(left_half, right_half)

def merge(left: List[Order], right: List[Order]) -> List[Order]:
    sorted_list = []
    i = j = 0
    
    #merge two halves by comparing the total times
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append the remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    # Convert tuples into Order objects
    orders = [Order(id, selection_t, shipping_t) for id, selection_t, shipping_t in data]
    
    # Apply mergesort
    sorted_orders = merge_sort(orders)
    
    # Extr and return the ids in the sorted order
    return [order.id for order in sorted_orders]

# Test block can be added here to verify functionality if needed locally

'''
Use for your local testing
'''
# Uncomment for testing
# if __name__ == '__main__':
#     data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
#     print(sort(data))  # Output should be: [3, 1, 2]
