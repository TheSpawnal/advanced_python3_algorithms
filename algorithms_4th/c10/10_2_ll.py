
LIST-sEARCH(L, k)
    x = L.head
    while x =! NIL and x.key =! k
        x = x.next
    return x

LIST-PREPEND(L,x)
    x.next = L.head
    x.prev = NIL
    if L.head =! NIL
        L.head.prev = x
    L.head = x

LIST-INSERT(x, y)
    x.next = y.next
    x.prev = y
    if y.next != NIL
        y.next.prev = x
    y.next = x

LIST-DELETE(L, x)
    if x.prev != NIL
        x.prev.next = x.next
    else L.head = x.next
    if x.next != NIL
        x.next.prev = x.prev


#Sentinels
LIST-DELETE′ (x)
    prev.next = x.next
    next.prev = x.prev

LIST-INSERT'(x,y)
    x.next = y.next
    x.prev = y
    y.next.prev = x
    y.next = x

LIST-SEARCH'(L,k)
    L.nil.key = k //stoe the key in the sentinel to guarantee it is in list
    x = L.nil.next // start at the head of the list
    while x.key != k
        x = x.next
    if x == L.nil //found k in the sentinel
        return NIL // k was not really in the list
    else return x // found k in element x

