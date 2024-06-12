"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

def findValue(nums, target):
    l, r = 0, len(nums)-1
    #print(l, r)

    while l < r:
        mid = (l + r)//2
        mid_value = nums[mid]
        #print(l, r, mid, mid_value)
        if mid_value == target:
            return mid
        elif mid_value > target:
            r = mid
        else:
            l = mid+1
    #print(l, r)
    return -1

nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12,16,20,22]
target2 = 9
nums3 = [-1,0,3,5,9,12,16,20,22]
target3 = 20
nums4 = [-1,0,3,5,9,12]
target4 = 8
nums5 = [-1,0,3,5,9,12]
target5 = -2
nums6 = [-1,0,3,5,9,12]
target6 = 15
print(findValue(nums1, target1)) # 4
print(findValue(nums2, target2)) # 4
print(findValue(nums3, target3)) # 7
print(findValue(nums4, target4)) # -1
print(findValue(nums5, target5)) # -1
print(findValue(nums6, target6)) # -1