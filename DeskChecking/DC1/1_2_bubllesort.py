"""
The code implements theOrder class. An Order will contain 3 fields: id,selectiontime,
shippingtime.The=,<,>operatorshavebeenoverloaded.Abubblesortalgorithmhasbeen
implemented, thebubble sort algorithm is wrapped in the sort method that parses 
thedat and creates Order objects to pass to the bubble sort core method.


Pseudocode
1 Define Order class
2   Define init(id, selection time, shipping time)
3   Assign id to field id
4   Assign selection time to field selection time
5   Assign shipping time to field shipping time
6  Define eq(other)
7   Return true if this object and other object have same fields value
      else false
8 Define gt(other):
9   Return true if this object fields sum is greater than other object
      fields sum else false
10
11 Define bubbleSort(array)
12   for each item in the array with i being the current index
13     for each element but the last i
14       swap current element with the following if the following is
            smaller than the current
15
16 Define sort(data)
17   for each triplet in data
18       append order initialized with the triplet to the array
19    bubbleSort(array)
20
21    return list of [id of each order in array]

Code:
"""
 class Order:
   def init (self, id, selectiontime, shippingtime):
     self.id: int = id
     self.selectiontime: int = selectiontime
     self.shippingtime: int = shippingtime

   def eq (self, other):
     return (self.selectiontime + self.shippingtime) == (other.
       selectiontime + other.shippingtime)

 def gt (self, other):
   return (self.selectiontime + self.shippingtime)>(other.
      selectiontime + other.shippingtime)


 def bubbleSort(array: List[Order]):
   n = len(array)

   for i in range(n-1): #line17

     for j in range(1, n-i-1):

       if array[j]>array[j+1]:
           array[j], array[j+1] = array[j+1], array[j]

 def sort(data: List[Tuple[int,int,int]])->List[int]:
   arr: List[Order] = []

   for id, selectiont, shipping t in data:
     arr.append(Order(id, selectiont, shipping t))

    bubbleSort(arr)

    return [a.id for a in arr]


'''
-On line 17, range(n-1) prevents the i index to traverse all the elements leaving
 the last element untouched.True:
The range in python includes the first item (0 by default), but excludes the last item. 
Since the last item of a list has index = the length of the list-1, we have to pass 
the length of the list to range since it will not reach it, but we’ll stop at the 
length- 1, which is our last index. Using n-1 will therefore prevent the last element 
to be ever visited.

-Theimplementation is correct and contains no bug.False
  
-The j index is misused since it avoids comparing the first item of the list with the second.True
• being j in the range(1, n-i-1) it will start from 1 instead of 0, causing the first element
of the list to never be compared with the second.
  
-on line 22, a support variable should be used to swap the array values, 
otherwise the result could be non deterministic.False
• Inpython we are allowed to use this kind of object swap without relying 
on support variables.
Due to the order the expression is evaluated, in the assignment cases python always 
evaluates the right-hand side of the expression first.

'''

