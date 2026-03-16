class ListNode:
    def __init__(self, val: int=0, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self) -> None:
        self.L = ListNode()
        self.R = ListNode()
        self.L.next = self.R
        self.R.prev = self.L

    def get(self, index: int) -> int:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        return curr.val if curr and index == 0 and curr != self.R else -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prev_node = self.L
        next_node = self.L.next
        prev_node.next = node
        node.next = next_node
        next_node.prev = node
        node.prev = prev_node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        next_node = self.R
        prev_node = self.R.prev
        next_node.prev = node
        node.prev = prev_node
        prev_node.next = node
        node.next = next_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node = ListNode(val)
            prev_node = curr.prev
            next_node = curr
            prev_node.next = node
            node.next = next_node
            next_node.prev = node
            node.prev = prev_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr != self.R:
            prev_node = curr.prev
            next_node = curr.next
            prev_node.next = next_node
            next_node.prev = prev_node


def test_my_linked_list():
    # LeetCode Example 1
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    assert obj.get(1) == 2
    obj.deleteAtIndex(1)
    assert obj.get(1) == 3

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_my_linked_list()
