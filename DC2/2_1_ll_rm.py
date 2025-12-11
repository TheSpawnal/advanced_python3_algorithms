

''' 
Define class Node
  Define init(value)
      Set field value to value
      Set field next to None

Define class LinkedList
  Define init
      Set head field to None

  Define append(value)
      Create a new node starting from the value parameter
      If there is no value in the list, then set the new node to the head field
      else
          Starting from the head
          Reach the last node in the list
          Attach the new node, referencing it in the next field of the current last value

  Define remove(value)
      If there is no node, terminate
      If the first element is the one to remove, then set the head to the second node
      Set the head as current node
      While there is a next value in the next field of the current node
          If the value of the next item is the one to remove then
              Set the next field to reference the node after the next node Terminate
          Set the current node to the next node
'''

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__ (self):
        self.head = None
 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.next = current
          
    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next.next
                return
            current = current.next
'''
which are true:

-This is a correct implementation of a ll and its append and remove methods FALSE

-line 58, assigning current.next.next.next would cause the method to remove the correct value but also the value after it. TRUE
Using current.next = current.next.next.next means that we are redirecting the next
object point not to the following object (current.next) (that we want to delete), not to the
second following (current.next.next), but to the third following (current.next.next.next)
which is too many deleted objects, we only wanted one to be deleted.

-The append method is bugged, since after adding a new item to a non-empty list we set 
    the last item's next field to the second last item, creating a loop among the 2 last nodes. TRUE
 After reaching the end of the list we assign the new node to the next field of the last object
 at line 45. After doing so, at line 46, we assign the previously last node to the next field
 of the new last item (the one we’ve just appended). This is clearly wrong because the last
 node’s next value should be set to now. Therefore, the last item is pointing to the second
 last node. Instead, the last node’s next field should be set to None since there is no node
 after the last node

the __init__ method in the LinkedList class is bugged, since we cannot have an empty list because then we have no previous item to attach new nodes to.FALSE
       Empty lists are often used and when we do not have any node, we simply use None. When a
new node is pushed into the list, then we assign it to the node head, with no previous node.
'''

# LL claude: 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0  # Track size of list
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def prepend(self, value):
        """Add node at beginning of list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, value, position):
        """Insert at specific position"""
        if position < 0 or position > self.length:
            raise IndexError("Invalid position")
        if position == 0:
            self.prepend(value)
            return
        
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def remove(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def get(self, position):
        """Get value at position"""
        if position < 0 or position >= self.length:
            raise IndexError("Invalid position")
        
        current = self.head
        for _ in range(position):
            current = current.next
        return current.value

    def search(self, value):
        """Return position of value or -1 if not found"""
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def is_empty(self):
        """Check if list is empty"""
        return self.head is None

    def clear(self):
        """Remove all nodes"""
        self.head = None
        self.length = 0

    def __len__(self):
        """Allow use of len() function"""
        return self.length

    def __str__(self):
        """String representation of list"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values) if values else 'Empty list'
    
    def reverse(self):
        """Reverse the linked list in-place"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self):
        """Get middle node using slow/fast pointer technique"""
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def has_cycle(self):
        """Detect if list has a cycle using Floyd's algorithm"""
        if not self.head:
            return False
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
