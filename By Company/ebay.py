# 54. spiral matrix
def spiralOrder(matrix):
    result = []
    top, bottom, = 0, len(matrix) - 1 # current top row, current bottom row
    left, right = 0, len(matrix[0]) - 1 # current left column, current right column
    while top <= bottom and left <= right:
        for col in range(left, right+1): # move right on the top row
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom+1): # move down on the right col
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom: # move left on the buttom row
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right: # move up on the left column
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    return result

# 73. set matrix zeros
def setZeros(matrix):
    m, n = len(matrix), len(matrix[0])
    zeros = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append([i, j])
    for row_n, col_n in zeros:
        for i in range(m):
            matrix[i][col_n] = 0
        for j in range(n):
            matrix[row_n][j] = 0

# 146.LRU cache
from collections import defaultdict
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
class LRU:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = {} # key_value -> node reference
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, k, v): # put k and v in cache
        if k in self.cache:
            node = self.cache[k]
            node.val = v
            self._remove_node(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(k, v)
            self._add_to_head(new_node)
            self.cache[k] = new_node
    
    def get(self, k): # get value
        # retrieve the node under k in cache, move this node to head
        if k in self.cache:
            node = self.cache[k]
            self._remove_node(node)
            self._add_to_head(node)
            return node.val
        return -1
    
# 50. pow(x, n)

# 473. matchsticks to sqaure
def makesquare(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    side_length = total // 4
    matchsticks.sort(reverse = True)
    if matchsticks[0] > side_length:
        return False
    sides = [0, 0, 0, 0]
    def backtrack(index):
        if index == len(matchsticks):
            return sides[0] == sides[1] == sides[2] == sides[3] == side_length
        for i in range(4):
            if sides[i] + matchsticks[i] <= side_length:
                sides[i] += matchsticks[i]
                if backtrack(index+1):
                    return True
                sides[i] -= matchsticks[i]
            if sides[i] == 0:
                break
        return False
    return backtrack(0)

# 981. Time based key-value store
import bisect
class TimeMap():
    """Design a time-based key-value data structure that can store multiple values for the same key at different time stamps,
    and retrieve the key's value at a certain timestamp."""
    def __init__(self) -> None:
        self.timeMap = defaultdict(list)

    def set(self, key, value, timestamp):
        self.timeMap[key].append((timestamp, value))
    
    def get(self, key, timestamp):
        # binary search the timestamp
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        #idx = bisect.bisect_right(values, (timestamp, chr(127)))
        left, right = 0, len(values)-1
        result = ""
        while left <= right:
            mid = (left + right)//2
            mid_ts, mid_value = values[mid]
            if mid_ts <= timestamp:
                left = mid + 1
                result = mid_value
            else:
                right = mid - 1
        return result

# 994. rotting oranges

# 22. generate parenthese
def generateParenthese(n):
    ans = []
    def backtrack(cur_path, l, r):
        if len(cur_path) == 2*n:
            ans.append(cur_path)
            return
        if l < n:
            backtrack(cur_path+"(", l+1, r)
        if l > r:
            backtrack(cur_path+")", l, r+1)
        return
    backtrack("", 0, 0)
    return ans

# 23. Merge K sorted lists

# 581. shortest unsorted continous subarray
def findUnsortedSubarray(nums):
    n = len(nums)
    # left pass - find the first decrease one
    left = -1
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            left = i
            break
    if left == -1:
        return 0
    # right pass - find the first decrease one
    right = -1
    for j in range(n-1, 0, -1):
        if nums[j] < nums[j-1]:
            right = j
            break

    min_val = min(nums[left:right+1])
    max_val = max(nums[left:right+1])
    while left > 0 and nums[left - 1] > min_val:
        left -= 1
    while right < n -1 and nums[right + 1] < max_val:
        right += 1
    return right - left + 1

# 752. open the lock
from collections import deque
def openLock(deadends, target):
    if '0000' in deadends:
        return -1
    visited = set()
    queue = deque()
    queue.append(['0000', 0])
    while queue:
        cur, step = queue.appendleft()
        if cur == target:
            return step
        for i in range(4):
            mid_digit = [(int(cur[i])+1)%10, (int(cur[i])-1)%10]
            next_wheels = [cur[:i] + str(mid_digit[0]) + cur[i+1:], cur[:i] + str(mid_digit[1]) + cur[i+1:]]
            for n in next_wheels:
                if n not in visited and n not in deadends:
                    visited.add(n)
                    queue.append([n, step+1])
    return -1

# 1909. remove one element to make array strictly
def canBeIncreasing(nums):
    violations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            violations += 1
            if violations > 1:
                return False
            # try remove nums[i-1]
            can_remove_prev = (i == 1) or (nums[i-2] < nums[i])
            # try remove nums[i]
            can_remove_curr = (i == len(nums)-1) or (nums[i-1] < nums[i+1])
            if not can_remove_prev and not can_remove_curr:
                return False
    return True