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