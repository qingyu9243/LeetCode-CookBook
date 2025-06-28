#########################################
####       Dynamic Programming       ####
#########################################
# 1326. Minimum Number of Taps to Open to Water a Garden
def minTaps(n, ranges):
    pass

# 300. Longest Increasing Subsequence
def longestIncreasingSub(nums):
    return

# 198. House Robber
def rob(nums):
    return

# 322. Coin Change
def coinChange(coins, amount):
    """coins type and total amount, return min coin count to satisfy amount"""
    # dp[i] = min(dp[i-coinA]+1, dp[i-coinB]+1, xxx)
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[-1] if dp[-1] != float('inf') else -1

# 983. Minimum Cost For Tickets
def mincostTickets(days, costs):
    return

# 70. Climbing Stairs
def climbStairs(n):
    return

# 85. Maximal Rectangle
def maximalRectangle(matrix):
    return

# 139. Word Break
def wordBreak(s, wordDict):
    return

# 931. Minimum Falling Path Sum
def minFallingPathSum(matrix):
    return

# 673. Number of Longest Increasing Subsequence
def findNumberOfLIS(nums):
    return

# 1537. Get the Maximum Score
def maxSum(nums1, nums2):
    return

# 42. Trapping Rain Water
def trap(height):
    return

# 2234. Maximum Total Beauty of the Gardens
def maximumBeauty(flowers, newFlowers, target, full, partial):
    return

# 2915. Length of the Longest Subsequence That Sums to Target
def lengthOfLongestSubsequence(nums, target):
    return

#########################################
####            Graph / BFS           ####
#########################################
from collections import defaultdict
# 210. Course Schedule II
def findOrder(numCourses, prerequisites):
    res = []
    inbound = [0] * numCourses
    course_map = defaultdict(list)
    for course, pre_course in prerequisites:
        course_map[pre_course].append(course)
        inbound[course] += 1
    q = [i for i in range(numCourses) if inbound[i] == 0]
    while q:
        cur_course = q.pop()
        res.append(cur_course)
        for next_course in course_map[cur_course]:
            inbound[next_course] -= 1
            if inbound[next_course] == 0:
                q.append(course)
    if len(res) < numCourses:
        return []
    return res

# 994. Rotting Oranges
def orangesRotting(grid):
    return

# 102. Binary Tree Level Order Traversal
def levelOrder(root):
    return

# 207. Course Schedule
def canFinish(numCourses, prerequisites):
    return

# 695. Max Area of Island
def maxAreaOfIsland(grid):
    return

# 1091. Shortest Path in Binary Matrix
def shortestPathBinaryMatrix(grid):
    return

# 1319. Number of Operations to Make Network Connected
def makeConnected(n, connections):
    return

# 2467. Most Profitable Path in a Tree
def mostProfitablePath(edges, bob, amount):
    return

#########################################
####             Greedy               ####
#########################################
# 1326. Minimum Number of Taps to Open to Water a Garden
# Already defined above

# 42. Trapping Rain Water
# Already defined above

# 621. Task Scheduler
def leastInterval(tasks, n):
    return

# 2234. Maximum Total Beauty of the Gardens
# Already defined above

# 1537. Get the Maximum Score
# Already defined above

# 767. Reorganize String
def reorganizeString(s):
    return

# 475. Heaters
def findRadius(houses, heaters):
    return

#########################################
####        Heap / Counting           ####
#########################################
# 347. Top K Frequent Elements
def topKFrequent(nums, k):
    return

# 621. Task Scheduler
# Already defined above

# 1698. Number of Distinct Substrings in a String
def countDistinctSubstrings(s):
    return

#########################################
####   Sliding Window / Two Pointers  ####
#########################################
# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    cur_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in cur_set:
            cur_set.remove(s[left])
            left += 1
        cur_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# 438. Find All Anagrams in a String
from collections import Counter
def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])
    if p_count == window_count:
        result.append(0)
    # slide window
    for i in range(len(p), len(s)):
        right_char = s[i]
        window_count[right_char] += 1
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result

# 15. 3Sum
""" -4, -1, -1, -1, 1, 2
"""#    i,   j        k
def threeSum(nums):
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            cur_sum = nums[i] + nums[j] + nums[k]
            if cur_sum < 0:
                j += 1
            elif cur_sum > 0:
                k -= 1
            else:
                ans.append(nums[i], nums[j], nums[k])
                while j + 1 < k and nums[j+1] == nums[k]:
                    j += 1
                while k - 1 > j and nums[k-1] == nums[j]:
                    k -= 1
                j += 1
                k -= 1
    return ans

# 2489. Number of Substrings With Fixed Ratio
def fixedRatioSubstrings(nums):
    
    return

#########################################
####              Stack               ####
#########################################
# 20. Valid Parentheses
def isValid(s):
    par_map = {')': '(', ']': '[', '}':'{'}
    stack = []
    for char in s:
        if char in ('(', '[', '{'):
            stack.append(char)
        else:
            if stack:
                last = stack.pop()
                if last != par_map[char]:
                    return False
            return False
    return stack == []

# 394. Decode String
def decodeString(s):
    return

# 155. Min Stack
class MinStack:
    def __init__(self):
        pass
    def push(self, val):
        pass
    def pop(self):
        pass
    def top(self):
        pass
    def getMin(self):
        pass

# 32. Longest Valid Parentheses
def longestValidParentheses(s):
    return

