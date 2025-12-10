"""
The code implements the Order class just like in the previous example. We did not copy the Order
class implementation, you can assume it s correct. The difference from the previous TaskOrder
implementation is that there is a Order.next field in this class which represents the following Order
(a pointer to the next element, just like in linked lists). The code implements a bottom-up merge
sort. The final sort method used in the previous Task code has been omitted, focus on the core
merge sort algorithm instead.
"""

Pseudocode
1 #Assume that the objects have a .next field that represent the following element, None if there’s none
2
3 Define merge sort(head)
4   if head is empty return None
5
6   arr = list of 32 Nones
7   result, next = None
8
9   result = head
10
11   #Merge nodes into array
12   while result is not null:
13     Save the reference to the result next node into next
14     Reset the result to None
15     For each value of arr
16       If current value is None then break
17       result = merge(current value, result)
18       Assign null to current value
19     Assign result to the second last value of arr
20     result = next
21
22   #Merge array into single list
23   result = null
24   For each item in arr
25     result = merge(current value, result)
26
27   return result
28
29 Define merge(left, right)
30   result = None
31   ref = None
32
33   While left is not null and right is not null:
34     If right greater or equal to left
35       If result is not null then append left to the result
36       else assign left to the result
37       Assign the value after left to left
38     else
39       If result is not null then append right to the result
40       else assign right to the result
41       Assign the value after right to right
42
43   While there are elements remaining in left
44     Append left to result
45     Assign the value after left to left
46
47   While there are elements remaining in right
48     Append right to result
49     Assign the value after right to right
50
51   Return the pointer to the start of the list


Code
1 def merge sort(head: Union[Order,None])−>Union[Order,None]:
2   if not head:
3     return None
4   arr: List[Union[Order,None]] = [None for in range(32)]
5   result: Union[Order,None] = None
6   next: Union[Order,None] = None
7   result = head
8
9   while result:
10     next = result.next
11     result.next = None
12     i = 0
13     for i in range(32):
14       if arr[i] is None:
15         break
16       result = merge(arr[i], result)
17       arr[i] = None
18
19     arr[i] = result
20     result = next
21
22   result = None
23   for i in range(32):
24     result = merge(arr[i], result)
25
26   return result
27
28
29 def merge(left: Union[Order,None], right: Union[Order,None])−>Union[Order,None]:
30   result: Union[Order,None] = None
31   ref: Union[Order,None] = None
32
33   while left and right:
34     if left<= right:
35       if result:
36         result.add next(left)
37         result = left
38       else:
39         ref = left
40         result = left
41
42       left = left.next
43
44     else:
45       if result:
46         result.add next(right)
47         result = right
48       else:
49         ref = right
50         result = right
51
52       right = right.next
53
54   while left:
55     if result:
56       result.add next(left)
57       result = left
58     else:
59       ref = left
60       result = left
61
62     left = left.next
63
64   while right:
65     if result:
66       result.add next(right)
67       result = right
68     else:
69       ref = right
70       result = right
71
72     right = right.next
73
74   return ref


which are true: 
-At line 15, we should not break but instead return result, otherwise the code will never return once we are at the end.False
• We need the break because we need to move on since we reached the end of the array.
Returning at the point in time would not guarantee that the list got sorted. Break allows us to exit the for loop.

-The implementation is correct and contains no bug.True • This represents an indeed correct implementation of merge sort.

-The code will only run for array of length divisible by 32.False
• The code simply partitions the list in sublist of max 32 elements, the code will work even if
the last sublist has more than 32 elements, making this code effective also for lists with a
length not divisible by 32.
                       
-At line 35 we cannot use while left and right: since they are lists and will never have True or False as a value.False
• All collection objects in python (lists, dictionaries, sets...) have a boolean value which is
determined by having or not elements in it. Their boolean value will be true if they have
at least one element in them. In this case the loop goes on as long as both left and right
have at least one element in each of them.

