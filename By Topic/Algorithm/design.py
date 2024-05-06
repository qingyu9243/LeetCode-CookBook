# 146	LRU Cache()	42.5%	Medium
"""
LRUCache(int capacity) # evict the least used element
algo: use build-in OrderedDict, move least use element to end every time we use(get,put) it.
     move_to_end(key)
     popitem(last = False) # remove the head of cache, FIFO
get(int key) -> int (time O(1))
put(int key) -> void (time O(1))
"""
from collections import OrderedDict
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]
    
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# 1570	Dot Product of Two Sparse Vectors 89.9%	Medium	
"""

"""     
       
# 380	Insert Delete GetRandom O(1)	54.4%	Medium	
# 588	Design In-Memory File System48.1%	Hard	
# 359	Logger Rate Limiter75.9%	Easy	
# 460	LFU Cache	44.2%	Hard	
# 716	Max Stack45.0%	Hard	
# 346	Moving Average from Data Stream78.3%	Easy	
# 362	Design Hit Counter68.7%	Medium	
# 981	Time Based Key-Value Store	49.4%	Medium	
# 295	Find Median from Data Stream	51.9%	Hard	
# 2296	Design a Text Editor	44.2%	Hard	
# 1166	Design File System62.8%	Medium	
# 642	Design Search Autocomplete System48.9%	Hard	
# 348	Design Tic-Tac-Toe58.0%	Medium	
# 353	Design Snake Game38.8%	Medium	
# 155	Min Stack
####################################################
