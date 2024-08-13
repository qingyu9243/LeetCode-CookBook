# 256. Paint House
def paintHouse1(costs):
    n = len(costs)
    dp = [] # dp[red, blue, green] represent the min costs until this house if choose red/blue/green color to paint
    for i in range(3):
        dp.append(costs[0][i])
    
    for i in range(1, n):
        red = costs[i][0] + min(dp[1], dp[2])
        blue = costs[i][1] + min(dp[0], dp[2])
        green = costs[i][2] + min(dp[0], dp[1])

        dp = [red, blue, green]

    return min(dp)
assert paintHouse1([[17,2,17],[16,16,5],[14,3,19]]) == 10
# 265. Paint House II

# 1473. Paint House III

# LRU
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict
class LRU_OrderedDic:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key):
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last = False)

class Node:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_DLL:
    def __init__(self) -> None:
        pass

    def remove(self, node):
        pass

    def add_to_head(self, node):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

# 130. Sorrounded Regions.
"""
replace surrounded regions to X.
"""
from collections import deque
def solve(board):

    if not board:
        return
    m, n = len(board), len(board[0])
    stack = []
    for i in range(m):
        if board[i][0] == 'O':
            stack.append((i, 0))
        if board[i][n - 1] == 'O':
            stack.append((i, n - 1))
    for i in range(1, n - 1):
        if board[0][i] == 'O':
            stack.append((0, i))
        if board[m - 1][i] == 'O':
            stack.append((m - 1, i))
    print(stack)
    while stack:
        i, j = stack.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = "#"
            stack += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
    board[:] = [['XO'[c == '#'] for c in row] for row in board]
solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# 1167
"""
ood 设计calendar，然后问了怎么实现给一堆users，怎么找他们共同的available time
"""


"""
Design an Event Manager
my solution:
Class EventManager {
// singleton
var events = [EventName: [UUID: Action]]()
func subscribe(eventName) -> token {}
func unsubscribe(eventName‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍, token) {}
func publish(eventName, Data) {}

"""
class EventManager:
    def __init__(self):
        self.events = [] #(event: action)

    def subscribe(self, eventName):
        pass

    def unsubscribe(self, eventName, token):
        pass

    def publish(self, eventName, data):
        pass

"""
"""
def snake_to_camel_case(snake_str):
    # Identify leading and trailing underscores
    leading_underscores = len(snake_str) - len(snake_str.lstrip('_'))
    trailing_underscores = len(snake_str) - len(snake_str.rstrip('_'))
    
    # Extract the main content between the underscores
    content = snake_str.strip('_')
    print("content", content)
    
    if not content:
        # If the content is empty, return the original string
        return snake_str
    
    # Split the content by underscores
    parts = content.split('_')
    print("parts", parts)

    # Convert to camel case
    camel_case_parts = [parts[0].lower()] + [part.capitalize() for part in parts[1:]]
    camel_case_content = ''.join(camel_case_parts)
    
    # Reassemble the string with the retained leading and trailing underscores
    return '_' * leading_underscores + camel_case_content + '_' * trailing_underscores

# Test cases
#print(snake_to_camel_case("__hello__world___"))  # __helloWorld___
#print(snake_to_camel_case("__hello__"))          # __hello__
#print(snake_to_camel_case("___"))                # ___
#print(snake_to_camel_case("hello"))              # hello
#print(snake_to_camel_case("__hello"))            # __hello
#print(snake_to_camel_case("hello__"))            # hello__
