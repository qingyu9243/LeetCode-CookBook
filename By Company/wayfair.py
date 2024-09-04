"""
BQ: most like project. most challenging project. conflict. disagreement
LLD: parking lot. 
HLD: URL Shortener. follow-up: how to do analytics? TTL?

SD1: nearby people.
SD2: 抢票系统

SD 长短网址
BQ 常规问题
OOD: 出租单车店
Coding: 两个数相加那道题

coding - add two integer, follow up 逗号
OOD: parking lot
就是design一个parking lot 跟网上说的差不多，没有payment system，面试官感觉不是特别friendly，一直challenge我的design，但是这一轮最后feedback很好，
SD: 这一轮爆炸了。。问的是一个checkin system，你checkin你的location，推荐附近的attractions
之前没有准备过geo这一部分的sys design，确实是不是很会，只能乱编
强行问我geohash这种 那种geo specific的design怎么implement，然后面试官就抓着这部分一直问

https://www.1point3acres.com/bbs/thread-891744-1-1.html
coding: 这真的非常简单的coding. 大概逻辑就是给你product, 你找product coupon有没有. 没有的话去找这个product的parent product, 再找coupon,直到找到为止.
SD: url shorting.  没有考到之前看到的面经yelp的 Quadtree, 很意外, senior也只考这个.
OOD: bike rental


Coding: 判断回文(String s), followup -> return all 最长回文 from the string
BQ: resume project related, conflicts, leader roles. etc.
SD: design YLEP 地点打卡‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍系统
OOD: parking lot

https://www.1point3acres.com/bbs/thread-1083163-1-1.html
第一轮是application design， 题目是设计停车场，要求user story, application workflow, database diagram三个图都要画出来。
第二轮是hackerrank 上的coding, 没有利口原题，是做一个类似coupon的系统，题本身不难，只是要求输出的格式比较严。但要求用java，而我对java不熟所以没做完。
第三轮是system design，要求做一个类似sha‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍zam 的app, 也不难。
第四轮就是manager，问一些behaviour question。

"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

####################################
######       Bike Rental      ######
####################################
"""
https://excalidraw.com/#json=dNJe3KfPNFzGvkZhdtsXI,oWlrAvozR2TXhIMx0j_ipA

requirement:
    1. user can rent a bike
    2. when user return the bike, calculate the cost

需要處理客人是否有欠款，需要可以快查店裡那些車出租了，那些還在，誰租了哪個租了多久，上次租了啥麼車
錢跟租借時間比較難處理一點

OO Design: bike and scooter rental shop
一个rental shop 有两个product
bike: 分size, 大中小
scooter: 分type, electric & gas
要求实现的功能有：
1. add product into inventory
2. create user
3. rent product
4. check for balance for a user (if they owe us money)
5. remove a product from inventory i.e. permanently make a product un-rentalable, for example due to damage
6. return a product
要完成：
class diagram
DB schema
API
sequence diagram
system diagram ??不记得了
follow up: what if we want to open up a new shop

