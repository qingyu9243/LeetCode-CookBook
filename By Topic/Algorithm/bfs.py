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
"""
1. DP. dp[n] = min(dp[n-k]) + 1, k is square number
2. BFS. 
dry run:
n = 12
num_squares = [1, 4, 9, 16]

"""
def numSquares(n):
    pass

# 322. Coin Change


# 199. Binary Tree Right Side View


# 286. Walls and Gates


# 2385. Amount of Time for Binary Tree to Be Infected


# 127. Word Ladder, Hard
"""
Input:
    begin word = "hit", end word = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
Output:
    5 (shortest transform "hot" -> "dot" -> "dog" -> cog")
Algo: 将单词的每一个位置替换成一个符号，这样就可以快速找到相邻的单词，bfs. Use dict to store word transforms
"""
def ladderLength(beginWord, endWord, wordList):
    if (
        endWord not in wordList
        or not endWord
        or not beginWord
        or not wordList
    ):
        return 0
    l = len(beginWord)
    # construct a dictionary that stores the relationship for word transforming
    all_comb_dict = defaultdict(list)
    for word in wordList: # word: hot, tmp_w: *ot, h*t, ho*
        for i in range(l):
            tmp_w = word[:i]+"*"+word[i:]
            all_comb_dict[tmp_w].append(word) # key: *ot, value: hot

    visited = set()
    queue = deque((beginWord, 1))
    while queue:
        cur_word, level = queue.popleft()
        for i in range(l):
            search_word = cur_word[:i]+"*"+cur_word[i:]
            for next_word in all_comb_dict[search_word]:
                if next_word == endWord:
                    return level + 1
                if next_word not in visited: 
                    queue.append((next_word, level + 1))
            all_comb_dict[search_word] = []
    return 0

# 126. Word Ladder II Hard
"""
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
    "hit" -> "hot" -> "lot" -> "log" -> "cog"
"""
def findLadders(beginWord: str, endWord: str, wordList): # -> List[List[str]]
    wordList = set(wordList)
    res = []
    edge = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            edge[word[:i] + "_" + word[i+1:]].append(word)
            
    q = {beginWord: [[beginWord]]}
    while q:
        wordList -= set(q.keys())
        new_q = defaultdict(list)
        for w in q:
            if w == endWord: 
                res += q[w]
            else:
                for i in range(len(w)):
                    for neww in edge[w[:i] + "_" + w[i+1:]]:
                        if neww in wordList:
                            new_q[neww] += [j + [neww] for j in q[w]]          
        q = new_q
    return res

# 815. Bus Routes


# 994. Rotting Oranges [BFS]
def rottingOranges(grid):
    m, n = len(grid), len(grid[0])
    max_time = 0
    queue = deque()
    fresh = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    while queue:
        x, y, time = queue.popleft()
        max_time = max(max_time, time)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                queue.append((nx, ny, time+1))
                grid[nx][ny] = 2
                fresh -= 1

    return max_time if fresh == 0 else -1
#print(rottingOranges([[2,1,1],[1,1,0],[0,1,1]]))

# 207. Course Schedule


# 827. Making a Large Island


# 1293. Shortest Path in a Grid with Obstacles Elimination


# 210. Course Schedule II


# 1091. Shortest Path in Binary Matrix


# 987. Vertical Order Traversal of a Binary Tree


# 297. Serialize and Deserialize Binary Tree


# 329. Longest Increasing Path in a Matrix