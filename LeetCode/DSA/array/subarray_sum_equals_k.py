from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        The input array is not ordered and may contain negative numbers.
            When traversing the nums, calculate the current sum is equal to target k number,
            if yes, we get a solution, and keep going through nums, there may be another solution,
            and the previous solution, say prev_subarray, combines the current solution, say curr_subarray
            will become a solution as well, i.e., prev_subarray + curr_subarray = new_subarray, it's also a solution
            so we have prev_subarray, curr_subarray, and new_subarray which has 3 solutions

        For the brute force, we use two pointer to track any possible subarray
            which has summation value of target value k, this has O(n^2) time
    
        Above logic we can store the previous solution in a hashmap,
            so no need to re-check the same portion while traversing

        The main idea behind the code is calculate the current sum of subarray,
            and check its previous sum is in previous solution hashmap or not,
            if yes, we get this solution plus the current subarray solution,
            which means the current subarray can remove somewhat subarray to keep it still as solution

        The base case is that when seeing the first num from nums, it has no prefix sum,
            and the edge case is that this nums has length of 1

        time = O(n)
        space = O(1)
        """
        
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        curr_sum = 0
        res = 0
        prefix_sums = {0: 1}
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            
            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return res



subarraySum = Solution().subarraySum

def test_subarraySum():
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2

    # Edge cases
    assert subarraySum([5], 1) == 0
    assert subarraySum([5], 5) == 1
    assert subarraySum([1, 2, 3], k = 3) == 2
    assert subarraySum([3, 1, 2], k = 3) == 2
    assert subarraySum([2, 3, 1], k = 3) == 1
    assert subarraySum([-1, -1, -1], -1) == 3
    assert subarraySum([-2, -1, 0, 1, 2], 0) == 3
    assert subarraySum([-2, 2, 0, 1, -1], 0) == 6


    print("All tests passed")

if __name__ == "__main__":
    test_subarraySum()
