#########################################
####        Tree/Binary Tree         ####
#########################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#----------------------------------------#
#--> Binary Tree Traversal & Structure <--#
#----------------------------------------#
# 94. Binary Tree Inorder Traversal Medium
def _94_inorderTraversal_recursive(root):
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res
def _94_inorderTraversal_iterative(root):
    res = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res
# 102. Binary Tree Level Order Traversal Medium
def _102_levelOrder(root):
    pass
# 103. Binary Tree Zigzag Level Order Traversal Medium
def _103_zigzagLevelOrder(root):
    pass
# 199. Binary Tree Right Side View Medium
def _199_rightSideView(root):
    pass
# 314. Binary Tree Vertical Order Traversal Hard
def _314_verticalOrder(root):
    pass
# 987. Vertical Order Traversal of a Binary Tree Hard
def _987_verticalTraversal(root):
    pass
# 297. Serialize and Deserialize Binary Tree Hard
def _297_serialize(root):
    pass
#----------------------------------------#
#-->        Binary Search Tree        <--#
#----------------------------------------#
# 98. Validate Binary Search Tree Medium
def _98_isValidBST(root):
    pass
# 173. Binary Search Tree Iterator Medium
def _173_BSTIterator(root):
    pass
# 230. Kth Smallest Element in a BST Medium
def _230_kthSmallest(root, k):
    pass
# 235. Lowest Common Ancestor of a BST Easy
def _235_lowestCommonAncestor(root, p, q):
    pass
# 270. Closest Binary Search Tree Value Easy
def _270_closestValue(root, target):
    pass
# 426. Convert Binary Search Tree to Sorted Doubly Linked List Medium
def _426_treeToDoublyList(root):
    pass
# 510. Inorder Successor in BST II Medium
def _510_inorderSuccessor(root, p):
    pass
# 538. Convert BST to Greater Tree Medium
def _538_convertBST(root):
    pass
# 938. Range Sum of BST Easy
def _938_rangeSumBST(root, low, high):
    pass
#----------------------------------------#
#--> Tree Construction & Manipulation <--#
#----------------------------------------#
# 109. Convert Sorted List to Binary Search Tree Medium
def _109_sortedListToBST(head):
    pass
# 116. Populating Next Right Pointers in Each Node Medium
def _116_connect(root):
    pass
# 117. Populating Next Right Pointers in Each Node II Medium
def _117_connect(root):
    pass
# 536. Construct Binary Tree from String Hard
def _536_str2tree(s):
    pass
# 814. Binary Tree Pruning Medium
def _814_pruneTree(root):
    pass
# 1110.Delete Nodes And Return Forest Medium
def _1110_delNodes(root, to_delete):
    pass
# 1485. Clone Binary Tree with Random Pointer Medium
def _1485_cloneTree(root):
    pass
#----------------------------------------#
#-->  Tree Properties & Algorithms  <--#
#----------------------------------------#
# 101. Symmetric Tree Easy
def _101_isSymmetric(root):
    pass
# 111. Minimum Depth of Binary Tree Easy
def _111_minDepth(root):
    pass
# 124. Binary Tree Maximum Path Sum Hard
def _124_maxPathSum(root):
    pass
# 129. Sum Root to Leaf Numbers Medium
def _129_sumNumbers(root):
    pass
# 236. Lowest Common Ancestor of a Binary Tree Medium
def _236_lowestCommonAncestor(root, p, q):
    pass
# 543. Diameter of Binary Tree Easy
def _543_diameterOfBinaryTree(root):
    pass
# 545. Boundary of Binary Tree Medium
def _545_boundaryOfBinaryTree(root):
    pass
# 863. All Nodes Distance K in Binary Tree Medium
def _863_distanceK(root, target, k):
    pass
# 958. Check Completeness of a Binary Tree Medium
def _958_isCompleteTree(root):
    pass
# 968. Binary Tree Cameras Hard
def _968_minCameraCover(root):
    pass
