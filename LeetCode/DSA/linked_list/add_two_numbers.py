from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 and l2 must have at least one node, and each node's value must be [0, 9],
            it's a math add rule, create a new linked list to store adding results,
            adding results is a combination of l1.val + l2.val + carry,
            if adding result value is greater or equal to 10, say 15,
            can't assign this 15 to current node, instead,
            current node stores only the adding result's mod,
            and then add 15 // 10 carry value with the next node value, and so on.

        time = O(m), m is the greater length of either l1 or l2
        space = O(m)
        """
        
        dummy = ListNode()
        head = dummy
        carry = 0
        
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            curr_num = l1_val + l2_val + carry
            mod = curr_num % 10
            carry = curr_num // 10
            
            head.next = ListNode(mod)
            head = head.next
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next


def build_list(vals):
    dummy = ListNode()
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

addTwoNumbers = Solution().addTwoNumbers

def test_addTwoNumbers():
    assert to_list(addTwoNumbers(build_list([2,4,3]), build_list([5,6,4]))) == [7,0,8]
    assert to_list(addTwoNumbers(build_list([0]), build_list([0]))) == [0]
    assert to_list(addTwoNumbers(build_list([9,9,9,9,9,9,9]), build_list([9,9,9,9]))) == [8,9,9,9,0,0,0,1]

    # Edge cases
    assert to_list(addTwoNumbers(build_list([1]), build_list([1]))) == [2]
    assert to_list(addTwoNumbers(build_list([1]), build_list([9]))) == [0, 1]
    assert to_list(addTwoNumbers(build_list([9]), build_list([9]))) == [8, 1]
    assert to_list(addTwoNumbers(build_list([1, 0, 0]), build_list([9]))) == [0, 1, 0]
    assert to_list(addTwoNumbers(build_list([1, 0, 0]), build_list([0]))) == [1, 0, 0]
    assert to_list(addTwoNumbers(build_list([1, 2, 3]), build_list([0]))) == [1, 2, 3]
    assert to_list(addTwoNumbers(build_list([1, 2, 3]), build_list([0, 8, 5]))) == [1, 0, 9]
    assert to_list(addTwoNumbers(build_list([1, 2, 3]), build_list([0, 8, 6]))) == [1, 0, 0, 1]
    assert to_list(addTwoNumbers(build_list([0]), build_list([1, 2, 3]))) == [1, 2, 3]
    assert to_list(addTwoNumbers(build_list([9]), build_list([1, 9, 3]))) == [0, 0, 4]
    assert to_list(addTwoNumbers(build_list([9]), build_list([9, 9, 9]))) == [8, 0, 0, 1]
    assert to_list(addTwoNumbers(build_list([9]), build_list([9, 8, 8]))) == [8, 9, 8]


    print("All tests passed")

if __name__ == "__main__":
    test_addTwoNumbers()
