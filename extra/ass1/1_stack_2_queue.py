
'''
Show how to implement a stack using two queues. 

QUEUE-EMPTY(Q)
    if Q.head == Q.tail
        return true
    else return false

QUEUE-FULL(Q)
    if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length)
        return true
    else return false

ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
        error "overflow"
    else
        Q[Q.tail] = x
        if Q.tail == Q.length
            Q.tail = 1
        else Q.tail = Q.tail + 1

DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
        error "underflow"
    else
        x = Q[Q.head]
        if Q.head == Q.length
            Q.head = 1
        else Q.head = Q.head + 1
        return x


STACK-EMPTY(S)
    if S.top == 0
        return TRUE
    else return FALSE

PUSH(S, x)
    if S.top == S.size
        error “overflow”
    else S.top = S.top + 1
        S[S.top] = x
 
POP(S)
    if STACK-EMPTY(S)
        error “underflow”
    else S.top = S.top – 1
        return S[S.top + 1]


#Solution pseudo-code.
STACK-INIT(S)
    S.q1 = new queue
    S.q2 = new queue
    S.q1.head = 1
    S.q1.tail = 1
    S.q2.head = 1
    S.q2.tail = 1

STACK-EMPTY(S)
    if QUEUE-EMPTY(S.q1)
        return TRUE
    else return FALSE

STACK-PUSH(S, x)
    ENQUEUE(S.q2, x)
    while not QUEUE-EMPTY(S.q1)
        y = DEQUEUE(S.q1)
        ENQUEUE(S.q2, y)
    swap S.q1 with S.q2

STACK-POP(S)
    if STACK-EMPTY(S)
        error "underflow"
    else
        return DEQUEUE(S.q1)

STACK-TOP(S)
    if STACK-EMPTY(S)
        error "underflow"
    else
        return S.q1[S.q1.head]
'''

class Queue:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.length = capacity
    
    def is_empty(self):
        return self.head == self.tail
    
    def is_full(self):
        return self.head == (self.tail + 1) % self.length
    
    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("overflow")
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.length
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("underflow")
        x = self.data[self.head]
        self.head = (self.head + 1) % self.length
        return x


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def is_empty(self):
        return self.q1.is_empty()
    
    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.q1.dequeue()
    
    def top(self):
        if self.is_empty():
            raise IndexError("underflow")
        return self.q1.data[self.q1.head]


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.top())
print(s.pop())
s.push(4)
print(s.pop())
print(s.pop())



# Complexity:
# PUSH: O(n) - transfer all elements from q1 to q2
# POP: O(1) - dequeue from q1
# TOP: O(1) - access front of q1
# Space: O(n)