# 1315. Sum of Nodes with Even-Valued Grandparent Medium
def _1315_sumEvenGrandparent(root):
    pass
# 1373. Maximum Sum BST in Binary Tree Hard
def _1373_maxSumBST(root):
    pass    
# 1522. Diameter of N-Ary Tree Medium
def _1522_diameter(root):
    pass
# 1650. Lowest Common Ancestor of a Binary Tree III Medium
def _1650_lowestCommonAncestor(root, p, q):
    pass
# 1644. Lowest Common Ancestor of a Binary Tree II Medium
def _1644_lowestCommonAncestor(root, p, q):
    pass
# 2265. Count Nodes Equal to Average of Subtree Medium
def _2265_countNodes(root):
    pass

#########################################
####          Linked List            ####
#########################################
# 2. Add Two Numbers Medium
def _2_addTwoNumbers(l1, l2):
    pass
# 19. Remove Nth Node From End of List Medium
def _19_removeNthFromEnd(head, n):
    pass
# 21. Merge Two Sorted Lists Easy
def _21_mergeTwoLists(l1, l2):
    pass
# 23. Merge k Sorted Lists Hard
def _23_mergeKLists(lists):
    pass
# 61. Rotate List Medium
def _61_rotateRight(head, k):
    pass
# 138. Copy List with Random Pointer Medium
def _138_copyRandomList(head):
    pass
# 141. Linked List Cycle Easy
def _141_hasCycle(head):
    pass
# 148. Sort List Medium
def _148_sortList(head):
    pass
# 160. Intersection of Two Linked Lists Easy
def _160_getIntersectionNode(headA, headB):
    pass
# 206. Intersection of Two Linked Lists Easy
def _206_reverseList(head):
    pass
# 234. Palindrome Linked List Easy
def _234_isPalindrome(head):
    pass
# 237. Delete Node in a Linked List Easy
def _237_deleteNode(node):
    pass
# 328. Odd Even Linked List Medium
def _328_oddEvenList(head):
    pass
# 708. Insert into a Cyclic Sorted List Medium
def _708_insert(head, insertVal):
    pass
# 876. Middle of the Linked List Easy
def _876_middleNode(head):
    pass

#########################################
####    Array & Matrix Problems      ####
#########################################
#----------------------------------------#
#-->         Array Manipulation       <--#
#----------------------------------------#
"""
- 1. Two Sum (55.7% Easy)
- 15. 3Sum (37.0% Med)
- 16. 3Sum Closest (46.9% Med)
- 18. 4Sum (38.1% Med)
- 26. Remove Duplicates from Sorted Array (60.3% Easy)
- 27. Remove Element (60.0% Easy)
- 53. Maximum Subarray (52.1% Med)
- 66. Plus One (47.5% Easy)
- 73. Set Matrix Zeroes (60.6% Med)
- 75. Sort Colors (67.5% Med)
- 80. Remove Duplicates from Sorted Array II (62.9% Med)
- 88. Merge Sorted Array (52.9% Easy)
- 118. Pascal's Triangle (77.0% Easy)
- 121. Best Time to Buy and Sell Stock (55.2% Easy)
- 122. Best Time to Buy and Sell Stock II (69.4% Med)
- 123. Best Time to Buy and Sell Stock III (51.0% Hard)
- 167. Two Sum II - Input Array Is Sorted (63.4% Med)
- 169. Majority Element (65.7% Easy)
- 189. Rotate Array (43.0% Med)
- 215. Kth Largest Element in an Array (67.9% Med)
- 238. Product of Array Except Self (67.7% Med)
- 268. Missing Number (70.0% Easy)
- 283. Move Zeroes (62.8% Easy)
- 347. Top K Frequent Elements (64.5% Med)
- 349. Intersection of Two Arrays (76.4% Easy)
- 350. Intersection of Two Arrays II (59.0% Easy)
- 384. Shuffle an Array (59.0% Med)
- 561. Array Partition (80.4% Easy)
- 905. Sort Array By Parity (76.3% Easy)
- 977. Squares of a Sorted Array (73.2% Easy)"""
#----------------------------------------#
#-->         Matrix & 2D Array        <--#
#----------------------------------------#
"""
- 48. Rotate Image (77.8% Med)
- 54. Spiral Matrix (53.8% Med)
- 74. Search a 2D Matrix (52.2% Med)
- 240. Search a 2D Matrix II (55.1% Med)
- 498. Diagonal Traverse (63.1% Med)
- 661. Image Smoother (68.3% Easy)
- 766. Toeplitz Matrix (69.4% Easy)
- 1424. Diagonal Traverse II (58.0% Med)"""
#----------------------------------------#
#-->         Subarray Problems        <--#
#----------------------------------------#
"""
- 209. Minimum Size Subarray Sum (49.3% Med)
- 525. Contiguous Array (49.3% Med)
- 560. Subarray Sum Equals K (45.4% Med)
- 643. Maximum Average Subarray I (45.3% Easy)
- 918. Maximum Sum Circular Subarray (47.6% Med)"""

