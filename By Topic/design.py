import random
from collections import defaultdict
# 146	LRU Cache()	42.5%	Medium
"""
LRUCache(int capacity) # evict the least used element
algo: use build-in OrderedDict, move least use element to end every time we use(get,put) it.
     move_to_end(key)
     popitem(last = False) # remove the head of cache, FIFO
get(int key) -> int (time O(1))
put(int key) -> void (time O(1))
"""
from collections import OrderedDict
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.dic.move_to_end(key) # 把item放到cache末尾
        return self.dic[key]
    
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key) # 把item放到cache末尾
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False) # 把cache头上最少用的item，pop出去

class Node:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_dll:
    def __init__(self, capacity) -> None:
        self.capcaity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        # connect head and tail (dummy nodes)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key): # O(1)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key, value): # O(1)
        if key in self.cache: # update value
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else: # consider of the cache capacity
            if len(self.cache) >= self.capcaity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def _remove(self, node): # O(1)
        # head <-> n1 <-> node <-> n2 <-> tail
        n1 = node.prev
        n2 = node.next
        n1.next = n2
        n2.prev = n1

    def _add_to_head(self, node): # O(1)
        # head <-> n1 <-> n2 <-> n3 <-> tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

# 1570	Dot Product of Two Sparse Vectors 89.9%	Medium	
class SparseVector:
    def __init__(self, nums) -> None:
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append([i, n])

    def dotProduct(self, vec):
        res = 0
        i, j = 0, 0
        n1 = self.pairs
        n2 = vec.pairs

        while i < len(n1) and j < len(n2):
            if n1[i][0] == n2[j][0]:
                result += n1[i][1]*n2[j][1]
                i += 1
                j += 1
            elif n1[i][0] < n2[j][0]:
                i += 1
            else:
                j += 1
        return res

# 380	Insert Delete GetRandom O(1)	54.4%	Medium	
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.value_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False

        self.values.append(val)
        self.value_to_index[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False

        # find index    
        index = self.value_to_index[val]
        last_value = self.values[-1]

        #exchange the value to be removed with the last value
        self.values[index] = last_value
        self.value_to_index[last_value] = index
        
        self.values.pop()
        del self.value_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# 588	Design In-Memory File System 48.1%	Hard	
class FileSystem:
    def __init__(self) -> None:
        pass

# 981	Time Based Key-Value Store	49.4%	Medium	
class TimeMap:
    def __init__(self) -> None:
        self.time_map = defaultdict(list)

    def set(self, key, value, ts):
        self.time_map[key].append((ts, value))

    def get(self, key, ts):
        arr = self.time_map[key]
        if not arr or ts < arr[0][0]:
            return ""
        if ts >= arr[-1][0]:
            return arr[-1][1]
        # [(ts1, value1), (ts2, value1), (ts3, value1)]
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid][0] == ts:
                return arr[mid][1]
            elif arr[mid][0] > ts:
                r = mid
            else:
                l = mid + 1
        return arr[l-1][1]
    
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
#print(timeMap.get("foo", 1))
#print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
#print(timeMap.get("foo", 4))
#print(timeMap.get("foo", 5))

# 359	Logger Rate Limiter 75.9%	Easy	
class RateLimiter:
    def __init__(self) -> None:
        pass
    
        

# 460	LFU Cache	44.2%	Hard	


# 716	Max Stack 45.0%	Hard
"""
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

    MaxStack() Initializes the stack object.
        void push(int x) Pushes element x onto the stack.
        int pop() Removes the element on top of the stack and returns it.
        int top() Gets the element on the top of the stack without removing it.
        int peekMax() Retrieves the maximum element in the stack without removing it.
        int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

3 5 1 3 6 7

"""
import heapq
class MaxStack: # Heap + lazy update.

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.cnt = 0

    def push(self, x: int) -> None: # push to stack and heap
        self.stack.append((x, self.cnt))
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.cnt += 1

    def pop(self) -> int: # pop from stack
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int: # get from stack
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int: # get top element from heap 
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]       

    def popMax(self) -> int: # pop max element from heap
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, idx = heapq.heappop(self.heap)
        self.removed.add(-idx)
        return -num     

# 346	Moving Average from Data Stream 78.3%	Easy	
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:  
    MovingAverage(int size) Initializes the object with the size of the window size.
    double next(int val) Returns the moving average of the last size values of the stream.
"""
from collections import deque
class MovingAverage:
    def __init__(self, size) -> None:
        self.queue = deque()
        self.size = size
        self.count = 0
        self.sum = 0

    def next(self,val):
        self.queue.append(val)
        self.count += 1
        self.sum += val
        if self.count > self.size:
            a = self.queue.popleft()
            self.sum = self.sum - a
        return self.sum/min(self.size, self.count)

# 362	Design Hit Counter 68.7%	Medium	


# 295	Find Median from Data Stream	51.9%	Hard	

# 715 Range Module
    
# 631 Design Excel Sum Formula
"""
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:
    Excel(int height, char width) Initializes the object with the height and the width of the sheet. 
    The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] 
    and the column index in the range ['A', width]. All the values should be zero initially.
        void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
        int get(int row, char column) Returns the value at mat[row][column].
        int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. 
            This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
            "ColRow" that represents a single cell.
                For example, "F7" represents the cell mat[7]['F'].
            "ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
                For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.
For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
"""
class Excel:
    def __init__(self) -> None:
        pass
    def set(row, col, va):
        pass
    def get(row, col):
        pass
    def sum(row, col, numbers):
        pass

# 2296	Design a Text Editor 44.2%	Hard	
    
# 1166	Design File System 62.8%	Medium	
    
# 642	Design Search Autocomplete System 48.9%	Hard	
    
# 348	Design Tic-Tac-Toe 58.0%	Medium	
    
# 353	Design Snake Game 38.8%	Medium	

# 155	Min Stack Medium
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

4 2 8 2 5 7 1 (stack)
4 2 2 1 (min stack)
only push in the the elments smaller
"""
class MinStack:
    def __init__(self):
        self.stack =[]
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
####################################################
