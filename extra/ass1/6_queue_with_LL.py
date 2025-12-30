

# We saw the implementation of a queue using arrays, 
# now implement a queue using linked lists. Is it easier to 
# implement with our without a sentinel? 

# Queue Implementation with Doubly Linked List - WITHOUT Sentinel

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class QueueWithoutSentinel:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, x):
        node = Node(x)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("underflow")
        x = self.head.key
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return x
    
    def peek(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.head.key


# Queue Implementation with Doubly Linked List - WITH Sentinel

class QueueWithSentinel:
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
    
    def is_empty(self):
        return self.nil.next == self.nil
    
    def enqueue(self, x):
        node = Node(x)
        node.next = self.nil
        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("underflow")
        node = self.nil.next
        x = node.key
        self.nil.next = node.next
        node.next.prev = self.nil
        return x
    
    def peek(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.nil.next.key


# Testing both implementations
print("WITHOUT SENTINEL:")
q1 = QueueWithoutSentinel()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.dequeue())
print(q1.peek())
print(q1.dequeue())
q1.enqueue(40)
print(q1.dequeue())
print(q1.dequeue())

print("\nWITH SENTINEL:")
q2 = QueueWithSentinel()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
print(q2.dequeue())
print(q2.peek())
print(q2.dequeue())
q2.enqueue(40)
print(q2.dequeue())
print(q2.dequeue())


# ANALYSIS:
# WITHOUT Sentinel: Must check if head/tail are None (special cases)
# WITH Sentinel: No special cases, cleaner logic, fewer conditionals
# 
# Verdict: WITH sentinel is easier - eliminates edge case handling
# Time: O(1) for both enqueue/dequeue in both versions
# Space: O(n) + constant sentinel overhead