#########################################
####        String Problems          ####
#########################################
#----------------------------------------#
#-->       String Manipulation        <--#
#----------------------------------------#
# 3. Longest Substring Without Repeating Characters Medium
def _3_lengthOfLongestSubstring(s):
    pass
# 5. Longest Palindromic Substring Medium
def _5_longestPalindrome(s):
    pass
# 6. ZigZag Conversion Medium
def _6_convert(s, numRows):
    pass
# 8. String to Integer (atoi) Medium
def _8_myAtoi(s):
    pass
# 13. Roman to Integer Easy
def _13_romanToInt(s):
    pass
# 14. Longest Common Prefix Easy
def _14_longestCommonPrefix(strs):
    pass
# 38. Count and Say Medium
def _38_countAndSay(n):
    pass
# 43. Multiply Strings Medium
def _43_multiply(num1, num2):
    pass
# 58. Length of Last Word Easy
def _58_lengthOfLastWord(s):
    pass
# 67. Add Binary Easy
def _67_addBinary(a, b):
    pass
# 68. Text Justification Hard
def _68_fullJustify(words, maxWidth):
    pass
# 125. Valid Palindrome Easy
def _125_isPalindrome(s):
    pass
# 151. Reverse Words in a String Medium
def _151_reverseWords(s):
    pass
# 415. Add Strings Easy
def _415_addStrings(num1, num2):
    pass
# 647. Palindromic Substrings Medium
def _647_countSubstrings(s):
    pass
# 680. Valid Palindrome II Easy
def _680_validPalindrome(s):
    pass
# 791. Custom Sort String Medium
def _791_customSortString(order, s):
    pass
# 824. Goat Latin Easy
def _824_toGoatLatin(S):
    pass
# 844. Backspace String Compare Easy
def _844_backspaceCompare(S, T):
    pass
# 1071. Greatest Common Divisor of Strings Easy
def _1071_gcdOfStrings(str1, str2):
    pass
#----------------------------------------#
#-->  Pattern Matching & Validation   <--#
#----------------------------------------#
# 65. Valid Number Hard
def _65_isNumber(s):
    pass
# 242. Valid Anagram Easy
def _242_isAnagram(s, t):
    pass
# 246. Strobogrammatic Number Easy
def _246_isStrobogrammatic(num):
    pass
# 247. Strobogrammatic Number II Medium
def _247_strobogrammaticInRange(low, high):
    pass
# 249. Group Shifted Strings Medium
def _249_groupStrings(strings):
    pass
# 408. Valid Word Abbreviation Easy
def _408_validWordAbbreviation(word, abbr):
    pass
# 1216. Valid Palindrome III Hard
def _1216_isValidPalindrome(s, k):
    pass
