"""
0 -- 1 -- 2
     |
3 -- 4 -- 5

root: [0, 1, 1, 3, 3, 5]
index: 0, 1, 2, 3, 4, 5

class UnionFind:
    def __init__(self, n):
        self.root = [-1]*n

    def find(x):
        if x != self.root[x]:
            root[x] = find[root[x]]
        return root[x]
    
    def union(x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x > root_y:
            root[root_x] = root_y
        elif root_x < root_y:
            root[root_y] = root_x
"""

# 547. Friend Circle
def findCircleNum(isConnected) -> int:
    n = len(isConnected)
    root = [i for i in range(n)]
    def find(x):
        if x != root[x]:
            root[x] = find(root[x])
        return root[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX > rootY:
            root[rootX] = rootY
        elif rootX < rootY:
            root[rootY] = rootX
    
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j] == 1:
                union(i, j)
    ans = set()
    for i in range(n):
        tmp_root = find(i)
        ans.add(tmp_root)
    return len(ans)
    
# 721	Accounts Merge	57.1%	Medium	
    
# 130. Surrounded Regions


# 200	Number of Islands 59.5%	Medium	

# 128	Longest Consecutive Sequence	47.3%	Medium
    
# 827	Making A Large Island	47.1%	Hard	
# 399	Evaluate Division	61.7%	Medium	

# 695	Max Area of Island	72.0%	Medium	
# 2709	Greatest Common Divisor Traversal	42.8%	Hard	
# 2092	Find All People With Secret	45.8%	Hard	
# 694	Number of Distinct Islands 61.2%	Medium	
# 1258	Synonymous Sentences