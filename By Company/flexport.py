## https://steady-way-fde.notion.site/Flexport-f7ed89d1b8d448d3aa363c6f13531d17#9dd53d08088d4f0392f24695c24b8d42

"""
Given a string, implement a method that given a word in the sentence, randomly return one of its following words. 
Plus, if the given wrod is in the end of the string, the first word is counted as its following word. . Χ
"""

import random
import logging
def word_generator(corpus, num_words):
    # 处理输入为空的情况
    if not corpus:
        return
    
    # 将corpus分割成单词列表
    words = corpus.split()
    
    # 构建字典，记录每个单词后面的可能的单词
    word_dict = {}
    for i in range(len(words)):
        if i < len(words) - 1:
            next_word = words[i + 1]
        else:
            next_word = words[0]  # 最后一个单词的下一个单词是第一个单词
        
        if words[i] in word_dict:
            word_dict[words[i]].append(next_word)
        else:
            word_dict[words[i]] = [next_word]
    logging.info("debug")
    # 随机选择初始单词
    current_word = random.choice(words)
    yield current_word
    print("hi",current_word)

    # 生成后续的单词
    for _ in range(num_words - 1):
        next_word = random.choice(word_dict[current_word])

        yield next_word
        current_word = next_word

# 示例使用
corpus = "the quick brown fox jumps over the lazy dog"
num_words = 3

generator = word_generator(corpus, num_words)
#for word in generator:
#    print(word, end=' ')

""" https://www.1point3acres.com/bbs/thread-1073476-1-1.html
偏向ood设计 让你实现一个城市模拟系统 有道路跟汽车还有红绿灯 汽车沿着一个方向在道路上行驶
红绿灯根据时间来回转换
"""

"""https://www.1point3acres.com/bbs/thread-1068415-1-1.html
题目是类似merge interval，不过换成了schedule ship，需要自己处理io，hackerrank 白板写， follow up是如果出现多个ship的话应该‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍怎么安排。
"""

"""https://www.1point3acres.com/bbs/thread-1076018-1-1.html
给一个集装箱比如1000size，然后我们有各种各样的货物，每个货物都有对应的size，比如说50 80 100，我们需要找到任意一个解，就是所有的货物加起来是集装箱的size，这道题乍一看感觉是背包?但是他要求求‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍任意一个解，
"""

"""
现有一储存货物的仓库，我们定义一次完整的存取流程为 load。
在一个 load 中，包含存入时间 load[0]，取出时间 load[1]，和货物数量 load[2]。
存入时刻视为货物在库，取出时刻认为货物不在库。货物均可视为同一种类。
现有一系列存取行为 loads, 当所有 loads 执行完成后，请返 time 时刻仓库中的货物量。
"""
def checkInventory(loads, ts):
    inventory = 0
    for load in loads:
        if ts >= load[0] and ts < load[1]:
            inventory += load[2]
    return inventory
assert (checkInventory([[1, 5, 10], [2, 6, 5], [5, 7, 7]], 4)) == 15
"""
在前述条件下，现在我们想知道仓库中曾出现的货物的最大值，以及最大值的时间区间。
如果有多个最大值区间，返回其中任意一个即可。
返回格式参考 load 定义, load[0] 为开始时刻, load[1] 为结束时刻, 均为闭区间。load[2] 为最大货物数量。
1 <= loads[i][0], loads[i][1] <= 2^31
"""
def get_max_inventory_in_warehouse(loads):
    events = []
    for t1, t2, amt in loads:
        events.append((t1, amt))
        events.append((t2, -amt))
    events.sort(key = lambda x:(x[0], -x[1]))
    print(events)

    current_inventory = 0
    max_inventory = 0
    max_interval = (0, 0)
    start = None

    i = 0
    while i < len(events):
        cur = events[i][1]
        j = i + 1
        while j < len(events) and events[i][0] == events[j][0]:
            cur += events[j][1]
            j += 1
        if cur > 0:
            current_inventory += cur
            #if current_inventory == max_inventory and start is None:
            #    start = events[i][0]
            if current_inventory > max_inventory:
                max_inventory = current_inventory
                start = events[i][0]
        elif cur < 0:
            if current_inventory == max_inventory and start is not None:
                max_interval = (start, events[i][0])
            current_inventory += cur
            start = None
        i = j
    return max_inventory, max_interval      
