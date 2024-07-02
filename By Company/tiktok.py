
# Job Scheduling
# live package tracking system
# design chat system
from collections import defaultdict
from typing import List


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

# 15    3Sum Medium
"""
[-5, -5, -4, -3, -1, -1, 1, 1, 2, 2, 4], target 5
 i        j                          k

"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # three pointers
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n-2):
        if nums[i] > 0:
            break # no possible answer
        if i > 0 and nums[i] == nums[i-1]: # optimize, skip the same number
            continue
        j, k = i+1, n-1
        while j < k:
            cur = nums[i] + nums[j] + nums[k]
            if cur > 0:
                k -= 1
            elif cur < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j + 1 < k and nums[j+1] == nums[k]:
                    j += 1
                while k - 1 > j and nums[k-1] == nums[k]:
                    k -= 1
                j += 1
                k -= 1
    return res

# 259	3Sum Smaller
"""
[1,2,2,-5,-1,-3,1,-5,-4,-1,4], 5
 f s    th
"""
def threeSumSmaller(nums, target):
    nums.sort()
    n = len(nums)
    ans = 0

    for first in range(n-2):
        second = first + 1
        third = n - 1
        while second < third:
            three_sum = nums[first] + nums[second] + nums[third]
            if three_sum < target:
                ans += third - second
                second += 1
            else:
                third -= 1
    return ans
#print(threeSumSmaller([1,2,2,-5,-1,-3,1,-5,-4,-1,4], 5))

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

# 1257 Smallest Common Region
"""
Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
"""
def findSmallestRegion(regions, region1, region2):
    # create parent map
    parent_map = {}
    for region in regions:
        for sub_reg in region[1:]:
            parent_map[sub_reg] = region[0]

    # create path to root for region1
    path1 = set()
    while region1 in parent_map:
        #print(region1)
        path1.add(region1)
        region1 = parent_map[region1]
    path1.add(region1)
    #print('path1',path1)
    
    # find the first common ancestor
    while region2 not in path1:
        region2 = parent_map[region2]
    return region2


#print(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "New York"))
#print(findSmallestRegion([["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"))

# 928	Minimize Malware Spread II	43.8%	Hard
# 403	Frog Jump	46.1%	Hard	
# 856	Score of Parentheses	64.1%	Medium	
# 1507	Reformat Date	66.1%	Easy	
# 93	Restore IP Addresses	50.3%	Medium	
"""
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""
def restoreIPaddress(s):
    res = []
    l = len(s)
    def is_valid(segment): # 0 ~ 9, or 10 ~ 255 (01, 09, 012 are invalid)
        #print(segment)
        if len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255):
            return True

    def backtrack(cur_index, l_ip):
        if cur_index == l and len(l_ip) == 4:
            res.append(".".join(l_ip))
            return
        for length in range(1, 4):
            if cur_index + length <= l:
                segment = s[cur_index:cur_index+length] # substring, include cur_index
                if is_valid(segment):
                    backtrack(cur_index+length, l_ip+[segment])

    backtrack(0, [])
    return res
#print(restoreIPaddress("25525511135"))

# 1293	Shortest Path in a Grid with Obstacles Elimination	45.2%	Hard	
# 772	[重点]Basic Calculator III	hard
def calculate(s):
    pass

# 1010	Pairs of Songs With Total Durations Divisible by 60	52.9%	Medium	
# 767	Reorganize String	54.7%	Medium	

# 
# 1062	Longest Repeating Substring
# 2791	Count Paths That Can Form a Palindrome in a Tree	47.8%	Hard	
# 395	Longest Substring with At Least K Repeating Characters	45.0%	Medium	
# 2050	Parallel Courses III	67.3%	Hard	
# 926	Flip String to Monotone Increasing	61.4%	Medium	
# 2290	Minimum Obstacle Removal to Reach Corner	53.9%	Hard	
