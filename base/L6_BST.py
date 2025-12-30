
TREE-SEARCH  
1  if  == NIL or  ==  x.key 
2    return x  
3  if k < x.key 
4    return TREE-SEARCH(x.left,k) 
5  else return TREE-SEARCH(x.right,k)  

ITERATIVE-TREE-SEARCH(x, k)
1  while x ≠ NIL and k ≠ x.key
2    if k < x.key
3      x = x.left
4    else x = x.right
5  return x

TREE-MINIMUM 
1  while x.left != NIL 
2    x=x.left 
3  return  

TREE-MAXIMUM 
1  while x.right != NIL 
2    x = x.right 
3  return x  

TREE-INSERT(T,z)  
1  x = T.root // node being compared with z
2  y = NIL //  y will be parent of z  
3  while x != NIL // descend until reaching a leaf 
4    y = x
5    if z.key < x.key 
6      x = x.left 
7    else x = x.right 
8  z.p = y   // found the location
9  if y == NIL #insert z with parent y
10    T.root=z   // tree  was empty 
11  elseif z.key <  y.key 
12    y.left = z   
13  else y.right = z  

TREE-SUCCESSOR(x)
1  if x.right ≠ NIL
2    return TREE-MINIMUM(x.right)  // leftmost node in right subtree
3  else // find the lowest ancestor of x whose left child is an ancestor of x
4    y = x.p
5    while y != NIL and x == y.right
6      x = y
7      y = y.p
8    return y

TREE-DELETE(T, z)
1  if z.left == NIL
2    TRANSPLANT(T, z, z.right)       // replace z by its right child
3  elseif z.right == NIL
4    TRANSPLANT(T, z, z.left)       // replace z by its left child
5  else y = TREE-MINIMUM(z.right)   // y is z’s successor
6    if y != z.right               // is y farther down the tree ? 
7      TRANSPLANT(T, y, y.right)   // replace y by its right child
8      y.right = z.right            // z’s right child becomes
9      y.right.p = y              //y’s right child
10    TRANSPLANT(T, z, y)        // replace z by its successor y
11    y.left = z.left            //and give z's left child to y,
12    y.left.p = y                // which had no left child

TRANSPLANT(T, u, v)
1  if u.p == NIL
2    T.r t = v
3  elseif u == u.p.left
4    u.p.left = v
5  else u.p.right = v
6  if v ≠ NIL
7    v.p = u.p