"""

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.rental_history = []

    def rent_bike(self, bike, rental_start_time):
        if bike.check_availability():
            rental = Rental(len(self.rental_history) + 1, self, bike, rental_start_time)
            self.rental_history.append(rental)
            bike.update_status('rented')
            return rental
        else:
            print("Bike is not available for rent.")
            return None

    def return_bike(self, rental_id, rental_end_time):
        rental = next((r for r in self.rental_history if r.rental_id == rental_id), None)
        if rental and rental.rental_end_time is None:
            cost = rental.end_rental(rental_end_time)
            rental.bike.update_status('available')
        else:
            print("Invalid rental ID or bike already returned.")

    def make_payment(self, cost, cash_amount, credit_card_number):

        print("User paid invoice")
        return True
class Payment:
    def __init__(self, cost, transaction_id, datetime):
        pass
    def pay(self):
        pass
class Bike:
    def __init__(self, bike_id, bike_type, price_per_hour):
        self.bike_id = bike_id
        self.bike_type = bike_type
        self.status = 'available'
        self.price_per_hour = price_per_hour

    def check_availability(self):
        return self.status == 'available'

    def update_status(self, new_status):
        self.status = new_status
class Rental:
    def __init__(self, rental_id, user, bike, rental_start_time):
        self.rental_id = rental_id
        self.user = user
        self.bike = bike
        self.rental_start_time = rental_start_time
        self.rental_end_time = None
        self.cost = 0

    def end_rental(self, rental_end_time):
        self.rental_end_time = rental_end_time
        return self.calculate_cost()

    def calculate_cost(self):
        duration_hours = (self.rental_end_time - self.rental_start_time).total_seconds() / 3600
        self.cost = duration_hours * self.bike.price_per_hour
        return self.cost

from datetime import datetime, timedelta
# Create a user
user1 = User(user_id=1, name="Alice", email="alice@example.com")
# Create some bikes
bike1 = Bike(bike_id=101, bike_type="standard", price_per_hour=5)
bike2 = Bike(bike_id=102, bike_type="electric", price_per_hour=10)
# User rents a bike
time_s = datetime.now()
rental1 = user1.rent_bike(bike1, time_s)
# Simulate some time passing...
time_e = time_s + timedelta(hours = 1)
# User returns the bike
user1.return_bike(rental1.rental_id, time_e)
#user1.make_payment(rental1)
# Check rental history and cost
print(user1.rental_history)
print(rental1.cost)

####################################
######       Parking Lot      ######
####################################


#######################################
#######          Coding         ####### 
#######################################

## Coupon ##
"""Java
import java.util.*;

public class CouponFinder {

    public static String findCoupon(List<Map<String, String>> couponMap, List<Map<String, String>> parentMap, String category) {
        // Refactor two map lists into two hashmaps
        Map<String, String> couponMapNew = new HashMap<>();
        for (Map<String, String> coupon : couponMap) {
            String cName = "";
            String cCategory = "";
            for (Map.Entry<String, String> entry : coupon.entrySet()) {
                String k = entry.getKey();
                String v = entry.getValue();
                if (k.equals("Coupon Name")) {
                    cName = v;
                }
                if (k.equals("Category Name")) {
                    cCategory = v;
                }
            }
            couponMapNew.put(cCategory, cName);
        }

        Map<String, String> categoryParent = new HashMap<>();
        for (Map<String, String> parent : parentMap) {
            String categoryName = "";
            String parentName = "";
            for (Map.Entry<String, String> entry : parent.entrySet()) {
                String k = entry.getKey();
                String v = entry.getValue();
                if (k.equals("Category Name")) {
                    categoryName = v;
                }
                if (k.equals("Parent category Name")) {
                    parentName = v;
                }
            }
            categoryParent.put(categoryName, parentName);
        }

        // Find category's coupon (if not, check its parent's recursively)
        String currentCategory = category;
        while (currentCategory != null) {
            if (couponMapNew.containsKey(currentCategory)) {
                return couponMapNew.get(currentCategory);
            }
            currentCategory = categoryParent.getOrDefault(currentCategory, null);
        }

        return null;
    }

