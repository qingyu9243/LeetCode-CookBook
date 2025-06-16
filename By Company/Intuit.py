# 1326. Minimum Number of Taps to Open to Water a Garden
def minTaps(n, ranges):
    pass

# 210. Course Schedule II

# 20. valid parentheses
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in ("(", "{", "["):
            stack.append(char)
        else:
            if stack:
                last = stack.pop()
                if last != mapping[char]:
                    return False
            else:
                return False
    return stack == []

# 139. Word Break
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (1+n)
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]

# 322. Coin Change

# 37. Sudoku Solver

# 994. Rotting Oranges

# 238. Product of Array except self

# 1. two sum

# 54. Spiral Matrix

# 359. Logger Rate Limiter

# 15. 3 Sum

# 155. Min stack

# 300. Longest Increasing Subsequence

# 347. Top K Frequent Elements

# 1760. Minimum Limit of Balls in a Bag

# 236. Lowest Common Ancestor of a Binary Tree

# 66. Plus One

# 739. Daily Temperatures

# 628. Maximum Product of Three Numbers

# [354. Russian Doll Envelopes]

# [759. Employee Free Time]