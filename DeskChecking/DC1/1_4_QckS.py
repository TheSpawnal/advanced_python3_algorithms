
'''
 Define swap(arr, i, j)
      Swap objects between the indexes i and j of the arr list

 Define quicksort(arr, lo, hi)
      If lo and hi are greater or equal to 0 and if lo is less than hi
          Partition the array
          Call the quicksort on the right partition
          Call the quicksort on the left partition

 Define partition(arr, lo, hi)
     Pivot object is the object in the middle of the list

     Set one counter (i) to the index before the lower index
     Set one counter (j) to the index after the upper index

     Loop forever
         Update i by decreasing it by one
         While the value in arr at index i is less than the pivot
             Increase i (so that we are consider the next element in arr)
         Update j by decreasing it by one
         While the value in the arr at index j is greater that the pivot
             Increase j (so that we are consider the previous element in arr)

         If the indexes i and j have crossed (i>=j) then return j

         Swap the element at index i with the one at index j

 Define sort(data)
     Create an empty support list
     Fill the support list with the objects in data, converting them into an Order object
     Call quicksort on the list
     Return the id of every Order in the list

'''
class Order:
    def init (self, id, selectiontime, shippingtime):
        self.id: int = id
        self.selectiontime: int = selectiontime
        self.shippingtime: int = shippingtime
 
    def eq (self, other):
        return (self.selectiontime + self.shippingtime) == (other.selectiontime + other.shippingtime)
 
    def gt (self, other):
        return (self.selectiontime + self.shippingtime)>(other.selectiontime + other.shippingtime)


def swap(arr: List[Order], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]#line 2

def quicksort(arr: List[Order], lo: int, hi: int):
    if lo>= 0 and hi>= 0 and lo<hi:
    p = partition(arr, lo, hi)
    quicksort(arr, p + 1, hi)
    quicksort(arr, 0, p)

def partition(arr: List[Order], lo: int, hi: int):
    pivot = arr[(hi+lo)//2]#line10

    i = lo #line 12
    j = hi #line 13

    while(True):

        i = i + 1
        while arr[i]<pivot:
            i = i + 1

        j = j−1
        while arr[j]>pivot:
             j = j−1

        if i>= j:
             return j

        swap(arr, i, j)


def sort(data: List[Tuple[int,int,int]])−>List[int]:
    arr: List[Order] = []

    for id, selectiont, shipping t in data:
        arr.append(Order(id, selectiont, shipping t))

    quicksort(arr, 0, len(arr)−1)

    return [a.id for a in arr]

'''
which of the following statements about the code are true:

1/The implementation is correct and contains no bug.FALSE

2/At line 2, the value swap between two variables cannot be done in that manner. It is necessary to rely on a temporary variable.FALSE
As previously mentioned: in python we are allowed to use this kind of object swap without
relying on support variables. Due to the order the expression is evaluated, in the assignment
cases python always evaluates the right-hand side of the expression first.

3/At lines 12 and 13, the i and j indices should be initialized as i = lo - 1 and j = hi + 1.TRUE
 The i and j variables need to be set to i = lo-1 and j = hi+1 since once in the loop they
 will be respectively increased and decrease at every step to move towards the center. Since
 we want a single loop to run instead of one loop for the first step and a second loop for all
 the other steps, we need to set the variable to that ”correct” values. It is a simple coding
 trick that allows us to have a single loop, it is not really something specific about quicksort.
 If they are set to i = lo and j = hi then the first and last value will not be checked since
 in the while loop those values are then increased and decreased.

4/At lines 12 and 13, the i and j indices should be initialized as i = lo + 1 and j = hi - 1.FALSE

5/At line 10, the pivot should be set as pivot = arr[lo], else the algorithm will not be able to sort correctly.FALSE
The pivot of the array can be any element in the array. The best pivot point would be the
 one that has items that are less than itself on the left, and greater than itself items on the
 right. The middle point of the array is often used as pivot since reduces the cases in which
 all the elements needs to be moved (if you pick the first item as pivot you’ll have to move
 many elements unless the pivot you picked is the smallest number). But any index can be
 picked as pivot, non affecting the correctness of the final solution.

 '''
