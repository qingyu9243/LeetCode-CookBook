def solution(balances, requests):
 
    def transfer(i, j, amount):
        if i >= 1 and j >= 1 and i <= len(balances) and j <= len(balances):
            if amount > balances[i-1]:
                return -1
            balances[i-1] -= amount
            balances[j-1] += amount
        else:
            return -1
        
    def deposit(i, amount):
        if i <= 0 or i > len(balances):
            return -1
        balances[i-1] += amount
        
    def withdraw(i, amount):
        if i <= 0 or i > len(balances) or amount > balances[i-1]:
            return -1
        balances[i-1] -= amount
    
    for acct, request in enumerate(requests):
        items = request.split(" ")
        if items[0] == "withdraw":
            if withdraw(int(items[1]), int(items[2])) == -1:
                return [-(acct+1)]
        if items[0] == "deposit":
            if deposit(int(items[1]), int(items[2])) == -1:
                return [-(acct+1)]
        if items[0] == "transfer":
            if transfer(int(items[1]), int(items[2]), int(items[3])) == -1:
                return [-(acct+1)]
    return balances


from collections import Counter
def solution(pattern):
    def valid(s, dot=0):
        parts = s.split(".")
        if len(parts) >= dot+1:
            for part in parts:
                if part == "":
                    return False
            return True
        else:
            return False
    
    def generate(s, i = 0, cur = "", dot=0):
        if i == len(s):
            if valid(cur, dot):
                return 1
            else:
                return 0
        if s[i] != "?":
            return generate(s, i+1, cur+s[i], dot)
        else:
            return 5 * generate(s, i+1, cur+"a", dot) + generate(s, i+1, cur+".")
         
    count = Counter(pattern)
    valids = set(["a", "b", "c", "d", "e", "?", ".", "@"])
    for c in count.keys():
        if c not in valids:
            return 0
    if count["@"] > 1:
        return 0
    elif count["@"] == 1:
        parts = pattern.split("@")
        return generate(parts[0]) * generate(parts[1], 0, "", 1)
    else:
        ans = 0
        for i in range(len(pattern)):
            if (pattern[i]) == "?":
                ans += generate(pattern[:i]) * generate(pattern[i+1:], 0, "", 1)
        return ans
        
