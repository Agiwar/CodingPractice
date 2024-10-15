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
        
        return self.queue.popleft()
            
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
