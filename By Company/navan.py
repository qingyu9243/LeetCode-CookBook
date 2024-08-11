# 256. Paint House
def paintHouse1(costs):
    n = len(costs)
    dp = [] # dp[red, blue, green] represent the min costs until this house if choose red/blue/green color to paint
    for i in range(3):
        dp.append(costs[0][i])
    
    for i in range(1, n):
        red = costs[i][0] + min(dp[1], dp[2])
        blue = costs[i][1] + min(dp[0], dp[2])
        green = costs[i][2] + min(dp[0], dp[1])

        dp = [red, blue, green]

    return min(dp)
assert paintHouse1([[17,2,17],[16,16,5],[14,3,19]]) == 10
# 265. Paint House II

# 1473. Paint House III

# LRU

