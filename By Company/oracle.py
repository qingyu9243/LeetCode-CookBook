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
def minimumAbsDifference(arr):
    arr.sort()
    min_abs = float('inf')
    for i in range(1, len(arr)):
        min_abs = min(min_abs, arr[i]-arr[i-1])
    ans = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff == min_abs:
            ans.append([arr[i-1], arr[i]])
    return ans

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

# 1209. Remove All Adjacent Duplicates in String II-Med.

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

# [15]. 3 sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums):
    # three pointers
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i + 1, n-1
        while j < k:
            cur = nums[i] + nums[j] + nums[k]
            if cur > 0:
                k -= 1
            elif cur < 0:
                j += 1
            else: # cur == 0
                res.append((nums[i], nums[j], nums[k]))
                while j + 1 < k and nums[j+1] == nums[k]:
                    j += 1
                while k - 1 > j and nums[k-1] == nums[j]:
                    k -= 1
                j += 1
                k -= 1
    return res

# 54. spiral matrix
def spiral_order(matrix):
    m, n = len(matrix), len(matrix[0])
    direction = 1
    i, j = 0, -1
    result = []
    # right -> down(direction is 1), then left -> up(direction is -1)
    while m*n > 0:
        for _ in range(n): # move right(1) or left(-1)
            j += direction
            result.append(matrix[i][j])
        n -= 1
        for _ in range(m): # move down(1) or up(-1)
            i += direction
            result.append(matrix[i][j])
        m -= 1
        direction *= -1
    return result
#print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))

# 56. merge intervals - medium
def mergeIntervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        current = intervals[i]
        prev = merged[-1]
        if prev[1] >= current[0]:
            merged[-1][1] = max(prev[1], current[1])
        else:
            merged.append(intervals[i])
    return merged

# 140. word break II - hard - dfs
"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
"""
def wordBreak(s, wordDict):
    # convert wordDict to a set for O(1) lookups
    word_set = set(wordDict)

    # memoization cache
    memo = {}
    def backtrack(start):
        # If we've already solved this subproblem, return the result
        if start in memo:
            return memo[start]
        result = []
        if start == len(s):
            result.append("")
            return result
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in word_set:
                sentences = backtrack(end)
                for sentence in sentences:
                    if sentence == "":
                        result.append(word)
                    else:
                        result.append(word+" "+sentence)
        memo[start] = result
        return result

    return backtrack(0)
print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))


# 206 reverse linked list

# 253. meeting rooms II

# 20. valid parentheses
def validParenthese(s):
    pass

# 33. search in rotated sorted arry
def searchInRotatedArray(arr):
    pass

# 772. Basic Calculator III
def basicCaculator():
    pass

# 71. simplify path

# 2062. Count Vowel Substrings of a String-Easy

# 300. Longest Increasing Subsequence-Med.
def longestIncreaseingSequence(nums):
    pass

# 134. Gas Station
def gasStation():
    pass

# 322. Coin Change-Med.

# 4. Median of Two Sorted Arrays-Hard

# 5. Longest Palindromic Substring-Med.

# 987. Vertical Order Traversal of a Binary Tree-Hard
def verticalOrderBinaryTree(root):
    col_dict = defaultdict(list) # key: col, value:(level, node.value)
    queue = [(root, 0, 0)] # node, col, level

    while queue:
        node, col, level = queue.pop(0)
        col_dict[col].append((level, node.val))
        if node.left:
            queue.append([node.left, col - 1, level + 1])
        if node.right:
            queue.append([node.right, col + 1, level + 1])
    
    result = []
    # sort col first
    for col in sorted(col_dict.keys()):
        values = sorted(col_dict[col])
        tmp = []
        for level, node_value in values:
            tmp.append(node_value)
        result.append(tmp)
    return result

# 994. Rotting Oranges-Med.

# 13. Roman to Integer-Easy

# 51. N-Queens-Hard
def nQueens(martix):
    pass

# 55. Jump Game-Med.

# [124]. Binary Tree Maximum Path Sum-Hard
def binaryTreeMaxPathSum(root):
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        cur_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, cur_path_sum)

        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

""" LC 112. Path Sum
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. """
def hasPathSum(root, targetSum):
    if not root:
        return False
    targetSum -= root.val
    if targetSum == 0 and not root.left and not root.right:
        return True
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

# 647. Palindromic Substrings-Med.
def palindromicSubstrings(s):
    if not s:
        return 0
    n = len(s)
    def expand_around_center(left, right):
        palindrome = 0
        while 0 <= left and right < n and s[left] == s[right]:
            palindrome += 1
            left -= 1
            right += 1
        return palindrome

    count = 0
    for i in range(n):
        count += expand_around_center(i, i)
        count += expand_around_center(i, i+1)
    return count
#print(palindromicSubstrings("abc"))

# 155. Min Stack-Med.

# 215. Kth Largest Element in an Array-Med.

# 221. Maximal Square-Med.

# 9. Palindrome Number
def palindromeNumber(x):
    if x < 0:
        return False
    s = str(x)
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
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