#print(get_max_inventory_in_warehouse([[1, 5, 10], [2, 6, 5], [5, 7, 7], [7, 8, 15]]))

"""

"""
from collections import defaultdict
class Player:
    def __init__(self, name, token_dic) -> None:
        self.name = name
        self.token_dic = token_dic # {color: count}
        self.card_list = [] # list of Card
        self.discount_dic = defaultdict(int) # obtained card dic, {color: count}

class Card:
    def __init__(self, name, cost, point, color) -> None:
        self.name = name
        self.cost = cost # [(color, amt), (color2, amt)]
        self.point = point # int
        self.color = color # color

def canPurchase(player, card):
    #print(player.token_dic, player.discount_dic)
    gold_token = player.token_dic['Gold']
    for color, amt in card.cost:
        if color in player.discount_dic: # check discount card first
            amt -= player.discount_dic[color]
            if 0 < amt and amt > player.token_dic[color]:
                if amt > gold_token: # can't purchase
                    return False
                else: # reduce 
                    gold_token -= gold_token - amt
        else: # no discount card
            if amt > player.token_dic[color] + gold_token: # can't purchase
                return False
            else:
                gold_token -= amt - player.token_dic[color]
    return True

def purchase(player, card):
    if canPurchase(player, card):
        for color, amt in card.cost:
            if color in player.discount_dic: # has discount cards, use them first
                amt -= player.discount_dic[color]
                if amt <= 0:
                    continue
            # amt > 0, still need tokens            
            diff = amt - player.token_dic[color]
            if diff > 0:
                player.token_dic[color] = 0
                player.token_dic['Gold'] -= diff
            else:
                player.token_dic[color] = -diff

        player.discount_dic[card.color] += 1
        player.card_list.append(card)
    else:
        raise ValueError(f"Player '{player.name}' cannot purchase the card '{card.name}'.")

    
token_dic_default = {'Red':3, 'Blue':3, 'Black':3, 'Green': 3, 'White': 3, 'Gold': 4}
#discounted_dict = {'Red':1, 'Blue':1}
playerA = Player("playerA", token_dic_default)
card_1 = Card("card_1", [('Red', 5), ('White', 3), ('Blue', 3)], 0, 'Red')
card_2 = Card("card_2", [('Red', 2), ('Green', 1)], 0, 'Blue')
card_3 = Card("card_3", [('Blue', 2)], 1, 'White')
print(canPurchase(playerA, card_1))
purchase(playerA, card_1)
print(canPurchase(playerA, card_2))
purchase(playerA, card_2)
#print(canPurchase(playerA, card_3))
#purchase(playerA, card_3)
print(playerA.token_dic, playerA.discount_dic)



#################################################################
         # 981. Time Based Key-Value Store [medium]   
#################################################################
"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key `key` with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""    
from collections import defaultdict
class TimeMap:
    def __init__(self) -> None:
        """
        self.map = {key: [(ts, value), (ts, value), ...]}
        """
        self.map = defaultdict(list)

    def set(self, key, value, ts):
        self.map[key].append((ts, value))

    def get(self, key, ts):
        # binary search to find the stored value with neareast ts
        #print(self.map)

        arr = self.map[key]
        l, r = 0, len(arr)

        if not arr or ts < arr[0][0]:
            return ""
        if ts >= arr[-1][0]:
            return arr[-1][1]

        while l < r:
            mid = (l+r)//2
            if arr[mid][0] == ts:
                return arr[mid][1]
            elif arr[mid][0] > ts:
                r = mid
            else:
                l = mid+1

        return arr[l-1][1]
    
