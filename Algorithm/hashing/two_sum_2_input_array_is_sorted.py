from typing import List


# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

class Solution1:
    # go through every num in numbers, find out the index of diff
    # cuz numbers is sorted, use binary search
    # time = O(n * log n)
    # space = O(1) but may be O(n) when slicing the list in each iteration creates a new list
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary_search(arr: List[int], target: int) -> int:
            L = 0
            R = len(arr) - 1
            
            while L <= R:
                m = L + (R - L) // 2
                
                if arr[m] < target:
                    L = m + 1
                elif arr[m] > target:
                    R = m - 1
                else:
                    return m
            
            return L
        
        
        for idx, num in enumerate(numbers):
            diff = target - num
            
            if diff in numbers[idx+1:]:
                idx_diff = binary_search(numbers[idx+1:], diff)
                idx_another = idx + idx_diff + 1
                
                return [idx + 1, idx_another + 1]


class Solution2:
    # go through every num in numbers, and store the index of diff in a hashmap
    # not use benefit of sorted
    # time = O(n), space = O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff_hash = {}
        for idx, num in enumerate(numbers):
            if num not in diff_hash:
                diff = target - num
                diff_hash[diff] = idx + 1
            else:
                return [diff_hash[num], idx + 1]


class Solution3:
    # use two pointers to slice numbers to find out the index
    # time = O(n) NOT O(log n), space = O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        
        while L < R:
            sums = numbers[L] + numbers[R]
            
            if sums < target:
                L += 1
            elif sums > target:
                R -= 1
            else:
                return [L + 1, R + 1]
        