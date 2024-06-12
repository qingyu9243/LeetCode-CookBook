from collections import defaultdict
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

#Best Time to Buy and Sell Stock

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
# 
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


# 125. Valid Palindrome
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

# 392. Is Subsequence
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

# Container With Most Water

# 3Sum

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


# Valid Sudoku

# Spiral Matrix

# Rotate Image

# Set Matrix Zeroes

# Game of Life

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

# Summary Ranges

# Merge Intervals

# Insert Interval

# Minimum Number of Arrows to Burst Balloons

##############################################################
####                         Stack                        ####
##############################################################

# Valid Parentheses

# Simplify Path

# Min Stack

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
print(calculator2(" 3+5 / 2 "))

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

# Maximum Depth of Binary Tree

# Same Tree

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

# Minimum Absolute Difference in BST

# Kth Smallest Element in a BST

# Validate Binary Search Tree

##############################################################
##                      Graph General                       ##
##############################################################

# Number of Islands

# Surrounded Regions

# Clone Graph

# Evaluate Division

# Course Schedule

# Course Schedule II

##############################################################
##                       Graph BFS                          ##
##############################################################
# Graph BFS

# Minimum Genetic Mutation

# Word Ladder

##############################################################
##                          Trie                            ##
##############################################################

# Implement Trie (Prefix Tree)

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

# Add Binary

# Reverse Bits

# Number of 1 Bits

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

# Climbing Stairs

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