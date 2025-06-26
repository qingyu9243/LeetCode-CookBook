# move blocks
from collections import defaultdict
def solve(width, height, num_blocks, grid):
    blocks_map = defaultdict(list)
    right_most = [-1] * height
    for i in range(height):
        for j in range(width):
            if grid[i][j].isdigit():
                right_most[i] = int(grid[i][j])
                blocks_map[int(grid[i][j])].append((i, j))
            elif grid[i][j] == "X":
                right_most[i] = -1
    
    def can_move(block):
        for i, j in blocks_map[block]:
            if right_most[i] != block:
                return False
        return True
    
    for right in right_most:
        if right >= 0:
            if can_move(right):
                return right
    