# define doubly linked list
class ListNode:

    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        # create two dummy linked lists
        self.L = ListNode(0)
        self.R = ListNode(0)
        self.L.next = self.R
        self.R.prev = self.L

    def get(self, index: int) -> int:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.R and index == 0:
            return curr.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next  = ListNode(val), self.L, self.L.next
        
        node.prev = prev
        prev.next = node
        node.next = next
        next.prev = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.R.prev, self.R

        node.prev = prev
        prev.next = node
        node.next = next
        next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node, prev, next = ListNode(val), curr.prev, curr

            node.prev = prev
            prev.next = node
            node.next = next
            next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.L.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.R and index == 0:
            prev, next = curr.prev, curr.next

            prev.next = next
            next.prev = prev
