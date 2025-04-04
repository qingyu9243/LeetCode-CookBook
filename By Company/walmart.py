#1. Two Sum-Easy

#3. Longest Substring Without Repeating Characters-Med.

#22. Generate Parentheses Med.

#20. Valid Parentheses-Easy

#407. Trapping Rain Water II-Hard

#716. Max Stack-Hard

#4. Median of Two Sorted Arrays-Hard

#5. Longest Palindromic Substring-Med.

#146. LRU Cache-Med.

#23. Merge k Sorted Lists-Hard

#33. Search in Rotated Sorted Array-Med.

#56. Merge Intervals-Med.

#322. Coin Change-Med.

#362. Design Hit Counter-Med.

#128. Longest Consecutive Sequence-Med.

#387. First Unique Character in a String-Easy

#139. Word Break-Med.

#994. Rotting Oranges-Med.

#12. Integer to Roman-Med.

#14. Longest Common Prefix-Easy

#15. 3Sum-Med.

#543. Diameter of Binary Tree-Easy

#36. Valid Sudoku-Med.

#39. Combination Sum-Med.

#1209. Remove All Adjacent Duplicates in String II-Med.

#41. First Missing Positive-Hard

#300. Longest Increasing Subsequenc-Med.
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

# 49. Group Anagrams-Med.

#50. Pow(x, n)-Med.

#57. Insert Interval-Med.

#67. Add Binary-Easy

#200. Number of Islands-Med.

# 460. LFU Cache-Hard

# 81. Search in Rotated Sorted Array II-Med.

# 341. Flatten Nested List Iterator-Med.

# 215. Kth Largest Element in an Array-Med.

# 730. Count Different Palindromic Subsequences-Hard

# 103. Binary Tree Zigzag Level Order Traversal-Med.

#490. The Maze-Med.
