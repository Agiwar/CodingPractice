class MinStack:

    def __init__(self):
        self.stack = []  # store the elements by "push method" order
        self.min_stack = []  # store the min element by comparing current val and the last element in min_stack
    
    def push(self, val: int) -> None:
        self.stack.append(val)

        # check which number is more min: val or last element in min_stack
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)

        # then push the more min number into min_stack
        self.min_stack.append(min_val)
        return None
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return None
    
    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return self.min_stack[-1]
