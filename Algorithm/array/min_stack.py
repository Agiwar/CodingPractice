class MinStack:

    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        return None
    
    def pop(self) -> None:
        self.stack.pop()
        return None
    
    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return min(self.stack)
