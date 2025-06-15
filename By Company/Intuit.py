

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
    pass


# 322. Coin Change

# 146. LRU Cache

# 1760. Minimum Limit of Balls in a Bag

# 236. Lowest Common Ancestor of a Binary Tree

# 66. Plus One

# 739. Daily Temperatures

# 628. Maximum Product of Three Numbers

# [354. Russian Doll Envelopes]

# [759. Employee Free Time]