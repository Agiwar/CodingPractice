from typing import List, Optional


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # there are many lists in the input lists, but they are sorted, merge them
    # merge first lists and second lists first, and merge this results and the rests from input lists

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1 and not list2:
                return None

            head = ListNode()
            tail = head

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next

                tail = tail.next

            if list1:
                tail.next = list1

            elif list2:
                tail.next = list2

            return head.next


        # if len(lists) == 1, no need to merge
        while len(lists) > 1:
            list_merged = []

            for i in range(0, len(lists), 2):
                L1 = lists[i]
                L2 = lists[i + 1] if (i + 1) < len(lists) else None

                list_merged.append(merge_two_sorted_lists(L1, L2))

            lists = list_merged

        return lists[0]