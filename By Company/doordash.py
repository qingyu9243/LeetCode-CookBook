# 1166. Design File System
"""
You are asked to design a file system that allows you to create new paths and associate them with different values.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.
Implement the FileSystem class:
bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
"""
class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        # basic path validations
        if path == '/' or len(path) == 0 or path in self.paths:
            return False
        # if the parent doesn't exist
        parent = path[:path.rfind('/')]

        if len(parent) > 1 and parent not in self.paths:
            return False
        # add new path to paths dic
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        return -1

# 124. Max path sum in binary tree
"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""
def maxPathSum(node):
    pass

# 286. Walls and Gates
from typing import List
from collections import deque
def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    # bfs from gates, update the empty room with min value
    print(rooms)
    m, n = len(rooms), len(rooms[0])
    def bfs(i, j):
        directions = [(1,0), (-1,0), (0, -1), (0, 1)]
        q = deque()
        q.append((i, j, 0))
        while q:
            cur_x, cur_y, s = q.pop()
            for x, y in directions:
                n_x, n_y = cur_x + x, cur_y + y
                if 0 <= n_x < m and 0 <= n_y < n and rooms[n_x][n_y] > 0:
                    val = rooms[n_x][n_y]
                    if val > s + 1:
                        rooms[n_x][n_y] = s + 1
                        q.append((n_x, n_y, s+1))
                
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                print(i, j)
                bfs(i, j)
    print(rooms)
#print(wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
#print(wallsAndGates([[-1]]))

# 1905. Count Sub Islands
"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
"""
def countSubIslands(grid1, grid2):
    pass

# 826. Most Profit Assigning Work
"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
"""
def maxProfitAssignment(difficulty, profit, worker):
    pass

# 827. Making a Large Island


# 1235. Maximum Profit in Job Scheduling
"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
"""
def jobScheduling(startTime, endTime, profit):
    pass

# 1790. Check if One String Swap Can Make String Equal
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)
    
    if len(diff) != 2:
        return False
    
    i, j = diff
    if s1[i] == s2[j] and s1[j] == s2[i]:
        return True
    return False
# 1779. Find Nearest Point that has the Same C or Y Coordinate


# 1268. Search Suggestion System

# 329. Longest Increasing Path in a Matrix
def longestIncreasingPath(matrix):
    pass
# 2049. Count Nodes With the Highest Score

# 296. Best Meeting Point
from math import ceil
def minTotalDistance(grid):
    rows, cols = len(grid), len(grid[0])
    row_counts, col_counts = [0]*rows, [0]*cols
    houses = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1
                houses.append((r, c))
    h = len(houses)
    #print(row_counts, col_counts, houses)
    def find_mid(counts):
        target = ceil(h/2)
        seen = 0
        for i in range(len(counts)):
            seen += counts[i]
            if seen >= target:
                return i
    meet_r, meet_c = find_mid(row_counts), find_mid(col_counts)
    return sum(abs(r-meet_r) + abs(c-meet_c) for r, c in houses)
#print(minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))

# 317. Shortest Distance From All Buildings

# 735. Asteroid Collisions

# 1834. Single-Threaded CPU

# 297. Serialize and Deserialize Binary Tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def serialize(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, string):
            if not root:
                string += "N,"
            else:
                string += root.val
                string = helper(root.left, string)
                string = helper(root.right, string)
            return string
        
        return helper(root, "")

    def deserialize(data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(l):
            if l[0] == "N":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = helper(l)
            root.right = helper(l)
            return root
        
        list_values = data.split(',')
        return helper(list_values)

# 428. Serialize and Deserialize Nary Tree
class NaryNode:
    def __init__(self, value: str, children: list) -> None:
        self.val = value
        self.children = children

class SolutionNary:
    def serialize(root: NaryNode):
        if not root:
            return []
        else:
            pass

    def deserialize(data: str):
        pass

# 1347. Min number of steps to make two strings anagram
from collections import Counter
def minSteps(self, s: str, t: str) -> int:
    counter_s = Counter(s)
    counter_t = Counter(t)
    #print(counter_s, counter_t)
    steps = 0
    for char in counter_s:
        if char in counter_t:
            if counter_s[char] > counter_t[char]:
                steps += counter_s[char] - counter_t[char]
        else:
            steps += counter_s[char]
    return steps
# 210. Course Schedule II

# 875. Making a Large Island

# 1779. Find Nearest Point That Has the Same X or Y Coordinate

# 658. Find K Closest Elements

# 772. Basic Calculator III

# 227. Basic Calculator II

# 621. Task Scheduler 

# 1. Two Sum

# 31. Next Permutation

# 164. Maximum Gap

# 1730. Shortest Path to Get Food

# 556. Next Great Element III

#2049. Count Nodes With the Highest ScoreMed.

# 208. Implement Trie (Prefix Tree)Med.

# 224. Basic CalculatorHard

# 277. Find the CelebrityMed.

# 588. Design In-Memory File SystemHard

# 859. Buddy StringsEasy

# 986. Interval List IntersectionsMed.

# 987. Vertical Order Traversal of a Binary TreeHard

# 1173. Immediate Food Delivery IEasy

# 1174. Immediate Food Delivery IIMed.

# 1944. Number of Visible People in a Queue Hard

# 1359. Count All Valid Pickup and Delivery Options Hard

# 1383. Maximum Performance of a TeamHard

# 1522. Diameter of N-Ary Tree Med.

# 2065. Maximum Path Quality of a Graph Hard

# 2565. Subsequence With the Minimum Score Hard

# 2611. Mice and Cheese
