
from typing import List
from collections import defaultdict, deque
import heapq

# 432. [All O's one data structure]
# use doubly linked list to store frequency and keys/strings with same frequency
class Node:
    def __init__(self, freq) -> None:
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self) -> None:
        self.map = {} # string: node reference
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def inc(self, key):
        """increment string key by 1 if exist, else create new Node with freq 1"""
        pass

    def dec(self, key): # 
        """decrement string key by 1. If freq = 0, delete this node """
        pass

    def getMaxKey(self):
        pass

    def getMinKey(self):
        pass

    def removeNode(self):
        pass

# 364. Nestest list weight sum II - dfs/bfs
class NestedInteger:
    def __init__(self, value=None):
        #If value is not specified, initializes an empty list.
        #Otherwise initializes a single integer equal to value.
        pass

    def isInteger(self): #-> bool
        #@return True if this NestedInteger holds a single integer, rather than a nested list.
        pass

    def add(self, elem): #-> void
        #Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        pass

    def setInteger(self, value): #-> void
        #Set this NestedInteger to hold a single integer equal to value.
        pass

    def getInteger(self):# -> int
        #@return the single integer that this NestedInteger holds, if it holds a single integer
        #Return None if this NestedInteger holds a nested list
        pass

    def getList(self): #-> List[NestedInteger]
        #@return the nested list that this NestedInteger holds, if it holds a nested list 
        #Return None if this NestedInteger holds a single integer
        pass

def _364_depthSumInverse_dfs(nestedList: List[NestedInteger]):
    integer_with_depth = []

    def dfs_get_max_depth(l, cur_depth):
        max_depth_found = cur_depth

        for item in l:
            if item.isInteger():
                max_depth_found.append((item.getInteger(), cur_depth))
            else:
                sub_list = item.getList()
                sub_depth = dfs_get_max_depth(sub_list, cur_depth+1)
                max_depth_found = max(max_depth_found, sub_depth)
        return max_depth_found

    max_depth = dfs_get_max_depth(nestedList, 1)

    total_sum = 0
    for integer, depth in integer_with_depth:
        weight = max_depth - depth + 1
        total_sum += integer*weight
    return total_sum

def _364_depthSumInverse_bfs(nestedList):
    queue = [(item, 1) for item in nestedList]
    max_depth = 1
    integer_with_depth = []

    while queue:
        item, depth = queue.pop(0)
        max_depth = max(max_depth, depth)
        if item.isInteger():
            integer_with_depth.append((item.getInteger(), depth))
        else:
            for nested_item in item.getList():
                queue.append((nested_item, depth + 1))

    total_sum = 0
    for integer, depth in integer_with_depth:
        weight = max_depth - depth + 1
        total_sum += integer*weight
    return total_sum

# 339. Nested List Weight Sum
def _339_depthSum(nestedList: List[NestedInteger]):
    pass

