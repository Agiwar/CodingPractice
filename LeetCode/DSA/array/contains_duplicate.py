from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        nums.length has minimum value of 1, so if [2] -> False
        nums is not ordered, and may contain negative numbers

        nums = [1,2,3,1] -> True
        nums = [1,2,3,4] -> False
        nums = [1,1,1,3,3,4,3,2,4,2] -> True

        time = O(n)
        space = O(n)
        """

        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)

        return False


containsDuplicate = Solution().containsDuplicate

def test_containsDuplicate():
    assert containsDuplicate([1,2,3,1]) == True
    assert containsDuplicate([1,2,3,4]) == False
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

    # Edge cases
    assert containsDuplicate([2]) == False
    assert containsDuplicate([2, 2]) == True
    assert containsDuplicate([0, 0]) == True
    assert containsDuplicate([-1, 0, 1]) == False
    assert containsDuplicate([-1, 0, -1]) == True

    print("All tests passed")

if __name__ == "__main__":
    test_containsDuplicate()
