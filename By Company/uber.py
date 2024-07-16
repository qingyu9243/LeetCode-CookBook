# 432.  All O's one Data Structure
class AllOne:
    def __init__(self) -> None:
        pass

    def inc(self, key):
        pass
    
    def dec(self, key):
        pass

    def getMaxKey(self,):
        pass

    def getMinKey(self,):
        pass
# 2508	Add Edges to Make Degrees of All Nodes Even	31.6%	Hard	
# 564	Find the Closest Palindrome	22.5%	Hard
	
# 815	Bus Routes	47.8%	Hard
from collections import deque
from collections import defaultdict
def busRoutes(routes, source, target):
    # construct dict, key: stop, value: buses to this stop
    if source == target:
        return 0
    ans = 0

    route_map = defaultdict(set)
    for bus, stops in enumerate(routes):
        for stop in stops:
            route_map[stop].add(bus)
    
    # bfs to search shortest path, using queue([route, num_buses_taken])
    queue = deque()
    for route in route_map[source]:
        queue.append((route, 1))
    visited_stops = set([source])
    visited_routes = set()
    
    while queue:
        current_route, buses_taken = queue.popleft()
        if current_route in visited_routes:
            continue
        visited_routes.add(current_route)

        for stop in routes[current_route]:
            if stop == target:
                return buses_taken
            if stop not in visited_stops:
                visited_stops.add(stop)
                for next_route in route_map[stop]:
                    if next_route not in visited_routes:
                        queue.append([next_route, buses_taken + 1])
    return -1
print(busRoutes([[1,2,7],[3,6,7]], 1, 6))

# 305	Number of Islands II 39.9%	Hard
"""
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Algo: Union-Find
    parent = {} # dict to store the each island cell's root
    rank = defaultdict(int) # dict to store how many child nodes attached to island cell.
"""
from collections import defaultdict
def numIslands(m, n, positions):
    parent = {}
    rank = defaultdict(int)
    res = [0 for i in range(len(positions))]

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(n1, n2):
        p1, p2 = parent[n1], parent[n2]
        if p1 == p2: # no need to union
            return False
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += 1
        else:
            parent[p1] = p2
            rank[p2] += 1
        return True
    
    count = 0
    for idx, (x, y) in enumerate(positions):
        # self-isolated island
        if (x, y) not in parent:
            parent[(x, y)] = (x, y)
            count += 1
        # unioned island
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in parent:
                union((x, y), (nx, ny))
                count -= 1
        res[idx] = count

    return res

# 1438	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit	49.6%	Medium	
# 427	Construct Quad Tree	75.6%	Medium	
# 2468	Split Message Based on Limit	44.3%	Hard	
# 855	Exam Room	43.5%	Medium	
# 212	Word Search II	36.4%	Hard	

# 1428	Leftmost Column with at Least a One 54.5%	Medium	
# 399	Evaluate Division	61.8%	Medium	
# 490	The Maze 58.1%	Medium	
# 729	My Calendar I	56.6%	Medium	
# 508	
# Most Frequent Subtree Sum	66.6%	Medium	
# 2958	
# Length of Longest Subarray With at Most K Frequency	55.8%	Medium	
# 981	
# Time Based Key-Value Store	49.3%	Medium	
# 384	
# Shuffle an Array	58.4%	Medium	
# 2444	
# Count Subarrays With Fixed Bounds	68.0%	Hard	
# 886	
# Possible Bipartition	50.6%	Medium	
# 934	
# Shortest Bridge	57.7%	Medium	
# 2610	
# Convert an Array Into a 2D Array With Conditions	87.2%	Medium	
# 417	
# Pacific Atlantic Water Flow	55.4%	Medium	
# 286	
# Walls and Gates
# 61.5%	Medium	
# 2402	
# Meeting Rooms III	44.5%	Hard	
# 230	
# Kth Smallest Element in a BST	72.9%	Medium	
# 79	
# Word Search	43.0%	Medium	
# 109	
# Convert Sorted List to Binary Search Tree	62.2%	Medium	
# 986	
# Interval List Intersections	71.7%	Medium	
# 791	
# Custom Sort String	70.8%	Medium	
# 1207	
# Unique Number of Occurrences	77.2%	Easy	
# 528	
# Random Pick with Weight	46.9%	Medium	
# 330	
# Patching Array	53.0%	Hard	
# 279	
# Perfect Squares	54.9%	Medium	
# 224	
# Basic Calculator	43.6%	Hard	
# 68	
# Text Justification	43.9%	Hard	
# 69	
# Sqrt(x)	39.0%	Easy	
# 4	
# Median of Two Sorted Arrays	40.4%	Hard	
# 931	
# Minimum Falling Path Sum	63.8%	Medium	
# 662	
# Maximum Width of Binary Tree	43.0%	Medium	
# 503	
# Next Greater Element II	64.0%	Medium	
# 56	
# Merge Intervals	47.6%	Medium	
# 451	
# Sort Characters By Frequency	72.7%	Medium	
# 785	
# Is Graph Bipartite?	55.8%	Medium	
# 121	
# Best Time to Buy and Sell Stock	53.8%	Easy	
# 1193	
# Monthly Transactions I	57.7%	Medium	
# 295	
# Find Median from Data Stream	52.0%	Hard	
# 22	
# Generate Parentheses	74.8%	Medium	
# 300	
# Longest Increasing Subsequence	55.6%	Medium	
# 217	
# Contains Duplicate	61.9%	Easy	
# 1	
# Two Sum	52.9%	Easy	
# 162	
# Find Peak Element	46.0%	Medium	
# 189	
# Rotate Array	40.8%	Medium	
# 42	
# Trapping Rain Water	62.3%	Hard	
# 334	
# Increasing Triplet Subsequence	39.7%	Medium	
# 540	
# Single Element in a Sorted Array	59.1%	Medium	
# 66	
# Plus One	45.6%	Easy	
# 496	
# Next Greater Element I	72.4%	Easy	
# 5	
# Longest Palindromic Substring	34.0%	Medium	
# 7	
# Reverse Integer	28.8%	Medium	
# 287	
# Find the Duplicate Number
# 61.0%	Medium	
# 234	
# Palindrome Linked List	53.5%	Easy	
# 876	
# Middle of the Linked List	78.7%	Easy	
# 200	
# Number of Islands
# 59.7%	Medium	
# 347	
# Top K Frequent Elements	62.9%	Medium	
# 48	
# Rotate Image	74.8%	Medium	
# 49	
# Group Anagrams	68.8%	Medium	
# 128	
# Longest Consecutive Sequence	47.3%	Medium	
# 35	
# Search Insert Position	46.3%	Easy	
# 53	
# Maximum Subarray	50.9%	Medium	
# 27	
# Remove Element	57.2%	Easy	
# 88	
# Merge Sorted Array