# 716. [Max Stack]
class MaxStack:
    def __init__(self) -> None:
        self.stack = [] # [num, ind]
        self.heap = [] # [-num, -ind]
        self.removed = set() # removed ind
        self.index = 0 # ind

    def push(self, x):
        self.stack.append((x, self.index))
        heapq.heappush(self.heap, (-x, -self.index)) # O(nlogn)
        self.index += 1

    def pop(self): # check stack, but need to update first based on removed
        while self.stack and self.stack[-1][-1] in self.removed:
            self.stack.pop()
        num, ind = self.stack.pop()
        self.removed.add(ind)
        return num

    def top(self): # O(1), # check stack, but need to update first based on removed
        while self.stack and self.stack[-1][-1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peakMax(self): # check heap, but need to update first based on removed
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return self.heap[0][0]

    def popMax(self):
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, ind = heapq.heappop(self.heap)
        self.removed.add(-ind)
        return num

# 155. Min Stack, O(1) for all op
class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = [] # same length with stack, but elment is the smallest value until now.
    
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x,self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# 1004. Max Consecutive Ones III
    """
    sliding window. moving right first until 0 count reach k. then move left.
    """
def longestOnes(nums, k):
    l = r = 0
    count_zero = 0
    ans = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            count_zero += 1
        while count_zero > k:
            if nums[l] == 0:
                count_zero -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans

# 20. Valid Parentheses, Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
def validParenthese(str):
    check_map = {"}": "{", ")": "(", "]": "["}
    stack = []
    for char in str:
        if char in ("(", "{", "["):
            stack.append(char)
        else:
            if not stack or stack[-1] != check_map[char]:
                return False
            stack.pop()
    return stack == []

# 50. Pow(x, n) x^n
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    result = 1
    current_power = x
    while n > 0:
        if n%2 == 1:
            result *= current_power
        current_power *= current_power
        n // 2
    return result

# 636. Exclusive time of functions
def exclusiveTime(n, logs):
    res = [0]*n
    stack = []
    prev_time = 0

    #for log in logs:
    #    fn_id, typ 
    return

# 516. Longest Palindromic Subsequence
def longestPaSub_dp(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Fill DP table
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]: # char is same, add both
                if length == 2:
                    dp[i][j] = 2
                else: 
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else: # char is different, choose best of exclusing i or j
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

# 200. Number of Islands
def numberOfIslands(grid):
    pass

# 243. Shortest Word Distance
def shortestDistance(wordsDict: List[str], word1: str, word2: str):
    pos1 = pos2 = -1
    min_distance = float('inf')

    for i, word in enumerate(wordsDict):
        if word == word1:
            pos1 = i
            if pos2 != -1:
                min_distance = min(min_distance, abs(pos1 - pos2))
        elif word == word2:
            pos2 = i
            if pos1 != -1:
                min_distance = min(min_distance, abs(pos1 - pos2))
    return min_distance
# 244. Shortest Word Distance II
class WordDistance:
    def __init__(self, wordList) -> None:
        self.indexs = defaultdict(list)
        for i, word in enumerate(wordList):
            self.indexs[word].append(i)

    def shortestWordDistance2(self, w1, w2):
        w1_indexes = self.indexs[w1] # [0, 1]
        w2_indexes = self.indexs[w2] # [3, 5]
        i = j = 0
        min_dis = float('inf')
        while i < len(w1_indexes) and j < len(w2_indexes):
            min_dis = min(min_dis, abs(w1_indexes[i] - w2_indexes[j]))
            if w1_indexes[i] < w2_indexes:
                i += 1
            else:
                j += 1
        return min_dis
# 245. Shortest Word Distance III
def shortestWordDistance3(wordsDict, word1, word2):
    if word1 == word2:
        # Special case: find shortest distance between two occurrences of the same word
        min_distance = float('inf')
        prev_pos = -1
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                if prev_pos != -1:
                    min_distance = min(min_distance, i - prev_pos)
                prev_pos = i
        
        return min_distance
    else:
        # Original case: two different words
        min_distance = float('inf')
        pos1 = -1  # Most recent position of word1
        pos2 = -1  # Most recent position of word2
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
                # If we've seen word2 before, calculate distance
                if pos2 != -1:
                    min_distance = min(min_distance, abs(pos1 - pos2))
            elif word == word2:
                pos2 = i
                # If we've seen word1 before, calculate distance
                if pos1 != -1:
                    min_distance = min(min_distance, abs(pos1 - pos2))
        
        return min_distance
     
# 277. Find the celebrity
def findCelebrity(n):
    def knows(a, b):
        pass
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and knows(candidate, i):
            return -1
    for i in range(n):
        if i != candidate and not knows(i, candidate):
            return -1
    return candidate

# 53. Maximum Subarray

# 127. [Word Ladder]
def wordLadder_simple(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    n = len(beginWord)
    queue = deque()
    queue.append([beginWord, [beginWord]]) # [beginWord, 1]
    visited = set([beginWord])
    path = []
    path.append(beginWord)
    while queue:
        cur_word, path = queue.popleft() # cur_word, length
        for i in range(n):
            for mid_char in "abcdefghijklmnopqrstuvwxyz":
                next_word = cur_word[:i] + mid_char + cur_word[i+1:]
                if next_word == endWord:
                    return path + [next_word] # length + 1
                if next_word in wordList and next_word not in visited:
                    visited.add(next_word)
                    queue.append([next_word, path + [next_word]]) # length + 1
    return []
#print(wordLadder_simple("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

def wordLadder(beginWord, endWord, wordList):
    # initial check
    if endWord not in wordList or not beginWord or not endWord or not wordList:
        return 0
    # intermediate words list
    wordList.append(beginWord)
    n = len(beginWord)
    next_words = defaultdict(list) 
    for word in wordList:
        for i in range(n):
            generic_word = word[:i] + "*" + word[i+1:]
            next_words[generic_word].append(word)
    print(next_words)
    # bfs
    queue = deque()
    queue.append([beginWord, 1])
    while queue:
        cur, n = queue.popleft()
        n_words = next_words[cur]
    return
#wordLadder("hit", "cog", ["hot","dot","dog","lot","log","cog"])

# 128. Word ladder II
def wordLadderII(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordList = set(wordList)
    res = []
    edge = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            edge[word[:i] + "_" + word[i+1:]].append(word)
            
    q = {beginWord: [[beginWord]]}
    while q:
        wordList -= set(q.keys())
        new_q = defaultdict(list)
        for w in q:
            if w == endWord: 
                return q[w]
            else:
                for i in range(len(w)):
                    for neww in edge[w[:i] + "_" + w[i+1:]]:
                        if neww in wordList:
                            new_q[neww].extend([j + [neww] for j in q[w]])          
        q = new_q
    return res

# [366]. Find leaves of Binary Tree - dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.value = val
        self.left = left
        self.right = right
def _366_find_tree_leaves(root):
    result = []
    def dfs(node):
        if not node:
            return -1
        # find left and right height
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        # calculate current height
        current_height = max(left_height, right_height) + 1
        # if entry a new level(upper level)
        if len(result) <= current_height:
            result.append([])
        result[current_height].append(node.val)
        return current_height

    dfs(root)
    return result

# 380. Insert Delete GetRandom

# 3480. [Maximize Subarrays after removing one conflict pair]
def maxSubarrays(N, A):
    right = [[] for _ in range(N+1)]
    for a, b in A:
        right[max(a, b)].append(min(a, b))
    ans = 0
    left = [0, 0]
    impl = [0] * (N+1)
    for r in range(1, N+1):
        for l in right[r]:
            left = max(left, [l, left[0]], [left[0], l])
        ans += r - left[0]
        impl[left[0]] += left[0] - left[1]
    return ans + max(impl)

# 605. Can place flowers

# 33. Search in Rotated Sorted Array

# 17. letter of comb
def _17_letter_comb():
    pass
# mutation - 

# 360. Sort Transformed Array
def sortTransFormedArray(nums, a, b, c):
    def transform(x):
        return a * x * x + b * x + c
    # Transform all numbers
    transformed = [transform(x) for x in nums]  
    # Sort and return
    return sorted(transformed)
def sortTransformedArray_twoPointer(nums, a, b, c):
    def transform(x):
        return a * x * x + b * x + c
    n = len(nums)
    l, r = 0, n - 1
    result = [0] * n
    if a > 0: # func face up
        for i in range(len(nums)-1, -1, -1):
            left_value = transform(nums[l])
            right_value = transform(nums[r])
            if left_value >= right_value:
                l += 1
                result[i] = left_value
            else:
                r -= 1
                result[i] = right_value
    else: # func face down
        for i in range(n):
            left_value = transform(nums[l])
            right_value = transform(nums[r])
            if left_value <= right_value:
                l += 1
                result[i] = left_value
            else:
                r -= 1
                result[i] = right_value
    return result
#print(sortTransformedArray_twoPointer([-4,-2,2,4], 1, 3, 5))

# 156. Binary Tree upside down
def upsideDownBinaryTree(root):
    pass

# 215. Kth largest element in 

# 256. Paint House I 
def minCostI(costs):
    n = len(costs)
    prev_red = costs[0][0]
    prev_blue = costs[0][1]
    prev_green = costs[0][2]

    for i in range(1, n):
        cur_red = costs[i][0] + min(prev_blue, prev_green)
        cur_blue = costs[i][1] + min(prev_red, prev_green)
        cur_green = costs[i][2] + min(prev_blue, prev_red)
        prev_red = cur_red
        prev_blue = cur_blue
        prev_green = cur_green
    #print(prev_red, prev_blue, prev_green)
    return min(prev_red, prev_blue, prev_green)
#print(minCostI([[17,2,17],[16,16,5],[14,3,19]]))

# 265. Paint House II
def minCostII(costs):
    n, k = len(costs), len(costs[0])
    dp = []
    for i in range(k):
        dp.append(costs[0][i])
    #print(dp)

    for house in range(1, n):
        tmp_list = []
        for color in range(k):
            smallest = float('inf')
            for pre_color in range(k):
                if color == pre_color: continue
                smallest = min(smallest, dp[pre_color])
            tmp_list.append(costs[house][color]+smallest)
        dp = tmp_list
    return min(dp)

# 272. Closet binary search Tree
def closestKValues(root, target, k): # time: nlogK)
    max_heap = [] # (-distance, node.val)
    def traverse(node):
        if not node:
            return
        distance = abs(node.val - target)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-distance, node.val))
        elif distance < -max_heap[0][0]:
            heapq.heapreplace(max_heap, (-distance, node.val))
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return [value for _, value in max_heap]

# 32. Longest Valid Parentheses
def longestValidParen(s):
    stack = [-1]
    res = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i) # record this invalid end position
            else:
                res = max(res, i - stack[-1])
    return res