#----------------------------------------#
#-->        String Algorithms        <--#
#----------------------------------------#
# 49. Group Anagrams Medium
def _49_groupAnagrams(strs):
    pass
# 159. Longest Substring with At Most Two Distinct Characters Medium
def _159_lengthOfLongestSubstringTwoDistinct(s):
    pass
# 271. Encode and Decode Strings Medium
def _271_encode(strs):
    pass
# 394. Decode String Medium
def _394_decodeString(s):
    pass
# 424. Longest Repeating Character Replacement Medium
def _424_characterReplacement(s, k):
    pass
#########################################
####    Binary Search & Two Pointer   ####
#########################################
#----------------------------------------#
#-->         Binary Search            <--#
#----------------------------------------#
"""
- 33. Search in Rotated Sorted Array (42.8% Med)
- 34. Find First and Last Position of Element in Sorted Array (46.8% Med)
- 35. Search Insert Position (48.9% Easy)
- 69. Sqrt(x) (40.3% Easy)
- 81. Search in Rotated Sorted Array II (38.9% Med)
- 153. Find Minimum in Rotated Sorted Array (52.6% Med)
- 162. Find Peak Element (46.5% Med)
- 378. Kth Smallest Element in a Sorted Matrix (63.5% Med)
- 540. Single Element in a Sorted Array (59.2% Med)
- 658. Find K Closest Elements (48.6% Med)
- 852. Peak Index in a Mountain Array (67.6% Med)
- 875. Koko Eating Bananas (49.1% Med)
- 973. K Closest Points to Origin (67.9% Med)
- 1011. Capacity To Ship Packages Within D Days (72.0% Med)
- 1060. Missing Element in Sorted Array (58.7% Med)
- 1283. Find the Smallest Divisor Given a Threshold (63.5% Med)
- 1482. Minimum Number of Days to Make m Bouquets (55.4% Med)
- 1539. Kth Missing Positive Number (62.2% Easy)
- 1891. Cutting Ribbons (52.6% Med)
"""
#----------------------------------------#
#-->          Two Pointers           <--#
#----------------------------------------#
"""
- 11. Container With Most Water (57.7% Med)
- 42. Trapping Rain Water (65.0% Hard)
- 76. Minimum Window Substring (45.3% Hard)
- 633. Sum of Square Numbers (36.5% Med)
- 670. Maximum Swap (51.8% Med)
- 1679. Max Number of K-Sum Pairs (56.2% Med)
"""

#########################################
####       Dynamic Programming       ####
#########################################
#----------------------------------------#
#-->           Classic DP            <--#
#----------------------------------------#
# 416. Partition Equal Subset Sum
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total//2
    # dp[i] 表示能否组成和为i
    dp = [False] * (target+1)
    dp[0] = True # 和为0总是可能的（空集）
    for num in nums:
        # 从后往前，避免重复使用同一个数
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]
    return dp[target]

# 62. Unique Paths (65.7% Med)
def uniquePaths(m, n):
    # dp[i][j] = dp[i][j-]
    return
# 70. Climbing Stairs (53.5% Easy)
# 72. Edit Distance (58.7% Med)
# 91. Decode Ways (36.5% Med)
# 115. Distinct Subsequences (50.0% Hard)
# 120. Triangle (59.2% Med)
# 139. Word Break (48.2% Med)
def wordBreak(s, wordDict):
    """can string s be divided by using words in wordDict"""
    dp = [False] * (1 + len(s))
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]
# 140. Word Break II (53.6% Hard)
def wordBreak2(s, wordDict):
    ans = []
    def backtrack():
        pass

    return ans
# 494. Target Sum (50.7% Med)
# 509. Fibonacci Number (72.9% Easy)
# 790. Domino and Tromino Tiling (52.0% Med)

#----------------------------------------#
#-->          Advanced DP           <--#
#----------------------------------------#
# 32. Longest Valid Parentheses Hard
def _32_longestValidParentheses(s):
    pass
# 85. Maximal Rectangle Hard
def _85_maximalRectangle(matrix):
    pass
