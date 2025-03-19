from typing import List
from collections import defaultdict
import math
# https://www.jianshu.com/p/fdbcba5fe5bc

###########################
# Domain
###########################
# 1. Leetcode 811
"""
Example 1:

Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
Explanation: We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
Example 2:

Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""
def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    domain_map = defaultdict(int)
    for cpdomain in cpdomains:
        cnt, domain = cpdomain.split()
        cnt = int(cnt)
        sub_domains = domain.split('.')
        for i in range(len(sub_domains)):
            cur_domain = sub_domains[i:]
            key = ".".join(cur_domain)
            domain_map[key] += cnt
    res = []
    for k, v in domain_map.items():
        res.append(f"{v} {k}")
    return res

# 2. Longest common continuous subarrary
"""
输入：
[
  ["3234.html", "xys.html", "7hsaa.html"], // user1
  ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]
["xys.html", "7hsaa.html"]
"""
def longestCommonConSubarray(users):
    if len(users) < 2:
        return []
    user1, user2 = users[0], users[1]
    max_count = 0
    result = []
    dp_grid = [[0]*(len(user2)+1) for _ in range(len(user1)+1)]

    for i in range(1, len(user1)+1):
        for j in range(1, len(user2)+1):
            if user1[i-1] == user2[j-1]:
                dp_grid[i][j] = dp_grid[i-1][j-1] + 1
                if dp_grid[i][j] > max_count:
                    max_count = dp_grid[i][j]
                    result = user1[i-max_count:i]
    return result
#print(longestCommonConSubarray([["3234.html", "xys.html", "7hsaa.html"], ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]]))

# 3. Ads Conversion Rate
"""
Analyzes ad effectiveness by tracking clicks and purchases

Args:
    completed_purchase_user_ids: List of user IDs who made purchases
    ad_clicks: Raw log data of ad clicks
    all_user_ips: Mapping between user IDs and IP addresses
    
Returns:
    List of strings with formatted output results
"""
def adsConversionRate(completedPurchaseUserIds, adClicks, allUserIPs):
    user_ids = set(completedPurchaseUserIds)
    conversion = {}
    ip_to_user_id = {}

    for user_ip in allUserIPs:
        user_id, ip = user_ip.split(',')
        ip_to_user_id[ip] = user_id

    for click in adClicks:
        parts = click.split(',')
        ip, ad_text = parts[0], parts[2]

        if ad_text in conversion:
            conversion[ad_text][1] += 1
            if ip_to_user_id.get(ip) in user_ids:
                conversion[ad_text][0] += 1
        else:
            bought = 1 if ip_to_user_id.get(ip) in user_ids else 0
            conversion[ad_text] = [bought, 1]

    for ad_text, ratio in conversion.items():
        print(f"{ratio[0]} of {ratio[1]}  {ad_text}")
# Test data
completed_purchase_user_ids = [
  "3123122444", "234111110", "8321125440", "99911063"
]

ad_clicks = [
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens"
]

all_user_ips = [
  "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]
#adsConversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips)

###########################
# 选课
###########################
# 1. 两名学生的课程overlap

def findOverlapCourses(student_courses):
    map_courseList = defaultdict(set)
    for student, course in student_courses:
        map_courseList[student].add(course)
    #print(map_courseList)
    result = {}
    student_ids = list(map_courseList.keys())
    #print(student_ids)
    for i in range(len(student_ids)):
        for j in range(i+1, len(student_ids)):
            student1, student2 = student_ids[i], student_ids[j]
            overlapped = list(set(map_courseList[student1])&set(map_courseList[student2]))
            if overlapped:
                result[(student1, student2)] = overlapped
    return result
#print(findOverlapCourses([["58", "Software Design"],  ["58", "Linear Algebra"],  ["94", "Art History"],  ["94", "Operating Systems"],  ["17", "Software Design"],  ["58", "Mechanics"],  ["58", "Economics"],  ["17", "Linear Algebra"],  ["17", "Political Science"],  ["94", "Economics"],  ["25", "Economics"],]))

# 2. 输出中间课程
"""
Find all courses that could be at the midpoint of any curriculum track.

