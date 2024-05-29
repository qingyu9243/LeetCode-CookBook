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