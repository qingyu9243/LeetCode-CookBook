
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

    def dec(self, key):
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

# 20. Valid Parentheses


# 50. Pow(x, n)


# 244. Shortest Word Distance II

# 277. Find the celebrity

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
print(wordLadder_simple("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

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
        n_words = next_words[cu]
    return
#wordLadder("hit", "cog", ["hot","dot","dog","lot","log","cog"])

# 128. Word ladder II
def wordLadderII():
    pass

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

# 636. Exclusive TIme of 

# 200. Number of Islands

# 3480. [Maximize Subarrays after]


# 605. Can place flowers

# 33. Search in Rotated Sorted Array

# 17. letter of comb
def _17_letter_comb():
    pass

# mutation - 

# 156. Binary Tree upside down

# 215. Kth largest element in 

# 256. Paint House

# 272. Closet binary search Tree

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

#

#

#

#

#

#