from typing import List, Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
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


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        the input lists may be empty, so return empty list directly
            and the sublist may be empty either, return empty list directly as well
        
        the main idea behind the code is implement the merge two sorted lists algorithm,
            imagine there're 10 sorted lists, for each loop,
            do (total number of lists divided by 2) times "merge two",
            like 10 -> 5; 5 -> 3; 3 -> 2; 2 -> 1

            so first loop, implement "merge two": 
                list1 merge list2  >>  listA,
                list3 merge list4  >>  listB, and so on

            second loop:
                listA merge listB  >>  listAB, and so on

        time = O(n * log k), n is total number of nodes
        space = O(k)
        """

        while (k := len(lists)) > 1:
            merged = []
            for i in range(0, k, 2):
                if i == k - 1:
                    merged.append(lists[i])
                    break
                merged.append(mergeTwoLists(lists[i], lists[i + 1]))
            lists = merged

        return lists[0] if lists else None


mergeKLists = Solution().mergeKLists

def list_to_linked(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_mergeKLists():
    # LeetCode examples
    assert linked_to_list(mergeKLists([list_to_linked([1,4,5]), list_to_linked([1,3,4]), list_to_linked([2,6])])) == [1,1,2,3,4,4,5,6]
    assert linked_to_list(mergeKLists([])) == []
    assert linked_to_list(mergeKLists([None])) == []

    # Edge cases
    print("All tests passed")
    assert linked_to_list(mergeKLists([list_to_linked([]), list_to_linked([1, 2])])) == [1, 2]
    assert linked_to_list(mergeKLists([list_to_linked([1, 2])])) == [1, 2]
    assert linked_to_list(mergeKLists([list_to_linked([1, 2]), list_to_linked([-2, -1])])) == [-2, -1, 1, 2]
    assert linked_to_list(mergeKLists([list_to_linked([1, 2]), list_to_linked([-2, -1]), list_to_linked([0, 3])])) == [-2, -1, 0, 1, 2, 3]
    assert linked_to_list(mergeKLists([list_to_linked([0, 1, 2]), list_to_linked([-4, -3, -2, -1]), list_to_linked([0]), list_to_linked([0, 5])])) == [-4, -3, -2, -1, 0, 0, 0, 1, 2, 5]


if __name__ == "__main__":
    test_mergeKLists()
