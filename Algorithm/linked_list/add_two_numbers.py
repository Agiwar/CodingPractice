from typing import Optional


class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0
        
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total_current_val = l1_val + l2_val + carry
            
            current_node_val = total_current_val % 10
            carry = total_current_val // 10
            
            tail.next = ListNode(current_node_val)
            tail = tail.next
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return head.next