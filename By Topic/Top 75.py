from typing import List
##############################################################
###                     Array/String                       ###
##############################################################
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

##############################################################
###                     Two pointers                       ###
##############################################################
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

##############################################################
###                     Sliding Window                     ###
##############################################################
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

##############################################################
###                       Prefix Sum                       ###
##############################################################
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

##############################################################
###                    Hashmap/Hashset                     ###
##############################################################
# 1657. Determine if two strings are close
""" 
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
"""
from collections import Counter
def closeStrings(word1, word2):
    c1 = Counter(word1)
    c2 = Counter(word2)
    #print(c1.values(), c2.values())
    if sorted(c1.keys()) != sorted(c2.keys()):
        return False
    elif sorted(c1.values()) != sorted(c2.values()):
        return False
    return True

# [重点]2352. Equal Row and Column Pairs
"""
count the total num of pairs that col == row.
"""
def equalPairs(grid):
    cnt = 0
    n = len(grid)
    row_cnt = Counter(tuple(row) for row in grid)

    for c in range(n):
        col = [grid[i][c] for i in range(n)]
        cnt += row_cnt[tuple(col)]
    return cnt

##############################################################
###                    Stack & Queue                       ###
##############################################################
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
#print(asteroidsCollision([-2,-2,1,-2]))

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

##############################################################
###                     Linked List                        ###
##############################################################

##############################################################
###                Binary Tree - DFS & BFS                 ###
##############################################################
#### 104. Max Depth of Binary Tree ####
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

#### 100. Same Tree ####
def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

#### 872. Leaf-Similar Trees(DFS) ####
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

#### 1448. Count good nodes in binary tree(DFS) ####
def goodNodes(root):
    def dfs(root, max_val):
        res = int(root.val >= max_val)
        if root.left:
            dfs(root.left, max(max_val,root.val))
        if root.right:
            dfs(root.right, max(max_val, root.val))
        return res

    return dfs(root, float('-inf'))

#### [重点] 112. Path Sum III [dfs+backtrack] ####
def pathSumIII(root, targetSum):
    if not root:
        return 0
    def dfs(node, cur_path):
        if not node:
            return 0
        cur_path.append(node)
        path_cnt, path_sum = 0, 0
        for i in range(len(cur_path)-1, -1, -1):
            path_sum += cur_path[i]
            if path_sum == targetSum:
                path_cnt += 1
        path_cnt += dfs(node.left, cur_path)
        path_cnt += dfs(node.right, cur_path)    
        cur_path.pop()
        return path_cnt
    dfs(root, [])  

#### [重点] 1372. Longest ZigZag Path in Binary Tree (DFS) ####
def longestZigZag(root):
    max_length = 0

    def dfs(node, is_left, length):
        if not node:
            return
        max_length = max(max_length, length)
        if is_left:
            dfs(node.left, False, length+1)
            dfs(node.right, True, 1)
        else:
            dfs(node.right, True, length+1)
            dfs(node.left, False, 1)

    dfs(root, True, 0)
    dfs(root, False, 0)
    return max_length


#### 199. Binary Tree Right Side View (BFS) ####
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

##############################################################
###                  Binary Search Tree                    ###
##############################################################
#### 700. Search in BST ####
def searchBST(root, val):
    if not root:
        return
    if root.val == val:
        return root
    elif root.val < val:
        return searchBST(root.right, val)
    elif root.val > val:
        return searchBST(root.left, val)    

#### [重点题]450. Delete Node in BST ####
def deleteNode(root, key):
    pass

##############################################################
###                  Graphs - DFS & BFS                    ###
##############################################################
#### 841. Keys and Rooms
def canVisitAllRooms(rooms):
    visited_rooms = set([0])
    stack = [0]
    while stack:
        cur = stack.pop()
        for key in rooms[cur]:
            if key not in visited_rooms:
                stack.append(key)
                visited_rooms.add(key)
    return len(visited_rooms) == len(rooms)

#### 547. Number of Provinces
def findCircleNum(isConnected: List[List[int]]):
    n = len(isConnected)
    provinces = 0
    visited = [False]*n
    def dfs(city, visited):
        for j in range(n):
            if isConnected[city][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j, visited)
    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            provinces += 1
    return provinces    

#### [重点]994. Rotting Oranges [BFS]
"""
BFS. use queue to store all rotten oranges at first，edge case：2个烂橘子同时出发开始烂。
"""
def orangeRotting(grid):
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for i in range(m):
        for j in range(n):
            # append all rotten oranges
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            # count fresh oranges
            elif grid[i][j] == 1:
                fresh += 1
    max_time = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y, time = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx <m and 0 <= ny <n and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                fresh -= 1
                queue.append((nx, ny, time+1))
                max_time = max(max_time, time+1)
    return max_time if fresh == 0 else -1

#### 1926. Nearest Exit from Entrance in Maze [BFS]
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append((entrance[0], entrance[1], 0))
    maze[entrance[0]][entrance[1]] = "+"

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny <n and maze[nx][ny] == ".":
                if nx == 0 or nx == m-1 or ny == 0 or ny == n-1:
                    return steps + 1
                queue.append((nx, ny, steps+1))
                maze[nx][ny] = '+'
    return -1

