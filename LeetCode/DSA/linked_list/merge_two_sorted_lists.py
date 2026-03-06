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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        cuz list1 and list2 are already sorted, in order to merge them in a new linked list in order,
            create an empty linked list node, and use two pointer which go through list1 and list2, respectively
            while traversing, compare the current value which is smaller from list1's node and list2's node,
            pick up the smaller value to be head's next node, and move this node one step, and so on,
            until either list1 or list2 traversal done, then directly make head's next link the left list1 or list2

        time = O(n + m), n is linked-list with smaller length, m is the other
        space = O(1)
        """
        
        dummy = ListNode()
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
            
        head.next = list1 or list2
        return dummy.next
        

mergeTwoLists = Solution().mergeTwoLists

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

def test_mergeTwoLists():
    # LeetCode examples
    assert to_list(mergeTwoLists(build_list([1,2,4]), build_list([1,3,4]))) == [1,1,2,3,4,4]
    assert to_list(mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(mergeTwoLists(build_list([]), build_list([0]))) == [0]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_mergeTwoLists()
