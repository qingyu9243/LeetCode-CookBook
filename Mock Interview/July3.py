
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
from collections import deque

def numOfIsland(matrix):
    if not matrix:
        return 0
    ans = 0 # num of islands
    m, n = len(matrix), len(matrix[0])
    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        while queue:
            cur_x, cur_y = queue.popleft()
            matrix[cur_x][cur_y] = "0"
            for x, y in direct:
                n_x = cur_x + x
                n_y = cur_y + y
                if 0 <= n_x < m and 0 <= n_y < n and matrix[n_x][n_y] == "1":
                    queue.append((n_x, n_y))                  

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                bfs(i, j)
                ans += 1
    return ans

grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

# print(numOfIsland(grid1))
# print(numOfIsland(grid2))

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a(i), b(i)] indicates that you must take course b(i) first if you want to take course a(i).

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]

# indegree, key: course: value: int
# dict, key: course, value:[next_course1, next_course2,..]

from collections import defaultdict
from collections import deque
def courseOrder(numCourses, prerequisites):
    indegree = [0] * numCourses
    dic_next_courses = defaultdict(list)

    for courseA, courseB in prerequisites:
        indegree[courseA] += 1
        dic_next_courses[courseB].append(courseA)
    
    res = []
    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    print(indegree)
    print(dic_next_courses)

    while queue:
        print(queue)
        cur = queue.pop()
        res.append(cur)
        for course in dic_next_courses[cur]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)

    return res
# 3, [[1, 0], [0, 1]]
#print(courseOrder(2, [[1,0]]))
#print(courseOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
#print(courseOrder(1, []))
print(courseOrder(3, [[1, 0], [0, 1]]))