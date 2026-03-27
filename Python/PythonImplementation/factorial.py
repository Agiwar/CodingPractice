class Solution:
    """
    recursion method is break big problem to smaller one
    clarify that, say n = 5, we get started at n = 5,
    to get 5! need to get 4!; need to get 4!, 3! is required, and so on,
    before hit n <= 1, the pending result like 5! = 5 * 4! and 4! = 4 * 3!,
    they are temporary stored in function call stack not a data structure,
    so when we hit n = 1, no need to count 1!, it's math assumption,
    so we have a constant one, so 2! = 2 * 1! which can be gotten as well,
    3! = 3 * 2!, and so on, like after breaking big problem to base case,
    then use this base result to go back to original big problem,
    and during this progress of breaking,
    the formula is already stored in function call stack,
    that's why we go back from 1, then 2, 6, 24, 120, which is answer
    
    time = O(n)
    space = O(n), call stack
    """
    
    def factorial(self, n: int) -> int:
        return 1 if n <= 1 else n * self.factorial(n - 1)

factorial = Solution().factorial

def test_factorial():
    # Basic cases
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

    # Edge cases
    assert factorial(2) == 2
    assert factorial(3) == 6

    print("All tests passed")

if __name__ == "__main__":
    test_factorial()
