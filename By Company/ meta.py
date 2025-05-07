
# 1249. Minimum Remove to Make Valid Parentheses Med.
def _1249_minRemoveToMakeValid(s):
    open_count = 0
    result = []

    for char in s: # first pass to remove invalid )
        if char == "(":
            open_count += 1
            result.append(char)
        elif char == ")":
            if open_count > 0:
                open_count -= 1
                result.append(char)
            # if open_count == 0, skip to add
        else:
            result.append(char)
    
    close_count = 0
    final_result = []
    for char in reversed(result): # second pass to remove (
        if char == ")":
            close_count +=1
            final_result.append(char)
        elif char == "(":
            if close_count > 0:
                close_count -= 1
                final_result.append(char)
        else:
            final_result.append(char)

    return "".join(reversed(final_result))
assert _1249_minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"

# 408. Valid Word Abbreviation Easy
def _408_validWordAbb(word, abbr):
    p1 = p2 = 0
    while p1 < len(word) and p2 < len(abbr):
        p1 = 0
    pass

# 314. Binary Tree Vertical Order Traversal Med.
#def 
"""
215. Kth Largest Element in an Array Med.

680. Valid Palindrome II Easy

543. Diameter of Binary Tree Easy

1650. Lowest Common Ancestor of a Binary Tree III Med.

1762. Buildings With an Ocean View Med.

560. Subarray Sum Equals K Med.

227. Basic Calculator II Med.

199. Binary Tree Right Side View Med.

88. Merge Sorted Array Easy

339. Nested List Weight Sum Med.

162. Find Peak Element Med.

236. Lowest Common Ancestor of a Binary Tree Med.

138. Copy List with Random Pointer Med.

50. Pow(x, n) Med.

528. Random Pick with Weight Med.

125. Valid Palindrome Easy

56. Merge Intervals Med.

347. Top K Frequent Elements Med.

71. Simplify Path Med.

129. Sum Root to Leaf Numbers Med.

1. Two Sum Easy

1091. Shortest Path in Binary Matrix Med.

346. Moving Average from Data Stream Easy

146. LRU Cache Med.

1570. Dot Product of Two Sparse Vectors Med.

938. Range Sum of BST
87.4%
Easy

791. Custom Sort String
71.9%
Med.

31. Next Permutation
42.7%
Med.

973. K Closest Points to Origin
67.8%
Med.

827. Making A Large Island
54.5%
Hard

23. Merge k Sorted Lists
56.4%
Hard

670. Maximum Swap
51.8%
Med.

986. Interval List Intersections
72.6%
Med.

121. Best Time to Buy and Sell Stock
55.0%
Easy

1004. Max Consecutive Ones III
65.6%
Med.

34. Find First and Last Position of Element in Sorted Array
46.5%
Med.

65. Valid Number
21.4%
Hard

76. Minimum Window Substring
45.0%
Hard

133. Clone Graph
61.8%
Med.

863. All Nodes Distance K in Binary Tree
66.2%
Med.

987. Vertical Order Traversal of a Binary Tree
50.9%
Hard

921. Minimum Add to Make Parentheses Valid
74.7%
Med.

282. Expression Add Operators
41.4%
Hard

498. Diagonal Traverse
62.9%
Med.

708. Insert into a Sorted Circular Linked List
38.0%
Med.

19. Remove Nth Node From End of List
48.6%
Med.

249. Group Shifted Strings
67.2%
Med.

1539. Kth Missing Positive Number
62.1%
Easy

20. Valid Parentheses
42.1%
Easy

270. Closest Binary Search Tree Value
49.9%
Easy

523. Continuous Subarray Sum
30.8%
Med.

207. Course Schedule
48.9%
Med.

219. Contains Duplicate II
48.7%
Easy

636. Exclusive Time of Functions
64.5%
Med.

480. Sliding Window Median
38.6%
Hard

647. Palindromic Substrings
71.5%
Med.

173. Binary Search Tree Iterator
74.6%
Med.

415. Add Strings
51.8%
Easy

489. Robot Room Cleaner
77.4%
Hard

26. Remove Duplicates from Sorted Array
60.0%
Easy

1768. Merge Strings Alternately
82.2%
Easy

2. Add Two Numbers
45.9%
Med.

200. Number of Islands
62.0%
Med.

4. Median of Two Sorted Arrays
43.4%
Hard

15. 3Sum
36.8%
Med.

224. Basic Calculator
45.3%
Hard

536. Construct Binary Tree from String
58.2%
Med.

426. Convert Binary Search Tree to Sorted Doubly Linked List
65.4%
Med.

398. Random Pick Index
64.4%
Med.

2667. Create Hello World Function
82.1%
Easy

1047. Remove All Adjacent Duplicates In String
71.3%
Easy

8. String to Integer (atoi)
19.0%
Med.

14. Longest Common Prefix
45.2%
Easy

235. Lowest Common Ancestor of a Binary Search Tree
67.9%
Med.

301. Remove Invalid Parentheses
49.1%
Hard

348. Design Tic-Tac-Toe
58.5%
Med.

378. Kth Smallest Element in a Sorted Matrix
63.4%
Med.

721. Accounts Merge
59.2%
Med.

824. Goat Latin
69.3%
Easy

1757. Recyclable and Low Fat Products
89.3%
Easy

3. Longest Substring Without Repeating Characters
36.7%
Med.

9. Palindrome Number
59.0%
Easy

70. Climbing Stairs
53.5%
Easy

78. Subsets
80.6%
Med.

1216. Valid Palindrome III
49.1%
Hard

73. Set Matrix Zeroes
59.4%
Med.

127. Word Ladder
42.4%
Hard

253. Meeting Rooms II
52.1%
Med.

269. Alien Dictionary
36.6%
Hard

295. Find Median from Data Stream
53.1%
Hard

354. Russian Doll Envelopes
37.3%
Hard

392. Is Subsequence
48.3%
Easy

3371. Identify the Largest Outlier in an Array
35.1%
Med.

53. Maximum Subarray
51.9%
Med.

163. Missing Ranges
35.1%
Easy

605. Can Place Flowers
28.9%
Easy

724. Find Pivot Index
60.3%
Easy

958. Check Completeness of a Binary Tree
58.2%
Med.

3527. Find the Most Common Response
73.7%
Med.

33. Search in Rotated Sorted Array
42.6%
Med.

49. Group Anagrams
70.7%
Med.

75. Sort Colors
66.8%
Med.

116. Populating Next Right Pointers in Each Node
65.2%
Med.

126. Word Ladder II
27.1%
Hard

239. Sliding Window Maximum
47.4%
Hard

246. Strobogrammatic Number
47.6%
Easy

658. Find K Closest Elements
48.5%
Med.

2877. Create a DataFrame from List
81.5%
Easy

1094. Car Pooling
56.0%
Med.

21. Merge Two Sorted Lists
66.6%
Easy

139. Word Break
48.1%
Med.

140. Word Break II
53.3%
Hard

169. Majority Element
65.6%
Easy

283. Move Zeroes
62.7%
Easy

2265. Count Nodes Equal to Average of Subtree
86.3%
Med.

317. Shortest Distance from All Buildings
44.2%
Hard

394. Decode String
60.9%
Med.

529. Minesweeper
68.0%
Med.

766. Toeplitz Matrix
69.4%
Easy

1891. Cutting Ribbons
52.3%
Med.

5. Longest Palindromic Substring
35.6%
Med.

66. Plus One
47.3%
Easy

67. Add Binary
55.5%
Easy

74. Search a 2D Matrix
52.0%
Med.

94. Binary Tree Inorder Traversal
78.3%
Easy

122. Best Time to Buy and Sell Stock II
69.2%
Med.

189. Rotate Array
42.8%
Med.

311. Sparse Matrix Multiplication
68.9%
Med.

329. Longest Increasing Path in a Matrix
55.1%
Hard

643. Maximum Average Subarray I
45.1%
Easy

977. Squares of a Sorted Array
73.2%
Easy

1011. Capacity To Ship Packages Within D Days
71.7%
Med.

1110. Delete Nodes And Return Forest
72.4%
Med.

1209. Remove All Adjacent Duplicates in String II
59.4%
Med.

11. Container With Most Water
57.5%
Med.

17. Letter Combinations of a Phone Number
63.5%
Med.

42. Trapping Rain Water
64.7%
Hard

54. Spiral Matrix
53.5%
Med.

124. Binary Tree Maximum Path Sum
41.1%
Hard

148. Sort List
61.4%
Med.

167. Two Sum II - Input Array Is Sorted
63.2%
Med.

234. Palindrome Linked List
55.5%
Easy

247. Strobogrammatic Number II
53.1%
Med.

297. Serialize and Deserialize Binary Tree
58.7%
Hard

380. Insert Delete GetRandom O(1)
54.9%
Med.

510. Inorder Successor in BST II
61.0%
Med.

695. Max Area of Island
73.0%
Med.

704. Binary Search
59.4%
Easy

825. Friends Of Appropriate Ages
49.0%
Med.

934. Shortest Bridge
58.5%
Med.

22. Generate Parentheses
76.9%
Med.

43. Multiply Strings
42.1%
Med.

80. Remove Duplicates from Sorted Array II
62.6%
Med.

117. Populating Next Right Pointers in Each Node II
55.3%
Med.

128. Longest Consecutive Sequence
47.1%
Med.

155. Min Stack
56.2%
Med.

202. Happy Number
57.8%
Easy

210. Course Schedule II
53.1%
Med.

240. Search a 2D Matrix II
54.9%
Med.

242. Valid Anagram
66.4%
Easy

300. Longest Increasing Subsequence
57.5%
Med.

304. Range Sum Query 2D - Immutable
56.3%
Med.

2235. Add Two Integers
88.2%
Easy

341. Flatten Nested List Iterator
65.1%
Med.

419. Battleships in a Board
76.4%
Med.

503. Next Greater Element II
65.9%
Med.

545. Boundary of Binary Tree
47.0%
Med.

2551. Put Marbles in Bags
72.5%
Hard

852. Peak Index in a Mountain Array
67.7%
Med.

905. Sort Array By Parity
76.3%
Easy

1060. Missing Element in Sorted Array
58.5%
Med.

1071. Greatest Common Divisor of Strings
52.6%
Easy

1424. Diagonal Traverse II
57.9%
Med.

1443. Minimum Time to Collect All Apples in a Tree
62.9%
Med.

1868. Product of Two Run-Length Encoded Arrays
59.3%
Med.

13. Roman to Integer
64.6%
Easy

35. Search Insert Position
48.7%
Easy

55. Jump Game
39.3%
Med.

61. Rotate List
39.7%
Med.

101. Symmetric Tree
59.0%
Easy

151. Reverse Words in a String
51.2%
Med.

205. Isomorphic Strings
46.6%
Easy

206. Reverse Linked List
79.0%
Easy

2176. Count Equal and Divisible Pairs in an Array
84.1%
Easy

303. Range Sum Query - Immutable
67.9%
Easy

328. Odd Even Linked List
61.9%
Med.

368. Largest Divisible Subset
48.7%
Med.

399. Evaluate Division
63.0%
Med.

485. Max Consecutive Ones
62.1%
Easy

494. Target Sum
50.5%
Med.

784. Letter Case Permutation
75.0%
Med.

875. Koko Eating Bananas
49.0%
Med.

953. Verifying an Alien Dictionary
55.5%
Easy

509. Fibonacci Number
72.8%
Easy

1079. Letter Tile Possibilities
83.5%
Med.

1229. Meeting Scheduler
55.2%
Med.

2965. Find Missing and Repeated Values
83.7%
Easy

1295. Find Numbers with Even Number of Digits
79.3%
Easy

6. Zigzag Conversion
51.2%
Med.

7. Reverse Integer
30.1%
Med.

16. 3Sum Closest
46.8%
Med.

18. 4Sum
37.9%
Med.

29. Divide Two Integers
18.3%
Med.

38. Count and Say
60.2%
Med.

39. Combination Sum
74.3%
Med.

40. Combination Sum II
57.4%
Med.

51. N-Queens
72.3%
Hard

62. Unique Paths
65.6%
Med.

69. Sqrt(x)
40.2%
Easy

95. Unique Binary Search Trees II
60.1%
Med.

98. Validate Binary Search Tree
34.2%
Med.

102. Binary Tree Level Order Traversal
70.2%
Med.

103. Binary Tree Zigzag Level Order Traversal
61.4%
Med.

118. Pascal's Triangle
76.7%
Easy

123. Best Time to Buy and Sell Stock III
50.7%
Hard

136. Single Number
75.7%
Easy

149. Max Points on a Line
28.7%
Hard

153. Find Minimum in Rotated Sorted Array
52.4%
Med.

198. House Robber
52.2%
Med.

2145. Count the Hidden Sequences
56.7%
Med.

221. Maximal Square
48.5%
Med.

238. Product of Array Except Self
67.6%
Med.

271. Encode and Decode Strings
49.3%
Med.

333. Largest BST Subtree
45.2%
Med.

334. Increasing Triplet Subsequence
39.1%
Med.

2302. Count Subarrays With Score Less Than K
62.5%
Hard

405. Convert a Number to Hexadecimal
50.6%
Easy

416. Partition Equal Subset Sum
48.2%
Med.

424. Longest Repeating Character Replacement
56.8%
Med.

2401. Longest Nice Subarray
64.8%
Med.

435. Non-overlapping Intervals
55.2%
Med.

455. Assign Cookies
53.6%
Easy

490. The Maze
59.3%
Med.

525. Contiguous Array
49.1%
Med.

556. Next Greater Element III
34.5%
Med.

584. Find Customer Referee
71.7%
Easy

2579. Count Total Number of Colored Cells
66.2%
Med.

606. Construct String from Binary Tree
70.0%
Med.

2560. House Robber IV
65.2%
Med.

678. Valid Parenthesis String
38.8%
Med.

733. Flood Fill
66.1%
Easy

763. Partition Labels
81.5%
Med.

705. Design HashSet
66.9%
Easy

865. Smallest Subtree with all the Deepest Nodes
72.4%
Med.

896. Monotonic Array
61.6%
Easy

1008. Construct Binary Search Tree from Preorder Traversal
83.1%
Med.

1028. Recover a Tree From Preorder Traversal
83.3%
Hard

2962. Count Subarrays Where Max Element Appears at Least K Times
62.5%
Med.

3043. Find the Length of the Longest Common Prefix
56.3%
Med.

3174. Clear Digits
82.6%
Easy

1275. Find Winner on a Tic Tac Toe Game
54.1%
Easy

2192. All Ancestors of a Node in a Directed Acyclic Graph
61.9%
Med.

1358. Number of Substrings Containing All Three Characters
73.1%
Med.

1399. Count Largest Group
75.1%
Easy

1493. Longest Subarray of 1's After Deleting One Element
69.1%
Med.

3356. Zero Array Transformation II
43.7%
Med.

1614. Maximum Nesting Depth of the Parentheses
84.3%
Easy

1644. Lowest Common Ancestor of a Binary Tree II
68.5%
Med.

1832. Check if the Sentence Is Pangram
83.8%
Easy

1926. Nearest Exit from Entrance in Maze
47.4%
Med.

27. Remove Element
59.8%
Easy

28. Find the Index of the First Occurrence in a String
44.8%
Easy

32. Longest Valid Parentheses
36.1%
Hard

36. Valid Sudoku
62.0%
Med.

41. First Missing Positive
40.9%
Hard

45. Jump Game II
41.3%
Med.

48. Rotate Image
77.6%
Med.

52. N-Queens II
76.4%
Hard

57. Insert Interval
43.2%
Med.

58. Length of Last Word
56.0%
Easy

59. Spiral Matrix II
73.2%
Med.

72. Edit Distance
58.5%
Med.

82. Remove Duplicates from Sorted List II
49.6%
Med.

84. Largest Rectangle in Histogram
47.0%
Hard

86. Partition List
58.7%
Med.

90. Subsets II
59.2%
Med.

92. Reverse Linked List II
49.4%
Med.

96. Unique Binary Search Trees
62.3%
Med.

109. Convert Sorted List to Binary Search Tree
64.2%
Med.

110. Balanced Binary Tree
55.0%
Easy

113. Path Sum II
60.3%
Med.

120. Triangle
59.0%
Med.

2047. Number of Valid Words in a Sentence
29.9%
Easy

131. Palindrome Partitioning
71.8%
Med.

2071. Maximum Number of Tasks You Can Assign
51.4%
Hard

135. Candy
44.6%
Hard

137. Single Number II
65.0%
Med.

141. Linked List Cycle
52.3%
Easy

2060. Check if an Original String Exists Given Two Encoded Strings
43.1%
Hard

143. Reorder List
62.1%
Med.

144. Binary Tree Preorder Traversal
72.8%
Easy

150. Evaluate Reverse Polish Notation
54.6%
Med.

166. Fraction to Recurring Decimal
26.1%
Med.

179. Largest Number
41.1%
Med.

2104. Sum of Subarray Ranges
60.2%
Med.

182. Duplicate Emails
72.3%
Easy

2119. A Number After a Double Reversal
81.0%
Easy

204. Count Primes
34.6%
Med.

209. Minimum Size Subarray Sum
49.1%
Med.

212. Word Search II
37.2%
Hard

213. House Robber II
43.4%
Med.

2140. Solving Questions With Brainpower
60.3%
Med.

2149. Rearrange Array Elements by Sign
84.3%
Med.

225. Implement Stack using Queues
66.9%
Easy

228. Summary Ranges
52.9%
Easy

229. Majority Element II
54.0%
Med.

231. Power of Two
48.3%
Easy

261. Graph Valid Tree
49.2%
Med.

266. Palindrome Permutation
68.5%
Easy

2256. Minimum Average Difference
43.5%
Med.

332. Reconstruct Itinerary
43.5%
Hard

349. Intersection of Two Arrays
76.3%
Easy

350. Intersection of Two Arrays II
59.0%
Easy

364. Nested List Weight Sum II
65.4%
Med.

383. Ransom Note
64.3%
Easy

402. Remove K Digits
34.7%
Med.

410. Split Array Largest Sum
57.7%
Hard

443. String Compression
57.8%
Med.

460. LFU Cache
46.2%
Hard

463. Island Perimeter
73.4%
Easy

2460. Apply Operations to an Array
74.9%
Easy

516. Longest Palindromic Subsequence
63.9%
Med.

538. Convert BST to Greater Tree
70.4%
Med.

2503. Maximum Number of Points From Grid Queries
59.6%
Hard

542. 01 Matrix
51.1%
Med.

546. Remove Boxes
48.2%
Hard

2523. Closest Prime Numbers in Range
51.5%
Med.

567. Permutation in String
47.0%
Med.

572. Subtree of Another Tree
49.7%
Easy

2537. Count the Number of Good Subarrays
66.1%
Med.

595. Big Countries
68.2%
Easy

602. Friend Requests II: Who Has the Most Friends
60.5%
Med.

610. Triangle Judgement
73.5%
Easy

633. Sum of Square Numbers
36.4%
Med.

2563. Count the Number of Fair Pairs
52.9%
Med.

2570. Merge Two 2D Arrays by Summing Values
82.1%
Easy

661. Image Smoother
68.2%
Easy

671. Second Minimum Node In a Binary Tree
45.2%
Easy

682. Baseball Game
78.6%
Easy

692. Top K Frequent Words
59.1%
Med.

2629. Function Composition
87.0%
Easy

2635. Apply Transform Over Each Element in Array
86.1%
Easy

716. Max Stack
45.4%
Hard

2694. Event Emitter
74.4%
Med.

781. Rabbits in Forest
58.3%
Med.

2799. Count Complete Subarrays in an Array
75.8%
Med.

814. Binary Tree Pruning
72.3%
Med.

622. Design Circular Queue
52.4%
Med.

867. Transpose Matrix
74.0%
Easy

872. Leaf-Similar Trees
70.1%
Easy

876. Middle of the Linked List
80.4%
Easy

478. Generate Random Point in a Circle
40.8%
Med.

886. Possible Bipartition
51.4%
Med.

909. Snakes and Ladders
44.1%
Med.

918. Maximum Sum Circular Subarray
47.3%
Med.

935. Knight Dialer
61.1%
Med.

946. Validate Stack Sequences
69.6%
Med.

2864. Maximum Odd Binary Number
82.7%
Easy

968. Binary Tree Cameras
47.1%
Hard

980. Unique Paths III
82.3%
Hard

981. Time Based Key-Value Store
49.3%
Med.

1044. Longest Duplicate Substring
30.7%
Hard

1074. Number of Submatrices That Sum to Target
74.4%
Hard

1245. Tree Diameter
61.1%
Med.

1141. User Activity for the Past 30 Days I
49.4%
Easy

1331. Rank Transform of an Array
70.6%
Easy

1382. Balance a Binary Search Tree
84.6%
Med.

3108. Minimum Cost Walk in Weighted Graph
68.6%
Hard

1944. Number of Visible People in a Queue
70.9%
Hard

3105. Longest Strictly Increasing or Strictly Decreasing Subarray
65.1%
Easy

3151. Special Array I
81.8%
Easy

1251. Average Selling Price
36.8%
Easy

1268. Search Suggestions System
65.0%
Med.

3272. Find the Count of Good Integers
69.8%
Hard

1415. The k-th Lexicographical String of All Happy Strings of Length n
85.1%
Med.

1431. Kids With the Greatest Number of Candies
88.1%
Easy

1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
56.7%
Med.

1470. Shuffle the Array
88.8%
Easy

1482. Minimum Number of Days to Make m Bouquets
55.4%
Med.

3396. Minimum Number of Operations to Make Elements in Array Distinct
71.6%
Easy

1498. Number of Subsequences That Satisfy the Given Sum Condition
43.7%
Med.

1484. Group Sold Products By The Date
77.6%
Easy

1524. Number of Sub-arrays With Odd Sum
56.1%
Med.

3503. Longest Palindrome After Substring Concatenation I
43.0%
Med.

1752. Check if Array Is Sorted and Rotated
55.0%
Easy

1790. Check if One String Swap Can Make Strings Equal
49.4%
Easy

1838. Frequency of the Most Frequent Element
44.1%
Med.

1861. Rotating the Box
79.0%
Med.

1854. Maximum Population Year
62.5%
Easy
"""