##############################################################
###                 Heap(Priority Queue)                   ###
##############################################################
import heapq
from operator import itemgetter
from heapq import heappush, heappop
#### [重点]215. Kth Largest Element in an Array
"""
get the Kth largest element in a unsorted array without using Sort.
"""
def findKthLargest(nums, k):
    min_heap = []
    for n in nums:
        heapq.heappush(min_heap, n)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

#### 2336. Smallest Number in Infinite Set
"""
维护一个堆，存加入符合条件的数，并在一个set中存入同样的数，用来判断是否已经存在，
如果堆里有元素，就pop堆里最小的
"""
class SmallestInfiniteSet:
    def __init__(self):
        pass
    def popSmallest(self):
        pass
    def addBack(self):
        pass

#### [重点]2542. Maximum Subsequence Score [Medium - Hard]
def maxScore(nums1, nums2, k):
    res, prefixSum, minHeap = 0, 0, []
    for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), resverse=True):
        prefixSum += a
        heappush(minHeap, a)
        if len(minHeap) == k:
            res = max(res, prefixSum*b)
            prefixSum -= heappop(minHeap)
    return res

##############################################################
###                    Binary Search                       ###
##############################################################
# 374. Guess Number higher or lower
def guess(n):
    pass
def guessNumber(n: int) -> int:
    l, r = 1, n
    while l <= r:
        mid = (l+r)//2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == -1:
            r = mid -1
        else:
            l = mid + 1
    return -1

# 2300. Successful Pairs of Spells and Potions
def successfulPairs(spells, potions, success):
    ans = []
    m = len(potions)
    potions.sort()
    for s in spells:
        i = bisect.bisect_left(potions, math.ceil(success/s))
        ans.append(m-i)
    return ans    

# 162. [重点] Find Peak Element
"""
Input: nums = [1,2,3,4,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
def findPeak(nums):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        l_neighbor = nums[m-1] if m-1 >=0 else float('-inf')
        r_neighbor = nums[m+1] if m+1 < len(nums) else float('-inf')
        if l_neighbor < nums[m] > r_neighbor:
            return m
        elif l_neighbor > nums[m]:
            r = m
        elif r_neighbor > nums[m]:
            l = m+1

# 875. Koko Eating Bananas
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    def eatingHours(k):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        return hours
    while l < r:
        mid = (l+r)//2
        if eatingHours(mid) <= h:
            r = mid
        else:
            l = mid+1
    return r
#print(minEatingSpeed([30,11,23,4,20], 5))

##############################################################
###                      Backtrack                         ###
##############################################################
# 17.[重点]Letter of Combinations of a Phone number
"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
def letterCombinations(digits):
    ans = []
    dic = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl",
        "6": "mno", "7": "qprs", "8":"tuv", "9": "wxyz"}
    def backtrack(cur_digit, cur_str):
        if cur_digit == len(digits):
            ans.append(cur_str)
        else:
            char = dic[digits[cur_digit]]
            for c in char:
                backtrack(cur_digit+1, cur_str+c)
    if len(digits) == 0:
        return []
    backtrack(0, "")
    return ans

# 216.[重点]Combination Sum III
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
"""
def combinationSum3(k: int, n: int):
    ans = []
    nums = list(range(1, 10))
    def backtrack(cur_k, cur_num, cur_nums):
        print(cur_k, cur_nums)
        if sum(cur_nums) == n and cur_k == k:
            ans.append(cur_nums.copy())
        elif sum(cur_nums) > n:
            return
        elif sum(cur_nums) < n and cur_k < k:
            for n_ in range(cur_num, 10):
                cur_nums.append(n_)
                backtrack(cur_k+1, n_+1, cur_nums)
                cur_nums.pop()
        return
    backtrack(0, 1, [])
    return ans

##############################################################
###                 Dynamic Programming                    ###
##############################################################

# 1137. N-th Tribonacci Number [easy]
"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""
def tribonacci(n: int) -> int:
    if 1 <= n < 3:
        return 1
    if n == 0:
        return 0
    dp = [0 for i in range(n+1)]
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

# 746. Min Cost Climbing Stairs [easy]
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Input: cost = [10,15,20]
Output: 15
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
"""
def minCostClimbingStairs(cost):
    # dp[i] = cost[i] + min(dp[i-2], dp[i-1])
    l = len(cost)
    dp = [0 for i in range(l)]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
    return min(dp[l-1]+cost[l-1], dp[l-2]+cost[l-2])

# 198. Hourse Robber
def houseRobber(nums):
    l = len(nums)
    if l == 1:
        return nums[0]
    if l == 2:
        return max(nums)
    dp = [0 for i in range(l)]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, l):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

##############################################################
###                  Bit Manipulation                      ###
##############################################################

##############################################################
###                        Trie                            ###
##############################################################
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

##############################################################
###                      Intervals                         ###
##############################################################
# 435. Non-overlapping Intervals[medium]

# 452. Minimum Number of Arrows to Burst Ballons[medium]


##############################################################
###                      Monotonic                         ###
##############################################################
