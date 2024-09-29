# 22. Generate parentheses
"""
algo:backtrack
"""
def generateParentheses(n: int):
    ans = []
    def backtrack(l, r, cur_s):
        if len(cur_s) == 2*n:
            ans.append(cur_s)
        if l < n:
            backtrack(l+1, r, cur_s+'(')
        if l > r:
            backtrack(l, r+1, cur_s+')')
    backtrack(0, 0, "")
    return ans

# 17	Letter Combinations of a Phone Number	60.4%	Medium	
"""
Algo: backtrack, func to store cur_digit and cur_string
"""
def letterComb(digits):
    ans = []
    dic = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl",
    "6": "mno", "7": "qprs", "8":"tuv", "9": "wxyz"}    
    def backtrack(cur_d, cur_s):
        if len(cur_s) == len(digits):
            ans.append(cur_s)
        else:
            chrs = dic[digits[cur_d]]
            for c in chrs:
                backtrack(cur_d+1, cur_s+c)
    if len(digits) == 0:
        return []
    backtrack(0, "")
    return ans
#print(letterComb("23"))

# 79	Word Search	42.8%	Medium	
"""
Check if the word exist in the board
algo: dfs/backtrack
time: O(N*3^L), N is the total number of cells in the board, 
                3 is the 3 directions to search in board
                L is the the length of the word to be matched.
"""
def wordSearch(board, word): # -> True/False
    def dfs(x, y, l): # x y location in the matrix, l: 遍历到word的哪一个位置了
        if l == len(word):
            return True 
        for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dirx < m and 0 <= y + diry < n and flag[x+dirx][y+diry]\
            and board[x+dirx][y+diry] == word[l]:
                flag[x+dirx][y+diry] = False
                if dfs(x+dirx, y+diry, l+1):
                    return True
                flag[x+dirx][y+diry] = True

        return False            

    m, n = len(board), len(board[0])
    flag = [[True]*n for i in range(m)] # available to visit
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                flag[i][j] = False
                if dfs(i, j, 1):
                    return True
                flag[i][j] = True
    return False

# 465	Optimal Account Balancing 49.6%	Hard

# 51	N-Queens	68.2%	Hard


# 1239 Maximum Length of a Concatenated String with Unique Characters	54.1%	Medium

# 140	Word Break II	48.0%	Hard

# 691	Stickers to Spell Word	48.6%	Hard

# 39	Combination Sum	71.4%	Medium

# 78	Subsets	77.5%	Medium

# 37	Sudoku Solver	61.1%	Hard

# 212	Word Search II	36.3%	Hard

# 46	Permutations Medium

# 77. Combinations
"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
def combine(n, k):
    ans = []
    def backtrack(cur_comb, cur_n, cur_k):
        if cur_k == k:
            ans.append(cur_n)
        tmp = cur_comb.append(cur_n)
        backtrack(tmp, cur_n+1, cur_k+1)
    for i in range(1, n+1):
        backtrack([], i, 0)
    return ans