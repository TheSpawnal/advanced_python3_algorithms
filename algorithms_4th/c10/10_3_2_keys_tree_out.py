
# write and O(n)-time recursive procedure that, given an n-node binary tree, 
# prints out the key of each node in the tree.

PRINT-BINARY-TREE(T)
    PRINT-BINARY-TREE-AUX(T.root)

PRINT-BIANRY-TREE-AUX(x)
    if node != NIL
        PRINT-BINARY-TREE-AUX(x.left)
        print x.key
        PRINT-BIANRY-TREE-AUX(x.right)

        