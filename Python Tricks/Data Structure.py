#### Math ####

'''
+ - * / ** // %
/ : 除3/4 -> 0.75
//: 整除 3//4 -> 0, 4//3 -> 1
**: 幂次方 3**2 = 9
%: 余数 5%3 = 2
'''

#### Array ####
## Insert 
nums.insert(index, "")
Append
nums.append("")
Extend
nums.extend(nums2)

a[::-1] 

# changing array length
nums = [1, 2, 3, 4, 5]
(index  0, 1, 2, 3, 4)
nums[1:4] = [6, 7]    # [1, 6, 7, 5]        (replace 3 elements with 2)
nums[-1:] = [8, 9, 0] # [1, 6, 7, 8, 9, 0]  (replace 1 element with 3)
nums[:1] = []         # [6, 7, 8, 9, 0]     (replace 1 element with 0)

Loop/Iterate

2d array. arr = [[a, b], [a, b], [a, b]]
for a, b in arr:

1d array. arr = [0, 7, 8, 10]
for i, n in enumerate(arr):
for i in range(len(arr))
for j in range(len(arr)-1, -1, -1)

# break: exit the loop
# continue: go to the next loop

# if no break in the for loop, can use else
for xx loop:
    if xx:
       break
else:
     xxx   

Python Compare/Check

# if char is an integer.

#### String ####

s = "    words high   "
s.strip() # Remove spaces at the beginning and at the end of the string:
print(s) -> "words high"
s.split(" ")

s[::-1] 

s.lower()
s.upper()
s.isalpha()

#### Dictionary ####
import collections
from collections import Counter
### counter ###
cnt = Counter(nums)

### defaultdict ###
d = collections.defaultdict(list)

### ordered dict ####
d = collections.OrderedDict()
# update a value of under a key, the order doesn't change
# compare two ordered dict
od1 == od2 (compare content and order)
# reverse 
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
my_dict.reverse()
# pop item LIFO 
last_item = my_dict.popitem(last=True) 
# pop item FIFO
last_item = my_dict.popitem(last=False)
# insert existing key to end
my_dict.move_to_end(key)
# insert existing key to begin
my_dict.move_to_end(key, last=False)
my_dict.move_to_start(key)
# delete item
my_dict.pop(key)



#### Queue ####
from collections import deque
q = collections.deque()
q = deque([root, 0])
q.append()
q.popleft()



#### Stack ####



#### Heap(priority queue) ####
''' heap都是最小堆，要做最大堆就放 -xx 进去 '''
import heapq
arr = []

heapq.heappush(arr, 3) # Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap) # Pop and return the smallest item from the heap, maintaining the heap invariant.
arr[0] # acess the smallest item without popping it.
heapq.heappushpop(heap, item) # Push item on the heap, then pop and return the smallest item from the heap.
heapq.heapfy(arr) # Transform list x into a heap, in-place, in linear time.
heapq.nlargest(


https://docs.python.org/3/library/heapq.html
https://github.com/gmertk/python-cheatsheets/blob/master/cheatsheet-queues.py
https://www.pythonsheets.com/notes/python-heap.html

Python sort() & sorted()

arr.sort(key=lambda x: x[1])



new_arr = sorted(arr, key=lambda x:x[0])

footballers_and_nums = [("Fabregas", 4),("Beckham" ,10),("Yak", 9), ("Lampard", 8), ("Ronaldo", 7), ("Terry", 26), ("Van der Saar", 1), ("Yobo", 2)]
sorted_footballers_and_nums = sorted(footballers_and_nums, key=lambda index : index[1])


https://www.freecodecamp.org/news/lambda-sort-list-in-python/