# 131. Palindrome Partitioning Medium
def _131_partition(s):
    pass
# 132. Palindrome Partitioning II Hard
def _132_minCut(s):
    pass
# 135. Candy Hard
def _135_candy(ratings):
    pass
# 329. Longest Increasing Path in a Matrix Hard
def _329_longestIncreasingPath(matrix):
    pass
# 354. Russian Doll Envelopes Hard
def _354_maxEnvelopes(envelopes):
    pass
# 368. Largest Divisible Subset Medium
def _368_largestDivisibleSubset(nums):
    pass
# 410. Split Array Largest Sum Hard
def _410_splitArray(nums, m):
    pass
# 689. Maximum Sum of 3 Non-Overlapping Subarrays Hard
def _689_maxSumOfThreeSubarrays(nums, k):
    pass
# 698. Partition to K Equal Sum Subsets Medium
def _698_canPartitionKSubsets(nums, k):
    pass
# 1235. Maximum Profit in Job Scheduling Hard
def _1235_jobScheduling(startTime, endTime, profit):
    pass
#########################################
####          Stack & Queue         ####
#########################################
#----------------------------------------#
#-->         Stack Problems           <--#
#----------------------------------------#
# 20. Valid Parentheses Easy
def _20_isValid(s: str) -> bool:
    pass
# 71. Simplify Path Medium
def _71_simplifyPath(path: str) -> str:
    pass
# 84. Largest Rectangle in Histogram Hard
def _84_largestRectangleArea(heights):
    pass
# 155. Min Stack Easy
def _155_MinStack():
    pass
# 224. Basic Calculator Hard
def _224_calculate(s: str) -> int:
    pass
# 227. Basic Calculator II Medium
def _227_calculate(s: str) -> int:
    pass
# 239. Sliding Window Maximum Hard
def _239_maxSlidingWindow(nums, k):
    pass
# 503. Next Greater Element II Medium
def _503_nextGreaterElements(nums):
    pass
# 556. Next Greater Element III Medium
def _556_nextGreaterElement(n: int) -> int:
    pass
# 636. Exclusive Time of Functions Medium
def _636_exclusiveTime(n, logs):
    pass
# 716. Max Stack Medium
def _716_MaxStack():
    pass
# 735. Asteroid Collision Medium
def _735_asteroidCollision(asteroids):
    pass
# 921. Minimum Add to Make Parentheses Valid Medium
def _921_minAddToMakeValid(S: str) -> int:
    pass
# 946. Validate Stack Sequences Medium
def _946_validateStackSequences(pushed, popped):
    pass
# 1047. Remove All Adjacent Duplicates In String Easy
def _1047_removeDuplicates(S: str) -> str:
    pass
# 1209. Remove All Adjacent Duplicates In String II Medium
def _1209_removeDuplicates(s: str, k: int) -> str:
    pass
# 1249. Minimum Remove to Make Valid Parentheses Medium
def _1249_minRemoveToMakeValid(s: str) -> str:
    pass
# 1944. Number of Visible People in a Queue Medium
def _1944_countVisiblePeople(heights):
    pass
#----------------------------------------#
#-->          Queue & Deque          <--#
#----------------------------------------#
# 239. Sliding Window Maximum Hard
def _239_maxSlidingWindow(nums, k):
    pass
# 346. Moving Average from Data Stream Easy
def _346_MovingAverage(size):
    pass
# 480. Sliding Window Median Hard
def _480_medianSlidingWindow(nums, k):
    pass
#########################################
####         Graph & BFS/DFS         ####
#########################################
#----------------------------------------#
#-->         Graph Traversal          <--#
#----------------------------------------#
# 133. Clone Graph Medium
def _133_cloneGraph(node):
    pass
# 200. Number of Islands Medium
def _200_numIslands(grid):
    pass
# 207. Course Schedule Medium
def _207_canFinish(numCourses, prerequisites):
    pass