Args:
    prereqs: List of [source, destination] pairs representing course prerequisites
    
Returns:
    Set of course names that could be at the midpoint of a track
"""
def find_midpoint_courses(prereqs):
    graph = defaultdict(list)
    all_courses = set()
    has_prereqs = set()

    for src, dst in prereqs:
        graph[src].append(dst)
        all_courses.add(src)
        all_courses.add(dst)
        has_prereqs.add(dst)
    # find root courses (no prerequistites)
    root_courses = all_courses - has_prereqs
    all_path = []

    def dfs(course, path):
        current_path = path + [course]
        if course not in graph or not graph[course]:
            all_path.append(current_path)
            return
        for next_course in graph[course]:
            dfs(next_course, current_path)
    
    for root in root_courses:
        dfs(root, [])
    #print(all_path)
    midpoint_courses = set()
    for path in all_path:
        if len(path) % 2 == 0:
            midpoint_courses.add(path[len(path)//2 - 1])
            #print("-----")
            #print(path)
            #print(path[len(path)//2 - 1])
        else:
            midpoint_courses.add(path[len(path)//2])
            #print("-----")
            #print(path)
            #print(path[len(path)//2 - 1])
    return midpoint_courses

# Test with the example from the problem statement
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]
#print(find_midpoint_courses(all_courses))
# Additional test cases from the JavaScript code
prereqs_courses1 = [
    ['Data Structures', 'Algorithms'],
    ['Foundations of Computer Science', 'Operating Systems'],
    ['Computer Networks', 'Computer Architecture'],
    ['Algorithms', 'Foundations of Computer Science'],
    ['Computer Architecture', 'Data Structures'],
    ['Software Design', 'Computer Networks'],
]
prereqs_courses2 = [
    ['Data Structures', 'Algorithms'],
    ['Algorithms', 'Foundations of Computer Science'],
    ['Foundations of Computer Science', 'Logic'],
]
prereqs_courses3 = [['Data Structures', 'Algorithms']]
#print(find_midpoint_courses(prereqs_courses1))
#print(find_midpoint_courses(prereqs_courses2))
#print(find_midpoint_courses(prereqs_courses3))


###########################
# 矩阵题
###########################
# 1. 

###########################
# reflow字符串
###########################


###########################
# 计算器
###########################


###########################
# 矩阵合法
###########################
# 1. 给一个N*N的矩阵，判定是否是有效的矩阵。有效矩阵的定义是每一行或者每一列的数字都必须正好是1到N的数。输出一个bool。
def isValidMatrix(matrix):
    n = len(matrix)
    # check row
    for row in matrix:
        if len(row) != n or set(row) != set(range(1, n+1)):
            return False 
    # check col
    for col in range(n):
        column = [matrix[row][col] for row in range(n)]
        if set(column) != set(range(1, n+1)):
            return False
    return True
# 2. nonogram
"""
A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions. 
Specifically, each cell can be either black or white, which we will represent as 0 for black and 1 for white.

+------------+
| 1  1  1  1 |
| 0  1  1  1 |
| 0  1  0  0 |
| 1  1  0  1 |
| 0  0  1  1 |
+------------+

For each row and column, the instructions give the lengths of contiguous runs of black (0) cells. 
For example, the instructions for one row of [ 2, 1 ] indicate that there must be a run of two black cells, 
followed later by another run of one black cell, and the rest of the row filled with white cells.

These are valid solutions: [ 1, 0, 0, 1, 0 ] and [ 0, 0, 1, 1, 0 ] and also [ 0, 0, 1, 0, 1 ]
This is not valid: [ 1, 0, 1, 0, 0 ] since the runs are not in the correct order.
This is not valid: [ 1, 0, 0, 0, 1 ] since the two runs of 0s are not separated by 1s.

Your job is to write a function to validate a possible solution against a set of instructions. 
Given a 2D matrix representing a player's solution; 
and instructions for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

Example instructions #1

matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]
rows1_1    =  [], [1], [1,2], [1], [2]
columns1_1 =  [2,1], [1], [2], [1]
validateNonogram(matrix1, rows1_1, columns1_1) => True