def longestValidParen_twoPass(s):
    if not s:
        return 0
    max_len = 0
    left = right = 0
    for char in s:
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2*left)
        elif right > left:
            left = right = 0
    left = right = 0
    for char in reversed(s):
        if char == "(":
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2*left)
        elif left > right:
            left = right = 0    

    return max_len

# 297. Serialize and Deserialize Binary Tree
def serialize(root):
    vals = []
    def preorder(node):
        if not node:
            vals.append('null')
        else:
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
    preorder(root)
    return ",".join(vals)
def deserialize(data):
    vals = data.split(',')
    index = 0
    def build_tree():
        nonlocal index
        if index >= len(vals):
            return None
        val = int(vals[index])
        index += 1
        if val == 'null':
            return None
        node = TreeNode(val)
        node.left = build_tree()
        node.right = build_tree()
        return node
    build_tree()

# 763. Partition Labels
def partitionLabels(s):
    last = {ch: i for i, ch in enumerate(s)}
    start = end = 0
    res = []

    for i, char in enumerate(s):
        end = max(end, last[char])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res

# 1944. Number of Visible pp in a Queue
def numVisiblePP(heights):
    ans = [0]*len(heights)
    stack = []
    for i, v in enumerate(heights):
        while stack and heights[stack[-1]] <= v:
            ans[stack.pop()] += 1
        if stack:
            ans[stack[-1]] += 1
        stack.append(i)
    return ans

