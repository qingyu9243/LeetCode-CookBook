"""
Implement a database to store transactions that has following functions:
set(k, v)
get(k)
unset(k)
----------------------------------------------------------------------
begin()
rollback()
commit()

"""
from collections import defaultdict
class database:
    def __init__(self):
        self.data = defaultdict(str)
        self.tmp_data = defaultdict(str) # record the changes after begin
        self.to_delete = set() # record the keys that need to del in self.data
        self.begin_flag = False

    def begin(self):
        self.begin_flag = True

    def rollback(self):
        self.tmp_data = defaultdict(str)
        self.to_delete = set()

    def commit(self):
        self.begin_flag = False
        for d in self.to_delete:
            del self.data[d]
        for k, v in self.tmp_data.items():
            self.data[k] = v
        self.tmp_data = defaultdict(str)
        self.to_delete = set()

    def set(self, k, v):
        if self.begin_flag:
            self.tmp_data[k] = v
        else:
            self.data[k] = v
    
    def unset(self, k):
        if self.begin_flag:
            if k in self.tmp_data:
                del self.tmp_data[k]
            else:
                self.to_delete.add(k)
        else:
            del self.data[k]
    
    def get(self, k):
        if self.begin_flag:
            if k in self.tmp_data:
                return self.tmp_data[k]
        if k not in self.data:
            print("no such key exist.", k)
        return self.data[k]

db = database()
db.set("apple", "kkkk")
print(db.get("apple")) # -> kkkk
db.unset("apple")
print(db.get("apple")) # -> no such key exist, apple
print(db.get("banana")) # -> no such key exist, banana
db.set("pear", "pppp")
## -------- ##
db.begin()
db.set("pear", "pppp2")
db.set("pear", "pppp3")
db.set("apple", "kkkk2")
print(db.get("apple")) # -> "kkkk2"
print(db.get("pear")) # -> "pppp3"
db.rollback()
print(db.get("apple")) # -> None
print(db.get("pear")) # -> "pppp"
db.commit()
## -------- ##
print(db.get("apple")) # -> None
print(db.get("pear")) # -> "pppp"
print(db.data)

