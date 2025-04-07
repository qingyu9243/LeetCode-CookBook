from collections import defaultdict, deque, Counter
import heapq
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
"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def longestSubstringWithoutRepeatChar(s):
    max_length = 0
    char_set = set()
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            left += 1
            char_set.remove(s[left])
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# 49. group anagrams
def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

# 239. Sliding window maximum - HARD
"""
nums  =  [1, 3, -1, -3, 5, 3, 6, 7]
window = [0]
"""
def maxSlidingWindow(nums, k):
    n = len(nums)
    res = []
    window = deque() # store the index, not values
    for i in range(n):
        while window and window[0] < i - k + 1:
            window.popleft()
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res

# 1797. Design authentication manager
class AuthenticationManager:
    def __init__(self, timeToLive) -> None:
        self.ttl = timeToLive
        self.tokens = {} # key:tokenId, value: expiry time

    def generate(self, tokenId, currentTime):
        expiry = currentTime + self.ttl
        self.tokens[tokenId] = expiry

    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = self.ttl + currentTime

    def countUnexpiredTokens(self, currentTime):
        cnt = 0
        for expiry in self.tokens.values():
            if expiry > currentTime:
                cnt += 1
        return cnt

# 1200. minimum absolute difference

# 347. Top k frequent elements
def topKelements(nums, k):
    heap = []
    counter = Counter(nums)
    for num, freq in counter.items():
        if len(heap) == k:
            heapq.heappushpop(heap, (freq, num))
        else:
            heapq.heappush(heap, (freq, num))
    result = []
    for _, num in heap:
        result.append(num)

# [23]. merge k sorted lists - Hard
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    # Handle edge cases
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # Remove any None/empty lists
    lists = [lst for lst in lists if lst]
    if not lists:
        return None
    
    # Method 1: Using a min heap
    import heapq
    
    # Create a dummy head for the result list
    dummy = ListNode(0)
    current = dummy
    
    # Create a min heap
    # We need to use a counter to break ties when values are equal
    # (since ListNode doesn't implement comparison)
    heap = []
    counter = 0
    
    # Add the first node from each list to the heap
    for i, head in enumerate(lists):
        if head:
            # Use (value, counter, node) tuple for heap
            # counter is used as a tiebreaker when values are equal
            heapq.heappush(heap, (head.val, counter, head))
            counter += 1
    
    # Process the heap until it's empty
    while heap:
        # Pop the smallest element
        val, _, node = heapq.heappop(heap)
        
        # Add it to our result list
        current.next = node
        current = current.next
        
        # If this node has a next, add it to the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1
    
    return dummy.next
# 199. binary tree right side view
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def binaryTreeRightView(root):
    # level order traversal. BFS
    if not root:
        return []
    ans = []
    queue = []
    queue.append([root]) # store each level nodes as a list in the queue
    while queue:
        level_nodes = queue.pop(0)
        ans.append(level_nodes[-1].val)
        next_level_nodes = []
        for node in level_nodes:
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        if len(next_level_nodes) > 0:
            queue.append(next_level_nodes)

    return ans

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