# 210. Course Schedule II Medium
def _210_findOrder(numCourses, prerequisites):
    pass
# 261. Graph Valid Tree Medium
def _261_validTree(n, edges):
    pass
# 269. Alien Dictionary Hard
def _269_alienOrder(words):
    pass
# 286. Walls and Gates Medium
def _286_wallsAndGates(rooms):
    pass
# 317. Shortest Distance from All Buildings Hard
def _317_shortestDistance(grid):
    pass
# 399. Evaluate Division Medium
def _399_calcEquation(equations, values, queries):
    pass
# 489. Robot Room Cleaner Hard
def _489_cleanRoom(robot):
    pass
# 684. Redundant Connection Medium
def _684_findRedundantConnection(edges):
    pass
# 695. Max Area of Island Medium
def _695_maxAreaOfIsland(grid):
    pass
# 721. Accounts Merge Medium
def _721_accountsMerge(accounts):
    pass
# 743. Network Delay Time Medium
def _743_networkDelayTime(times, n, k):
    pass
# 778. Swim in Rising Water Hard
def _778_swimInWater(grid):
    pass
# 797. All Paths From Source to Target Medium
def _797_allPathsSourceTarget(graph):
    pass
# 827. Making A Large Island Medium
def _827_largestIsland(grid):
    pass
# 909. Snakes and Ladders Medium
def _909_snakesAndLadders(board):
    pass
# 934. Shortest Bridge Medium
def _934_shortestBridge(grid):
    pass
# 994. Rotting Oranges Medium
def _994_orangesRotting(grid):
    pass
# 1091. Shortest Path in Binary Matrix Medium
def _1091_shortestPathBinaryMatrix(grid):
    pass
# 1254. Number of Closed Islands Medium
def _1254_closedIsland(grid):
    pass
# 1443. Minimum Time to Collect All Apples in a Tree Medium
def _1443_minTime(n, edges, hasApple):
    pass
# 1778. Shortest Path in a Hidden Grid Medium
def _1778_shortestPath(grid, start, end):
    pass
# 1857. Largest Color Value in a Directed Graph Medium
def _1857_largestPathValue(colors, edges):
    pass
# 1926. Nearest Exit from Entrance in Maze Medium
def _1926_nearestExit(maze, entrance):
    pass
# 2192. All Ancestors of a Node in a Directed Acyclic Graph Medium
def _2192_getAncestors(n, edges):
    pass
#----------------------------------------#
#-->        Specialized Graph         <--#
#----------------------------------------#
# 127. Word Ladder Hard
def _127_ladderLength(beginWord, endWord, wordList):
    pass
# 126. Word Ladder II Hard
def _126_findLadders(beginWord, endWord, wordList):
    pass
# 212. Word Search II Hard
def _212_findWords(board, words):
    pass
# 332. Reconstruct Itinerary Medium
def _332_findItinerary(tickets):
    pass
#########################################
####     Data Structure Design        ####
#########################################
import heapq
# 146. LRU Cache Medium

# 295. Find Median from Data Stream Hard
class MedianFinder:
    def __init__(self):
        self.max_heap = [] # (-1, -2, -3)
        self.min_heap = [] # (5, 6, 7)

    def addNum(self, num: int) -> None:
        # step 1. add to appropriate heaps,
        if not self.max_heap or num < -self.max_heap[0]: # prefer to add to max first
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # step 2. balance the heap, max heap only have at most 1 more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        #print(self.max_heap, self.min_heap)
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (self.min_heap[0] - self.max_heap[0])/2

# 303. Range Sum Query - Immutable Easy

# 348. Design Tic-Tac-Toe Medium

# 359. Logger Rate Limiter Easy

# 380. Insert Delete GetRandom O(1) Medium

# 398. Random Pick Index Medium

# 528. Random Pick with Weight Medium

# 703. Kth Largest Element in a Stream Easy

# 981. Time Based Key-Value Store Medium

