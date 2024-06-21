####################################
######     Search In Array    ###### 
####################################
# 704. Binary Search
def binarySearch(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r)//2
        #print(l, mid, r)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return -1
#print(binarySearch([-1,0,3,5,9,12], 0))
#print(binarySearch([5], 5))

# 35. Search Insert Position
def searchInsert(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return l
#print(searchInsert([1,3,5,6], 5))
#print(searchInsert([1,3,5,6], 2))
#print(searchInsert([1,3,5,6], 7))

####################################
######     Rotated Array    ###### 
####################################



####################################
######     Standard Search    ###### 
####################################



####################################
######            Math        ###### 
####################################


####################################
######    Tricky Invariant    ###### 
####################################

####################################
######       As A Tool        ###### 
####################################

####################################
######   On Solution Space    ###### 
####################################

####################################
####  With Dynamic Programming  #### 
####################################


# 1235	Maximum Profit in Job Scheduling	54.6%	Hard

#4	Median of Two Sorted Arrays	40.0%	Hard

#528	Random Pick with Weight	46.8%	Medium	


#2468	Split Message Based on Limit	44.1%	Hard	
#162	Find Peak Element	45.9%	Medium


#2513 Minimize the Maximum of Two Arrays	29.8%	Medium	
#875	Koko Eating Bananas	48.9%	Medium	
#349	Intersection of Two Arrays	74.5%	Easy	
#1268	Search Suggestions System	65.2%	Medium	
#300	Longest Increasing Subsequence	55.3%	Medium	
#1838 Frequency of the Most Frequent Element	45.0%	Medium	
#362	Design Hit Counter68.7%	Medium	
#33	Search in Rotated Sorted Array	40.7%	Medium	
#981	Time Based Key-Value Store	49.4%	Medium	
#287	Find the Duplicate Number 60.8%	Medium	
#2945	Find Maximum Non-decreasing Array Length	15.5%	Hard	
#1011	Capacity To Ship Packages Within D Days	69.4%	Medium	
#34	Find First and Last Position of Element in Sorted Array	44.3%	Medium	
#658	Find K Closest Elements	47.4%	Medium	
#69	Sqrt(x)	38.7%	Easy	
#268	Missing Number	66.8%	Easy	
#2035	Partition Array Into Two Arrays to Minimize Sum Difference	20.2%	Hard	
#410	Split Array Largest Sum