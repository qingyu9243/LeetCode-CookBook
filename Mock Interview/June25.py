
### LeetCode 773
# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. 
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.


# Input: board = [[4,1,2],
#                 [5,0,3]]
# Output: 5
#  "412503"
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:

# After move 1: [[4,1,2],
#                 [0,5,3]]
# After move 2: [[0,1,2],
#                 [4,5,3]]
# After move 3: [[1,0,2],
#                 [4,5,3]]
# After move 4: [[1,2,0],
#                 [4,5,3]]
# After move 5: [[1,2,3],
#                 [4,5,0]]

# set = () # ("412503")
# inital: "412503" -> 142503 -> 
#                     512403 ->
#
from collections import deque

def swap(str, i, j):
    ls = list(str)
    ls[i], ls[j] = ls[j], ls[i]
    return ''.join(ls)

def swapGrid(grid, target):
    m = len(grid)
    n = len(grid[0])

    # convert to string
    start = ""
    for i in range(m):
        for j in range(n):
            start += str(grid[i][j])
    
    end = ""
    for i in range(len(target)):
        for j in range(len(target[0])):
            end += str(target[i][j])

    directions = { # neighors index
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    queue = deque()
    queue.append((start, start.index('0'), 0)) # [start string, location, steps]
    visited = {start}
    while queue:
        current_state, pos, steps  = queue.popleft()
        # check if the current_state is target
        if current_state == end:
            return steps

        # explore neighors
        for neigbor in directions[pos]:
            # swap
            new_state = swap(current_state, pos, neigbor)
            if new_state not in visited:
                queue.append((new_state, neigbor, steps+1))
                visited.add(new_state)
    return -1


target = [[1,2,3], [4,5,0]]

print(swapGrid([[4,1,2],[5,0,3]], target))
print(swapGrid([[1,2,3],[5,4,0]], target))
print(swapGrid([[1,2,3],[4,0,5]], target))
print(swapGrid([[1,3,2],[4,0,5]], target))