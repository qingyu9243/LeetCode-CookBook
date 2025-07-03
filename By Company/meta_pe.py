### Arrays & String
# 1. array split equal sum

# 2. goat latin
def toGoatLatin(S: str) -> str:
    res = []
    for i, word in enumerate(S.split()):
        if word[0].lower() in 'aeiou':
            res.append(word + 'ma' + 'a'*(i + 1))
        else:
            res.append(word[1:] + word[0] + 'ma' + 'a'*(i + 1))
    return ' '.join(res)

# 3. validate palindrome
def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# 438. find all anagrams
def findAnagrams(s, p):
    return

# 161. One edit distance
def isOneEditDistance(s, t):
    return

### Tree Problems
class TreeNode:
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None

# 98. Validate Binary Search Tree


# filter BST

# 426. convert BST to sorted DDL

# binary tree paths
def binaryTreePath(root):
    return

### Permutation & Combinations
def primeProducts(primes):
    return

### Bash Programming
import sys
from collections import deque
# monitor vmstat for vilations that exceed threshold
def process_vmstat(metric, limit, count, window):
    limit = int(limit)
    count = int(count)
    violations = deque()
    headers = []
    first_line_skipped = False
    for line in sys.stdin:
        if line.startswith('procs'):
            headers = next(sys.stdin).split()
            metric_idx = headers.index(metric)
            continue
        if headers and not first_line_skipped:
            first_line_skipped = True
            continue
        #if he
    return


