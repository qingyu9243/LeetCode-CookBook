"""
https://www.1point3acres.com/bbs/thread-1044267-1-1.html
1. 画图，给你一个 input array 都是坐标，需要画一个直角坐标系，input的点，用星号代表
2. system design: 设计一个标记交易的系统，标记本身是提供api，关键在于怎么使用，follow up：如何让用户在标记是不好的情况下，影响最小。体验最好
3. hr：为什么来 okx，经历
4. system design：设计一个ML system，对于用户上传的信息进行加密，follow u‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍p：model更新的时候，怎么保证数据在更新的时候不丢。

https://www.1point3acres.com/bbs/thread-872859-1-1.html
第一面问了一些基本的算法，比如top-k elements from unsorted list，这边说了Quick Select。还有一些Python相关知识，GIL之类。另外问了很多金融产品相关知识
第二面又问了一遍top-k elements from unsorted list，我依然说Quick Select，面试官询问最差情况的时间复杂度，回答O(n^2)，于是要求优化，最后是回答max heap。然后又问了一遍GI‍‍‌‌‌‍‍‌‍‍‌‍‌‍‌‍‍L，线程和进程区别，如何进程间通讯等老生常谈的问题。
HR面就是聊天，没有实际内容。

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

"""
为了在直角坐标系中绘制给定的点，我们需要将这些点绘制在一个图表中，用星号 (*) 来表示这些点。
下面是一个Python脚本，它可以接受一组坐标点，并在终端上输出一个简易的直角坐标系，其中星号表示给定的点。
"""

def plot_points(points):
    # 找到最大和最小的x和y坐标，以确定绘图的范围
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    # 创建一个二维数组（列表的列表），初始化为空白
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # 将点绘制在二维数组上，用星号表示
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'

    # 打印二维数组，形成直角坐标系图
    for row in grid:
        print(' '.join(row))

# 示例输入
points = [(1, 2), (2, 3), (3, 1), (4, 4), (2, 2)]
plot_points(points)