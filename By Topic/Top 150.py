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

# 26. Remove Duplicates from Sorted Array[easy]
"""
two pointers: insert_index as index to replace value, j is the moving index
Java:
public int removeDuplicates(int[] nums) {
    int insert = 1;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j-1] != nums[j]) {// swap
            nums[insert] = nums[j];
            insert ++;
        }
    }
    return insert;
"""
def removeDuplicates(nums):
    insert = 1
    # [0,1,2,3,1,2,2,3,3,4]
    #    i
    #    j
    for j in range(1, len(nums)):
        if nums[j-1] != nums[j]:
            nums[insert] = nums[j]
            insert += 1
    return insert

# 80. Remove Duplicates from Sorted Array II
"""
allow at most twice for each num. in-place modify
[1,1,2,2,3,3]
           i
           j
"""
def removeDuplicates2(nums):
    insert = 1
    pass

# 169. Majority Element[easy]
"""
Boyer-Moore Voting Algorithm
"""
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
assert majorityElement([2,2,1,1,1,2,2]) == 2

# Rotate Array

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

# Longest Common Prefix

# Reverse Words in a String

# Zigzag Conversion

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
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
def minSubArray(target, nums):
    pass

# 3. Longest Substring Without Repeating Characters
def longestSubtringWithoutRepeatChar(s):
    max_length = 0
    left = 0
    cur_str = set()

    for right in range(len(s)):
        while s[right] in cur_str:
            left += 1
            cur_str.remove(s[left])
        cur_str.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
#print(longestSubtringWithoutRepeatChar("bbbbb"))
#print(longestSubtringWithoutRepeatChar("abcabcbb"))

# Substring with Concatenation of All Words


# Minimum Window Substring
from collections import Counter
def minWindow(self, s, t):
    # Create hashmaps to keep track of counts of characters in t and in the current window
    need = Counter(t)
    window = {}

    # Initialize two pointers for the sliding window
    left, right = 0, 0
    # Initialize variables for tracking the number of valid characters and the minimum window length
    valid = 0
    min_length = float('inf')
    start = 0

    # Expand the window to the right
    while right < len(s):
        # Get the character at the right pointer
        char = s[right]
        right += 1
        
        # Update the window hashmap
        if char in need:
            window[char] = window.get(char, 0) + 1
            # Check if we have the correct count for this character
            if window[char] == need[char]:
                valid += 1
        
        # Check if the current window is valid
        while valid == len(need):
            # Update the minimum window if necessary
            if right - left < min_length:
                min_length = right - left
                start = left
            
            # Prepare to contract the window by moving the left pointer
            char = s[left]
            left += 1
            
            # Update the window hashmap
            if char in need:
                if window[char] == need[char]:
                    valid -= 1
                window[char] -= 1

    # Return the minimum window substring found, or an empty string if no valid window was found
    return "" if min_length == float('inf') else s[start:start + min_length]

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

# 383. Ransom Note [easy]
def canConstruct(ransomNote: str, magazine: str) -> bool:
    cnt1 = Counter(ransomNote)
    cnt2 = Counter(magazine)
    print(cnt1, cnt2)
    for k in cnt1.keys():
        if k not in cnt2.keys():
            return False
        elif k in cnt2.keys() and cnt1[k] > cnt2[k]:
            return False
    return True

# 205. Isomorphic Strings [easy]
def isIsomorphic(s: str, t: str) -> bool:
    dic_s, dic_t = defaultdict(list), defaultdict(list)
    for i, char in enumerate(s):
        dic_s[char].append(i)
    for i, char in enumerate(t):
        dic_t[char].append(i)  

    count = 0
    if len(dic_s) != len(dic_t):
        return False
    for k, v in dic_s.items():
        if v in dic_t.values():
            count += 1
    return len(dic_s) == count

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

