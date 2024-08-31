"""
presentation to improve,
practice 

1. def minSteps(arr, word1, word2):
2. direction: overall alorithm: BFS => Trie+BFS+binary (HARD)
3. how? => dry run 
4. coding
5. back to #3 (verify #4)
6. add some more test cases
"""
# https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/?ref=shm
# https://www.geeksforgeeks.org/software-engineering-system-design-strategy/?ref=lbp

#### Math ####
import math
"""
+ - * / ** // %
/ : 除3/4 -> 0.75
//: 整除 3//4 -> 0, 4//3 -> 1
**: 幂次方 3**2 = 9
%: 余数 5%3 = 2
"""
# big number
big_num = float('inf')
big_neg = float('-inf')
# Rounds a number up to the nearest integer
math.ceil()
# Rounds a number down to the nearest integer
math.floor()
# Returns the number of ways to choose k items from n items without repetition and order
n = 5
k = 2
res = math.comb(n, k)
# Returns the value of x to the power of y
x, y = 3, 2
math.pow(x, y) # 3**2
# Returns the square root of a number
math.sqrt()
int(math.sqrt(13)) # -> 3.60xxx to 3
# True -> int 1, False ->int 0
# round(num, digits)
a = round(4.56667, 3)
# character to int(ASCII)
a = ord("A") # A -> 65
b = chr(65)  # 65 -> A

#### Array ####
## Insert 
nums = [1, 2, 3, 5, 6]
a = [7]
nums.insert(3, 4) # insert(index, value) -> nums = [1, 2, 3, 4, 5, 6]
## Append
nums.append(7) # -> nums = [1, 2, 3, 4, 5, 6, 7]
## +
nums + a # -> [1, 2, 3, 5, 6, 7]
## Extend
nums2 = [8, 9]
nums.extend(nums2) # -> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
## Reverse ([::-1] both applys for str and array)
nums[::-1]
# Changing array length
nums = [1, 2, 3, 4, 5]
#(index 0, 1, 2, 3, 4)
nums[1:4] = [6, 7]    # [1, 6, 7, 5]        (replace 3 elements with 2)
nums[-1:] = [8, 9, 0] # [1, 6, 7, 8, 9, 0]  (replace 1 element with 3)
nums[:1] = []         # [6, 7, 8, 9, 0]     (replace 1 element with 0)
# Zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
paris = list(zip(nums1, nums2)) # pairs = [(1, 4), (2, 5), (3, ,6)]
# itemgetter

### frozen set ###
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
# frozensets are immutable
fSet.add('v') # got errors
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet) # The frozen set is: frozenset({'name', 'sex', 'age'})
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)
# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})
# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})
# difference
print(A.difference(B))  # Output: frozenset({1, 2})
# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])
# isdisjoint() method
print(A.isdisjoint(C))  # Output: True
# issubset() method
print(C.issubset(B))  # Output: True
# issuperset() method
print(B.issuperset(C))  # Output: True

## Loop/Iterate ##
# 2D array 
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum += arr[i][j]

for a, b, c in arr:
    sum += a + b + c

# 1D array
arr_1d = [0, 7, 8, 10]
l = []
  # index and element 
for i, n in enumerate(arr):
     l.append((i, n))
  # loop from back
for i in range(len(arr)-1, -1, -1):
    l.append(i)

# break: exit the loop
# continue: go to the next loop
"""
# if no break in the for loop, can use else
for xx loop:
    if xx:
       break (exit this for loop)
    else:
        xxx   
"""

#### matrix ####
matrix =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix.reverse()
# transpose matrix in place
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# flip the NxN image
matrix.reverse() # then transpose

# iterate the transposed matrix
transposed = zip(*matrix)
for col in transposed:
    print(col)

#### String ####

## Compare character
word = "abc"
for s in word:
    if s.isdigit():
        continue

s = "    words high   "
s.strip() # Remove spaces at the beginning and at the end of the string:
print(s) # -> "words high"
s.split(" ")

s[::-1] 

s.lower()
s.upper()
s.isalpha()

# find parent root from a path
s = '/path/abcd'
new = s[:s.rfind('/')] # rfind -> the index of '/'

