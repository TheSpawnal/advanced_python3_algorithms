
#  Give an O(n lg k)-time algorithm to merge k sorted lists into one sorted list,
#  where n is the total number of elements in all the input lists. (Hint: Use a
#  min-heap for k-way merging.)

MERGE-K-LISTS(lists, k)
    # Build min-heap with first element from each list
    H = empty min-heap
    for i = 1 to k
        if lists[i] is not empty
            MIN-HEAP-INSERT(H, (lists[i].first, i))
    
    result = empty list
    while H is not empty
        (value, list_index) = MIN-HEAP-EXTRACT-MIN(H)
        append value to result
        
        # Get next element from the same list
        if lists[list_index] has more elements
            next = lists[list_index].next
            MIN-HEAP-INSERT(H, (next, list_index))
    
    return result

    
#Running time analysis:
#Initial heap build: O(k lg k)
#n total elements, each requires: extract-min O(lg k) + insert O(lg k)
#Total: O(k lg k) + O(n lg k) = O(n lg k)

#Key idea: Maintain a min-heap of size ≤ k containing the smallest unprocessed 
#element from each list. Extract minimum, add it to result, insert next element 
#from same list.

