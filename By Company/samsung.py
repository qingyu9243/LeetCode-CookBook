#300. Longest Increasing Subsequence
def longestIncreasingSebsequence(nums):
    if not nums:
        return 0
    
    # Initialize DP array - dp[i] represents the length of the 
    # longest increasing subsequence ending at index i
    dp = [1] * len(nums)

    # Fill the dp array
    for i in range(1, len(nums)):
        # Check all previous elements
        for j in range(i):
            # If current element is greater than previous element
            # and including it gives a longer subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in dp array
    return max(dp)

# 886. Possible Bipartition

# 785. Is Graph Bipartite?

# 146. LRU Cache
class Node:
    def __init__(self) -> None:
        pass

class LRU:
    def __init__(self) -> None:
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass

# 1. Two Sum
def twoSum(nums, target):
    map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [map[diff], i]
        map[diff] = i
    return []

# 312. Burst Balloons

# 33. Search in Rotated Sorted Array

# 994. Rotting Oranges

#300. Longest Increasing Subsequence

# 42. Trapping Rain Water

# 53. Maximum Subarray

# 23. Merge k Sorted Lists




