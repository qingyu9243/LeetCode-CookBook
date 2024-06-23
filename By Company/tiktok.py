
# Job Scheduling
# live package tracking system
# design chat system
from collections import defaultdict


# 588	Design In-Memory File System	https://leetcode.com/problems/design-in-memory-file-system/description/
class FileSystem:
    def __init__(self) -> None:
        pass

# 465	[重点]Optimal Account Balancing   https://leetcode.com/problems/optimal-account-balancing/description/
def minTransactions(transactions):
    account_bal = defaultdict(int)
    for a1, a2, amount in transactions:
        account_bal[a1] -= amount
        account_bal[a2] += amount
    
    def dfs(start):
        pass
    return dfs(0)
#print(minTransactions([[0,1,10],[1,0,1],[1,2,5],[2,0,5]]))

# 358	Rearrange String k Distance Apart


# 1530	[重点]Number of Good Leaf Nodes Pairs	63.5%	Medium	
class TreeNode:
    def __init__(self, value = 0, left = None, right = None) -> None:
        self.val = value,
        self.left = left
        self.right = right
def countPairs(root, distance):
    pair_count = 0


# 2263	Make Array Non-decreasing or Non-increasing	
def convertArray(nums):
    pass
# 2217	Find Palindrome With Fixed Length	36.9%	Medium	

# 15    3Sum
def threeSum(nums):
    pass


# 259	3Sum Smaller
def threeSumSmaller(nums):
    pass

# 694	[重点]Number of Distinct Islands
def numDistinctInslands(grid):
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]): # out of boundary
            return
        if (row, col) in seen or not grid[row][col]: # if in seen or value == 0
            return
        seen.add((row, col))
        current_island.add((row-row_origin, col-col_origin)) # add the island shape(difference)
        dfs(row-1, col)
        dfs(row, col-1)
        dfs(row+1, col)
        dfs(row, col+1)

    seen = set()
    unique_islands = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current_island = set()
            row_origin = row
            col_origin = col
            dfs(row, col)
            if current_island:
                print(current_island)
                unique_islands.add(frozenset(current_island))
                print(unique_islands)
    return len(unique_islands)
#print(numDistinctInslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
#print(numDistinctInslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))


# 928	Minimize Malware Spread II	43.8%	Hard	
# 403	Frog Jump	46.1%	Hard	
# 856	Score of Parentheses	64.1%	Medium	
# 1507	Reformat Date	66.1%	Easy	
# 93	Restore IP Addresses	50.3%	Medium	
# 1293	Shortest Path in a Grid with Obstacles Elimination	45.2%	Hard	
# 772	[重点]Basic Calculator III	hard
def calculate(s):
    pass

# 1010	Pairs of Songs With Total Durations Divisible by 60	52.9%	Medium	
# 767	Reorganize String	54.7%	Medium	
# 1062	Longest Repeating Substring
# 2791	Count Paths That Can Form a Palindrome in a Tree	47.8%	Hard	
# 395	Longest Substring with At Least K Repeating Characters	45.0%	Medium	
# 2050	Parallel Courses III	67.3%	Hard	
# 926	Flip String to Monotone Increasing	61.4%	Medium	
# 2290	Minimum Obstacle Removal to Reach Corner	53.9%	Hard	
