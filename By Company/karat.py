from typing import List
from collections import defaultdict, Counter
from itertools import combinations
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
# 1. 找一个矩形 find a retangular
"""
there is an image filled with 0s and 1s.  There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.
"""
def findRetangular(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return []
    result =[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                result.append([i, j])
                height = 1
                width = 1
                # find height
                while i + height < len(grid) and grid[i + height][j] == 0:
                    height += 1
                # find width
                while j + width < len(grid[0]) and grid[i][j+width] == 0:
                    width += 1
                result.append([i+height-1, j+width-1])
                return result
    return result       
#print(findRetangular([[1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 1, 1],[1, 0, 0, 0, 1, 1],[1, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1]]))               

# 2. 找多个矩形 find multiple retangle
"""
for the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s. The rectangles are separated by 1s. Find all the rectangles.
"""
def findMultipleRetangle(board):
    if not board or len(board) == 0 or len(board[0]) == 0:
        return []
    rows, cols = len(board), len(board[0])
    result =[]
    visited = [[False]*cols for _ in range(rows)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 and not visited[i][j]:
                retangle = []
                retangle.append([i, j])
                height, width = 1, 1
                while i + height < rows and board[i+height][j] == 0:
                    height += 1
                while j + width < cols and board[i][j+width] == 0:
                    width += 1
                retangle.append([i+height-1, j+width-1])
                print("retangle")
                print(retangle)
                print(height, width)
                for m in range(i, i+height):
                    for n in range(j, j+width):
                        visited[m][n] = True
                result.append(retangle)

    return result
#print(findMultipleRetangle([[1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 1, 0, 0, 1],[1, 0, 0, 1, 0, 0, 1],[1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 1, 0, 1],[1, 0, 0, 0, 1, 0, 1],[1, 1, 1, 1, 1, 1, 1]]))

# 3. 
"""
the image has random shapes filled with 0s, separated by 1s. Find all the shapes. Each shape is represented by coordinates of all the elements inside.
"""
def findMultipleShapes(board):
    rows, cols = len(board), len(board[0])
    visited = [[False]*cols for _ in range(rows)]
    result = []

    def bfs(i, j):
        queue = []
        queue.append([i, j])
        directions = [(1, 0), (-1, 0), (0, 1),(0, -1)]
        shape = []
        while queue:
            curi, curj = queue.pop(0)
            shape.append([curi, curj])
            for nx, ny in directions:
                ni, nj = curi + nx, curj + ny
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 0 and not visited[ni][nj]:
                    queue.append([ni, nj])
                    visited[ni][nj] = True
        return shape

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                t_result = bfs(i, j)
                result.append(t_result)

    return result
#print(findMultipleShapes(([[1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 1, 0, 0, 1],[1, 0, 1, 1, 0, 0, 1],[1, 1, 0, 1, 1, 1, 1],[1, 0, 0, 0, 1, 1, 1],[1, 0, 0, 0, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1]])))

###########################
# reflow字符串
###########################
# 1. word wrap
"""
给一个word list 和最大的长度，要求把这些word用 "-" 串联起来，但不能超过最大的长度。
"""
def wordWrap(words, maxLength):
    if not words:
        return ""
    if len(words[0]) > maxLength:
        return ""
    # try to add word one by one
    cur_length = len(words[0])
    result = words[0]
    for i in range(1, len(words)):
        if cur_length + len(words[i]) + 1 <= maxLength:
            result += "-" + words[i]
            cur_length += len(words[i]) + 1
        else:
            break
    return result
#print(wordWrap(["apple", "banana", "cherry", "date"], 20))

# 2. word processor
"""
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.
Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width. If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.
Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.

lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) ... "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

"""
def reflow_text(lines, max_width):
    words = []
    for line in lines:
        words.extend(line.split())

    # add each line with fixed length, including words as much as possible
    result = []
    i, l = 0, len(words)
    while i < l:
        cur_line = []
        cur_length = 0

        # add as many words as possible to the current line
        while i < l and cur_length + len(words[i]) + (1 if cur_line else 0) <= max_width:
            if cur_line:
                cur_length += 1

            cur_line.append(words[i])
            cur_length += len(words[i])
            i += 1
        print(cur_line)
        # if we have at least one word
        if cur_line:
            if len(cur_line) == 1:
                # single word case - no padding needed
                result.append(cur_line[0])
            else:
                # multiple words - justify the word
                total_word_length = sum(len(word) for word in cur_line)
                total_gaps = len(cur_line) - 1
                total_separators = max_width - total_word_length
                # Calculate distribution of separators
                separators_per_gap = total_separators // total_gaps
                extra_separators = total_separators % total_gaps
                # Build justified line
                justified_line = ""
                for j in range(len(cur_line) - 1):
                    justified_line += cur_line[j]
                    # Add separators for this gap
                    num_separators = separators_per_gap + (1 if j < extra_separators else 0)
                    justified_line += "-" * num_separators     
                # Add last word
                justified_line += cur_line[-1]
                result.append(justified_line)
        
    return result
lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]
#print(reflow_text(lines, 24))

###########################
# 计算器
###########################
# 1. 基本加减计算器
"""
给输入为string，例如"2+3-999+3"，之包含+-操作，返回计算结果。
"""
def basicCalculator(expression):
    if not expression:
        return 0
    
    num = 0
    operation = "+"
    result = 0

    for char in expression:
        if char.isdigit():
            num = num*10 + int(char)
            print(num)
        elif char in ["+", "-"]:
            print("char")
            print(char)
            if operation == "+":
                result += num
            else:
                result -= num
            num = 0 # clear the number after operation done
            operation = char # save the current operator to be used next time

    # deal with the last operation and number            
    if operation == "+":
        result += num
    else:
        result -= num
    return result
#print(basicCalculator("-2+3-999+3"))

# 2.basic calculator. LC 224. 加上parenthesis， 例如"2+((8+2)+(3-999))"，返回计算结果。
def basicCalculator2(expression):
    result = 0
    stack = []
    num = 0
    sign = 1 # 1 means +, -1 means -

    for ch in expression:
        if ch.isdigit():
            num = 10*num + int(ch)
        elif ch == "+":
            result += sign*num
            num = 0
            sign = 1
        elif ch == "-":
            result += sign*num
            num = 0
            sign = -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif ch == ")":
            result += sign*num
            num = 0
            result *= stack.pop() # get the sign
            result += stack.pop() # get the last result
    return result + sign*num
print(basicCalculator2("2+((8+2)+(3-999))"))

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
# 1. 0个或1个parent的节点 
"""
input: {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}} (parent -> child)
to get below graph
  1    2    3
/  \  /      \
4    5        6
                \
                  7
output: 只有0个parents和只有1个parent的节点
"""
def findNodesWithZeroOrOneParent(edges):
    parent_map = defaultdict(list) # key: node, value: parent list
    all_nodes = set()
    for parent, child in edges:
        parent_map[child].append(parent)
        all_nodes.add(parent)
        all_nodes.add(child)
    print(parent_map)
    result = []
    for node in all_nodes:
        if len(parent_map[node]) <= 1:
            result.append(node)
    return result
#print(findNodesWithZeroOrOneParent([{1,4}, {1,5}, {2,5}, {3,6}, {6,7}]))

# 2. 两个节点是否有公共祖先
def hasCommonAncestor(edges, x, y):
    parent_map = defaultdict(list)
    for parent, child in edges:
        parent_map[child].append(parent)

    # bfs to search
    ancestors_x = set()
    queue = parent_map[x].copy()
    visited_x = set()

    while queue:
        node = queue.pop(0)
        if node in visited_x:
            continue
        ancestors_x.add(node)
        visited_x.add(node)
        for parent in parent_map[node]:
            queue.append(parent)
    print(ancestors_x)
    print(parent_map)
    queue2 = parent_map[y].copy()
    visited_y = set()
    while queue2:
        node = queue2.pop(0)
        if node in visited_y:
            continue
        visited_y.add(node)
        print(visited_y)
        if node in ancestors_x:
            return True
        for parent in parent_map[node]:
            queue2.append(parent)

    return False
#print(hasCommonAncestor([(1, 4), (1, 5), (2, 5), (3, 6), (6, 7)], 4, 5)) #  Simple Tree with Common Ancestor
#print(hasCommonAncestor([(1, 4), (1, 5), (2, 5), (3, 6), (6, 7)], 4, 7)) #  No Common Ancestor
#print(hasCommonAncestor([(1, 2), (2, 3), (3, 4)], 2, 4)) # One Node is an Ancestor of the Other
#print(hasCommonAncestor([(1, 3), (2, 3), (3, 4), (3, 5)], 4, 5)) # Multiple Common Ancestors
#print(hasCommonAncestor([(1, 2), (2, 3), (3, 1), (4, 2)], 2, 3)) # Cyclic Graph
#print(hasCommonAncestor([(1, 2), (2, 3), (4, 5), (5, 6)], 3, 6)) # Disconnected Nodes
#print(hasCommonAncestor([(1, 2), (1, 3), (2, 4)], 2, 2)) # Same Node

# 3. 最远祖先 The most distant ancestor
def ealiestAncestor(edges, x):
    # build relationship map: child -> [parents]
    parent_map = defaultdict(set)
    for parent, child in edges:
        parent_map[child].add([parent])
    return
    
###########################
# 门禁刷卡
###########################
# 1. 找进出记录不符的人
"""
Given a list of people who enter and exit, find the people who entered without
their badge and who exited without their badge.

// badge_records = [
//   ["Martha",   "exit"],
//   ["Paul",     "enter"],
//   ["Martha",   "enter"],
//   ["Martha",   "exit"],
//   ["Jennifer", "enter"],
//   ["Paul",     "enter"],
//   ["Curtis",   "enter"],
//   ["Paul",     "exit"],
//   ["Martha",   "enter"],
//   ["Martha",   "exit"],
//   ["Jennifer", "exit"],
// ]

// Expected output: ["Paul", "Curtis"], ["Martha"]
"""
def find_badge_violations(records):
    state = {}
    result = [[],[]]
    invalid_enter = set()
    invalid_exit = set()
    for ppl, action in records:
        if ppl not in state:
            state[ppl] = 0 # ended state
        if action == "enter":
            if state[ppl] == 0:
                state[ppl] = 1 # entered state
            else:
                invalid_enter.add(ppl)
        if action == "exit":
            if state[ppl] == 1:
                state[ppl] = 0
            else:
                invalid_exit.add(ppl)

    for k, v in state.items():
        if v == 1:
            invalid_enter.add(k)

    for name in invalid_enter:
        result[0].append(name)
    for name in invalid_exit:
        result[1].append(name)

    return result
#print(find_badge_violations([["Martha",   "exit"],["Paul",     "enter"],["Martha",   "enter"],["Martha",   "exit"],["Jennifer", "enter"],["Paul",     "enter"],["Curtis",   "enter"],["Paul",     "exit"],["Martha",   "enter"],["Martha",   "exit"],["Jennifer", "exit"],]))

# 2. 一小时内access多次
"""
给 list of [name, time], time is string format: '1300' //下午一点
return: list of names and the times where their swipe badges within one hour. if there are multiple intervals that satisfy the condition, return any one of them.
name1: time1, time2, time3...
name2: time1, time2, time3, time4, time5...
example:
input: [['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']] 
output: {
'Martha': ['1600', '1620', '1530']
}
"""
def frequentAccess(records):
    ts_map = defaultdict(list)
    for name, ts in records:
        ts_map[name].append(ts)

    result = defaultdict(set)

    def timeConvert(time):
        return int(time[:2])*60 + int(time[2:])

    for name, times in ts_map.items():
        times.sort()
        for i in range(len(times)-1):
            if timeConvert(times[i+1]) - timeConvert(times[i]) <= 60:
                result[name].add(times[i])
                result[name].add(times[i+1])
    
    return result
#print(frequentAccess([['James', '1300'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]))

# 3. 找到某一组人共用会议室最长的时间段。
"""
We want to find employees who badged into our secured room together often. 
Given an unordered list of names and access times over a single day, find the largest group of people that were in the room together during two or more separate time periods, 
and the times when they were all present.
"""
def together(records):
    # Step 1: Convert raw records into a timeline of employee presence
    employee_presence = defaultdict(list)
    
    for name, time, action in records:
        time = int(time)
        if action == "enter":
            employee_presence[name].append((time, 1))  # 1 for enter
        elif action == "exit":
            employee_presence[name].append((time, -1))  # -1 for exit
    print(employee_presence)
    # Step 2: Process employee presence data to generate time intervals
    employee_intervals = {}
    
    for name, events in employee_presence.items():
        sorted_events = sorted(events)
        intervals = []
        
        # Fix for the case where we have more exits than enters (like John in example 1)
        # or missing exit/enter pairs
        stack = 0
        start_time = None
        
        for time, action in sorted_events:
            stack += action
            
            if stack == 1 and action == 1:  # First enter
                start_time = time
            elif stack == 0 and action == -1 and start_time is not None:  # Last exit for a sequence
                intervals.append((start_time, time))
                start_time = None
        
        # Handle case where employee enters but never exits
        if stack > 0 and start_time is not None:
            intervals.append((start_time, float('inf')))
            
        employee_intervals[name] = intervals
    print("employee intervals")
    print(employee_intervals)
    # Step 3: Find all overlapping time intervals for all possible groups
    all_employees = list(employee_intervals.keys())
    group_intervals = {}
    
    # Check for all possible groups, starting from the largest
    for size in range(len(all_employees), 1, -1):
        for group in combinations(all_employees, size):
            group_set = set(group)
            
            # Get intervals for first employee in the group
            common_intervals = []
            if not employee_intervals[group[0]]:
                continue
                
            for start, end in employee_intervals[group[0]]:
                # Check if this interval overlaps with intervals of all other employees in the group
                valid_interval = True
                actual_start, actual_end = start, end
                
                for other_emp in group[1:]:
                    overlap_found = False
                    
                    for other_start, other_end in employee_intervals[other_emp]:
                        # Find overlap
                        overlap_start = max(start, other_start)
                        overlap_end = min(end, other_end)
                        
                        if overlap_start < overlap_end:
                            overlap_found = True
                            actual_start = max(actual_start, overlap_start)
                            actual_end = min(actual_end, overlap_end)
                            break
                    
                    if not overlap_found:
                        valid_interval = False
                        break
                
                if valid_interval:
                    common_intervals.append((actual_start, actual_end))
            
            if len(common_intervals) >= 2:
                # Sort intervals by start time
                common_intervals.sort()
                # Merge overlapping intervals
                merged = []
                for interval in common_intervals:
                    if not merged or merged[-1][1] < interval[0]:
                        merged.append(interval)
                    else:
                        merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
                
                if len(merged) >= 2:
                    group_intervals[group] = merged
    
    # Step 4: Find the largest group with at least 2 separate time intervals
    result_group = None
    result_intervals = []
    
    for group, intervals in group_intervals.items():
        if len(intervals) >= 2:
            if result_group is None or len(group) > len(result_group):
                result_group = group
                result_intervals = intervals
            # If we have two groups of the same size, choose the one with more intervals
            elif len(group) == len(result_group) and len(intervals) > len(result_intervals):
                result_group = group
                result_intervals = intervals
    
    # Step 5: Format the output
    if result_group:
        # Format group names
        if len(result_group) == 2:
            group_str = f"{result_group[0]}, {result_group[1]}"
        else:
            group_str = ", ".join(result_group[:-1]) + f", and {result_group[-1]}"
        
        # Format intervals
        intervals_str = []
        for start, end in result_intervals:
            if end == float('inf'):
                end_str = "inf"
            else:
                end_str = str(end)
            intervals_str.append(f"{start} to {end_str}")
        
        return f"{group_str}: {', '.join(intervals_str)}"
    else:
        return "No group was found that meets the criteria."

records = [
    ["Curtis", "2", "enter"],
    ["John", "1510", "exit"],
    ["John", "455", "enter"],
    ["John", "512", "exit"],
    ["Jennifer", "715", "exit"],
    ["Steve", "815", "enter"],
    ["John", "930", "enter"],
    ["Steve", "1000", "exit"],
    ["Paul", "1", "enter"],
    ["Angela", "1115", "enter"],
    ["Curtis", "1510", "exit"],
    ["Angela", "2045", "exit"],
    ["Nick", "630", "exit"],
    ["Jennifer", "30", "enter"],
    ["Nick", "30", "enter"],
    ["Paul", "2145", "exit"],
    ["Ben", "457", "enter"],
    ["Ben", "458", "exit"],
    ["Robin", "459", "enter"],
    ["Robin", "500", "exit"]
]
records2 = [
    ["Paul", "1545", "exit"],
    ["Curtis", "1410", "enter"],
    ["Curtis", "222", "enter"],
    ["Curtis", "1630", "exit"],
    ["Paul", "10", "enter"],
    ["Paul", "1410", "enter"],
    ["John", "330", "enter"],
    ["Jennifer", "330", "enter"],
    ["Jennifer", "1410", "exit"],
    ["John", "1410", "exit"],
    ["Curtis", "330", "exit"],
    ["Paul", "330", "exit"],
]

# Run test cases
print(together(records))
#print(together(records2))
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
def find_free_intervals(intervals):
    pass

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

''' 
A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and an instruction for each row and each column. The player has to color each row and column using the corresponding instruction. Each cell can be either black or white, which we will represent as 'B' for black and 'W' for white.

+------------+
| W  W  W  W |
| B  W  W  W |
| B  W  B  B |
| W  W  B  W |
| B  B  W  W |
+------------+

For each row and column, the corresponding instruction gives the lengths of contiguous runs of black ('B') cells. For example, the instruction [ 2, 1 ] for a specific row indicates that there must be a run of two black cells, followed later by another run of one black cell, and the rest of the row is filled with white cells.

These are valid solutions: [ W, B, B, W, B ] and [ B, B, W, W, B ] and also [ B, B, W, B, W ]
This is not valid: [ W, B, W, B, B ] since the runs are not in the correct order.
This is not valid: [ W, B, B, B, W ] since the two runs of Bs are not separated by Ws.

Your job is to write a function to validate a possible solution against a set of instructions. Given a 2D matrix representing a player's solution; and instructions for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

Example solution matrix:

validateNonogram(matrix1, rows1_1, columns1_1) => True

matrix1 ->
                                 rows1_1
                +------------+     
                | W  W  W  W | <-- []
                | B  W  W  W | <-- [1]
                | B  W  B  B | <-- [1,2]
                | W  W  B  W | <-- [1]
                | B  B  W  W | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
               [2,1] | [2] |
  columns1_1        [1]   [1]
       

Example instructions #2

(same matrix as above)
rows1_2    =  [], [], [1], [1], [1,1]
columns1_2 =  [2], [1], [2], [1]
validateNonogram(matrix1, rows1_2, columns1_2) => False

The second, third and last rows and the first column do not match their respective instructions.

All Test Cases:
validateNonogram(matrix1, rows1_1, columns1_1) => True
validateNonogram(matrix1, rows1_2, columns1_2) => False
validateNonogram(matrix1, rows1_3, columns1_3) => False
validateNonogram(matrix1, rows1_4, columns1_4) => False
validateNonogram(matrix1, rows1_5, columns1_5) => False
validateNonogram(matrix1, rows1_6, columns1_6) => False
validateNonogram(matrix1, rows1_7, columns1_7) => False
validateNonogram(matrix1, rows1_8, columns1_8) => False
validateNonogram(matrix2, rows2_1, columns2_1) => False
validateNonogram(matrix2, rows2_2, columns2_2) => False
validateNonogram(matrix2, rows2_3, columns2_3) => False
validateNonogram(matrix2, rows2_4, columns2_4) => False
validateNonogram(matrix2, rows2_5, columns2_5) => True
validateNonogram(matrix2, rows2_6, columns2_6) => False
validateNonogram(matrix3, rows3_1, columns3_1) => True
validateNonogram(matrix3, rows3_2, columns3_2) => False

n: number of rows in the matrix
m: number of columns in the matrix
time: O(mn)
space: O(2mn) - > O(mn)
'''
matrix1 = [
	['W','W','W','W'],
	['B','W','W','W'],
	['B','W','B','B'],
	['W','W','B','W'],
	['B','B','W','W']
]
rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]

rows1_2 = [[],[],[1],[1],[1,1]]
columns1_2 = [[2],[1],[2],[1]]

rows1_3 = [[],[1],[3],[1],[2]]
columns1_3 = [[3],[1],[2],[1]]

rows1_4 = [[],[1,1],[1,2],[1],[2]]
columns1_4 = [[2,1],[1],[2],[1]]

rows1_5 = [[],[1],[1],[1],[2]]
columns1_5 = [[2,1],[1],[2],[1]]

rows1_6 = [[],[1],[2,1],[1],[2]]
columns1_6 = [[2,1],[1],[2],[1]]

rows1_7 = [[],[1],[1,2],[1],[2,1]]
columns1_7 = [[2,1],[1],[2],[1]]

rows1_8 = [[1],[1],[1,2],[1],[2]]
columns1_8 = [[2,1],[1],[2],[1]]

matrix2 = [
	['W','W'],
	['B','B'],
	['B','B'],
	['W','B']
]

rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]

