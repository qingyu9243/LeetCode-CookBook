# 22. Generate parentheses
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

# 79	Word Search	42.8%	Medium	
"""
algo: dfs/backtrack
"""
def wordSearch(board, word):
    def backtrack(x, y, l):
        if l == len(word):
            return True 
        

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                backtrack(i, j, 1)


# 465	Optimal Account Balancing 49.6%	Hard	

# 51	N-Queens	68.2%	Hard	

# 1239 Maximum Length of a Concatenated String with Unique Characters	54.1%	Medium	
# 140	Word Break II	48.0%	Hard	
# 691	Stickers to Spell Word	48.6%	Hard	
# 39	Combination Sum	71.4%	Medium	
# 78	Subsets	77.5%	Medium	
# 37	Sudoku Solver	61.1%	Hard	
# 212	Word Search II	36.3%	Hard	
# 46	Permutations