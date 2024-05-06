class DoubleLinkedNode:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = None

# 146	LRU Cache	42.5%	Medium	
"""
Least Recently Used. Evict the least recently used entry.
"""
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.next = self.head

    def get(self, key):
        pass

    def put(self, key, value):
        pass

    def __evit(self, key):
        pass

    def __delete(self, key):
        pass

    def __addToEnd(self, key):
        pass


# 2	Add Two Numbers	42.8%	Medium	
"""
Add two likedlist by adding values up in same location
[2] -> [4] -> [3]
        +
[5] -> [6] -> [4]
==>
[8] -> [0] -> [7]
"""
def addTwoNumbers(l1, l2):
    n1, n2 = l1, l2
    num1, num2 = "", ""
    while n1:
        num1 = str(n1.val) + num1
        n1 = n1.next
    while n2:
        num2 = str(n2.val) + num2
        n2 = n2.next
    num = str(int(num1) + int(num2))

    head = ListNode()
    cur = head
    for i in range(len(num)):
        node = ListNode(num[i])
        cur.next = node
        cur = cur.next
    return head.next

# 23	Merge k Sorted Lists	52.8%	Hard

# 716	Max Stack 45.0%	Hard
# 21	Merge Two Sorted Lists	64.3%	Easy
"""
[1] -> [2] -> [4]
    merge
[1] -> [3] -> [4]
-----------------
[1] -> [1] -> [2] -> [3] -> [4] -> [4]
Merge the two lists into one list, not to create a new list
"""
def mergeTwoLists(l1, l2):
    head = ListNode()
    cur = head
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
    cur.next = l1 if l1 else l2
    return head.next

# 1171	Remove Zero Sum Consecutive Nodes from Linked List	52.8%	Medium	
# 426	Convert Binary Search Tree to Sorted Doubly Linked List64.8%	Medium	
# 138	Copy List with Random Pointer	56.1%	Medium	
# 206	Reverse Linked List	76.5%	Easy	
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
def reverseList(head):
    pass
# 460	LFU Cache	44.2%	Hard	
# 143	Reorder List

#432	All O`one Data Structure	36.8%	Hard	
#1472	Design Browser History	77.5%	Medium	
#430	Flatten a Multilevel Doubly Linked List

