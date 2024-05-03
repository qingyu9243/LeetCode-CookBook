# 42	Trapping Rain Water	62.0%	Hard
"""
Algo: DP.
"""

# 121	Best Time to Buy and Sell Stock	53.6%	[Easy]
"""
Algo: one pass
"""
def maxProfit(prices):
    cur_min = float('inf')
    ans = -float('inf')
    for p in prices:
        cur_min = min(cur_min, p)
        cur_profit = p - cur_min
        ans = max(ans, cur_profit)
    return ans

# 5 Longest Palindromic Substring	33.8%	Medium	

# 1235 Maximum Profit in Job Scheduling	54.6%	Hard	
# 629	K Inverse Pairs Array	50.0%	Hard	
# 70 Climbing Stairs	52.9%	Easy	
# 22	Generate Parentheses	74.5%	Medium	
# 53	Maximum Subarray	50.8%	Medium	
# 935	Knight Dialer	60.1%	Medium	
# 1531	String Compression II	52.7%	Hard	
# 368	Largest Divisible Subset	45.3%	Medium	
# 279	Perfect Squares	54.8%	Medium	
"""
1. DP. dp[n] = min(dp[n-k]) + 1, k is square number
Time: O(n*sqrt(n))
"""
import math
def numSquares(n):
    square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square]+1)
    return dp[-1]

# 85	Maximal Rectangle 50.4%	Hard	
# 1012	Numbers With Repeated Digits	42.0%	Hard	
# 446	Arithmetic Slices II - Subsequence	54.6%	Hard	
# 907	Sum of Subarray Minimums	37.4%	Medium	
# 198	House Robber	51.0%	Medium	
# 300	Longest Increasing Subsequence	55.3%	Medium	
# 1043 Partition Array for Maximum Sum	76.5%	Medium	
# 118	Pascal's Triangle	74.2%	Easy	
# 322	Coin Change	43.9%	Medium	
# 55	Jump Game	38.5%	Medium	
# 465	Optimal Account Balancing 49.6%	Hard	
# 2851 String Transformation	29.1%	Hard	
# 678	Valid Parenthesis String	37.9%	Medium	
# 647	Palindromic Substrings	70.1%	Medium	
# 124	Binary Tree Maximum Path Sum	40.0%	Hard	
# 2571 Minimum Operations to Reduce an Integer to 0	54.6%	Medium	
# 10	Regular Expression Matching	28.2%	Hard	
# 122	Best Time to Buy and Sell Stock II