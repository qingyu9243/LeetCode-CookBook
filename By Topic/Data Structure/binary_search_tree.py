import copy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 938	Range Sum of BST	86.8%	Easy	
# 426	Convert Binary Search Tree to Sorted Doubly Linked List64.8%	Medium	
# 98	Validate Binary Search Tree	32.9%	Medium	
# 96	Unique Binary Search Trees	61.0%	Medium	
# 270	Closest Binary Search Tree Value51.7%	Easy	
# 501	Find Mode in Binary Search Tree

# Find the longest increasing path in BST
def longestIncreasingPath(root):
    longest = 0
    longest_path = []

    def dfs(root):
        nonlocal longest
        nonlocal longest_path
        left, right = [], []
        if root.left:
            left, _ = dfs(root.left)
            left.append(root.left.val)
        #print(root.val)
        if root.right:
            _, right = dfs(root.right)
            right.insert(0, root.right.val)
    
        if longest < len(left)+len(right):
            longest = len(left)+len(right)
            longest_path = copy.copy(left)
            longest_path.append(root.val)
            longest_path.extend(right)
        print(root.val, left, right)
        return left, right
    dfs(root)
    return longest, longest_path
