# word ladder:
# find the min steps to transfor a word A to another word B in dictionary. If A cannot be transfored to B, return -1
# example:

# dictionary: "hit", "hot", "hat", "dot","dog","lot","log","cog"
# hit -> cog: hit, 
# "hit" -> "hot" -> "dot" -> "dog" -> cog"
# *it, h*t - > "hot", "hat" -> 
#            -> "*ot" -> "dot", "lot"(here)
#                     "dot" -> "*ot" - end

#                           -> "d*t" - "dot"
#                           -> "do*" -
#                     "lot" 
#                   -> 
#            -> "*at"
# returns 4

# dictionary: dog, log, fog, tag, fox, zoo, 
# dog to fox: dog->fog->fox
# return 2

"""
q = [dog]
set(dog)
dog<=q ([])
q = [(*og, 1), (d*g, 1), do*]
=> [(log, 2), fog]
=> ....
=> [... fox, ...]
=> fox <= [...]
=> 
"""

"""
1. def minSteps(arr, word1, word2):
2. approach: overall alorithm: BFS => Trie+BFS+binary (HARD)
3. how? => dry run 
4. coding
5. back to #3 (verify #4)
6. add some more test cases
"""

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
"""
----- dry run
dic:
{
    3: 2,
    4: 1,
    5: 2,
    2: 1,
}
"""

nums=[
     [3,4,5],
     [3,5,2,100],
     [4,5]
 ]
# => [5]

from typing import DefaultDict
import collections

def findIntersections(nums):
    dic = DefaultDict(int)
    for arr in nums:
        for n in arr:
            dic[n] += 1
    
    res = []
    for k, v in dic.items():
        if v >= len(nums):
            res.append(k)
    return sorted(res)

# Testcases
print(findIntersections(nums))