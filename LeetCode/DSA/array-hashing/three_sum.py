from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        to find out all 3sums, sorted is required, then traverse the array nums,
            based on the traversal pointer idx to define the two pointers l_pt and r_pt
            to track the current summation is zero or not
            define l_pt is greater than idx by 1, and r_pt is the last index of nums

        after sorting nums, there're some situations:
            1. if first number is larger than zero which mustn't have 3sum = 0
                so terminate the loop immediately.
            2. each 3sum combination must be unique, when traversing,
                skip the current number if current number is equal to previous number
            3. otherwise, collecting all 3sums by nums with idx, l_pt, r_pt, respectively,
                if current 3sum is larger than zero, then decrease the r_pt,
                if smaller than zero, we increase l_pt,
                this makes sense to find out the all 3sum memberships
            4. same logic, can't collect the duplicated, if the current l_pt is smaller than r_pt,
                and the current number by l_pt is equal to previous number,
                then directly move l_pt to next one until the unique number by l_pt.

        time = O(n^2)
        space = O(1)
        """
        
        nums.sort()
        n = len(nums)
        triplets = []
        
        for idx in range(n - 2):
            if nums[idx] > 0:
                break
            
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            l_pt = idx + 1
            r_pt = n - 1
            
            while l_pt < r_pt:
                sums = nums[idx] + nums[l_pt] + nums[r_pt]
                
                if sums > 0:
                    r_pt -= 1
                
                elif sums < 0:
                    l_pt += 1
                
                else:
                    triplets.append([nums[idx], nums[l_pt], nums[r_pt]])
                    l_pt += 1
                    r_pt -= 1
                    
                    while l_pt < r_pt and nums[l_pt] == nums[l_pt - 1]:
                        l_pt += 1
        
        return triplets


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
