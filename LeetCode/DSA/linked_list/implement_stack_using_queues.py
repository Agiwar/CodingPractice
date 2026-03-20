from collections import deque


class MyStack:

    def __init__(self) -> None:
        self.q = deque([])
    
    def _rotate(self) -> None:
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self._rotate()
        return self.q.popleft()

    def top(self) -> int:
        self._rotate()
        
        top_num = self.q.popleft()
        self.push(top_num)
        return top_num

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