Example solution matrix:
matrix1 ->
                                   row
                +------------+     instructions
                | 1  1  1  1 | <-- []
                | 0  1  1  1 | <-- [1]
                | 0  1  0  0 | <-- [1,2]
                | 1  1  0  1 | <-- [1]
                | 0  0  1  1 | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
  column       [2,1] | [2] |
  instructions      [1]   [1]


Example instructions #2

(same matrix as above)
rows1_2    =  [], [], [1], [1], [1,1]
columns1_2 =  [2], [1], [2], [1]
validateNonogram(matrix1, rows1_2, columns1_2) => False

The second and third rows and the first column do not match their respective instructions.

Example instructions #3

matrix2 = [
[ 1, 1 ],
[ 0, 0 ],
[ 0, 0 ],
[ 1, 0 ]
]
rows2_1    = [], [2], [2], [1]
columns2_1 = [1, 1], [3]
validateNonogram(matrix2, rows2_1, columns2_1) => False

The black cells in the first column are not separated by white cells.

n: number of rows in the matrix
m: number of columns in the matrix
"""
def isValidNonogram(matrix, rows_ins, col_ins):
    m = len(matrix)
    n = len(matrix[0])
    if m != len(rows_ins) or n != len(col_ins):
        return False
    
    def isValid(line, ins):
        # [0, 0, 1, 0, 0] vs [2, 2]
        zeros_count = []
        count = 0
        for element in line:
            if element == 0:
                count += 1
            elif count > 0:
                zeros_count.append(count)
                count = 0
        if count > 0:
            zeros_count.append(count)
        return zeros_count == ins
    
    # valid for each row
    for i in range(m):
        row = matrix[i]
        cur_row_ins = rows_ins[i]
        if not isValid(row, cur_row_ins):
            return False
    
    # valid for each col
    for j in range(n):
        col = [matrix[i][j] for i in range(m)]
        cur_col_ins = col_ins[j]
        if not isValid(col, cur_col_ins):
            return False

    return True

matrix1 = [[1,1,1,1],
           [0,1,1,1],
           [0,1,0,0],
           [1,1,0,1],
           [0,0,1,1]]
rows1_1    =  [[], [1], [1,2], [1], [2]]
columns1_1 =  [[2,1], [1], [2], [1]]
#print(isValidNonogram(matrix1, rows1_1, columns1_1))

###########################
# 祖先
###########################


###########################
# 门禁刷卡
###########################


###########################
# 开会
###########################
# 1. 是否有空余时间
def canSchedule(meetings, start, end):
    if start > end:
        return False
    for meeting in meetings:
        m_start, m_end = meeting
        if start < end and end > m_start:
            return False
    return True
meetings = [[1300, 1500], [930, 1200], [830, 845]]
assert canSchedule(meetings, 820, 830) == True
assert canSchedule(meetings, 1450, 1530) == False

# 2. 返回空闲时间段


###########################
# Sparse Vector
###########################
# 1. 设计sparse vector
class SparseVector:
    """
    A sparse vector implementation that efficiently stores vectors with mostly zero values.
    Supports addition, dot product, and cosine similarity operations.
    """    
    def __init__(self,size):
        if size <= 0:
            raise ValueError("Size must be positive")
        self.size = size
        self.values = {}

    def set(self, index, value):
        """
        Set the value at the specified index.
        
        Args:
            index (int): The index to set
            value (float): The value to set
            
        Raises:
            IndexError: If the index is out of bounds
        """
        self._validate_index(index)
        
        if value == 0.0:
            # If value is zero, remove from dictionary to save space
            self.values.pop(index, None)
        else:
            self.values[index] = value

    def get(self, index):
        """
        Get the value at the specified index.
        
        Args:
            index (int): The index to get
            
        Returns:
            float: The value at the index (0.0 if not explicitly set)
            
        Raises:
            IndexError: If the index is out of bounds
        """
        self._validate_index(index)
        return self.values.get(index, 0.0)

    def _validate_index(self, index):
        """
        Validate that the index is within bounds.
        
        Args:
            index (int): The index to validate
            
        Raises:
            IndexError: If the index is out of bounds
        """
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds for size {self.size}")
    def _validate_size_match(self, other):
        """
        Validate that two vectors have the same size.
        
        Args:
            other (SparseVector): The other vector to compare with
            
        Raises:
            ValueError: If the vectors have different sizes
        """
        if self.size != other.size:
            raise ValueError(f"Vector sizes don't match: {self.size} vs {other.size}")
    
    def add(self, other):
        """
        Add this vector to another vector.
        
        Args:
            other (SparseVector): The vector to add
            
        Returns:
            SparseVector: A new vector containing the sum
            
        Raises:
            ValueError: If vectors have different sizes
        """
        self._validate_size_match(other)
        
        result = SparseVector(self.size)
        
        # Copy all values from this vector
        for index, value in self.values.items():
            result.set(index, value)
        
        # Add values from the other vector
        for index, value in other.values.items():
            result.set(index, result.get(index) + value)
        
        return result
    
    def dot(self, other):
        """
        Calculate the dot product with another vector.
        
        Args:
            other (SparseVector): The vector to calculate dot product with
            
        Returns:
            float: The dot product
            
        Raises:
            ValueError: If vectors have different sizes
        """
        self._validate_size_match(other)
        
        # For efficiency, iterate over the vector with fewer non-zero values
        if len(self.values) <= len(other.values):
            smaller, larger = self.values, other.values
        else:
            smaller, larger = other.values, self.values
        
        result = 0.0
        for index, value in smaller.items():
            if index in larger:
                result += value * larger[index]
        
        return result
    
    def norm(self):
        """
        Calculate the Euclidean norm (magnitude) of the vector.
        
        Returns:
            float: The norm of the vector
        """
        sum_squares = sum(value ** 2 for value in self.values.values())
        return math.sqrt(sum_squares)
    
    def cos(self, other):
        """
        Calculate the cosine similarity with another vector.
        
        Args:
            other (SparseVector): The vector to calculate cosine similarity with
            
        Returns:
            float: The cosine similarity
            
        Raises:
            ValueError: If vectors have different sizes or if either vector is a zero vector
        """
        self._validate_size_match(other)
        
        norm_self = self.norm()
        norm_other = other.norm()
        
        if norm_self == 0 or norm_other == 0:
            raise ValueError("Cannot compute cosine similarity with a zero vector")
        
        return self.dot(other) / (norm_self * norm_other)
    
    def __str__(self) -> str:
        """
        Return a string representation of the vector.
        
        Returns:
            str: String representation of the vector
        """
        return "[" + ", ".join(str(self.get(i)) for i in range(self.size)) + "]"
    
    def __getitem__(self, index):
        """
        Enable bracket notation for getting values.
        
        Args:
            index (int): The index to get
            
        Returns:
            float: The value at the index
        """
        return self.get(index) # j = a[index] -> j = a.__getitem__(index)
    
    def __setitem__(self, index, value):
        """
        Enable bracket notation for setting values.
        
        Args:
            index (int): The index to set
            value (float): The value to set
        """
        self.set(index, value)
    
    def nnz(self):
        """
        Get the number of non-zero elements.
        
        Returns:
            int: Number of non-zero elements
        """        
        return len(self.values)
# Example usage (without the main guard)
v1 = SparseVector(5)
v1[0] = 4.0
v1[1] = 5.0

v2 = SparseVector(5)
v2[1] = 2.0
v2[3] = 3.0

v3 = SparseVector(2)
"""

