from typing import Optional


# definition for singly-linked list
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_pointer = head
        prev_pointer = None

        while curr_pointer:
            nxt = curr_pointer.next
            curr_pointer.next = prev_pointer
            prev_pointer = curr_pointer
            curr_pointer = nxt
        
        return prev_pointer