rows2_2 = [[],[2],[2],[1]]
columns2_2 = [[3],[3]]

rows2_3 = [[],[],[],[]]
columns2_3 = [[],[]]

rows2_4= [[],[2],[2],[1]]
columns2_4 = [[2,1],[3]]

rows2_5= [[],[2],[2],[1]]
columns2_5 = [[2],[3]]

rows2_6= [[],[2],[2],[1]]
columns2_6 = [[2],[1,1]]

matrix3 = [
  ['B', 'W', 'B', 'B', 'W', 'B']
]
rows3_1 = [[1, 2, 1]]
columns3_1 = [[1], [], [1], [1], [], [1]]

rows3_2 = [[1, 2, 2]]
columns3_2 = [[1], [], [1], [1], [], [1]]


def is_valid_sudoku(grid):
    n = len(grid)
    
    if n == 0:
        return False
    for row in grid:
        if len(row) != n:
            return False
            
    expected_set = set()
    for i in range(1, n+1):
        expected_set.add(i)
    #print(expected_set)
    # check row 
    for row in grid:
        #print('row')
        #print(set(row))
        #print(expected_set)
        if set(row) != expected_set:
            #print('test row')
            return False
    # check col
    for j in range(n):
        col = [grid[i][j] for i in range(n)]
        #print('col')
        #print(col)
        #print(set(col))
        if set(col) != expected_set:
            #print('test col')
            return False
    return True
    
