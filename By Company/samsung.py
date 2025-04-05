from collections import deque
import heapq
from typing import Optional
#300. Longest Increasing Subsequence
def longestIncreasingSebsequence(nums):
    if not nums:
        return 0
    # Initialize DP array - dp[i] represents the length of the 
    # longest increasing subsequence ending at index i
    dp = [1] * len(nums)

    # Fill the dp array
    for i in range(1, len(nums)):
        # Check all previous elements
        for j in range(i):
            # If current element is greater than previous element
            # and including it gives a longer subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in dp array
    return max(dp)

# 886. Possible Bipartition - color dfs
def possibleBipartition(n, dislikes):
    # Build adjacency list
    graph = [[] for _ in range(n + 1)]  # +1 because people are labeled 1 to n
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)  # Bidirectional dislike
    print(graph)
    # Colors: 0 = uncolored, 1 = group 1, -1 = group 2
    colors = [0] * (n + 1)
    
    # DFS coloring function
    def dfs(node, color):
        colors[node] = color
        
        for neighbor in graph[node]:
            # If neighbor is uncolored, assign opposite color
            if colors[neighbor] == 0:
                if not dfs(neighbor, -color):
                    return False
            # If neighbor has same color as current node, conflict!
            elif colors[neighbor] == color:
                return False
        
        return True
    
    # Try to color each uncolored node
    for i in range(1, n + 1):
        if colors[i] == 0:
            if not dfs(i, 1):
                return False
    
    return True

# 785. Is Graph Bipartite? - color dfs
def isGraphBipartite(graph):
    n = len(graph)
    # Use -1 to indicate uncolored nodes, 0 and 1 for the two colors
    colors = [-1] * n
    
    # Function for DFS coloring
    def dfs_color(node, color):
        # Color the current node
        colors[node] = color
        
        # Visit all neighbors
        for neighbor in graph[node]:
            # If neighbor is uncolored, color it with the opposite color
            if colors[neighbor] == -1:
                if not dfs_color(neighbor, 1 - color):
                    return False
            # If neighbor has the same color as current node, graph is not bipartite
            elif colors[neighbor] == color:
                return False
        
        # If no conflicts found, current component is bipartite
        return True
    
    # Try to color each uncolored component
    for i in range(n):
        # Only start DFS from uncolored nodes (handles disconnected graph)
        if colors[i] == -1:
            if not dfs_color(i, 0):
                return False
    
    # If all components are bipartite, the whole graph is bipartite
    return True

# 146. LRU Cache
class Node:
    def __init__(self) -> None:
        pass

class LRU:
    def __init__(self) -> None:
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass

# 1. Two Sum
def twoSum(nums, target):
    map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff], i]
        map[diff] = i
    return []

# 312. Burst Balloons - Hard
def maxCoins():
    # Add 1 at the beginning and end to handle boundary cases
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Initialize DP table
    # dp[i][j] represents the maximum coins that can be collected
    # by bursting all balloons between indices i and j (exclusive)
    dp = [[0] * n for _ in range(n)]
    
    # Length of subarray
    for length in range(2, n):
        # Start index i
        for i in range(0, n - length):
            # End index j
            j = i + length
            
            # Last balloon to burst in the range (i,j)
            for k in range(i + 1, j):
                # Calculate coins: 
                # Left boundary * Current balloon * Right boundary + 
                # Best way to burst balloons in the left subarray +
                # Best way to burst balloons in the right subarray
                coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                dp[i][j] = max(dp[i][j], coins)
    
    # Return the maximum coins for the entire array
    return dp[0][n-1]# 33. Search in Rotated Sorted Array

# 994. Rotting Oranges
def orangesRotting(grid) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    fresh_count = 0
    rotten = deque()
    
    # Count fresh oranges and find initial rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_count += 1
            elif grid[r][c] == 2:
                rotten.append((r, c, 0))  # (row, col, minutes)
    
    # If there are no fresh oranges, return 0
    if fresh_count == 0:
        return 0
    
    # BFS to rot oranges
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    max_minutes = 0
    
    while rotten:
        row, col, minutes = rotten.popleft()
        max_minutes = max(max_minutes, minutes)
        
        # Check all four directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if the new position is valid and has a fresh orange
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                grid[new_row][new_col] == 1):
                # Make it rotten
                grid[new_row][new_col] = 2
                fresh_count -= 1
                # Add to queue with increased time
                rotten.append((new_row, new_col, minutes + 1))
    
    # If there are still fresh oranges left, it's impossible
    return max_minutes if fresh_count == 0 else -1

# 42. Trapping Rain Water - hard

# 53. Maximum Subarray

# 23. Merge k Sorted Lists - hard
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeKLists(lists) -> Optional[ListNode]:
    q = []
    # put the first node from each list
    for i in range(len(lists)):
        if lists[i]:
            #print(lists[i])
            heapq.heappush(q, (lists[i].val, i))
            lists[i] = lists[i].next
    #print(q)
    res = ListNode()
    cur = res
    while q:
        val, i = heapq.heappop(q)
        cur.next = ListNode(val)
        cur = cur.next
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i))
            lists[i] = lists[i].next
    return res.next



