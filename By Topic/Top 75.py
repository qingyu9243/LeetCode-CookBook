### Array/String ###
# 1768. Merge Strings Alternatively - Easy
def mergeAlternately(self, word1: str, word2: str) -> str:
    l1, l2 = len(word1), len(word2)
    i = j = 0
    res = ""
    while i < l1 and j < l2:
        res += word1[i] + word2[j]
        i += 1
        j += 1
    if i < l1:
        res += word1[i:]
    if j < l2:
        res += word2[i:]
    return res

# [怪题]1071. Greatest Common Divisor of Strings
"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
import math
def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]

# 
### Two pointers ###
# 283. Move Zeros
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
def moveZeros(nums):
    l, r, n = 0, 0, len(nums)
    while r < n:
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
        r += 1
    while l < n:
        nums[l] = 0
        l += 1

# 392. Is Subsequence 
"""
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Follow up:
If there are lots of incoming S, say S1, S2, … , Sk where k >= 1B, 
and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?
"""
from collections import defaultdict
import bisect
def isSubsequence(s, t):
    dic = defaultdict(list)
    for i, c in enumerate(t):
        dic[c].append(i)

    cur = -1
    for c in s:
        if c not in dic:
            return False
        l = dic[c]
        p = bisect.bisect_left(l, cur)

        if p == len(l):
            return False
        cur = l[p]+1
    return True    

# 11. Container with Most Water
def maxArea(height) -> int:
    res = 0
    l, r = 0, len(height)-1
    while l < r:
        res = max(res, min(height[r], height[l]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


### Sliding Window ###
# 643. Maximum Average Subarray I
"""
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""
def findMaxAverage(nums, k) -> float:
    moving_sum = 0
    for i in range(k):
        moving_sum += nums[i]
    res = moving_sum  
    for i in range(k, len(nums)):
        moving_sum += nums[i]-nums[i-k]
        res = max(res, moving_sum)
    return res/k

### Prefix Sum ###


### Hashmap/Hashset ###


### Stack & Queue ###
# 735. Asteroid Collision
"""行星碰撞
Input: asteroids = [5,10,-5]
Output: [5,10]
Input: asteroids = [-2,-2,1,-2]
Output: [-2, -2, -2]
# + + -> append
# - - -> append
# - + -> append
# + - -> collision
#    big   -small -> while loop,not append
#    same  same -> while loop, pop 
#    small -big -> while loop, pop and need to continue to check left side
"""
def asteroidsCollision(asteroids):
    stack = []
    for star in asteroids:
        if not stack or star > 0 or stack[-1] < 0:
            stack.append(star)
            continue
        while stack and stack[-1] > 0:
            if stack[-1] > abs(star):
                break
            x = stack.pop()
            if x + star == 0:
                break
            # 隐含condition：stack[-1] < abs(star),需要继续pop看左边的stars
        else: # ???
            stack.append(star)
    return stack

# 394. Decode String
"""
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
def decodeString(s):

### Linked List ###

### Binary Tree - DFS & BFS ###


### Binary Search Tree ###

### Heap(Priority Queue) ###

### Binary Search ###

### Backtrack ###

### Dynamic Programming ###

### Bit Manipulation ###

### Trie ###
"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""
# 208. Implement Trie(Prefix Tree) -> trie.py
# 1268. Search Suggestions System -> trie.py

### Intervals ###



### Monotonic ###