# 273. Integer to English Words[H]
def numberToWords(self, num: int) -> str:
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
        'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousand = 'Thousand Million Billion'.split()
    
    def word(num, idx=0):
        if num == 0:
            return []
        if num < 20:
            return [to19[num-1]]
        if num < 100:
            return [tens[num//10-2]] + word(num%10)
        if num < 1000:
            return [to19[num//100-1]] + ['Hundred'] + word(num%100)

        p, r = num//1000, num%1000
        print(p, r)
        space = [thousand[idx]] if p % 1000 !=0 else []
        print(space)
        return word(p, idx+1) + space + word(r)
    return ' '.join(word(num)) or 'Zero'


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
"""
	d = {
		'A': [0, 0, 0],  # initialize array of size len(string)
		'B': [0, 0, 0],
		...
	}
"""
def rankTeams(self, votes) -> str:
    d = {}

    for vote in votes:
        for i, char in enumerate(vote):
            if char not in d:
                d[char] = [0] * len(vote)
            d[char][i] += 1

    voted_names = sorted(d.keys())
    return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))


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

# 2069. Walking Robot Simulation II
class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.dir = 0
        self.dirs = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.width = width - 1
        self.height = height - 1
        self.mid = height + width - 2

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= (self.mid * 2)
        if self.pos > self.mid + self.width:
            self.dir = 3
        elif self.pos > self.mid:
            self.dir = 2
        elif self.pos > self.width:
            self.dir = 1
        elif not self.pos:
            self.dir = 3
        else:
            self.dir = 0

    def getPos(self):
        if self.pos > self.mid + self.width:
            return [0,self.height - (self.pos - self.mid - self.width)]
        elif self.pos > self.mid:
            return [self.width - (self.pos - self.mid) ,self.height]
        elif self.pos > self.width:
            return [self.width, self.pos - self.width]
        else:
            return [self.pos,0]

    def getDir(self) -> str:
        return self.dirs[self.dir]
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

# 804. Unique Morse Code Words[E]
def uniqueMorseRepresentations(self, words) -> int:
    letters = "abcdefghijklmnopqrstuvwxyz"
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_dict = dict(zip(letters, morse_code))
    words2 = []
    for word in words:
        k = ""
        for i in word:
            k += morse_dict[i]
        words2.append(k)
    return len(set(words2))

# 1790. Check if One String Swap Can Make Strings Equal
"""  """
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    for i in range(len(s1)):
        for j in range(i, len(s1)):
            tmp = list(s1)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            if ''.join(tmp) == s2:
                return True
    return False

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
"""A和B长度不同，返回false
A和B长度相同，而且为相同字符串，如果存在任一个字符出现的次数大于1，返回True
A和B长度相同，而且为不同字符串，对应位置组成pair，字母不同的pair数为2，前两个pair相反，返回True"""
def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    if A == B:
        s = set()
        for a in A:
            if a in s:
                return True
            s.add(a)
        return False
    pair = []
    for a, b in zip(A, B):
        if a != b:
            pair.append((a, b))
        if len(pair) > 2:
            return False
    return len(pair) == 2 and pair[0] == pair[1][::-1]    

# 394. Decode String
"""使用栈，每次遇到左括号之后，将当前的数和字母压栈，遇到右括号出栈，
并将当前的字符重复栈中数字的次数，并与之前的字符串进行连接"""
def decodeString(s):
    stack = []
    cur_num = cur_str = ''
    for c in s:
        if c == '[':
            stack.append(cur_str)
            stack.append(int(cur_num))
            cur_num = cur_str = ''
        elif c == ']':
            num = stack.pop()
            prev_str = stack.pop()
            cur_str = prev_str + cur_str * num
        elif c.isdigit():
            cur_num += c
        else:
            cur_str += c
    return cur_str

# 48. Rotate Image
"""先reverse矩阵，之后沿着主对角线两两互换"""
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 139. Work Break
"""dp[i]表示字符串s[:i]是否可分的，dp[len(s)]为所求
dp[i] = any(s[i - l: i] == word and dp[i - l], l = len(word))"""
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for w in wordDict:
            l = len(w)
            if s[i-l:i] == w and dp[i-1]:
                dp[i] = True
                break
    return dp[-1]

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
"""找到松鼠依次把每一颗松子捡起来放到树上的最短total distance"""
def minDistance(height, width, tree, squirrel, nuts):
    def getDist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    total_distance = 0
    for nut in nuts:
        total_distance += 2*getDist(nut, tree)
    ans = float('inf')
    for nut in nuts:
        squirrel_to_nut = getDist(nut, squirrel)
        nut_to_tree = getDist(nut, tree)
        ans = min(ans, total_distance + squirrel_to_nut - nut_to_tree)
    return ans

# 1814. Count Nice Pairs in an Array
from collections import defaultdict
import math
def countNicePairs(self, nums) -> int:
    dic = defaultdict(int)

    for n in nums:
        re_n = int(str(n)[::-1])
        diff = abs(re_n - n)
        dic[diff] += 1

    res = 0
    for value in dic.values():
        res += math.comb(value, 2)
    return res

# 2768. Number of Black Blocks
from collections import Counter
def countBlackBlocks(self, m: int, n: int, coordinates):
    dict1 = defaultdict(int)
    
    for i,j in coordinates:
        for x in range(i-1,i+1):
            for y in range(j-1,j+1):
                if 0 <= x < m-1 and 0 <= y < n-1:
                    dict1[(x,y)] += 1
                    
    dict2 = Counter(dict1.values())
            
    return [(m-1)*(n-1)-sum(dict2.values()),dict2[1],dict2[2],dict2[3],dict2[4]]