# 71. Simplify Path [medium]
"""Java
import java.util.*;

class Solution {
    public String simplifyPath(String path) {
        // Initialize a stack to use as a list for the simplified path parts
        LinkedList<String> res = new LinkedList<>();
        
        // Split the path by "/" and process each part
        String[] splited = path.split("/");
        
        // Iterate over each part of the path
        for (String e : splited) {
            // If the part is "." or empty, we skip it
            if (e.equals(".") || e.isEmpty()) {
                continue;
            } 
            // If the part is "..", pop the last valid part from the list (if any)
            else if (e.equals("..")) {
                if (!res.isEmpty()) {
                    res.removeLast();
                }
            } 
            // Otherwise, it's a valid directory name, so add it to the list
            else {
                res.add(e);
            }
        }
        
        // Construct the simplified path from the list
        return "/" + String.join("/", res);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String path = "/a/./b/../../c/";
        System.out.println(sol.simplifyPath(path));  // Output: "/c"
        
        path = "/../";
        System.out.println(sol.simplifyPath(path));  // Output: "/"
        
        path = "/home//foo/";
        System.out.println(sol.simplifyPath(path));  // Output: "/home/foo"
    }
}
"""
def simplifyPath(path):
    res = []
    splited = path.rstrip('/').split('/')
    for e in splited:
        if e == '.' or e == '':
            continue
        elif e == '..':
            if len(res) > 0:
                res.pop()
        else:
            res.append(e)
    return '/'+ '/'.join(res)
#print(simplifyPath("/home/user/Documents/../Pictures"))

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

# 150. Evaluate Reverse Polish Notation [medium]

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

# 104. Maximum Depth of Binary Tree
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

# 100. Same Tree [easy]
def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    return root1.val == root2.val \
        and sameTree(root1.left, root2.left) \
        and sameTree(root1.right, root2.right)

# 226. Invert Binary Tree
def invertTree(root):
    return

