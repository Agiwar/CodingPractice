from typing import Optional


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    # time = O(n), space = O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False
        
        list_node_visited = set()
        curr = head
        
        while curr:
            if curr in list_node_visited:
                return True
            
            list_node_visited.add(curr)
            curr = curr.next
    
        return False


class Solution2:
    # time = O(n), space = O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False
