from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        using two pointers, slow and fast, both starting at head.
            slow moves one step, fast moves two steps per iteration.
            if there's a cycle, fast will eventually catch up to slow.
            if no cycle, fast reaches None and the loop exits.
            only fast and fast.next need to be checked in the while condition,
            because fast always reaches the end before slow.

        time = O(n), n is head.length
        space = O(1)
        """
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True

        return False


def build_cycle_list(vals, pos):
    dummy = ListNode()
    curr = dummy
    nodes = []
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
        nodes.append(curr)
    if pos >= 0:
        curr.next = nodes[pos]
    return dummy.next

hasCycle = Solution().hasCycle

def test_hasCycle():
    assert hasCycle(build_cycle_list([3,2,0,-4], 1)) == True
    assert hasCycle(build_cycle_list([1,2], 0)) == True
    assert hasCycle(build_cycle_list([1], -1)) == False

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_hasCycle()
