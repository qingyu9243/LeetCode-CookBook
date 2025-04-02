from collections import defaultdict
# 146. LRU cache - least recently used cache.
class Node:
    def __init__(self, key = None, value = None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = {} # key -> value(node's reference)
        self.head = Node()
        self.tail = Node()
        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value): # O(1) time
        if key in self.cache: # exist, update the node value and location
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else: # new node
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
        
    def get(self, key): # O(1) time
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
        return -1

    def _remove(self, node):
        # head <-> n1 <-> n2 <-> tail
        # remove the node from double linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add_to_head(self, node):
        # head <-> n1 <-> n2 <-> tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

# 3438. Find Valid Pair of Adjacent Digits in String
def findValidPair(self, s: str) -> str:
    # construct to map
    _map = defaultdict(int)
    for char in s:
        _map[char] += 1
    print(_map)

    for i in range(len(s)-1):
        first_digit = s[i]
        second_digit = s[i+1]
        if first_digit != second_digit:
            if int(first_digit) == _map[first_digit] and int(second_digit) == _map[second_digit]:
                return first_digit + second_digit
    return ""

# 200. number of islands
def numOfIslands(board):
    pass

# 1. two sum
def twoSum():
    pass

# 3. longest substring without repeating characters

# 49. group anagrams

# 239. Sliding window maximum
def slidingWinMax(nums, k):
    

# 1797. Design authentication manager

# 1200. minimum absolute difference

# 347. Top k frequent elements

# 23. merge k sorted lists

# 199. binary tree right side view

# 15. 3 sum

# 54. spiral matrix

# 56. merge intervals

# 206 reverse linked list

# 253. meeting rooms II

# 20. valid parentheses

# 33. search in rotated sorted arry

# 71. simplify path

# 2062. Count Vowel Substrings of a String-Easy

# 1209. Remove All Adjacent Duplicates in String II-Med.

# 300. Longest Increasing Subsequence-Med.

# 322. Coin Change-Med.

# 4. Median of Two Sorted Arrays-Hard

# 5. Longest Palindromic Substring-Med.

# 987. Vertical Order Traversal of a Binary Tree-Hard

# 994. Rotting Oranges-Med.

# 13. Roman to Integer-Easy

# 51. N-Queens-Hard

# 55. Jump Game-Med.

# 124. Binary Tree Maximum Path Sum-Hard

# 647. Palindromic Substrings-Med.

# 155. Min Stack-Med.

# 215. Kth Largest Element in an Array-Med.

# 221. Maximal Square-Med.
################################################
# 
## product prices ##
class ProductPrice:
    def __init__(self) -> None:
        self.prices = []
        self.min = float('inf')
        self.max = float('-inf')

    def update(self, ts, price):
        self.prices.append((ts, price))
        if price < self.min:
            self.min = price
        if price > self.max:
            self.max = price

    def minimum(self):
        if not self.prices:
            return None
        return self.min

    def maximum(self):
        if not self.prices:
            return None
        return self.max

    def lastest(self):
        if not self.prices:
            return None
        return self.prices[-1][-1]