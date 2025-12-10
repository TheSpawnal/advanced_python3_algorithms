'''

the following code implements a Job class (similar to Assignment 1 Task 3), where p is processing time and w is importance;
a job finishing at time t has a cost of t*w. 
The goal is to sequence jobs to minimize the total cost, using Smith’s rule (scheduling jobs by the order if their ratio of processing time over weight ratio).
This greedy rule turns out to be optimal. 
The code implement a quick sort. This time, differently from the assignment, we do not care if the order of equal jobs is the same both in the input and the output, 
if the jobs are equal according to == then they can be in whatever order.


pseudocode:
 Define the Job class
    Define the Job constructor(self, id, p, w)

    Override the greater or equal operator(self, other)
        Return the result of self.p/self.w>= other.p/self.w

    Override the less than operator(self, other)
        Return the result of self.p/self.w<other.p/self.w

    Override the greater than operator(self, other)
        Return the result of self.p/self.w>other.p/self.w

 Define quicksort(ar)
    If there is one or less elements return ar

    Pick the middle element as pivot
    Create two empty lists, one for objects smaller and one for objects greater than the pivot
    If you are analyzing the pivot then skip to the next object in list
    Put elements greater than the pivot in the list for the greater objects
    Put elements smaller than the pivot in the list for the smaller objects
    Put elements equal to the pivot in the greater or smaller list based on their index


    Set as the left list the quicksorted list with objects smaller than the pivot
    Set as the right list the quicksorted list with objects greater than the pivot
    Return the left list, appending the pivot, appending the right list

 Define sort(data)
    Define an empty array of jobs

    For every value in data
        Create a Job object starting from the three individual values (id, p for processing time, w for importance) and add it to the list ofjobs

    Run quicksort on the array

    Return every id of the job in the sorted array
'''
class Job:
    def init (self, id, p, w):
        self.id: int = id
        self.p: int = p
        self.w: int = w
    def ge (self, other):
        return ((self.p / self.w)>= (other.p / other.w))
    def lt (self, other):
        return ((self.p / self.w)<(other.p / other.w))
    def gt (self, other):
        return ((self.p / self.w)>(other.p / other.w))

def quicksort(ar: List[Job]):
    if len(ar)<= 1:
        return ar

    mid = len(ar)//2
    pivot = ar[mid]
    
    smaller,greater = [],[]

    for i, val in enumerate(ar):
        if i == mid:
            smaller.append(val)
        if val<pivot:
            smaller.append(val)
        elif val>pivot:
            greater.append(val)
        else:
            if i<mid:#line36
                greater.append(val)
            else:
                smaller.append(val)
    
    left = quicksort([smaller])
    right = quicksort([greater])
    return left+[pivot]+right

def sort(data:List[Tuple[int,int,int]])−>List[int]:
    arr: List[Job] = []
    for id, p, w in data:
        arr.append(Job(id, p, w))

    arr = quicksort(arr)
    return [a.id for a in arr]

'''
which are true ? 

The if statement at line 36, appends jobs equal to the pivot into the wrong list, 
preventing the correct sorting of the list. FALSE
Appending the pivot to one of the two sides isn't an error itself, it is an error adding it to a
list and also returning it in the return statement, but doing only one of those is not an error
itself. Also there is not a wrong list, the pivot can be appended to any list.

The implementation is correct and contains no bug. FALSE

The code will duplicate the pivot value of the array passed to the quicksort method. TRUE
The code will indeed duplicate the pivot object since it will be both placed in the smaller
list and also returned in the return statement. In this way every time the function returns,
it will return a duplicated pivot.


The greater and smaller lists passed to quicksort will not be correctly unpacked, preventing the correct execution.TRUE
The lists passed as left = quicksort([smaller]) and its right counterpart will not be
correctly unpacked since they're surrounded by brackets. This will make the list be the only
element of another list, and when the quicksort method will run it will not be able to find
multiple elements, the only found element will be a list of objects instead of an object.

'''
