class LinkedNode:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

# 146	LRU Cache	42.5%	Medium	
"""
Least Recently Used. Evict the least recently used entry.
"""
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
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
        


# 2	Add Two Numbers	42.8%	Medium	


# 2296	Design a Text Editor	44.2%	Hard	


# 23	Merge k Sorted Lists	52.8%	Hard	
# 716	Max Stack 45.0%	Hard	
# 21	Merge Two Sorted Lists	64.3%	Easy	
# 1171	Remove Zero Sum Consecutive Nodes from Linked List	52.8%	Medium	
# 426	Convert Binary Search Tree to Sorted Doubly Linked List64.8%	Medium	
# 138	Copy List with Random Pointer	56.1%	Medium	
# 206	Reverse Linked List	76.5%	Easy	
# 460	LFU Cache	44.2%	Hard	
# 143	Reorder List


#432	All O`one Data Structure	36.8%	Hard	
#1472	Design Browser History	77.5%	Medium	
#430	Flatten a Multilevel Doubly Linked List

