# 273. Integer to English Words[H]



# 2296. Design a Text Editor[H]
"""
Design a text editor with a cursor that can do the following:
    Add text to where the cursor is.
    Delete text from where the cursor is (simulating the backspace key).
    Move the cursor either left or right.
    When deleting text, only characters to the left of the cursor will be deleted. 
    The cursor will also remain within the actual text and cannot be moved beyond it.
    More formally, we have that 0 <= cursor.position <= currentText.length always holds.
Implement the TextEditor class:
TextEditor() Initializes the object with empty text.
void addText(string text) 
    Appends text to where the cursor is. The cursor ends to the right of text.
int deleteText(int k) 
    Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
string cursorLeft(int k) 
    Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, 
    where len is the number of characters to the left of the cursor.
string cursorRight(int k) 
    Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, 
    where len is the number of characters to the left of the cursor.
"""
class TextEditor:    
    def __init__(self):
        self.cursor = 0
        self.text = ""
    def addText(self, str): # be cautious that the cursor can be placed in any position
        self.text = self.text[:self.cursor] + str + self.text[self.cursor:]
        self.cursor += len(str)

    def deleteText(self, k): # create new cursor
        new_cursor = max(0, self.cursor-k)
        self.text = self.text[:new_cursor] + self.text[self.cursor:]
        diff = self.cursor - new_cursor
        self.cursor = new_cursor
        return diff

    def cursorLeft(self, k):
        self.cursor = max(0, self.cursor-k)
        l = min(10, self.cursor)
        return self.text[self.cursor-l:self.cursor]

    def cursorRight(self, k):
        self.cursor = min(len(self.text), k)
        l = min(10, self.cursor)
        return self.text[self.cursor-l:self.cursor]

# 699. Falling Sqaures[H]


# 2069. Walking Robot Simulation II


# 969. Pancake Sorting
"""每次找最大的煎饼, 先翻到第一个位置, 再翻到最后一个位置, 经过2n次, 可以得到结果"""
def pancakeSort(arr):
    result, n = [], len(arr)
    for k in range(n, 0, -1):
        pos = arr.index(k)
        if pos == k - 1: # this means the element k is already in the ideal position k - 1
            continue # find next k (k-1)
        if pos != 0: #说明需要翻到第一个
            result.append(k)
            arr[:pos+1] = arr[:pos+1][::-1]
        result.append(k) #当前k已经在index 0上了
        arr[:k] = arr[:k][::-1]
    return result

# 490. The Maze
""" DFS 遍历迷宫，注意每次移动只能走到障碍物才能进行下一次移动"""
def hasPath(maze, start, destination):
    m, n = len(maze), len(maze[0])
    visited = set()
    stack = [start]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while stack:
        curx, cury = stack.pop()
        if [curx, cury] == destination:
            return True
        for dirx, diry in directions:
            tx, ty = curx, cury
            while 0 <= tx+dirx < m and 0 <= ty+diry < n and maze[tx+dirx][ty+diry] != 1: # exit the while loop when encounter wall
                tx += dirx
                ty += diry
            if (tx,ty) not in visited:
                visited.add((tx, ty))
                stack.append((tx, ty))
    return False


# 1366. Rank Team by Votes

# 1861. Rotating the Box
"""先把每一行的石头按照重力规律移到右边, 再翻转matrix"""
def rotateBox(self, box):
    # move by gravity 
    m, n = len(box), len(box[0])
    shifted_box = []
    for row in box:
        stone, emtpy = 0, 0
        new_row = []
        for i in range(n):
            if row[i] == '#':
                stone += 1
            if row[i] == '.':
                emtpy += 1
            if row[i] == '*':
                new_row.extend('.'*emtpy)
                new_row.extend('#'*stone)
                stone = 0
                emtpy = 0
        new_row.extend('.'*emtpy)
        new_row.extend('#'*stone)
        shifted_box.append(new_row)
    # shift the matrix
    new_box = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            new_box[i][j] = shifted_box[m-j-1][i]
    return new_box

# 271 Encode and Decode Strings

# 2069

# 804

# 1790

# 359

# 208. Implement Trie(Prefix Tree)
"""字典树的每一个节点都是一个map, key是当前字母, value是所有的子树, 如果一个单词结束, 就在下方插入一个#作为标记"""
class Trie:
    def __init__(self,):
        self.dic = {}

    def insert(self, word):
        "Insert word into the trie."
        cur = self.dic # set pointer cur to the root of trie
        for c in word:
            if c not in cur:
                cur[c] = {} # create a sub dictionary
            cur = cur[c] # move the pointer to the dict that direct from the char
        cur['#'] = True # end the word by add "#"

    def search(self, word):
        "Returns if the word is in the trie."
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur
    
    def startWith(self, prefix):
        "Returns if there is any word in the trie that starts with the given prefix."
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# 64. Minimum Path Sum
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


# 112. Path Sum[E] (return True of False if a path exist)
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum): # recursive
    if not root:
        return False
    targetSum -= root.val
    if targetSum == 0 and not root.left and not root.right:
        return True
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


# 113. Path Sum II (return all paths)
def pathSum(root, targetSum):
    pass

# 859. Buddy Strings[E]

# 394. Decode String

# 48. Rotate Image

# 139. Work Break

# 200. Number of Islands
"""遍历这个矩阵, 每次遇到1的时候意味着遇到了一个新的岛, 结果加一, 并从这个位置开始BSF/DFS把与他相邻的所有格子标成0, 继续遍历"""
def numsIslands(grid):
    def bfs(i, j): # traversal the grid and change the surronding 1 to 0 until can't find any 1s.
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                if 0 <= x + dx < m and 0 <= y + dy < n and grid[x+dx][y+dy] == "1":
                    grid[x+dx][y+dy] = "0"
                    queue.append((x+dx, y+dy))

    m, n =  len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                bfs(i, j)
                res += 1
    return res

# 573. Squirrel Simulation

# 1814. Count Nice Pairs in an Array

# 2768. Number of Black Blocks