tmap = TimeMap()
tmap.set("foo", "bar", 1)
assert tmap.get("foo", 1) == "bar"
assert tmap.get("foo", 3) == "bar"

tmap.set("foo", "bar2", 4)
assert tmap.get("foo", 4) == "bar2"
assert tmap.get("foo", 5) == "bar2"

tmap.set("foo","zigzag", 7)
tmap.set("foo","conundrum",8)
tmap.set("foo","hyperbole",9)
tmap.set("foo","blasphemy",11)
assert tmap.get("foo", 10) == "hyperbole"
#print("passed all")

#################################################################
                  # 729. My Calendar I [medium]
#################################################################
"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
"""

class MyCalender: # ds: a list of events sorted. algo: binary search
    def __init__(self) -> None:
        self.events = []

    def book(self, start, end):
        pass


#################################################################
   # 17. letter of combinations of a phone number [medium]
#################################################################
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
def letterComb(digits): # algo: backtrack
    pass

#################################################################
            # 1958. Check if Move is Legal [medium]
#################################################################
def checkMove(board, rMove, cMove, color):
    pass

#################################################################
            # 2747. Count Zero Request Servers
#################################################################
"""
You are given an integer n denoting the total number of servers and a 2D 0-indexed integer array logs, where logs[i] = [server_id, time] denotes that the server with id server_id received a request at time time.
You are also given an integer x and a 0-indexed integer array queries.
Return a 0-indexed integer array arr of length queries.length where arr[i] represents the number of servers that did not receive any requests during the time interval [queries[i] - x, queries[i]].
Note that the time intervals are inclusive.
"""
from collections import defaultdict
def countServers(n, logs, x, queries):
    logs = sorted(logs, key=lambda x: x[1])
    query_sort = sorted(queries.copy())

    cur_map = defaultdict(int)

    start = query_sort[0] - x
    result = defaultdict(int)

    left = 0
    while left < len(logs) and logs[left][1] < start:
        left += 1
    right = left

    for i in range(len(query_sort)):
        start = query_sort[i] - x
        while right < len(logs) and logs[right][1] <= query_sort[i]:
            cur_map[logs[right][0]] += 1
            right += 1
        while left < len(logs) and logs[left][1] < start:
            cur_map[logs[left][0]] -= 1
            if cur_map[logs[left][0]] == 0:
                del cur_map[logs[left][0]]
            left += 1
        if left == len(logs): break
        result[query_sort[i]] = len(cur_map)
        #print(result)
    
    ans = []
    for query in queries:
        ans.append(n - result[query])
    return ans
assert countServers(3, [[2,4],[2,1],[1,2],[3,1]], 2, [3,4,5,6,7,8,9,10]) == [0,1,2,2,3,3,3,3]

#################################################################
            # Meeting Rooms
#################################################################

# 252. meeting room I (easy)
"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""
def meetingRoomsI(intervals):
    intervals.sort()
    for i in range(len(intervals)-1):
        cur, next = intervals[i], intervals[i+1]
        if cur[1] > next[0]:
            return False
    return True

assert meetingRoomsI([[0,30],[5,10],[15,20]]) == False
assert meetingRoomsI([[7,10],[2,4]]) == True

# 253. meeting room II (medium)
"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""
import heapq
def meetingRoomsII(intervals):
    free_rooms = [] # heap initialization
    intervals.sort(key = lambda x:x[0]) # sort by start time

    for i in intervals:
        # need new meeting room
        if free_rooms == [] or free_rooms[0] > i[0]:
            heapq.heappush(free_rooms, i[1]) # add [end] in heap, heap contains the unfinished meetings
        # no need meeting room, update ending time
        else:
            heapq.heapreplace(free_rooms, i[1]) # pop and insert i[1] into the heap
            #free_rooms[0] = i[1]
    return len(free_rooms)

assert meetingRoomsII([[0,30],[5,10],[15,20]]) == 2

## 2402. meeting room III (hard)
"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
"""
def meetingRoomsIII(n, meetings):
    pass