# 1166. Design File System Medium

# 1570. Dot Product of Two Sparse Vectors Medium

#########################################
####    Math & Number Theory        ####
#########################################
"""
- 7. Reverse Integer (30.3% Med)
- 9. Palindrome Number (59.2% Easy)
- 50. Pow(x, n) (37.0% Med)
- 149. Max Points on a Line (28.9% Hard)
- 166. Fraction to Recurring Decimal (26.2% Med)
- 179. Largest Number (41.2% Med)
- 202. Happy Number (58.0% Easy)
- 282. Expression Add Operators (41.6% Hard)
- 326. Power of Three (48.0% Easy)
- 367. Valid Perfect Square (44.2% Easy)
- 392. Is Subsequence (48.4% Easy)
- 405. Convert a Number to Hexadecimal (50.8% Easy)
- 463. Island Perimeter (73.5% Easy)
- 478. Generate Random Point in a Circle (40.9% Med)
- 564. Find the Closest Palindrome (31.6% Hard)
- 678. Valid Parenthesis String (38.9% Med)
- 724. Find Pivot Index (60.5% Easy)
- 781. Rabbits in Forest (58.3% Med)
- 825. Friends Of Appropriate Ages (49.1% Med)
- 836. Rectangle Overlap (45.7% Easy)
- 838. Push Dominoes (63.0% Med)
- 896. Monotonic Array (61.7% Easy)
"""

#########################################
####    Game Theory & Simulation     ####
#########################################
"""
- 419. Battleships in a Board (76.5% Med)
- 529. Minesweeper (68.1% Med)
- 1094. Car Pooling (56.0% Med)
- 1275. Find Winner on a Tic Tac Toe Game (54.2% Easy)
- 1861. Rotating the Box (79.1% Med)
"""
#########################################
####    Backtracking & Recursion     ####
#########################################
# 17. Letter Combinations of a Phone Number Medium
def _17_letterCombinations(digits: str) -> list[str]:
    pass
# 22. Generate Parentheses Medium
def _22_generateParenthesis(n: int) -> list[str]:
    pass
# 51. N-Queens Hard
def _51_solveNQueens(n: int) -> list[list[str]]:
    pass
# 78. Subsets Medium
def _78_subsets(nums: list[int]) -> list[list[int]]:
    pass
# 90. Subsets II Medium
def _90_subsetsWithDup(nums: list[int]) -> list[list[int]]:
    pass
# 113. Path Sum II Medium
def _113_pathSum(root, targetSum):
    pass
# 301. Remove Invalid Parentheses Hard
def _301_removeInvalidParentheses(s: str) -> list[str]:
    pass
# 784. Letter Case Permutation Medium
def _784_letterCasePermutation(s: str) -> list[str]:
    pass

#########################################
####          Sliding Window         ####
#########################################
"""
- 76. Minimum Window Substring (45.3% Hard)
- 159. Longest Substring with At Most Two Distinct Characters (56.5% Med)
- 209. Minimum Size Subarray Sum (49.3% Med)
- 239. Sliding Window Maximum (47.6% Hard)
- 424. Longest Repeating Character Replacement (57.1% Med)
- 480. Sliding Window Median (38.7% Hard)
- 1004. Max Consecutive Ones III (65.9% Med)
- 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (56.7% Med)
- 1493. Longest Subarray of 1's After Deleting One Element (69.2% Med)
"""

#########################################
####             Intervals           ####
#########################################
"""
- 56. Merge Intervals (49.3% Med)
- 253. Meeting Rooms II (52.1% Med)
- 621. Task Scheduler (61.5% Med)
- 986. Interval List Intersections (72.7% Med)
- 1229. Meeting Scheduler (55.2% Med)
"""

#########################################
####       Trie & Prefix Trees       ####
#########################################
# 212. Word Search II Hard
def _212_findWords(board, words):
    pass
# 1166. Design File System Medium
def _1166_FileSystem():
    pass





