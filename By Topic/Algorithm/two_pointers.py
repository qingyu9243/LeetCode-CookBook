#88	Merge Sorted Array	49.6%	Easy 
"""
Algo: 3 pointers
nums1 = [4, 5, 6, 0, 0, 0]
               i         k
nums2 = [2, 5, 6]
               j
"""
def merge(nums1, nums2, m, n):
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0: 
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
    while j >= 0: # if nums2 left, need to add the remaining elements to nums1
        nums1[k] = nums2[j]
        j, k = j-1, k-1


#42	Trapping Rain Water	62.0%	Hard
"""
Algo: two pointers
"""
def  trapWater(heights):
    pass
    #for 

#5	Longest Palindromic Substring	33.8%	Medium	
#408	Valid Word Abbreviation 35.8%	Easy	
#1650	Lowest Common Ancestor of a Binary Tree III 79.6%	Medium	
#1768	Merge Strings Alternately	79.7%	Easy	
#15	3Sum	34.5%	Medium	
#680	Valid Palindrome II	40.6%	Easy	
#11	Container With Most Water	55.2%	Medium	
#1570	Dot Product of Two Sparse Vectors 89.9%	Medium	
#948	Bag of Tokens	58.9%	Medium	
#31	Next Permutation	39.9%	Medium	
#253	Meeting Rooms II51.3%	Medium	
#283	Move Zeroes	61.7%	Easy	
#349	Intersection of Two Arrays	74.5%	Easy	
#125	Valid Palindrome	47.4%	Easy	
#455	Assign Cookies	52.6%	Easy	
#189	Rotate Array	40.6%	Medium	
#295	Find Median from Data Stream	51.9%	Hard	
#26	Remove Duplicates from Sorted Array	55.6%	Easy	
#986	Interval List Intersections	71.6%	Medium	
#443	String Compression	54.4%	Medium	
#647	Palindromic Substrings	70.1%	Medium	
#143	Reorder List w58.7%	Medium	
#202	Happy Number	56.1%	Easy	
#287	Find the Duplicate Number60.8%	Medium	
#18	4Sum	36.3%	Medium	
