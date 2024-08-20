from collections import defaultdict
from collections import deque
from typing import Any, List
##############################################################
###                     Array/String                       ###
##############################################################

# 1. Two Sum[easy]
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Algo: hashmap-> key: nums[i], value:i
"""
def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dic:
            return [i, dic[diff]]
        dic[nums[i]] = i

# 217. Contains Duplicate[easy]
"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# 238. Product of Array Except Self
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
follow up
"""
def productExceptSelf(nums):
    ans = []

# 88. Merge Sorted Array (easy)
"""
Do not return anything, modify nums1 in-place instead.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
                    i     k                       j
Output: [1,2,2,3,5,6]
algo: 使用三个指针，两个指向两个数组有数部分的结尾，第三个指向第一个数组末尾，依次比较两个数组较小的数，放到第三个指针的位置
"""
def mergeArray(nums1, m, nums2, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k, i = k-1, i-1
        else:
            nums1[k] = nums2[j]
            k, j = k-1, j-1
    while j >= 0: # nums2 没有iterate完
        nums1[k] = nums2[j]
        k, j = k-1, j-1

# 27. Remove Element(Easy)
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Input: nums = [0,1,2,2,3,0,4,2], val = 2
                         i
                             j
Output: 5, nums = [0,1,4,0,3,_,_,_]
algo: two pointers. reader pointer j reads everything, writer pointer i writes selectively.
"""
def removeElement(nums, val): # -> return end index
    # two pointer, i is write pointer, j is read pointer
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

#Remove Duplicates from Sorted Array

#Remove Duplicates from Sorted Array II

#Majority Element

#Rotate Array

# 121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    cur_min = float('inf')
    ans = -float('inf')
    for p in prices:
        cur_min = min(cur_min, p)
        cur_profit = p - cur_min
        ans = max(ans, cur_profit)
    return ans

#Best Time to Buy and Sell Stock II

# 55. Jump Game
"""
"""
def canJump(nums):
    pass

#Jump Game II

#H-Index

#Insert Delete GetRandom O(1)

#Gas Station

#Candy

#Trapping Rain Water

#Roman to Integer

#Integer to Roman

# Length of Last Word
# 
# Longest Common Prefix
# 
# Reverse Words in a String
# 
# Zigzag Conversion
# 
# Find the Index of the First Occurrence in a String

# Text Justification


##############################################################
###                     Two pointers                       ###
##############################################################

# 125. Valid Palindrome[easy]
"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
"""
def validPalindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        if not s[i].isalnum() or s[i] == ' ':
            i += 1
            continue
        if not s[j].isalnum() or s[j] == ' ':
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
    return True

# 392. Is Subsequence[easy]
def isSubsequence(s, t):
    pt = -1
    for c in s:
        while pt < len(t) -1:
            pt += 1
            if c == t[pt]:
                break
        else:
            return False
    return True

# Two Sum II - Input Array Is Sorted
def twoSum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers)-1
    while i < j:
        #print(numbers[i], numbers[j])
        if numbers[i] + numbers[j] == target:
            return [i+1,j+1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
    return [i+1, j+1]

# Container With Most Water[easy]
def maxArea(height):
    res = 0
    i, j = 0, len(height)-1
    while i < j:
        res = max(res, min(height[i], height[j])*(j-i))
        if height[i] < height[j]:
            i += 1
        else:
            r -= 1
    return res

# 15. 3Sum[medium]
"""
Given an integer array nums, return all the deduped triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
nums = [-1,0,1,2,-1,-4]
output = [[-1,-1,2],[-1,0,1]]
"""
def threeSum(nums):
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, n-1
        while j < k:
            cur = nums[i] + nums[j] + nums[k]
            if cur > 0:
                k -= 1
            elif cur < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j+1 < k and nums[j+i] == nums[k]:
                    j += 1
                while k-1 > j and nums[k-1] == nums[k]:
                    k -= 1
                j += 1
                k -= 1
    return res
#print(threeSum(nums =[-1,0,1,2,-1,-4]))

##############################################################
###                     Sliding Window                     ###
##############################################################

# Minimum Size Subarray Sum

# Longest Substring Without Repeating Characters

# Substring with Concatenation of All Words

# Minimum Window Substring

##############################################################
###                          Matrix                        ###
##############################################################
# 36. Valid Sudoku[medium]
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
def validSudoku(board):
    def validRow():
        for row in board:
            if not isValid(row):
                return False
        return True

    def validCol(board):
        for col in zip(*board):
            if not isValid(col):
                return False
        return True
    
    def validBox(board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                if not isValid([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                    return False
        return True

    def isValid(unit):
        tmp = [i for i in unit if i != '.']
        return len(tmp) == len(set(tmp))

    return validBox(board) and validCol(board) and validBox(board)
#print(validSudoku(board))

# 54. Spiral Matrix[顺时针螺旋走位matrix]
def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        matrix = [*zip(*matrix)][::-1]
    return res

# 48. [重点]Rotate Image[medium]
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = [[7,4,1],[8,5,2],[9,6,3]]
"""
def rotate(matrix):
    matrix.reverse()
    #print(matrix)
    for i in range(len(matrix)):
        for j in range(i):
            print(i, j)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # tranpose the matrix
    print(matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#print(rotate(matrix))
#print(matrix)

# 73. Set Matrix Zeroes
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""
def setZeros(matrix):
    m, n = len(matrix),len(matrix[0])
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

# 289. [重点]Game of Life
def gameOfLife(board):
    pass

##############################################################
###                    Hashmap/Hashset                     ###
##############################################################

# Ransom Note

# Isomorphic Strings

# Word Pattern

# Valid Anagram

# Group Anagrams

# Two Sum

# Happy Number

# Contains Duplicate II

# Longest Consecutive Sequence

##############################################################
###                      Intervals                         ###
##############################################################

# 228.Summary Ranges[easy]
"""
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
"""
def summaryRanges(nums):
    l = len(nums)
    if l == 0:
        return []
    ans = []
    start = 0  # each interval start index
    nums.append(float('inf'))

    for i in range(l):
        if nums[i+1] != nums[i]+1: # this interval ends
            if start == i: # single num interval
                ans.append(str(nums[i]))
            else: # multi num interval
                ans.append("%s->%s", nums[start], nums[i])
            start = i+1
        else:
            continue
    return ans

# 56. Merge Intervals[medium]
"""
intervals = [[1,4],[2,3]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
"""
def mergeIntervals(intervals):
    intervals.sort()
    ans = [].append(intervals[0])
    for s, e in intervals:
        p_s, p_e = ans[-1]
        if p_e >= s:
            ans.pop()
            ans.append([p_s, max(e, p_e)])
        else:
            ans.append([s, e])
    return ans

# 57. [重点]Insert Interval[medium]
"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
case 1: intervals = [[1,3],[6,9]], newInterval = [4,5]
case 2: intervals = [[1,3],[6,9]], newInterval = [2,5]
case 3: intervals = [[2,3],[6,9]], newInterval = [0,1]
"""
def insertInterval(intervals, newInterval):
    n = len(intervals)
    i = 0
    ans = []
    # no overlapping, append current interval
    while i < n and intervals[i][1] < newInterval[0]:
        ans.append(intervals[i])
        i += 1
    # overlapping, merge and append
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])        
        i += 1
    ans.append(newInterval)
    # append the rest of intervals
    ans.extend(intervals[i:])
    return ans


# Minimum Number of Arrows to Burst Balloons


##############################################################
####                         Stack                        ####
##############################################################

# 20.Valid Parentheses[easy]
def validParenthese(s):
    pare = {']':'[', '}':'{', ')':'('}
    stack = []
    for c in s:
        if c in pare.values():
            stack.append(c)
        else:
            if not stack or stack.pop() != pare[c]:
                return False
    return stack == []

# Simplify Path



# 155.Min Stack[medium]
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

# Evaluate Reverse Polish Notation

# 224. Basic Calculator[hard]
"""
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
def calculator(s):
    stack = []

    return 
# 227. Basic Calculator II [medium]
"""
Input: s = "3+2*2"
Output: 7
Input: s = " 3+5 / 2 "
Output: 5
""" 
def calculator2(s):
    stack, cur, op = [], 0, '+'
    for c in s + '+':
        if c == " ":
            continue
        elif c.isdigit():
            cur = (cur * 10) + int(c)
        else:
            if op == '-':
                stack.append(-cur)
            elif op == '+':
                stack.append(cur)
            elif op == '*':
                stack.append(stack.pop() * cur)
            elif op == '/':
                stack.append(int(stack.pop() / cur))
            cur, op = 0, c
    return sum(stack)    
#print(calculator2(" 3+5 / 2 "))

def calculator2_optimize(s):
    # 常规：使用栈，遇到加减法，直接把数加到栈中，乘除法需要先进行计算，将计算的结果再加入栈中
    # 优化：使用last number，不使用stack
    cur_digit, operator = 0, '+'
    last_num, ans = 0, 0
    for c in s+'+':
        if c == " ":
            continue
        elif c.isdigit():
            cur_digit = cur_digit*10 + int(c)
        else:
            if operator == "+" or operator == "-":
                ans += last_num
                if operator == "+":
                    last_num = cur_digit
                else:
                    last_num = -cur_digit
                cur_digit = 0
            if operator == "/":
                last_num = int(last_num/cur_digit)
            if operator == "*":
                last_num *= cur_digit
            operator = c
            cur_digit = 0
    ans += last_num
    return ans

##############################################################
##                       Linked List                        ##
##############################################################

# Linked List Cycle

# Add Two Numbers

# Merge Two Sorted Lists

# Copy List with Random Pointer

# Reverse Linked List II

# Reverse Nodes in k-Group

# Remove Nth Node From End of List

# Remove Duplicates from Sorted List II

# Rotate List

# Partition List

# LRU Cache

##############################################################
##                  Binary Tree General                     ##
##############################################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Maximum Depth of Binary Tree
def maximumDepth(root:TreeNode):
    if not root:
        return 0
    return max(maximumDepth(root.left), maximumDepth(root.right))+1

def maximumDepth_interative_dfs(root:TreeNode):
    stack = [(root, 0)]
    ans = 0
    while stack:
        n, depth = stack.pop()
        if not n.left and not n.right:
            ans = max(ans, depth)
        if n.left:
            stack.append((n.left, depth+1))
        if n.right:
            stack.append((n.right, depth+1))
    return ans

# Same Tree
def sameTree(root1, root2):
    pass

# Invert Binary Tree

# Symmetric Tree

# Construct Binary Tree from Preorder and Inorder Traversal

# Construct Binary Tree from Inorder and Postorder Traversal

# Populating Next Right Pointers in Each Node II

# Flatten Binary Tree to Linked List

# Path Sum

# Sum Root to Leaf Numbers

# Binary Tree Maximum Path Sum

# Binary Search Tree Iterator

# Count Complete Tree Nodes

# Lowest Common Ancestor of a Binary Tree

##############################################################
###                 Binary Tree BFS                         ###
##############################################################
# Binary Tree Right Side View

# Average of Levels in Binary Tree

# Binary Tree Level Order Traversal

# Binary Tree Zigzag Level Order Traversal

##############################################################
##                  Binary Search Tree                      ##
##############################################################

# 530. Minimum Absolute Difference in BST
"""
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the values of any two different nodes in the tree.
"""
def getMinimumDifference(root):
    values = []
    def inOrder(node):
        if not node:
            return
        values.append(node.val)
        inOrder(node.left)
        inOrder(node.right)
    ans = float('inf')
    values.sort()
    for i in range(1, len(values)):
        ans = min(ans, values[i]-values[i-1])
    return ans
# 230. Kth Smallest Element in a BST
def kthSmallest(root, k):
    stack = []
    pass

# Validate Binary Search Tree

##############################################################
##                      Graph General                       ##
##############################################################
# 130. Surrounded Regions
def solve(board):
    pass
# Clone Graph

# Evaluate Division

# Course Schedule

# Course Schedule II

##############################################################
##                       Graph BFS                          ##
##############################################################
# 909. snakes and Ladders
def snakesAndLadders(self, board: List[List[int]]) -> int:
    def get_board_value(board, n, index):
        quot, rem = divmod(index - 1, n)
        row = n - 1 - quot
        col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
        return board[row][col]
        
    n = len(board)
    target = n * n
    visited = set()
    queue = deque([(1, 0)])  # (current square, number of moves)

    while queue:
        current, moves = queue.popleft()
        if current == target:
            return moves
        for i in range(1, 7):
            next_square = current + i
            if next_square <= target:
                value = get_board_value(board, n, next_square)
                if value != -1:
                    next_square = value
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
    return -1    

# Minimum Genetic Mutation


# 127. Word Ladder
"""
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
"""
def wordLadder(beginWord, endWord, wordList):
    # 典型bfs. 

    # initial check
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    
    # intermediate words dict
    wordList.append(beginWord)
    n = len(beginWord)
    all_comb_dict = defaultdict(list)

    for word in wordList:
        for i in range(n):
            genertic_word = word[:i] + '*' + word[i+1:]
            all_comb_dict[genertic_word].append(word)
    print(all_comb_dict)
    # BFS
    queue = deque()
    queue.append([beginWord, 1])
    visited = set(beginWord)

    while queue:
        cur_word, step = queue.popleft()

        for i in range(n):
            next_word = cur_word[:i] + '*' + cur_word[i+1:]
            for word in all_comb_dict[next_word]:
                if word == endWord:
                    return step + 1
                if word not in visited:
                    visited.add(word)
                    queue.append([word, step+1])
            all_comb_dict[next_word] = [] # optional
    return 0
#print(wordLadder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
#print(wordLadder("hit", "cog", ["hot","dot","dog","lot","log"]))

##############################################################
##                          Trie                            ##
##############################################################

# Implement Trie (Prefix Tree)
class Trie:
    def __init__(self) -> None:
        pass
# Design Add and Search Words Data Structure

# Word Search II

##############################################################
##                       Backtracking                       ##
##############################################################

# Letter Combinations of a Phone Number

# Combinations

# Permutations

# Combination Sum
# Solution
# Medium
# 
# N-Queens II

# Generate Parentheses

# Word Search

##############################################################
##                   Divide & Conquer                       ##
##############################################################

# Convert Sorted Array to Binary Search Tree

# Sort List

# Construct Quad Tree

# Merge k Sorted Lists

##############################################################
##                  Kadane's Algorithm                      ##
##############################################################

# Maximum Subarray

# Maximum Sum Circular Subarray

##############################################################
##                      Binary Search                       ##
##############################################################

# Search Insert Position

# Search a 2D Matrix

# Find Peak Element

# Search in Rotated Sorted Array

# Find First and Last Position of Element in Sorted Array

# Find Minimum in Rotated Sorted Array

# Median of Two Sorted Arrays

##############################################################
##                          Heap                            ##
##############################################################

# Kth Largest Element in an Array

# IPO

# Find K Pairs with Smallest Sums

# Find Median from Data Stream

##############################################################
##                    Bit Manipulation                      ##
##############################################################

# 67. Add Binary [easy]
"""
Given two binary strings a and b, return their sum as a binary string.
"""
def addBinary(a, b):
    res = ""
    i, j, carry = len(a) - 1, len(b) - 1, 0
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0 : 
            sum += int(a[i])
        if j >= 0 : 
            sum += int(b[j])
        i, j = i - 1, j - 1
        carry = 1 if sum > 1 else 0
        res += str(sum % 2)

    if carry != 0 : res += str(carry)
    return res[::-1]
assert addBinary("11", "1") == "100"

# 190. Reverse Bits [easy]
"""
Reverse bits of a given 32 bits unsigned integer.
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
"""
def reverseBits(n: int) -> int:
    res, power = 0, 31
    while n:
        res += (n & 1) << power
        n >>= 1
        power -= 1
    return res
# assert reverseBits(00000010100101000001111010011100) == 964176192

# 191. Number of 1 Bits [easy]
"""
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
"""
def hammingWeight(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res

# Single Number

# Single Number II

# Bitwise AND of Numbers Range

##############################################################
###                          Math                           ##
##############################################################

# Palindrome Number

# Plus One

# Factorial Trailing Zeroes

# Sqrt(x)

# Pow(x, n)

# Max Points on a Line

##############################################################
###                          1D DP                          ##
##############################################################

# 70. Climbing Stairs
def climbStairs(n):
    # dp[i] = dp[i-1]+dp[i-2]
    dp = [i for i in range(0, n)]
    if n <= 2:
        return n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]
#print(climbStairs(2))

# House Robber

# Word Break

# Coin Change

# Longest Increasing Subsequence

##############################################################
##                   Multidimensional DP                    ##
##############################################################

# Triangle

# Minimum Path Sum

# Unique Paths II

# Longest Palindromic Substring

# Interleaving String

# Edit Distance

# Best Time to Buy and Sell Stock III

# Best Time to Buy and Sell Stock IV

# Maximal Square