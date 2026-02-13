from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        the nums.length must have length of 3, but there may be no answer for requirement,
            the output's order doesn't matter, and outputs must be distinct,
            but num with different index can be used multiple times

        at first, sort the input nums, and use two pointer to track the current summation is zero or not
            define left pointer is greater than idx by 1, where idx is the index when traversing nums,
            and right pointer is from the nums' end index

        cuz nums is sorted, if current summation is greater than zero, move right pointer by -1,
            if less than, move left pointer by 1, else it's the potential membership
            add this membership to result array if this membership hasn't been seen

        time = O(n^2)
        space = O(1)
        """

        n = len(nums)
        nums.sort()
        res = []

        for idx in range(n):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            if nums[idx] > 0:
                break
            
            L, R = idx + 1, n - 1
            
            while L < R:
                i, j, k = nums[idx], nums[L], nums[R]
                
                if i + j + k > 0:
                    R -= 1
                
                elif i + j + k < 0:
                    L +=1
                
                else:
                    res.append([i, j, k])
                    
                    L += 1
                    R -= 1
                    
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        
        return res


threeSum = Solution().threeSum
def assert_reorder_three_sums(actual: List[int], expected: List[List[int]]):
    assert {tuple(sorted(nums)) for nums in actual} == {tuple(sorted(nums)) for nums in expected}


def test_threeSum():
    assert_reorder_three_sums(threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    assert_reorder_three_sums(threeSum([0,1,1]), [])
    assert_reorder_three_sums(threeSum([0,0,0]), [[0,0,0]])

    # Edge cases
    assert_reorder_three_sums(threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
    assert_reorder_three_sums(threeSum([0, 1, 2]), [])
    assert_reorder_three_sums(threeSum([-1, -2, 2]), [])
    assert_reorder_three_sums(threeSum([-1, 0, 2]), [])
    assert_reorder_three_sums(threeSum([-1, 0, 1]), [[-1, 0, 1]])
    assert_reorder_three_sums(threeSum([4, 2, -1, 0, 1]), [[-1, 0, 1]])
    assert_reorder_three_sums(threeSum([4, 2, -1, 0, 1, -4]), [[-1, 0, 1], [4, 0, -4]])
    assert_reorder_three_sums(threeSum([-2, 4, 2, -1, 0, 1, -4]), [[-2, 2, 0], [-1, 0, 1], [4, 0, -4]])


    print("All tests passed")

if __name__ == "__main__":
    test_threeSum()
