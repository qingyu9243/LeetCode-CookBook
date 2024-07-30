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

# 124. Max path sum in binary tree[h]- **
"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""
def maxPathSum(node):
    def helper(root):
        if not root:
            return 0
        left_max = max(helper(node.left), 0)
        right_max = max(helper(node.right), 0)

        current_max = node.val + left_max + right_max
        max_sum = max(max_sum, current_max)

        return node.val + max(left_max, right_max)

    max_sum = float('inf')
    helper(node)
    return max_sum

# 286. Walls and Gates[m] done
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
def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    if not grid1 or not grid1[0] or not grid2 or not grid2[0]:
        return 0

    ROWS, COLS = len(grid1), len(grid1[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    island_count = 0

    def dfs_explore(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0:
            return True 
        
        # Mark cell as visited
        grid2[r][c] = 0

        # Disqualify as sub-island if cell is water in grid1
        if grid1[r][c] == 0:
            nonlocal is_sub_island 
            is_sub_island = False

        for dr, dc in DIRECTIONS:
            dfs_explore(r + dr, c + dc)
        
        return is_sub_island

    for row in range(ROWS):
        for col in range(COLS):
            if grid2[row][col] == 1:
                is_sub_island = True 
                if dfs_explore(row, col):
                    island_count += 1

    return island_count 

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
    # Combine difficulty and profit into a list of tuples and sort them by difficulty
    jobs = sorted(zip(difficulty, profit))
    
    # Sort worker abilities
    worker.sort()
    
    max_profit = 0
    best = 0
    i = 0
    n = len(jobs)
    
    for ability in worker:
        # Increase the best profit up to the current worker's ability
        while i < n and jobs[i][0] <= ability:
            best = max(best, jobs[i][1])
            i += 1
        # Add the best profit the current worker can get
        max_profit += best
    
    return max_profit

# 827. Making a Large Island
"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
"""
def largestIsland(self, grid: List[List[int]]) -> int:
    def dfs(x, y, index):
        q = [(x, y)]
        visit = {(x, y)}
        while q:
            curx, cury = q.pop()
            grid[curx][cury] = index
            for dx, dy in directions:
                tx, ty = curx + dx, cury + dy
                if 0 <= tx < n and 0 <= ty < n and grid[tx][ty] == 1:
                    q.append((tx, ty))
                    visit.add((tx, ty))
        return len(visit)

    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area = {}
    index = 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                area[index] = dfs(i, j, index)
                index += 1
    res = max(area.values() or [0])
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                tmp = set()
                for dx, dy in directions:
                    tx, ty = i + dx, j + dy
                    if 0 <= tx < n and 0 <= ty < n and grid[tx][ty] > 1:
                        tmp.add(grid[tx][ty])
                res = max(res, 1 + sum(area[t] for t in tmp))
    return res

# 1235. Maximum Profit in Job Scheduling
"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
"""
import heapq
def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit))
    heap = []
    max_profit = 0 # represents the max profits from all possible combinations ends before the start time

    for s, e, p in jobs:
        while heap and s >= heap[0][0]:
            max_profit = max(max_profit, heap[0][1])
            heapq.heappop(heap)
        heapq.heappush(heap, (e, p + max_profit))

    # find the max in the heap
    ans = 0
    while heap:
        ans = max(ans, heap[0][1])
        heapq.heappop(heap)
    return ans
#print(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))

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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(node.words) < 3:
                node.words.append(word)
    def prefixSearch(self, pref):
        node = self.root
        ans = []
        for c in pref:
            if c not in node.children:
                return ans + [[] for _ in range(len(pref) - len(ans))]
            node = node.children[c]
            ans.append(node.words[:])
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        return trie.prefixSearch(searchWord)

# 329. Longest Increasing Path in a Matrix
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    loc_dic = {}
    
    def dfs(i, j):
        if (i, j) in loc_dic:
            return loc_dic[(i, j)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        length = 0
        for x, y in directions:
            n_x, n_y = i + x, j + y
            if 0 <= n_x < m and 0 <= n_y < n and matrix[n_x][n_y] > matrix[i][j]:
                length = max(length, dfs(n_x, n_y))
        loc_dic[(i, j)] = length + 1        
        return length + 1
        
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    return ans


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
def shortestDistance(self, grid: List[List[int]]) -> int:
    if not grid:
        return -1
    # create a list of buildings and a set of empty lands for easy search later
    build, land = [], set()
    for x,y in itertools.product(range(len(grid)), range(len(grid[0]))):
        if grid[x][y] == 0:
            land.add((x,y))
        elif grid[x][y] == 1:
            build.append((x,y))
    # if there is no empty land available, we can't proceed further
    if not land:
        return -1
    
    d = {x: [float('inf')]*len(build) for x in land}
    
    # BFS for a given building's location
    def BFS(loc):
        x, y = build[loc]
        q = deque([(x,y,0)]) 
        while q:
            x, y, dist = q.popleft()
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (i,j) in land and d[(i,j)][loc] > dist + 1:
                    d[(i,j)][loc] = dist + 1
                    q.append((i,j,dist+1))
    
    # run BFS routine for all buildings
    for loc in range(len(build)):
        BFS(loc)
        
    # compute the shortest distance to all buildings for each empty land
    min_dist = min(sum(d[x]) for x in land)
    return -1 if min_dist == float('inf') else min_dist

# 735. Asteroid Collisions
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    # + + -> append
    # - - -> append
    # - + -> append
    # + - -> collision
    #    big   -small
    #    same  same
    #    small -big
    for i, star in enumerate(asteroids):
        if not stack or stack[-1] < 0 or star > 0:
            stack.append(star)
            continue
        while stack and stack[-1] > 0:
            if stack[-1] > abs(star):
                break
            x = stack.pop()
            if x + star == 0:
                break
        else:
            print(i, star)
            stack.append(star)
    return stack
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
