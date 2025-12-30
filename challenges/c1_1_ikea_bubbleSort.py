'''
Supply Chain Management Software at IKEA(Let's pretend).
IKEA has finally decided to invest in digitising their operations and the supply chain. They contracted
us to design an algorithm to sort a list of orders by selection time (t_selection, finding the good in
the warehouse and bringing it to the surface) plus shipping time (t_shipping, constant). 
The customer orders can be retrieved (in the same order as placed) from a server database. 
You should expect between 100-10K elements.
Hint: Bubble sort may do the job.

Example 2. The sort() function takes a data list of tuples (list[tuple[id:int, t_selection:int,
t_shipping:int]]) as a parameter representing the data-set of orders. Where, id, t_selection and
t_shipping are of type unsigned int, and, n is the number of orders.
[(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.

Call: sort([(1, 500, 100), (2, 700, 100), (3, 100, 100)])
Returns (list[int]): [3, 1, 2]
'''

#!/usr/bin/env python3


from typing import Optional, List, Tuple, Union


class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int,
                 next: Optional["Order"] = None):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        '''
        Remove me if you don't need me.
        Or, add a method to assign to me if you want to use linked lists.
        '''
        self.next: Union[Order, None] = next


    def __lt__(self, other: "Order") -> bool:
        total_time_self = self.selection_time + self.shipping_time
        total_time_other = other.selection_time + other.shipping_time
        return total_time_self < total_time_other

    def __gt__(self, other: "Order") -> bool:
        total_time_self = self.selection_time + self.shipping_time
        total_time_other = other.selection_time + other.shipping_time
        return total_time_self > total_time_other

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    if not data:
        return []

    # Creating the head of the linked list from the first order data
    head = Order(*data[0])
    current = head

    # Populate the linked list with subsequent Order objects
    for item in data[1:]:
        next_order = Order(*item)
        current.next = next_order
        current = next_order

    # Implementing bubble sort directly on the linked list
    changed = True
    while changed:
        current = head
        previous = None
        changed = False
        while current and current.next:
            if current > current.next:
                if previous:
                    previous.next = current.next
                else:
                    head = current.next
                # Swapping the nodes
                temp = current.next
                current.next = temp.next
                temp.next = current
                changed = True
                previous = temp
            else:
                previous = current
                current = current.next

    # Extracting the sorted IDs from the linked list
    sorted_ids = []
    current = head
    while current:
        sorted_ids.append(current.id)
        current = current.next

    return sorted_ids

'''
Use for your local testing
'''
if __name__ == '__main__':
    data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
    sort(data)
