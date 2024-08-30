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
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
"""
requirement:
    1. user can rent a bike
    2. when user return the bike, calculate the cost
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
            rental.end_rental(rental_end_time)
            rental.bike.update_status('available')
        else:
            print("Invalid rental ID or bike already returned.")


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
        self.calculate_cost()

    def calculate_cost(self):
        duration_hours = (self.rental_end_time - self.rental_start_time).total_seconds() / 3600
        self.cost = duration_hours * self.bike.price_per_hour

    
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

# Check rental history and cost
print(user1.rental_history)
print(rental1.cost)

#######################################
#######          Coding         ####### 
#######################################

# 152. Maximum Product Subarray Med.
def maxProductSubarray(nums):
    pass

# 415. Add Strings Easy


# 2235. Add two integers


#1212. Team Scores in Football Tournament Med.
#
#1604. Alert Using Same Key-Card Three or More Times in a One Hour Period Med.
#
#1014. Best Sightseeing Pair  Med.
#
#1244. Design A Leaderboard Med.
#
#1189. Maximum Number of Balloons Easy
#
#1957. Delete Characters to Make Fancy String Easy
#
#2139. Minimum Moves to Reach Target Score Med.
#
#1405. Longest Happy String Med.
#
#1895. Largest Magic Square Med.
#
#1194. Tournament Winners Hard
#
#5. Longest Palindromic Substring Med.
#
#49. Group Anagrams Med.
#
#125. Valid Palindrome Easy
#
#236. Lowest Common Ancestor of a Binary Tree Med.
#
#300. Longest Increasing Subsequence Med.
#
#647. Palindromic Substrings Med.
#
#1456. Maximum Number of Vowels in a Substring of Given Length Med.
#
#2004. The Number of Seniors and Juniors to Join the Company Hard
