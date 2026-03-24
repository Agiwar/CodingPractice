from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        the definition that there's a cycle in a linked list is that the tail next pointer to pos,
            there may be no node, so return False directly.

        the main idea behind the code is store the seen node when traversing,
            if tail.next node appears in seen nodes, return True

        time = O(n), n is head.length
        space = O(n)
        """

        
        if not head:
            return False
        
        curr = head
        seen = set()
        
        while curr:
            if curr in seen:
                return True
            
            seen.add(curr)
            curr = curr.next
        
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