# 2276. Count Integers in Intervals
class CountIntervals:
    def __init__(self) -> None:
        self.intervals = []
        self.cur_count = 0

    def add(self, left, right):
        new_intervals = []
        new_left, new_right = left, right

        for interval_left, interval_right in self.intervals:
            if interval_right < left or interval_left > right: # on overlapping
                new_intervals.append([interval_left, interval_right])
            else:
                new_left = min(left, interval_left)
                new_right = max(right, interval_right)
                self.cur_count -= (interval_right-interval_left + 1) # remove the original one. a

        new_intervals.append([new_left, new_right]) # add new interval
        self.cur_count += (new_right - new_left + 1) # aad new count
        self.intervals = new_intervals

    def count(self):
        return self.cur_count
"""  
print("count interval")
intervals = CountIntervals()
intervals.add(2, 3)
intervals.add(7, 10)
print(intervals.count())
intervals.add(1, 8)
print(intervals.intervals)
"""  

# 1856. [Largest Color Value in a Directed Graph]
def largestPathValue(colors, edges):
    n = len(colors)
    graph = [[] for _ in range(n)]
    in_degree = [0]*n
    # build graph
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    print("graph", graph)
    print("in degree", in_degree)
    # topological sort
    topo_order = []
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    print(queue)
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    print("topo order", topo_order)
    # cycle detection
    if len(topo_order) != n:
        return -1
    # DP. dp[i][c] = max count of color c in paths ending at node i
    dp = [[0]*26 for _ in range(n)]
    for node in topo_order:
        node_color = ord(colors[node]) - ord('a') # convert to a num
        dp[node][node_color] = max(dp[node][node_color], 1)
        # update neigbhors
        for neighbor in graph[node]:
            for color in range(26):
                if color == ord(colors[neighbor]) - ord('a'):
                    dp[neighbor][color] = max(dp[neighbor][color], dp[node][color] + 1)
                else:
                    dp[neighbor][color] = max(dp[neighbor][color], dp[node][color])

    return max(max(row) for row in dp)
print(largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]))
#print(largestPathValue("a", [[0, 0]]))

# 373. Find K pairs with smallest sums
def kSmallestPairs(nums1, nums2, k):
    heap = []
    result = []
    for j in range(min(len(nums2), k)):
        heapq.heappush(heap, (nums1[0]+nums2[j], 0, j))
    while k > 0 and heap:
        cur_sum, i, j = heapq.heappop(heap)
        result.append(nums1[i], nums2[j])
        if i + 1 < len(nums1):
            heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
        k -= 1
    return result

# 658. Find K closest Elements
def findClosetElements(arr, k, x): # binary search
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right)//2
        if x - arr[mid] > arr[mid] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left: left+k]

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#