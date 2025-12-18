'''
hashing with chaining
when collisions are resolved with chaining, the dictionary operations must call on the linked list operation.

CHAINED-HASH-INSERT(T,x)
1 LIST-PREPEND(T[h(x.key)],x)

CHAINED-HASH-SEARCH(T,k)
1  return LIST-SEARCH(T[h(k)],k)

CHAINED-HASH-DELETE(T,x)
1 LIST-DELETE(T[h(x.key)],x)

if the lists are doubly linked, deletion takes constant time to run.
LIST-DELETE(x)
1  x.prev.next = x.next
2  x.next.prev = x.prev

LIST-SEARCH(L,k)
1  L.nil.key = k
2  x = L.nil.next
3  while x.key != k
4    x = x.next
5  if x == L.nil
6    return NIL
7  else return x
the search op has a worst case running time proportional to the list length

LIST-PREPEND(L, x)
1  x.next = L.head
2  x.prev = NIL
3  if L.head != NIL
4    L.head.prev = x  
5  L.head = x
Assuming the element inserted is not already in the table, insertion takes constant time to run.


When collisions are resolved with chaining, the dictionary operations must call on the linked list operations.
To maximize the efficiency of hashing with chaining, it is best to evenly 
distribute collisions in the hashing table

'''