# 101. Symmetric Tree [easy]
"""
典型recursive
"""
def isSymmetric(node):
    def isMirror(n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
        elif n1.val != n2.val:
            return False
        return n1.val == n2.val and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
    isMirror(node.left, node.right)

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


# 433. Minimum Genetic Mutation [medium]
"""Java
import java.util.*;

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        // Use a queue to perform BFS
        Queue<Pair<String, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(startGene, 0));
        Set<String> visited = new HashSet<>();
        
        // Convert the bank to a set for faster lookups
        Set<String> bankSet = new HashSet<>(Arrays.asList(bank));

        while (!queue.isEmpty()) {
            Pair<String, Integer> current = queue.poll();
            String cur = current.getKey();
            int step = current.getValue();
            
            // Check if the current gene is the end gene
            if (cur.equals(endGene)) {
                return step;
            }
            
            // Try all possible mutations
            for (int i = 0; i < cur.length(); i++) {
                for (char c : new char[]{'A', 'C', 'G', 'T'}) {
                    // Generate the next mutation by changing one character at a time
                    String nextCur = cur.substring(0, i) + c + cur.substring(i + 1);
                    
                    // If the next mutation is in the bank and hasn't been visited
                    if (bankSet.contains(nextCur) && !visited.contains(nextCur)) {
                        queue.offer(new Pair<>(nextCur, step + 1));
                        visited.add(nextCur);
                    }
                }
            }
        }
        
        // If no mutation path leads to the endGene, return -1
        return -1;
    }

    // Helper class to store a pair of String and Integer
    static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String startGene = "AACCGGTT";
        String endGene = "AACCGGTA";
        String[] bank = {"AACCGGTA"};
        System.out.println(sol.minMutation(startGene, endGene, bank)); // Output: 1
    }
}
"""
def minMutation(startGene: str, endGene: str, bank: List[str]):
    # bfs to get min mutations
    queue = deque()
    queue.append((startGene, 0))
    visited = set()
    while queue:
        cur, step = queue.pop()
        # check mutation in bank
        if cur == endGene:
            return step
        for char in "ACGT":
            for i in range(len(endGene)):
                next_cur = cur[:i]+char+cur[i+1:]
                if next_cur in bank and next_cur not in visited:
                    queue.append((next_cur, step+1))
                    visited.add(next_cur)
    return -1


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

# 208. Implement Trie (Prefix Tree) [medium]
class Trie:
    def __init__(self) -> None:
        self.dic = {}

    def insert(self, word):
        cur = self.dic
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = True
        
    def search(self, word):
        cur = self.dic
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return "#" in cur

    def startWith(self, prefix):
        cur = self.dic
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
    
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startWith("app") == True
trie.insert("app")
assert trie.search("app") == True


# 211. Design Add and Search Words Data Structure[medium]
"""
word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")
assert word_dict.search("pad") == False
assert word_dict.search("bad") == True
assert word_dict.search(".ad") == True
assert word_dict.search("b..") == True
"""
class WordDictionary:
    def __init__(self):
        self.dic = {}

    def addWord(self, word):
        cur = self.dic
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur["#"] = True

    """
    Returns true if there is any string in the data structure that matches word or false otherwise. 
    word may contain dots '.' where dots can be matched with any letter.
    """
    def search(self, word):
        return self.dfs(self.dic, word, 0)
    
    def dfs(self, node, word, i):
        if i == len(word):
            return "#" in node
        if word[i] == '.':
            for child in node:
                if child != "#" and self.dfs(node[child], word, i+1):
                    return True
            return False
        if word[i] not in node:
            return False
        return self.dfs(node[word[i]], word, i+1)
    

# 212. Word Search II [hard][重点]
def findWords(board, words):
    # construct trie for words. Using dfs to find matching word in the board
    def dfs(x, y, root):
        letter = board[x][y]
        cur = root[letter]
        word = cur.pop("#", False)
        if word:
            res.append(word)
        board[x][y] = '*'
        for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            curx, cury = x + dirx, y + diry
            if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                dfs(curx, cury, cur)
        board[x][y] = letter
        if not cur:
            root.pop(letter)

    trie = {} # only need insert func
    for word in words:
        cur = trie
        for w in word:
            cur = cur.setdefault(w, {}) # set key -> value if key doesn't exist.
            #print(cur)
        cur["#"] = word
    

    m, n = len(board), len(board[0])
    res = []
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie:
                dfs(i, j, trie)

    return res

#print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
#print(findWords([["a","b"],["c","d"]], ["abcb"]))

##############################################################
##                       Backtracking                       ##
##############################################################

# LC 17. Letter Combinations of a Phone Number
def lettersComb(digits):
    digit_map = {'2':'abc', '3':'def', '4':'ghi', 
        '5':'jkl', '6':'mno', '7':'pqrs',
        '8':'tuv', '9':'wxyz'}
    def backtrack(cur_path, index):
        if len(cur_path) == len(digits):
            ans.append(cur_path)
            return
        cur_digit = digits[index]
        for char in digit_map[cur_digit]:
            backtrack(cur_path+char, index+1)
    ans = []
    backtrack("", 0)
    return ans
#print(lettersComb("23"))

# LC 77. Combinations
def combine(n, k):
    def backtrack(cur_comb, start):
        if len(cur_comb) == k:
            ans.append(cur_comb.copy())
            return
        for i in range(start, n + 1):
            cur_comb.append(i)
            backtrack(cur_comb, i+1)
            cur_comb.pop() # critial point, remove this possible number and try other possible numbers
    ans = []
    backtrack([], 1)
    return ans
#print(combine(4, 2))

# LC 46. Permutations
def permute(nums):
    l = len(nums)
    def backtrack(cur_nums, used):
        print("entry")
        print(cur_nums)
        if len(cur_nums) == l:
            ans.append(cur_nums.copy())
            return
        for i in range(l):
            print("check---")
            print(used)
            if not used[i]:
                cur_nums.append(nums[i])
                used[i] = True
                print(cur_nums)
                print(used)
                print('above is new')
                backtrack(cur_nums, used)
                used[i] = False
                cur_nums.pop()
    ans = []
    backtrack([], [False]*l)
    return ans
#print(permute([1, 2, 3]))

# Combination Sum

# N-Queens II
def nQueensI(n): # return all the possible 
    def canPlace(i, j):
        if j in cols or (i-j) in diag1 or (i+j) in diag2:
            return False
        return True
    
    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                board.append("".join(row_board[r]))
            ans.append(board)
            return
        
        for col in range(n):
            if canPlace(row, col):
                row_board[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row+1)

                row_board[row][col] = "."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

    ans = []
    cols, diag1, diag2 = set(), set(), set()
    row_board = [['.']*n for _ in range(n)]
    backtrack(0)
    return ans
#print(nQueensI(4))

def nQueensII(n): # return the number of possible ways
    def canPlace(i, j):
        if j in cols or (i-j) in diag1 or (i+j) in diag2:
            return False
        return True

    def backtrack(row):
        if row == n:
            ans[0] += 1
            return
        for col in range(n):
            if canPlace(row, col):
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
            
                backtrack(row+1)

                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

    ans = [0]
    cols, diag1, diag2 = set(), set(), set()
    backtrack(0)
    return ans[0]
print(nQueensII(4))    

# LC 22. Generate Parentheses. given n pairs of (), generate all possible well-formed paratheses.
def generateParenthese(n):
    def backtrack(cur_path, l, r):
        if len(cur_path) == 2*n:
            ans.append(cur_path)
            return
        # given a cur_path with l and r count, add l first.
        if l < n:
            backtrack(cur_path + "(", l+1, r)
        if l > r:
            backtrack(cur_path + ")", l, r+1)
    ans = []
    backtrack("", 0, 0)
    return ans
#print(generateParenthese(3))

# LC 79. Word Search - search a word in letter grid
def wordSearch(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def backtrack(r, c, i): # return True/False
        if i == len(word):
            return True
        if 0 > r or r >= rows or 0 > c  or c >= cols or grid[r][c] != word[i]:
            return False
        temp = grid[r][c]
        grid[r][c] = "#"
        for dx, dy in directions:
            if backtrack(r+dx, c+dy, i+1):
                return True
        grid[r][c] = temp
        return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                if backtrack(i, j, 0):
                    return True
    return False
#print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
#print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

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
"""
Binary Search Template

Template 1: Classic Binary Search
This template is used when you want to find the exact position of an element in a sorted array.
"""
def binary_search_classic(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid  # Return the index of the found target
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
            
    return -1  # Target not found
"""
Template 2: Binary Search for Lower Bound (First Occurrence)
This template finds the first occurrence (lower bound) of the target in a sorted array.
"""
def binary_search_lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Continue searching in the left half
    
    if left < len(nums) and nums[left] == target:
        return left  # Return the first occurrence index
    return -1  # Target not found
"""
Template 3: Binary Search for Upper Bound (Last Occurrence)
This template finds the last occurrence (upper bound) of the target in a sorted array.
"""
def binary_search_upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] <= target:
            left = mid + 1  # Continue searching in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    if right >= 0 and nums[right] == target:
        return right  # Return the last occurrence index
    return -1  # Target not found

"""
Template 4: Binary Search for a Condition
This template is used when the search is not for a specific element but for the first element that satisfies a certain condition. 
This is common in problems where you're asked to find the minimum or maximum value that satisfies a condition.
"""
def binary_search_condition(nums, condition):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if condition(nums[mid]):
            right = mid  # Continue searching in the left half
        else:
            left = mid + 1  # Continue searching in the right half
            
    return left if condition(nums[left]) else -1  # Return the index of the first element that satisfies the condition


import bisect
# 35. Search Insert Position
def searchInsert(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l
    #return bisect.bisect_left(nums, target)

assert searchInsert([1,3,5,6], 5) == 2
assert searchInsert([1,3,5,6], 2) == 1
assert searchInsert([1,3,5,6], 7) == 4

# 74. Search a 2D Matrix
def search2DMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    if n == 0:
        return False
    if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
        return False
    tmp = []
    for i in range(m):
        tmp.append(matrix[i][0])
    ind = bisect.bisect_left(tmp, target)
    if ind == len(tmp):
        ind = ind - 1
    if target < matrix[ind][0]:
        ind = ind - 1
    ind2 = bisect.bisect_left(matrix[ind], target)
    if ind2 == n:
        return False
    return matrix[ind][ind2] == target
assert search2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert search2DMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False

# 162. Find Peak Element [medium]
def findPeakElement(nums: List[int]) -> int:
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r-l)//2
        l_neighbor = nums[mid-1] if mid-1 >= 0 else float('-inf')
        r_neighbor = nums[mid+1] if mid+1 < len(nums) else float('-inf')
        # find the peak
        if l_neighbor < nums[mid] > r_neighbor:
            return mid
        # check right neighbor
        elif r_neighbor > nums[mid]:
            l = mid + 1
        # check left neighbor
        elif l_neighbor > nums[mid]:
            r = mid
assert findPeakElement([1,2,3,1]) == 2
assert findPeakElement([1,2,1,3,5,6,4]) == 5

# 33. Search in Rotated Sorted Array[medium]
def findMin(nums):
    i, j = 0, len(nums)-1
    while i < j:
        mid = (i+j)//2
        if nums[mid] <= nums[j]:
            j = mid
        else:
            i = mid + 1
    return nums[i]

### 34. Find First and Last Position of Element in Sorted Array[medium]
def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums)-1
    res = [-1, -1]
    
    # first binary search to find lower bound
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    if l < len(nums) and nums[l] == target:
        res[0] = l

    # second binary search to find upper bound
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    if r >= 0 and nums[r] == target:
        res[1] = r

    return res
assert searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert searchRange([], 0) == [-1,-1]
assert searchRange([1], 1) == [0,0]

# 153. Find Minimum in Rotated Sorted Array[medium]
def findMin(nums):
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] <= nums[r]:
            r = mid
        else:
            l = mid + 1
    return nums[l]
