from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse linked list in-place using three pointers.

        - prev: points to reversed portion
        - curr: current node being processed  
        - next_node: save next before breaking link

        time = O(n)
        space = O(1)
        """
        
        curr = head
        prev = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


reverseList = Solution().reverseList

def build_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_reverseList():
    # LeetCode examples
    assert to_list(reverseList(build_list([1,2,3,4,5]))) == [5,4,3,2,1]
    assert to_list(reverseList(build_list([1,2]))) == [2,1]
    assert to_list(reverseList(build_list([]))) == []

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_reverseList()
