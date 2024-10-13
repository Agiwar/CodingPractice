from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        """
        if wanna pop element from stack (LIFO),
        can't just remove the most right element from queue,
        cuz queue is FIFO, so need to reverse the order of queue
        (pop the most left element, then add it into the most right position)
        """
        
        for _ in range(len(self.queue) - 1):
            # self.queue.append(self.queue.popleft())
            
            # note that "self.queue.append" has been implemented as "self.push" method
            self.push(self.queue.popleft())
        
        the_most_left_element = self.queue.popleft()
        return the_most_left_element
            
    def top(self) -> int:
        the_most_right_element = self.queue[-1]
        return the_most_right_element

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
