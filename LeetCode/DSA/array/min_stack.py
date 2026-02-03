class MinStack:
    """
    You must implement a solution with O(1) time complexity for each function.
    
    time = O(1)
    space = 2 * O(n) ~ O(n)
    """

    def __init__(self) -> None:
        self.stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]




def test_MinStack():
    # LeetCode example
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

    # Edge cases (write your own)
    minStack2 = MinStack()
    minStack2.push(10)
    minStack2.push(-5)
    minStack2.push(7)
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.top() == -5
    minStack2.push(0)
    minStack2.push(-5)
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.getMin() == -5
    assert minStack2.top() == 0
    minStack2.pop()
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.getMin() == 10
    assert minStack2.top() == 10

    print("All tests passed")


if __name__ == "__main__":
    test_MinStack()