# add variable value to string
"%s->%s" %(nums[i], nums[j]) # -> "a->b"


#### Sorting ####
"""
Python sort() & sorted()

arr.sort(key=lambda x: x[1])



new_arr = sorted(arr, key=lambda x:x[0])

footballers_and_nums = [("Fabregas", 4),("Beckham" ,10),("Yak", 9), ("Lampard", 8), ("Ronaldo", 7), ("Terry", 26), ("Van der Saar", 1), ("Yobo", 2)]
sorted_footballers_and_nums = sorted(footballers_and_nums, key=lambda index : index[1])


https://www.freecodecamp.org/news/lambda-sort-list-in-python/
"""


#### Dictionary ####
from collections import Counter

### {} setdefault(k, v) ###
"""
Parameter	        Description

keyname	            Required. The keyname of the item you want to return the value from

value	            Optional.
                    If the key exist, this parameter has no effect.
                    If the key does not exist, this value becomes the key's value
                    Default value None

Return value -> is the value for the input key
"""
d = {}
d.setdefault("k", "v")

### counter ###
cnt = Counter(nums)

### defaultdict ###
from collections import defaultdict
d = defaultdict(list)
d = defaultdict(int)
d = defaultdict(list)

### Ordered Dict ####
from collections import OrderedDict
d1 = OrderedDict()
d2 = OrderedDict()
# update a value of under a key, the order doesn't change

# compare two ordered dict
d1 == d2 # -> (compare content and order)

# reverse 
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
my_dict.reverse()

# pop item LIFO 
last_item = my_dict.popitem(last=True) 
# pop item FIFO
last_item = my_dict.popitem(last=False)

# insert existing key to end
key = ""
my_dict.move_to_end(key)
# insert existing key to begin
my_dict.move_to_end(key, last=False)
my_dict.move_to_start(key)
# delete item
my_dict.pop(key)
# get item
my_dict.get(key, 0) # get key's value, otherwise return 0


#### Queue ####
from collections import deque
class TreeNode():
    def __init__(self, value=0, left=0, right=0):
        self.value = value
        self.left = left
        self.right = right
q = deque()
root = TreeNode(1)
q = deque([root, 0]) # append root and its column index
a = 5
q.insert(0, a) # Return the position of x in the deque (at or after index start and before index stop). 
               # Returns the first match or raises ValueError if not found.
q.append(a) # Add x to the right side of the deque.
q.appendleft(a) # Add x to the left side of the deque.
q.pop() # Remove and return an element from the right side of the deque. 
        # If no elements are present, raises an IndexError.
q.popleft() # Remove and return an element from the left side of the deque. 
            # If no elements are present, raises an IndexError.
q.remove(a) # Remove the first occurrence of value. If not found, raises a ValueError.



#### Stack ####



#### Heap(priority queue) ####
''' heap都是最小堆，要做最大堆就放 -xx 进去 '''
import heapq
arr = []

heapq.heappush(arr, 3) # Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(arr) # Pop and return the smallest item from the heap, maintaining the heap invariant.
        # If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
arr[0] # acess the smallest item without popping it.
item = ""

heapq.heappushpop(arr, item) # Push item on the heap, then pop and return the smallest item from the heap.

heapq.heapify(arr) # Transform list x into a heap, in-place, in linear time.

heapq.heapreplace(arr, item) # Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

heapq.merge() # Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

heapq.nlargest(arr, 2) # Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

heapq.merge() # Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

heapq.nlargest(arr, 2) # Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

heapq.nsmallest(arr, 2) # Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key)[:n].

"""
https://docs.python.org/3/library/heapq.html
https://github.com/gmertk/python-cheatsheets/blob/master/cheatsheet-queues.py
https://www.pythonsheets.com/notes/python-heap.html
"""

#####################
##### Template ######
#####################

#### Binary Search ####
def binary_search(search_space):
    def condition(num) -> bool:
        pass
    left, right = min(search_space), max(search_space)
    while left < right:
        mid = (left+right)//2
        if condition(mid): # >= or <=
            right = mid
        else:
            left = mid + 1

#### Backtrack ####
def function():
    def backtrack():
        # for loop
        # append
        # pop
        pass 
    backtrack()
