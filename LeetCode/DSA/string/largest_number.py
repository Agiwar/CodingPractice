class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        to get the largest number from rearranging nums, get the bigger leading num,
            using python's built in module functools.cmp_to_key
            to sort as such permutation

        time = O(n * log n), n is nums.length
        space = O(1), in-place sorting
        """

        if all(num == 0 for num in nums):
            return "0"
        
        
        from functools import cmp_to_key
        
        
        def compare(a: int, b: int) -> int:
            ab, ba = str(a) + str(b), str(b) + str(a)
            
            if ab > ba:
                return -1
            elif ab < ba:
                return 1
            else:
                return 0
            
            
        nums.sort(key=cmp_to_key(compare))
        return "".join(map(str, nums))


largestNumber = Solution().largestNumber

def test_largestNumber():
    # LeetCode examples
    assert largestNumber([10, 2]) == "210"
    assert largestNumber([3, 30, 34, 5, 9]) == "9534330"

    # Edge cases
    assert largestNumber([100]) == "100"
    assert largestNumber([100, 0]) == "1000"
    assert largestNumber([100, 9]) == "9100"
    assert largestNumber([0]) == "0"
    assert largestNumber([0, 0]) == "0"
    assert largestNumber([3, 20, 1]) == "3201"
    assert largestNumber([3, 20, 4]) == "4320"
    assert largestNumber([30, 31, 3]) == "33130"
    assert largestNumber([2, 10, 21]) == "22110"


    print("All tests passed")

if __name__ == "__main__":
    test_largestNumber()
