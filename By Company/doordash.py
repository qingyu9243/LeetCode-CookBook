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

# 286. Walls and Gates

# 1905. Count Sub Islands

# 826. Most Profit Assigning Work

# 1235. Maximum Profit in Job Scheduling

# 1790. Check if One String Swap Can Make String Equal

# 1779. Find Nearest Point that has the Same C or Y Coordinate

# 1268. Search Suggestion System

# 329. Longest Increasing Path in a Matrix

# 2049. Count Nodes With the Highest Score

# 296. Best Meeting Point

# 317. Shortest Distance From All Buildings