# 42. Trapping Rain Water
# Already defined above

#########################################
####          Array / Math            ####
#########################################
# 66. Plus One
def plusOne(digits):
    n = len(digits)
    for i in reversed(range(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# 238. Product of Array Except Self
def productExceptSelf(nums):
    return

# 1. Two Sum, if there is duplicates
def twoSum(nums, target):
    ans = []
    _map = defaultdict(list)
    for i, num in enumerate(nums):
        diff = target - num
        if diff in _map:
            for prev_index in _map[diff]:
                ans.append([ prev_index, i])
        _map[num].append(i)
    return ans

# 167. two sum II - input array sorted(num is unique)
def twoSumOrdered(nums, target):
    i, j = 0, len(nums)-1
    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            return [i+1, j+1]
    return -1

# 54. Spiral Matrix
def spiralOrder(matrix):
    return

# 628. Maximum Product of Three Numbers
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

# 3148. Maximum Difference Score in a Grid
def maxScore(grid):
    m, n = len(grid), len(grid[0])
    min_val = [[float('inf')]*n for _ in range(m)]
    res = float("-inf")
    for i in range(m):
        for j in range(n):
            if i > 0:
                res = max(res, grid[i][j] - min_val[i-1][j])
            if j > 0:
                res = max(res, grid[i][j] - min_val[i][j-1])
            if i > 0:
                min_val[i][j] = min(min_val[i][j], min_val[i-1][j])
            if j > 0:
                min_val[i][j] = min(min_val[i][j], min_val[i][j-1])
            min_val[i][j] = min(min_val[i][j], grid[i][j])
    print(min_val)
    return res

# 2453. Destroy Sequential Targets
def destroyTargets(nums, space):
    return

# 3088. Make String Anti-palindrome
def makeAntiPalindrome(s):
    return

# 6. Zigzag Conversion
def convert(s, numRows):
    return

#########################################
####         Design                  ####
#########################################
# 146. LRU Cache
class LRUCache:
    def __init__(self, capacity):
        pass
    def get(self, key):
        pass
    def put(self, key, value):
        pass

# 359. Logger Rate Limiter
class Logger:
    def __init__(self):
        pass
    def shouldPrintMessage(self, timestamp, message):
        pass

# 622. Design Circular Queue
class MyCircularQueue:
    def __init__(self, k):
        pass
    def enQueue(self, value):
        pass
    def deQueue(self):
        pass
    def Front(self):
        pass
    def Rear(self):
        pass
    def isEmpty(self):
        pass
    def isFull(self):
        pass

# 380. Insert Delete GetRandom O(1)
class RandomizedSet:
    def __init__(self):
        pass
    def insert(self, val):
        pass
    def remove(self, val):
        pass
    def getRandom(self):
        pass

# 297. Serialize and Deserialize Binary Tree
# Already under Tree

#########################################
####     String / Parsing / Trie      ####
#########################################
# 394. Decode String
# Already defined above

# 22. Generate Parentheses
def generateParenthesis(n):
    return

# 49. Group Anagrams
def groupAnagrams(strs):
    return

# 929. Unique Email Addresses
def numUniqueEmails(emails):
    return

# 770. Basic Calculator IV
def basicCalculatorIV(expression, evalvars, evalints):
    return

# 1698. Number of Distinct Substrings in a String
# Already defined above

# 3088. Make String Anti-palindrome
# Already defined above

#########################################
####        Tree / Binary Tree        ####
#########################################
# 102. Binary Tree Level Order Traversal
# Already defined above

# 297. Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        pass
    def deserialize(self, data):
        pass

# 2467. Most Profitable Path in a Tree
# Already defined above

#########################################
####         Matrix / Grid            ####
#########################################
# 54. Spiral Matrix
# Already defined above

# 695. Max Area of Island
# Already defined above

# 739. Daily Temperatures
def dailyTemperatures(temperatures):
    return

# 764. Largest Plus Sign
def orderOfLargestPlusSign(n, mines):
    return

# 1091. Shortest Path in Binary Matrix
# Already defined above

# 931. Minimum Falling Path Sum
# Already defined above

# 3148. Maximum Difference Score in a Grid
# Already defined above

#########################################
####         Backtracking             ####
#########################################
# 37. Sudoku Solver
def solveSudoku(board):
    return

# 22. Generate Parentheses
# Already defined above

# 139. Word Break
# Already defined above

#########################################
####       Binary Search              ####
#########################################
# 475. Heaters
# Already defined above

# 1760. Minimum Limit of Balls in a Bag
def minimumSize(nums, maxOperations):
    def can_achieve(penalty):
        pass
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right)//2
        if can_achieve(mid):
            right = mid
        else:
            left = mid + 1
    return left

# 4. Median of Two Sorted Arrays
def findMedianSortedArrays(nums1, nums2):
    return

from bisect import bisect, bisect_left
## 354. Russian Doll Envelopes - Hard
def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x:(x[0], -x[1]))
    heights = [h for _, h in envelopes]
    dp = []
    for h in heights:
        index = bisect.bisect_left(dp, h)
        if index == len(dp):
            dp.append(index)
        else:
            dp[index] = h
    return

#########################################
####        Linked List               ####
#########################################
# 876. Middle of the Linked List
def middleNode(head):
    return

# 234. Palindrome Linked List
def isPalindrome(head):
    return

# 21. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    return
