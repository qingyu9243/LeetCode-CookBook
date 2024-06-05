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
# 1732. Find the highest altitude [easy]
def largestAltitude(gain) -> int:
    max_altitude = 0
    cur_altitude = 0
    for g in gain:
        cur_altitude += g
        max_altitude = max(max_altitude, cur_altitude)

    return max_altitude

# 724. Find Pivot Index [easy]
"""
Find the index that the accumulated sum before index and after index are same.
"""
def pivotIndex(nums) -> int:
    s = sum(nums)
    pre_sum = 0
    for i, n in enumerate(nums):
        if pre_sum == (s-n)/2:
            return i
        pre_sum += n
    return -1

### Hashmap/Hashset ###


### Stack & Queue ###
# 【栈经典题】735. Asteroid Collision
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

# 【栈经典题】394. Decode String
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
    stack = []
    cur_num = cur_str = ""
    for c in s:
        if c == "[":
            stack.append(cur_str)
            stack.append(int(cur_num))
            cur_num = cur_str = ""
        elif c == "]":
            num = stack.pop()
            pre_str = stack.pop()
            cur_str = pre_str + num*cur_str
        elif c.isdigit():
            cur_num += c
        else:
            cur_str += c
    return cur_str

### Linked List ###

### Binary Tree - DFS & BFS ###
# 104. Max Depth of Binary Tree
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(root:TreeNode):
    if not root:
        return 0
    else:
        left_h = maxDepth(root.left)
        right_h = maxDepth(root.right)
        return max(left_h, right_h)+1
    
def maxDepth_iter(root:TreeNode):
    stack = []
    if root is not None:
        stack.append((1, root))

    depth = 0
    while stack != []:
        current_depth, root = stack.pop()
        if root is not None:
            depth = max(depth, current_depth)
            stack.append((current_depth + 1, root.left))
            stack.append((current_depth + 1, root.right))

    return depth

# 100. Same Tree
def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

# 872. Leaf-Similar Trees
def leafSimilar(root1, root2):
    def dfs(root, leaf):
        if not root:
            return
        if not root.left and not root.right:
            leaf.append(root.val)
        dfs(root.left, leaf)
        dfs(root.right, leaf)

    leaf1 = []
    leaf2 = []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2

# 1448. Count good nodes in binary tree
def goodNodes(root):
    def dfs(root, max_val):
        res = int(root.val >= max_val)
        if root.left:
            dfs(root.left, max(max_val,root.val))
        if root.right:
            dfs(root.right, max(max_val, root.val))
        return res

    return dfs(root, float('-inf'))

# 199. Binary Tree Right Side View (BFS)
"""
BFS, level order traversal
"""
from collections import deque
def rightSideView(root):
    if not root:
        return []
    q = deque()
    q.append([root]) # append list of the nodes in this level
    ans = []
    while q:
        l_nodes = q.popleft()
        ans.append(l_nodes[-1].val)
        l = []
        for n in l_nodes:
            if n.left:
                l.append(n.left)
            if n.right:
                l.append(n.right)
        if len(l) > 0:
            q.append(l)
    return ans

# 1161. Max level sum of a Binary Tree (BFS)
def maxLevelSum(root):
    if not root:
        return 0
    q = deque()
    q.append(root)
    max_sum_level = 0
    cur_level = 0
    max_sum = float('-inf')
    while q:
        cur_level += 1
        cur_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            cur_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if cur_sum > max_sum:
            max_sum_level = cur_level
            max_sum = cur_sum
    return max_sum_level

### Binary Search Tree ###

### Heap(Priority Queue) ###

### Binary Search Tree ###
# 700. Search in BST
def searchBST(root, val):
    if not root:
        return
    if root.val == val:
        return root
    elif root.val < val:
        return searchBST(root.right, val)
    elif root.val > val:
        return searchBST(root.left, val)    

# [重点题]450. Delete Node in BST
def deleteNode(root, key):
    pass
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