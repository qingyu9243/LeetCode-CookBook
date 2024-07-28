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
def wallsAndGates(rooms):
    pass

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

# 1779. Find Nearest Point that has the Same C or Y Coordinate

# 1268. Search Suggestion System

# 329. Longest Increasing Path in a Matrix

# 2049. Count Nodes With the Highest Score

# 296. Best Meeting Point

# 317. Shortest Distance From All Buildings

# 735. Asteroid Collisions

# 1834. Single-Threaded CPU

# 297. Serialize and Deserialize Binary Tree

# 1347. Min number of steps to make two strings anagram

# 210. Course 