# Test addition
print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1.add(v2))

try:
    print("v1 + v3 =", v1.add(v3))
except ValueError as e:
    print(f"Error with addition: {e}")

# Test dot product
print("v1 · v2 =", v1.dot(v2))

try:
    print("v1 · v3 =", v1.dot(v3))
except ValueError as e:
    print(f"Error with dot product: {e}")

# Test cosine similarity
print("cos(v1, v2) =", round(v1.cos(v2), 3))

try:
    print("cos(v1, v3) =", v1.cos(v3))
except ValueError as e:
    print(f"Error with cosine similarity: {e}")
"""
###########################
# 找宝藏
###########################
# 1. Find legal moves, 给一个i和j，找出身边四个方向里为0的所有格子。
"""
Find all legal moves from position (i, j) in a grid.
A legal move is to an adjacent cell (up, down, left, right) with value 0.

Args:
    grid: 2D list representing the game grid
    i: current row position
    j: current column position

Returns:
    List of tuples (row, col) representing legal moves
"""
def findLegalMoves(grid, i, j):
    rows = len(grid)
    cols = len(grid[0] if rows > 0 else 0)

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    legal_moves = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == 0:
                legal_moves.append((ni, nj))
            
    return legal_moves

# 2. 找能去的所有0区域
"""
Find all cells connected to the starting position (start_i, start_j) that have value 0.
Connected means you can reach the cell by moving up, down, left, or right through cells with value 0.