''' print(is_valid_sudoku(grid1))
print(is_valid_sudoku(grid2))
print(is_valid_sudoku(grid3))
print(is_valid_sudoku(grid4))
print(is_valid_sudoku(grid5))
print(is_valid_sudoku(grid6))
print(is_valid_sudoku(grid7))
print(is_valid_sudoku(grid8))
print(is_valid_sudoku(grid9))
print(is_valid_sudoku(grid10))
print(is_valid_sudoku(grid11))
print(is_valid_sudoku(grid12))
print(is_valid_sudoku(grid13))
print(is_valid_sudoku(grid14))
print(is_valid_sudoku(grid15))
print(is_valid_sudoku(grid16))
print(is_valid_sudoku(grid17))
print(is_valid_sudoku(grid18)) '''


def validateNonogram(matrix1, rows1_1, columns1_1):
    def get_blacks(sequence):
        result = []
        cur_blacks = 0
        
        for e in sequence:
            if e == "B":
                cur_blacks += 1
            elif cur_blacks > 0:
                result.append(cur_blacks)
                cur_blacks = 0
        if cur_blacks > 0:
            result.append(cur_blacks)
        return result
    
    # check rows
    for i, row in enumerate(matrix1):
        comparable_row = get_blacks(row)
        if comparable_row != rows1_1[i]:
            return False
    
    # check cols
    for j in range(len(matrix1[0])):
        col = [matrix1[i][j] for i in range(len(matrix1))]
        comparable_col = get_blacks(col)
        if comparable_col != columns1_1[j]:
            return False
    
    return True
    
print(validateNonogram(matrix1, rows1_1, columns1_1)) #=> True
print(validateNonogram(matrix1, rows1_2, columns1_2)) #=> False
print(validateNonogram(matrix1, rows1_3, columns1_3)) #=> False
print(validateNonogram(matrix1, rows1_4, columns1_4)) #=> False
print(validateNonogram(matrix1, rows1_5, columns1_5)) #=> False
print(validateNonogram(matrix1, rows1_6, columns1_6)) #=> False
print(validateNonogram(matrix1, rows1_7, columns1_7)) #=> False
print(validateNonogram(matrix1, rows1_8, columns1_8)) #=> False
print(validateNonogram(matrix2, rows2_1, columns2_1)) #=> False
print(validateNonogram(matrix2, rows2_2, columns2_2)) #=> False
print(validateNonogram(matrix2, rows2_3, columns2_3)) #=> False
print(validateNonogram(matrix2, rows2_4, columns2_4)) #=> False
print(validateNonogram(matrix2, rows2_5, columns2_5)) #=> True
print(validateNonogram(matrix2, rows2_6, columns2_6)) #=> False
print(validateNonogram(matrix3, rows3_1, columns3_1)) #=> True
print(validateNonogram(matrix3, rows3_2, columns3_2)) #=> False