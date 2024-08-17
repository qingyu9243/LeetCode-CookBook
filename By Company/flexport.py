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
Token Game
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
import bisect
class MyCalender: # ds: a list of events sorted. algo: binary search
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if len(self.events) == 0:
            self.events.append([start, end])
            return True

        ind = bisect.bisect(self.events, [start, end])
        if ind > 0:
            if self.events[ind-1][1] > start:
                return False
        if ind < len(self.events):
            if self.events[ind][0] < end:
                return False
        self.events.insert(ind, [start, end])

        return True


#################################################################
   # 17. letter of combinations of a phone number [medium]
#################################################################
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
def letterCombinations(digits: str): # algo: backtrack
    ans = []
    dic = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl",
        "6": "mno", "7": "qprs", "8":"tuv", "9": "wxyz"}
    def backtrack(cur_digit, cur_str):
        if cur_digit == len(digits):
            ans.append(cur_str)
        else:
            char = dic[digits[cur_digit]]
            for c in char:
                backtrack(cur_digit+1, cur_str+c)
    if len(digits) == 0:
        return []
    backtrack(0, "")
    return ans

#################################################################
            # 1958. Check if Move is Legal [medium]
#################################################################
from typing import List
def checkMove(board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
    def isLegal(r, c, direction):
        initial = color
        cur_x, cur_y = r+direction[0], c+direction[1]
        rack = [initial]
        state = 0
        # 0: pending middle, 1: ready for end
        while 0 <= cur_x < len(board) and 0 <= cur_y < len(board[0]):
            cur = board[cur_x][cur_y]
            rack.append(cur)
            if cur == ".":
                return False
            if state == 0:
                if cur == initial:
                    return False
                else:
                    state = 1
            elif state == 1:
                if cur == initial:
                    return True
            cur_x += direction[0]
            cur_y += direction[1]
        return False               

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for di in directions:
        if isLegal(rMove, cMove, di):
            return True
    return False

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


"""
ood设计 让你实现一个城市模拟系统 有道路跟汽车还有红绿灯 汽车沿着一个方向在道路上行驶
"""
class City:
    def __init__(self):
        self.roads = {}
        self.cars = []
        self.lights = []
        self.ts = 0

    def add_road(self, name, road):
        self.roads[name] = road

    def add_light(self, lights):
        self.lights.extend(lights)

    def add_car(self, car):
        self.cars.append(car)


    def simulate(self, time_step=1):
        self.ts += time_step
        print(f"Current time: {self.ts}")
        for light in self.lights:
            light.update()
        exit_cars = []
        for car in self.cars:
            section = self.roads[car.road_name].sections[car.section_idx]
            if car.direction == 0:
                #print(section.next_light[0].direction, self.roads[car.road_name].direction)
                if car.position + car.speed < section.length:
                    car.position += car.speed
                elif not section.next_light[0]:
                    exit_cars.append(car)
                elif section.next_light[0].direction != self.roads[car.road_name].direction:
                    car.position = section.length - 1
                else:
                    if car.section_idx == len(self.roads[car.road_name].sections) - 1:
                        exit_cars.append(car)
                    else:
                        car.position = car.position + car.speed - self.roads[car.road_name].sections[car.section_idx].length
                        car.section_idx += 1
            else:
                if car.position - car.speed >= 0:
                    car.position -= car.speed
                elif not section.next_light[1]:
                    exit_cars.append(car)
                elif section.next_light[1].direction != self.roads[car.road_name].direction:
                    car.position = 0
                else:
                    if car.section_idx == 0:
                        exit_cars.append(car)
                    else:
                        car.position = car.position + car.speed - self.roads[car.road_name].sections[car.section_idx].length
                        car.section_idx -= 1
        for exit_car in exit_cars:
            self.cars.remove(exit_car)
            print(f"{exit_car.name} exited")
        for car in self.cars:
            car.report()

class Road:
    def __init__(self, sections, lights, direction=0):
        self.sections = sections
        self.lights = lights
        self.direction = direction # 0: east-west, 1: north-south
        for i, section in enumerate(self.sections):
            if i < len(self.lights):
                section.next_light.append(self.lights[i])
            if i > 1:
                section.next_light.append(self.lights[i-1])


class Section:
    def __init__(self, length):
        self.length = length
        self.cars = []
        self.next_light = []


class Light:
    def __init__(self, name, direction=0, flip=True):
        self.name = name
        # 0: east-west green
        # 1: north-south green
        self.direction = direction
        self.flip = flip

    def update(self):
        if self.flip:
            self.direction = not self.direction


class Car:
    def __init__(self, name, road_name, section_idx, position=0, speed=1, direction=0):
        self.name = name
        self.road_name = road_name
        self.section_idx = section_idx
        self.position = position
        self.speed = speed
        #-1: east or south
        #1: west or north
        self.direction = direction

    def report(self):
        print(f"{self.name} at {self.road_name} section {self.section_idx} position {self.position}")


city = City()
#lights = [Light("AJ"), Light("BJ")]
lights = [Light("AJ", 1, False), Light("BJ", 1, False)]
city.add_light(lights)
road0 = Road([Section(2), Section(1), Section(1)], lights, 1)
city.add_road("road0", road0)
car = Car("car0", "road0", 0)
city.add_car(car)

for i in range(5):
    city.simulate()

"""
# exchange system


# Intro 
# You are the owner of a container yard, i.e. a facility where ocean containers are stored before and after a sailing, and where carriers store empty containers. You have several clients that store their containers at your location.
# You’d like to build a computer system that helps manage the day-to-day operations of the facility.
# Additionally, you’d like to provide a way for clients to buy and sell containers to each other, which would be a fairly unique feature of your business.

Part 1)
First and foremost, you would like to be able to manage your clients’ inventory. Completion of this part should enable the storage aspect of our facility.
Task: Design and code a solution that satisfies the following requirements:

Keep track of each client (who they are, how many containers they own, their account balance)
Add and remove resources (containers, money) for some client

Note: The real-life attributes of each container are the same: we don’t need to make containers unique and containers can be exchanged between clients freely.

Part 2) 
Next, we would like to implement the order placing functionality.

We will allow two types of orders: BUY and SELL. Orders should include a price, e.g. semantically: "Alice wants to buy a container for $100"

In our system, we want a running log of all orders that were placed, i.e. an order book. This represents the state of all orders placed in the system.

Task: Assume your system receives a stream of orders. Design and code an order book that keeps track of all orders made in the system; use this to write functions for placing "buy" and "sell" orders.

Note: We do not need to actually fill the order at this stage of the problem, but that will be done in the next part, so it might be helpful to think ahead.

Part 3) 

Now, we would like to be able to fill the orders. In order to match a new order with an existing order, the bid price of the buyer must be >= to the ask price of the seller (and vice versa).

Additionally we want to give the best price when fulfilling an incoming order. When a customer places a new order:

If a SELL offer exists that is lower than or equal to the desired BUY price, we should fill at the lower price.

If a BUY offer exists that is higher than or equal to the desired SELL price, we should fill at the higher price.

Task: Update your buy and sell functions to find the best matching offer for an incoming order, and make the appropriate updates to the clients’ accounts.

If no match can be found, we simply add the order to the book as we have been doing in the previous part.

"""
class Client:
    def __init__(self, name):
        self.name = name
        self.container_amount = 0
        self.balance = 0
        
    def add_container(self, amount):
        self.container_amount += amount
        
    def remove_container(self, amount):
        if amount > self.container_amount:
            raise ValueError("Amount remove is larger than client's current containers")
        else:
            self.container_amount -= amount
        
    def ajust_balance(self, dollor_amount):
        self.balance += dollor_amount

#import heapq
purchase_order_history = []
sell_order_history = []

# order_stream = [] # [(client, count, price), ...]
def buy_containers(client, buy_price):
    best_buy_price = float('inf')
    seller_index = -1

    for i, (client, sell_price) in enumerate(sell_order_history):
        if sell_price <= buy_price:
            best_buy_price = min(sell_price, best_buy_price)
            
    if best_buy_price < buy_price: # fulfill order.
        # remove sell order
        
        # add container
        client.add_container(1)
        client.ajust_balance(-best_buy_price)

    else: # add to purchase order
        order_info = (buy_price, client.name)
        #heapq.heappush(purchase_order_history, order_info)
        purchase_order_history.append(order_info)

def sell_containers(client, price):
    
    order_info = [(client.name, price)]
    sell_order_history.append(order_info)
    return
# purchase = [(a, 100), (b, 98), (c, 105)]
# sell = [(a, 100), (b, 98), (c, 105)]


# purchase = [--(bob, 100), --(bob, 105)]
# sell = [--(sarah, 100), (alice, 101), --(li, 98)]

    
################################################       
################################################      
#######           System Design          #######
################################################       
################################################  

# Design a flight reservation system
    

# Design Open Table

# database schema design, avoid double booking
