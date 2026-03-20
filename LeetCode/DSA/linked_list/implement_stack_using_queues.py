from collections import deque


class MyStack:

    def __init__(self) -> None:
        self.q = deque([])
        self._top_num = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self._top_num = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self._top_num

    def empty(self) -> bool:
        return len(self.q) == 0


def test_my_stack():
    # LeetCode Example 1
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    assert obj.top() == 2
    assert obj.pop() == 2
    assert obj.empty() == False

    # Edge cases
    obj = MyStack()
    obj.push(-1)
    assert obj.top() == -1
    assert obj.pop() == -1
    assert obj.empty() == True
    obj.push(3)
    obj.push(-2)
    assert obj.top() == -2
    assert obj.pop() == -2
    assert obj.top() == 3
    obj.push(-3)
    assert obj.top() == -3

    print("All tests passed")

if __name__ == "__main__":
    test_my_stack()