    public static void main(String[] args) {
        // Test cases
        List<Map<String, String>> couponMap = List.of(
            Map.of("Coupon Name", "50% off", "Category Name", "Bedding"),
            Map.of("Coupon Name", "BOGO", "Category Name", "Kitchen")
        );

        List<Map<String, String>> parentMap = List.of(
            new HashMap<>(Map.of("Category Name", "Comforter", "Parent category Name", "Bedding")),
            new HashMap<>(Map.of("Category Name", "Kitchen", "Parent category Name", "")),
            new HashMap<>(Map.of("Category Name", "Patio", "Parent category Name", "Garden"))
        );

        System.out.println(findCoupon(couponMap, parentMap, "Kitchen")); //.equals("BOGO");
        System.out.println(findCoupon(couponMap, parentMap, "Comforter"));
        System.out.println(findCoupon(couponMap, parentMap, "Patio"));
    }
}
"""
def findCoupon(coupon_map, parent_map, category):
    # refactor two map lists into two hashtable
    coupon_map_new = {}
    for coupon in coupon_map:
        c_name, c_category = "", ""
        for k, v in coupon.items():
            if k == "Coupon Name":
                c_name = v
            if k == "Category Name":
                c_category = v
        coupon_map_new[c_category] = c_name
    #print(coupon_map_new)

    category_parent = {}
    for parent in parent_map:
        category_name, parent_name = "", ""
        for k, v in parent.items():
            if k == "Category Name":
                category_name = v
            if k == "Parent category Name":
                parent_name = v
        category_parent[category_name] = parent_name
    #print(category_parent)

    # find category's coupon(if not, check its parent's)
    if category in coupon_map_new:
        return coupon_map_new[category]
    elif category in category_parent:
            p_category = category_parent[category]
            if p_category in coupon_map_new:
                return coupon_map_new[p_category]
            else:
                return None
    return None

coupon_map = [{"Coupon Name" : "50% off", "Category Name": "Bedding"}, {"Coupon Name" : "BOGO", "Category Name": "Kitchen"}]
parent_map = [{"Category Name" : "Comforter", "Parent category Name": "Bedding"}, {"Category Name" : "Kitchen", "Parent category Name": None},{"Category Name" : "Patio", "Parent category Name": "Garden"}]
#assert findCoupon(coupon_map, parent_map, "Kitchen") == "BOGO"
#assert findCoupon(coupon_map, parent_map, "Comforter") == "50% off"
#assert findCoupon(coupon_map, parent_map, "Patio") == None

# 152. Maximum Product Subarray Med.
def maxProductSubarray(nums):
    pass

# 415. Add Strings Easy

# 2235. Add two integers


#1604. Alert Using Same Key-Card Three or More Times in a One Hour Period Med.
def alertNames(keyName: List[str], keyTime: List[str]) -> List[str]:
    d, alerts = defaultdict(list), []
    keyTime = map(lambda x: int(x[:2])*60 + int(x[3:]), keyTime) # <-- 1.

    for name,time in zip(keyName,keyTime):                       # <-- 2.
        d[name].append(time)
    
    for name in d:                                               # <-- 3.
        uses = sorted(d[name])
        if any(third - first <= 60 for third, first in zip(uses[2:], uses)):
            alerts.append(name)                                  # <-- 4.

    return sorted(alerts)        
#1014. Best Sightseeing Pair  Med.

#1244. Design A Leaderboard Med.
class Leaderboard:

    def __init__(self):
        self.scores = {}        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score        

    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

#1189. Maximum Number of Balloons Easy
from collections import defaultdict
import math
def maxNumBallons(text):
    Cnt = defaultdict(int)
    for char in text:
        if char in "lo":
            Cnt[char] += 0.5
        elif char in "ban":
            Cnt[char] +=1
    if len(Cnt) < 5:
        return 0
    return math.floor(min(Cnt.values()))

#1957. Delete Characters to Make Fancy String Easy
def makeFancyString(s: str) -> str:
    res = []
    cur_cnt = 0
    for char in s:
        if len(res) > 0 and res[-1] == char:
            if cur_cnt == 2:
                continue
            elif cur_cnt < 2:
                res.append(char)
                cur_cnt += 1
        elif len(res) > 0 and char != res[-1]:
            res.append(char)
            cur_cnt = 1
        else:
            res.append(char)
            cur_cnt = 1
    return "".join(res)

#2139. Minimum Moves to Reach Target Score Med.
def minMoves(target: int, maxDoubles: int) -> int:
    c = 0
    while maxDoubles and  target > 1:
        if target % 2 == 0 and maxDoubles :
            c += 1
            maxDoubles -= 1
            target //= 2
        else:
            target -= 1
            c += 1
    if target>1:
        c += target-1
    return c 

#1405. Longest Happy String Med.
import heapq
"""
use Max-heap to store(-count, 'char') in the max-heap.
"""
def longestDiverseString(a, b, c):
    # Initialize a max heap with negative counts since heapq is a min heap by default
    max_heap = []
    if a > 0:
        heapq.heappush(max_heap, (-a, 'a'))
    if b > 0:
        heapq.heappush(max_heap, (-b, 'b'))
    if c > 0:
        heapq.heappush(max_heap, (-c, 'c'))
    
    result = []
    
    while max_heap:
        count1, char1 = heapq.heappop(max_heap) # Most frequent character

        # Check if we can add two of char1 without forming three consecutive characters
        if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
            if not max_heap:
                break # Can't use char1 and no other chars are left
            count2, char2 = heapq.heappop(max_heap) # Second most frequent character
            result.append(char2)
            count2 += 1 # Used one instance of char2
            
            # Push back the second character if it is still available
            if count2 < 0:
                heapq.heappush(max_heap, (count2, char2))
            
            # Push back the first character
            heapq.heappush(max_heap, (count1, char1))
        else:
            # Add one or two of the most frequent character
            result.append(char1)
            count1 += 1 # Used one instance of char1
            
            if count1 < 0:
                heapq.heappush(max_heap, (count1, char1))
    
    return ''.join(result)    

#1895. Largest Magic Square Med.
def largestMagicSquare(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # Row sum matrix
    rowPrefixSum = [[0]*(n+1) for r in range(m)]
    for r in range(m):
        for c in range(n):
            rowPrefixSum[r][c+1] = rowPrefixSum[r][c] + grid[r][c]
            
    #column sum Matrix        
    columnPrefixSum = [[0]*(m+1) for c in range(n)]
    for c in range(n):
        for r in range(m):
            columnPrefixSum[c][r+1] = columnPrefixSum[c][r] + grid[r][c]
    print(rowPrefixSum)
    print(columnPrefixSum)
    k = min(m, n)

    while k > 1:
        # find top left
        for r in range(m - k + 1):
            for c in range(n - k + 1):
                z = rowPrefixSum[r][c+k] - rowPrefixSum[r][c]
                valid = True
                for i in range(k):
                    if z != rowPrefixSum[r+i][c+k]-rowPrefixSum[r+i][c] or \
                        z != columnPrefixSum[c+i][r+k]-columnPrefixSum[c+i][r]:
                        valid = False
                        break
                if valid:
                    diag0, diag1 = 0, 0
                    for i in range(k):
                        diag0 += grid[r+i][c+i]
                        diag1 += grid[r+i][c+k-i-1]
                    if z == diag0 == diag1:
                        return k
        k -= 1
    return 1

#5. Longest Palindromic Substring Med.

#49. Group Anagrams Med.

#236. Lowest Common Ancestor of a Binary Tree Med.

#300. Longest Increasing Subsequence Med.

#647. Palindromic Substrings Med.
"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""
def countSubstrings(s: str) -> int:
# 0 1 2 3 4  original index
# a b c d e  
# 012345678  expanded index
    res = 0
    l = len(s)
    for mid in range(l * 2 - 1):
        left = mid // 2
        right = left + mid % 2
        print(mid, left, right)
        while left >= 0 and right < l and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        print(mid, left, right)
        print("end")
    print("res",res)
    return res
#print("test")
#countSubstrings("abbc")

#1456. Maximum Number of Vowels in a Substring of Given Length Med.
def maxVowels(s, k):
    vowels = "aeiou"
    ans = 0
    cur_w = s[:k]
    for c in cur_w:
        if c in vowels:
            ans += 1
    cur = ans
    for i in range(k, len(s)):
        if s[i] in vowels:
            cur += 1
        if s[i-k] in vowels:
            cur -= 1
        ans = max(ans, cur)
    return ans
assert maxVowels("abciiidef", 3) == 3

