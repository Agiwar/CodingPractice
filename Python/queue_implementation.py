from typing import Any, List, Optional


# implementation for queue data structure using array
class QueueArray:

    def __init__(self):
        self.array: List[Any] = []
    
    def is_empty(self) -> bool:
        if self.array:
            return False
        return True
    
    def enqueue(self, data: Any) -> None:
        """
        enqueue:
        Add an item into the first position of array.
        """
        self.array.insert(0, data)
        return None
    
    def dequeue(self) -> Any:
        """
        dequeue:
        Remove the last item from array.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self.array.pop()
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self.array[-1]



# denifition for singly-linked list
class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# implementation for queue data structure using linked-list
class QueueNode:

    def __init__(self, front=None, rear=None):
        self.front: Optional[ListNode] = front
        self.rear: Optional[ListNode] = rear
    
    def is_empty(self) -> bool:
        """
        Check queue is empty or not, 
        if queue.front is None, then queue.rear is obviously None as well,
        so the entire queue is empty.
        """
        if self.front:
            return False
        return True
    
    def enqueue(self, data: Any) -> None:
        """
        enqueue:
        Add an item into the last node,
        so need to check whether self.rear (the last node) is None or not,
        if self.rear is None, then the entire queue is empty for sure,
        so both self.rear and self.front point to the new item we wanna add;
        otherwise, the new node is added into the end, and self.rear needs to be updated.
        """
        new_node = ListNode(val= data)

        if not self.back:
            self.rear = new_node
            self.front = self.rear
            return None
        
        self.rear.next = new_node
        self.rear = new_node
        return None

    def dequeue(self) -> Optional[ListNode]:
        """
        dequeue:
        Remove the item from the first position in queue,
        and the current self.front needs to be updated.
        If there's nothing in queue after renoving the item, self.rear needs to set be None.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        
        output_node = self.front
        self.front = output_node.next

        if not self.rear:
            self.rear = None
        
        return output_node.val

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        
        return self.front.val
