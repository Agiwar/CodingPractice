from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Need O(n) time, so sorting is not allowed.

        The main idea is:
            1. Create a set to deduplicate and enable O(1) lookup
            2. Find all "starting points" numbers where (num - 1) is not in set
            3. From each starting point, count consecutive numbers (num + 1, num + 2, ...)
            4. Return the maximum length
                time = O(n), each number is visited at most twice (once for start check, once for counting)
                space = O(n), for the set
        """

        if len(nums_set := set(nums)) <= 1:
            return len(nums_set)

        starts = {num for num in nums_set if num - 1 not in nums_set}

        max_ct = 1
        for start in starts:
            curr_num = start
            ct = 1

            while curr_num + 1 in nums_set:
                ct += 1
                curr_num += 1

            max_ct = max(max_ct, ct)


        return max_ct

    

longestConsecutive = Solution().longestConsecutive

def test_longestConsecutive():
    # LeetCode examples
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longestConsecutive([1,0,1,2]) == 3

    # Edge cases
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1]) == 1
    assert longestConsecutive([-3]) == 1
    assert longestConsecutive([-3, -2]) == 2
    assert longestConsecutive([-2, 2]) == 1
    assert longestConsecutive([0, -2, -1]) == 3
    assert longestConsecutive([-2, 0, 2, -1]) == 3
    assert longestConsecutive([3, 3, 3, 3, 3]) == 1
    assert longestConsecutive([3, 3, 2, 1, 1]) == 3



    print("All tests passed")

if __name__ == "__main__":
    test_longestConsecutive()
