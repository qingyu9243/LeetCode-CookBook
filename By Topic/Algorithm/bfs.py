# 314. Binary Tree Vertical Order Traversal
"""
DS: queue to store (node, column), hashtable to store key: column, value: node values
ALGO: BFS
Time complexity: O(), Space Complexity: O(n)
"""
from collections import deque
from collections import defaultdict
class TreeNode():
    def __init__(self, value=0, left = None, right = None):
        self.val = value
        self.left = None
        self.right = None
def verticalOrder(root):
    if not root:
        return None
    queue = [(root, 0)]
    max_col = min_col = 0
    d = defaultdict(list) # store the node value under same column

    while queue:
        n, ind = queue.popleft()
        d[ind].append(n.value)
        min_col = min(min_col, ind)
        max_col = max(max_col, ind)
        queue.append((n.left, ind-1))
        queue.append((n.right, ind+1))

    return [d[x] for x in range(min_col, max_col+1)]


# 200. Number of Islands
"""
DS: queue/stack to store the points that to be visited.
ALGO: bfs/dfs to find the 1(lands) and change it to 0(water) until can't find any surrounding lands.
Time complexity: O(mn), Space Complexity: O(n)
"""
def numIslands(grid):
    def bfs(x, y):
        queue = deque((x, y))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in directions:
                if 0 <= cur_x + dx < m and 0 <= cur_y + dy < n and grid[cur_x + dx][cur_y + dy] == "1":
                    queue.append((cur_x + dx, cur_y + dy))
            grid[cur_x][cur_y] = "0"

    ans = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                bfs(i, j)
                ans += 1
    return ans

# 339. Nested List Weight Sum


# 279. Perfect Sqaures


# 322. Coin Change


# 199. Binary Tree Right Side View


# 286. Walls and Gates


# 2385. Amount of Time for Binary Tree to Be Infected


# 127. Word Ladder
"""
"""


# 815. Bus Routes


# 994. Rotting Oranges


# 207. Course Schedule


# 827. Making a Large Island


# 1293. Shortest Path in a Grid with Obstacles Elimination


# 210. Course Schedule II


# 1091. Shortest Path in Binary Matrix


# 987. Vertical Order Traversal of a Binary Tree


# 297. Serialize and Deserialize Binary Tree


# 329. Longest Increasing Path in a Matrix