assert findMin([3,4,5,1,2]) == 1
assert findMin([4,5,6,7,0,1,2]) == 0
assert findMin([11,13,15,17]) == 11
assert findMin([3,1,2]) == 1

# 4. Median of Two Sorted Arrays[hard]
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minX = float('inf') if partitionX == m else nums1[partitionX]
        minY = float('inf') if partitionY == n else nums2[partitionY]
        
        if maxX <= minY and maxY <= minX:
            if (m + n) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1
assert findMedianSortedArrays([1,3], [2]) == 2
assert findMedianSortedArrays([1,2], [3, 4]) == 2.5

##############################################################
##                          Heap                            ##
##############################################################
import heapq
# 215. Kth Largest Element in an Array[medium]
def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# 502. IPO[hard]
def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    pass

# 373. Find K Pairs with Smallest Sums[medium]
def kSamllestPairs(nums1, nums2, k):
    pass

# 295. Find Median from Data Stream[hard]
class MedianFinder:
    def __init__(self) -> None:
        pass
    def addNum(self, num):
        pass
    def findMedium(self):
        pass

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

# LC.198 House Robber
def robHouse(nums):
    # dp[i] represents the until ith house, max amount I can rob
    # dp[i] = max((dp[i-2] + nums[i]), dp[i-1]
    l = len(nums)
    if l == 1:
        return nums[0]
    if l == 2:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])
    for i in range(2, l):
        dp[i] = max((dp[i-2]+nums[i]), dp[i-1])
    return dp[-1]

# LC. 139 Word Break, s = "leetcode", wordDict = ["leet","code"]
def wordBreak(s, wordDict):
    # dp[i] = has existing word & dp[i - len(word]
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for word in wordDict:
            l = len(word)
            lookup = s[i-l:i]
            if lookup == word and dp[i-l]:
                dp[i] = True
                break
    return dp[-1]
#print(wordBreak("leetcode", ["leet","code"]))

# LC. 140. Word Break II, return all comb word breaks
def wordBreak2(s, wordDict):
    word_set = set(wordDict)
    memo = {}
    def backtrack(i):
        if i == len(s):
            return [""]
        if i in memo:
            return memo[i]
        res = []
        for j in range(i, len(s)):
            prefix = s[i:j+1]
            if prefix in word_set:
                tmp = backtrack(j+1)
                for words in tmp:
                    res.append((prefix + " " + words).strip())
        memo[i] = res
        return res
    return backtrack(0)
#print(wordBreak2("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))

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