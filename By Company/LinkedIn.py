
from typing import List
# 432. All O's one data structure

class AllOne:
    def __init__(self) -> None:
        pass
    
    def inc(self, key):
        pass

    def dec(self, key):
        pass

    def getMaxKey(self):
        pass

    def getMinKey(self):
        pass

# 364. Nestest list weight sum II - dfs/bfs
class NestedInteger:
    def __init__(self, value=None):
        #If value is not specified, initializes an empty list.
        #Otherwise initializes a single integer equal to value.
        pass

    def isInteger(self): #-> bool
        #@return True if this NestedInteger holds a single integer, rather than a nested list.
        pass

    def add(self, elem): #-> void
        #Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        pass

    def setInteger(self, value): #-> void
        #Set this NestedInteger to hold a single integer equal to value.
        pass

    def getInteger(self):# -> int
        #@return the single integer that this NestedInteger holds, if it holds a single integer
        #Return None if this NestedInteger holds a nested list
        pass

    def getList(self): #-> List[NestedInteger]
        #@return the nested list that this NestedInteger holds, if it holds a nested list 
        #Return None if this NestedInteger holds a single integer
        pass

def _364_depthSumInverse_dfs(nestedList: List[NestedInteger]):
    integer_with_depth = []

    def dfs_get_max_depth(l, cur_depth):
        max_depth_found = cur_depth

        for item in l:
            if item.isInteger():
                max_depth_found.append((item.getInteger(), cur_depth))
            else:
                sub_list = item.getList()
                sub_depth = dfs_get_max_depth(sub_list, cur_depth+1)
                max_depth_found = max(max_depth_found, sub_depth)
        return max_depth_found

    max_depth = dfs_get_max_depth(nestedList, 1)

    total_sum = 0
    for integer, depth in integer_with_depth:
        weight = max_depth - depth + 1
        total_sum += integer*weight
    return total_sum

def _364_depthSumInverse_bfs(nestedList):
    queue = [(item, 1) for item in nestedList]
    max_depth = 1
    integer_with_depth = []

    while queue:
        item, depth = queue.pop(0)
        max_depth = max(max_depth, depth)
        if item.isInteger():
            integer_with_depth.append((item.getInteger(), depth))
        else:
            for nested_item in item.getList():
                queue.append((nested_item, depth + 1))

    total_sum = 0
    for integer, depth in integer_with_depth:
        weight = max_depth - depth + 1
        total_sum += integer*weight
    return total_sum

# 716. Max Stack


# 20. Valid Parentheses


# 50. Pow(x, n)


# 244. Shortest Word Distance II

# 277. Find the celebrity

# 53. Maximum Subarray

# 127. Word Ladder

# [366]. Find leaves of Binary Tree - dfs
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.value = val
        self.left = left
        self.right = right
def _366_find_tree_leaves(root):
    result = []

    def dfs(node):
        if not node:
            return -1
        # find left and right height
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        # calculate current height
        current_height = max(left_height, right_height) + 1
        # if entry a new level(upper level)
        if len(result) <= current_height:
            result.append([])
        result[current_height].append(node.val)
        return current_height

    dfs(root)
    return result

# 380. Insert Delete GetRandom

# 636. Exclusive TIme of 

# 200. Number of Islands

# 3480. Maximize Subarrays after

# 605. Can place flowers

# 33. Search in Rotated Sorted Array

# 17. letter of comb
def _17_letter_comb():
    pass

# mutation - 

# 156. Binary Tree upside down

# 215. Kth largest element in 

# 256. Paint House

# 272. Closet binary search Tree

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#