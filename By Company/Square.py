# 273. Integer to English Words[H]


# 2296. Design a Text Editor[H]


# 699. Falling Sqaures[H]


# 2069. Walking Robot Simulation II


# 969. Pancake Sorting[E]

# 1366. Rank Team by Votes

# 1861. Rotating the Box
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


# 112. Path Sum[E]
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(self, root, targetSum): # recursive
    if not root:
        return False
    targetSum -= root.val
    if targetSum == 0 and not root.left and not root.right:
        return True
    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# 113. Path Sum