from typing import List
from collections import deque
#3	Longest Substring Without Repeating Characters	34.8%	Medium	
def lengthOfLongestSubstr(s):
    map = {} # key: char, value: index(latest)
    ans = 0
    substr_start = 0
    for i, c in enumerate(s):
        if c in map and substr_start <= map[c]:
            substr_start += 1
        else:
            ans = max(ans, i-substr_start+1)
        map[c] = i
    return ans

#2781 Length of the Longest Valid Substring	36.7%	Hard	
def longestValidSubstring(word, forbidden):
    pass

#713	Subarray Product Less Than K	51.3%	Medium	

#2962	Count Subarrays Where Max Element Appears at Least K Times	59.2%	Medium	

#1838	Frequency of the Most Frequent Element	45.0%	Medium	

#2444	Count Subarrays With Fixed Bounds	68.1%	Hard	

#239	[重点] Sliding Window Maximum	46.6%	Hard	https://leetcode.com/problems/sliding-window-maximum/
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = []
    q = deque()
    for i in range(n):
        while q and nums[q[-1]] < nums[i]:
            #print(q, i)
            q.pop()
        q.append(i)
        if q[0] == i-k:
            #print(i)
            #print(q, i-k)
            q.popleft()
        if i >= k-1:            
            res.append(nums[q[0]])
    return res

#76	Minimum Window Substring	43.0%	Hard	

#658	Find K Closest Elements	47.4%	Medium	

#2958	Length of Longest Subarray With at Most K Frequency	55.7%	Medium	

#424	Longest Repeating Character Replacement	53.9%	Medium	

#992	Subarrays with K Different Integers	63.1%	Hard	

#930	Binary Subarrays With Sum

# 438. Find all anagrams in a string
"""
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
"""
def findAnagrams(s, p):
    pass