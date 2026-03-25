class ListNode:
    def __init__(
        self,
        key: int=0,
        val: int=0,
        prev=None,
        next=None,
    ) -> None:

        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    In order to do get and put with O(1) time, so use hashmap,
        this cache (hashmap) stores the obj (key-val),
        where cache's key is the key of obj,
        and cache's value is pointed to the obj (key-val).

    In order to know which obj is LRU, 
        on the other hand, there must be MRU (most recently),
        so create two dummy nodes to track LRU and MRU.

    When doing get obj, this obj becomes MRU,
        needs to remove this obj from linked-list,
        and insert it into before tail.

    When doing put obj:
        1. if this obj's key is in cache,
            update obj's val, and this obj becomes MRU,
            remove this obj from linked-list,
            and insert it into before tail.

        2. if this obj's key isn't in cache,
            and cache's capacity is enough so far,
            just add this obj into cache,
            this obj is MRU, insert it into before tail

        3. if cache's capacity isn't enough,
            remove LRU which is after head, and add this obj into cache,
            this obj is MRU, insert it into before tail
    
    time:
        _remove = O(1), using double-linked-list, no need traversal
        _insert = O(1)
        get = O(1)
        put = O(1)
    
    space = O(capacity)
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _insert(self, node: ListNode) -> None:
        prev_node = self.tail.prev
        next_node = self.tail
        prev_node.next = node
        node.next = next_node
        next_node.prev = node
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        
        else:
            node = ListNode(key, value)
            
            if len(self.cache) >= self.cap:
                lru = self.head.next
                self._remove(lru)
                self.cache.pop(lru.key)
            
            self.cache[key] = node
        
        self._insert(node)


def test_lru_cache():
    # LeetCode Example 1
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Edge cases
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == -1
    assert cache.get(4) == 4

    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(1, 0)
    assert cache.get(1) == 0
    cache.put(3, 10)
    assert cache.get(2) == -1
    assert cache.get(3) == 10
    assert cache.get(1) == 0
    cache.put(4, 2)
    assert cache.get(1) == 0
    assert cache.get(3) == 10
    assert cache.get(4) == 2
    cache.put(4, 3)
    cache.put(4, 5)
    cache.put(2, 20)
    assert cache.get(1) == -1
    assert cache.get(4) == 5
    assert cache.get(2) == 20
    assert cache.get(3) == 10
    

    print("All tests passed")

if __name__ == "__main__":
    test_lru_cache()
