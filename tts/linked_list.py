
LIST-SEARCH(L,k)
1   x = L.head
2   while x != NIL and x.key != k
3       x = x.next
4   return x

#To add an element, x, to the front of the list L, run
LIST-PREPEND(L,x)
1   x.next = L.head
2   x.prev = NIL
3   if L.head != NIL
4       L.head.prev = x
5   L.head = x

#to add an element, x, following an element y, in the list
LIST-PREPEND(y,x)
1   x.next = y.next
2   x.prev = y
3   if y.next != NIL
4       y,next.prev = x
5   y.next = x

#sentinels inserting to the link list
# It is often useful to add a dummy object to lists, making them circular. 
# We call this object a sentinel, and have it represent NIL.
# Instead of referencing NIL, we now call the sentinel, L.nil. 
# To reference the head,  we call L.nil.next, and to reference the tail we call. L.nil.prev.
LIST-INSERT'(x,y)
1   x.next = y.next
2   x.prev = y
3   y.next.prev = x
4   y.next = x

#delete op
LIST-DELETE(x)
1   x.prev.next = x.next
2   x.next.prev = x.prev

#speedup list search with sentinel
LIST-SEARCH'(L,k)
1   L.nil.key = k
2   x = L.nil.key
3   while x.key != k
4       x = x.next
5   if x == L.nil
6       return NIL
7   else return x
