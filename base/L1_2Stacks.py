

"""
Explain how to implement two stacks as one array of size n, 
so that neither stack overflows, unless the total number of elements 
exceeds n. Implement Push and Pop operations that run in constant time. 

Sol: 
Have one stack grow left to right (starting at 1),
and the other right to left (starting at n)

TWO-STACKS
────────────────────────────────────────────────────────────
    A[1..n]     : array of size n
    top1        : index of top element of Stack 1 (grows left → right)
    top2        : index of top element of Stack 2 (grows right → left)

Initialization
INIT-TWO-STACKS(n)
────────────────────────────────────────────────────────────
1.  A <- new array of size n
2.  top1 <- 0           // Stack 1 empty: no valid element yet
3.  top2 <- n + 1       // Stack 2 empty: no valid element yet
4.  return (A, top1, top2)

Push Operations
PUSH-1(x)
────────────────────────────────────────────────────────────
// Push x onto Stack 1 (left stack, grows rightward)

1.  if top1 + 1 = top2                  // Stacks would collide
2.      error "Overflow"
3.  top1 <- top1 + 1
4.  A[top1] <- x
PUSH-2(x)
────────────────────────────────────────────────────────────
// Push x onto Stack 2 (right stack, grows leftward)

1.  if top2 - 1 = top1                  // Stacks would collide
2.      error "Overflow"
3.  top2 <- top2 - 1
4.  A[top2] <- x

Pop Operations
POP-1()
────────────────────────────────────────────────────────────
// Pop from Stack 1

1.  if top1 = 0                         // Stack 1 is empty
2.      error "Underflow"
3.  x <- A[top1]
4.  top1 <- top1 - 1
5.  return x
POP-2()
────────────────────────────────────────────────────────────
// Pop from Stack 2

1.  if top2 = n + 1                     // Stack 2 is empty
2.      error "Underflow"
3.  x <- A[top2]
4.  top2 <- top2 + 1
5.  return x


Auxiliary Operations
IS-EMPTY-1()
────────────────────────────────────────────────────────────
1.  return top1 = 0
IS-EMPTY-2()
────────────────────────────────────────────────────────────
1.  return top2 = n + 1
IS-FULL()
────────────────────────────────────────────────────────────
1.  return top1 + 1 = top2              // No space between them
SIZE-1()
────────────────────────────────────────────────────────────
1.  return top1
SIZE-2()
────────────────────────────────────────────────────────────
1.  return n - top2 + 1
"""
