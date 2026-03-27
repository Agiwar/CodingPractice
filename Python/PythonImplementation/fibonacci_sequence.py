class Solution:
    """
    using recursion to solve it, break the original problem into smaller one,
    cuz each fib-value is determined by the previous two,
    so this is two-branch decision tree recursion,
    the base case is the zeroth fib is zero and first one is one, respectively
    
    time = O(2^n)
    space = O(n)
    """
    
    def fibonacci(self, n: int) -> int:
        return n if n <= 1 else self.fibonacci(n - 1) + self.fibonacci(n - 2)

fibonacci = Solution().fibonacci

def test_fibonacci():
    # Basic cases
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

    # Edge cases
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2

    print("All tests passed")

if __name__ == "__main__":
    test_fibonacci()
