# 146. LRU cache - least recently used cache.
class Node:
    def __init__(self, key = None, value = None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = {} # key -> value(node's reference)
        self.head = Node()
        self.tail = Node()
        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value): # O(1) time
        if key in self.cache: # exist, update the node value and location
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else: # new node
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
        
    def get(self, key): # O(1) time
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
        return -1

    def _remove(self, node):
        # head <-> n1 <-> n2 <-> tail
        # remove the node from double linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add_to_head(self, node):
        # head <-> n1 <-> n2 <-> tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node










## product prices ##
class ProductPrice:
    def __init__(self) -> None:
        self.prices = []
        self.min = float('inf')
        self.max = float('-inf')

    def update(self, ts, price):
        self.prices.append((ts, price))
        if price < self.min:
            self.min = price
        if price > self.max:
            self.max = price

    def minimum(self):
        if not self.prices:
            return None
        return self.min

    def maximum(self):
        if not self.prices:
            return None
        return self.max

    def lastest(self):
        if not self.prices:
            return None
        return self.prices[-1][-1]