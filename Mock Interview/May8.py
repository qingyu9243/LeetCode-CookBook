# time to consume

# pipeline: [5, 10, 2, 4, 10, 10] (costs, cpu cycles to accomplish)
# K: max seconds to finish all tasks in the pipeline
# find min CPU capacity/Cycles per seconds
# cpu cycles/s = 16:  [[5, 10], [2,4,10], [10]] => batches = 3
# cpu cycles/s = 5: N/A => -1
#def minCapacity(pipeline, maxSeconds):
    

# ex1: minCapacity(ppl, 4) -> 14?
# ex1: minCapacity(ppl, 3) -> 16?

# [5, 10, 2, 4, 10, 10]
# 14: 5, 10, 6, 10, 10 -> not work
# 15: 15, 6, 10, 10 -> ok.
# total - 41//3 -> math.ceil (14*3= 42, 15) -> max(summary)
# time: O(n^2)
import math
from collections import deque
# optimize on linear search.
def minCapacity(pipeline, maxSeconds):
    low = math.ceil(sum(pipeline)/maxSeconds)
    upper = sum(pipeline)

    def getGroups(num):
        groups = 1
        q = deque(pipeline)
        cur_cap = 0
        
        while q:
            tmp_cost = q.popleft()
            cur_cap += tmp_cost
            if cur_cap > num:
                groups += 1
                cur_cap = tmp_cost

        return groups

    while low < upper:
        mid = (low+upper)//2
        if getGroups(mid) <= maxSeconds:
            upper = mid
        else:
            low = mid+1
            
    return low

pipeline = [5, 10, 2, 4, 10, 10]
maxSeconds = 3
print(minCapacity(pipeline, 3)) # 16
print(minCapacity(pipeline, 4)) # 14