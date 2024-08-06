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
for word in generator:
    print(word, end=' ')

# 981. Time Based Key-Value Store [medium]
"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

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

class TimeMap:
    def __init__(self) -> None:
        
        pass

    def set(self, key, value, ts):
        pass

    def get(self, key, ts):
        pass

# 729. My Calendar I [medium]
class MyCalender:
    def __init__(self) -> None:
        pass

    def book(self, start, end):
        pass

# 17. letter of combinations of a phone number [medium]
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
def letterComb(digits):
    pass

# 1958. Check if Move is Legal [medium]
def checkMove(board, rMove, cMove, color):
    pass

# 2747. Count Zero Request Servers
"""
You are given an integer n denoting the total number of servers and a 2D 0-indexed integer array logs, where logs[i] = [server_id, time] denotes that the server with id server_id received a request at time time.
You are also given an integer x and a 0-indexed integer array queries.
Return a 0-indexed integer array arr of length queries.length where arr[i] represents the number of servers that did not receive any requests during the time interval [queries[i] - x, queries[i]].
Note that the time intervals are inclusive.
"""
def countServers(n, logs, x, queries):
    pass