Args:
    grid: 2D list representing the game grid
    start_i: starting row position
    start_j: starting column position

Returns:
    List of tuples (row, col) representing all connected cells with value 0
"""
def findAllConnectedCells(grid, i, j):
    rows = len(grid)
    cols = len(grid[0] if rows > 0 else 0)

    visited = set()
    visited.add((i, j))
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    all_connected = []
    queue = [(i, j)]

    while queue: # bfs
        curi, curj = queue.pop(0)
        all_connected.append((curi, curj))
        for di, dy in directions:
            ni, nj = curi + di, curj + dy
            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj))

    return all_connected

grid_1 = [[1, 0, 1, 1],[0, 0, 0, 1],[1, 0, 1, 0],[1, 1, 0, 0]]
#print(findAllConnectedCells(grid_1, 1, 1))

# 3. 最短路径找treasure
"""
board3 中1代表钻石，给出起点和终点，问有没有一条不走回头路的路线，能从起点走到终点，并拿走所有的钻石，给出所有的最短路径。
board3 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]
treasure(board3, (5, 0), (0, 4)) -> None

treasure(board3, (5, 2), (2, 0)) ->
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
  Or
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

treasure(board3, (0, 0), (4, 1)) ->
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1)]
  Or
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]
"""
def findAllTreasures(grid, start, end):
    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # count the number of treasures
    numTreasures = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                numTreasures += 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    queue = [(start, [start], frozenset())]  # current_position, path, diamonds_collected

    shortest_paths = []
    min_length = float('inf')

    while queue:
        cur_pos, path, diamonds = queue.pop(0)
        # check if it's diamond
        if grid[cur_pos[0]][cur_pos[1]] == 1:
            diamonds = frozenset(list(diamonds) + [cur_pos])
        
        if cur_pos == end and len(diamonds) == numTreasures:
            if len(path) <= min_length:
                if len(path) < min_length:
                    min_length = len(path)
                    shortest_paths = []
                shortest_paths.append(path)
            continue # end this iteration
        
        if shortest_paths and len(path) > min_length:
            continue # end this iteration

        # check neighbors
        for di, dj in directions:
            ni, nj = cur_pos[0] + di, cur_pos[1] + dj
            new_pos = (ni, nj)
            if (0 <= ni < rows and 
                0 <= nj < cols and 
                grid[ni][nj] != -1 and 
                new_pos not in path):
                
                # Create a state key using position and collected diamonds
                new_state_key = (new_pos, diamonds)
                
                if new_state_key not in visited:
                    visited.add(new_state_key)
                    new_path = path + [new_pos]
                    queue.append((new_pos, new_path, diamonds))
    
    return shortest_paths if shortest_paths else None

board3 = [[  1,  0,  0, 0, 0 ], [  0, -1, -1, 0, 0 ], [  0, -1,  0, 1, 0 ], [ -1,  0,  0, 0, 0 ], [  0,  1, -1, 0, 0 ], [  0,  0,  0, 0, 0 ],]
#print(findAllTreasures(board3, (5, 0), (0, 4)))
#print(findAllTreasures(board3, (5, 2), (2, 0)))
#print(findAllTreasures(board3, (0, 0), (4, 1)))