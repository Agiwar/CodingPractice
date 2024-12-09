# In order to do get and put with O(1) time, so use hashmap,
# this cache (hashmap) stores the obj (key-val),
# where cache's key is the key of obj,
# and cache's value is pointed to the obj (key-val).

# In order to know which obj is LRU, 
# on the other hand, there must be MRU (most recently),
# so create two dummy nodes to track LRU and MRU.

# When doing get obj, this obj becomes MRU,
# needs to remove this obj from linked-list,
# and insert it into before tail.

# When doing put obj:
# 1. if this obj's key is in cache,
#    update obj's val, and this obj becomes MRU,
#    remove this obj from linked-list,
#    and insert it into before tail.
# 
# 2. if this obj's key isn't in cache,
#    and cache's capacity is enough so far,
#    just add this obj into cache,
#    this obj is MRU, insert it into before tail
# 
# 3. if cache's capacity isn't enough,
#    remove LRU which is after head, and add this obj into cache,
#    this obj is MRU, insert it into before tail

from typing import Optional



class ListNode:
    
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}
        
        # create two dummy nodes which are head and tail to track LRU and MRU, and connect them
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_from_linked_list(self, node: Optional[ListNode]) -> None:
        node_prev = node.prev
        node_next = node.next
        
        node_prev.next = node_next
        node_next.prev = node_prev
    
    def insert_into_before_tail(self, node: Optional[ListNode]) -> None:
        node_prev = self.tail.prev
        node_next = self.tail
        
        node_prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = node_prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_from_linked_list(self.cache.get(key))
            self.insert_into_before_tail(self.cache.get(key))
            
            return self.cache.get(key).val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_from_linked_list(self.cache.get(key))
        
        self.cache[key] = ListNode(key, value)
        self.insert_into_before_tail(self.cache.get(key))
        
        if len(self.cache) > self.cap:
            LRU = self.head.next
            self.remove_from_linked_list(LRU)
            self.cache.pop(LRU.key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)