"""
https://www.1point3acres.com/bbs/thread-1044267-1-1.html
1. 画图，给你一个 input array 都是坐标，需要画一个直角坐标系，input的点，用星号代表
2. system design: 设计一个标记交易的系统，标记本身是提供api，关键在于怎么使用，follow up：如何让用户在标记是不好的情况下，影响最小。体验最好
3. hr：为什么来 okx，经历
4. system design：设计一个ML system，对于用户上传的信息进行加密，follow u‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍p：model更新的时候，怎么保证数据在更新的时候不丢。

https://www.1point3acres.com/bbs/thread-1041187-1-1.html
Find elements of original array from doubled array - https://www.geeksforgeeks.org/find-elements-of-original-array-from-doubled-array/
"""
from collections import Counter
# Find elements of original array from doubled array
def findOriginal(nums):
    nums.sort()
    freq = Counter(nums)
    res = []

    for n in nums:
        if freq[n] > 0:
            if freq[2*n] > 0:
                res.append(n)
                freq[n] -= 1
                freq[2*n] -= 1
    return res
        
print(findOriginal([4, 1, 18, 2, 9, 8]))
print(findOriginal([4, 1, 2, 2, 8, 2, 4, 4]))

