from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        the brute force is iterating every num in num1 to multiply every num in num2,
            the edge case is one of num1 or num2 is "0", the directly return "0"

        time = O(m * n), m is num1.length, n is num2.length
        space = O(m * n)
        """
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        product = [
            (int(n1) * 10 ** c1) * (int(n2) * 10 ** c2)
            for c2, n2 in enumerate(num2[::-1])
            for c1, n1 in enumerate(num1[::-1])
        ]
        return str(sum(product))


multiply = Solution().multiply

def test_multiply():
    assert multiply("2", "3") == "6"
    assert multiply("123", "456") == "56088"

    # Edge cases
    assert multiply("0", "999") == "0"
    assert multiply("101", "0") == "0"
    assert multiply("0", "0") == "0"
    assert multiply("1", "999") == "999"
    assert multiply("1000", "99") == "99000"
    assert multiply("9876", "123") == "1214748"
    assert multiply("789", "5432") == "4285848"


    print("All tests passed")

if __name__ == "__main__":
    test_multiply()
