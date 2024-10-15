from typing import List


class Solution:
    # thoughts of solution is from buckets sort
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,2,2,3]
        occur_hash = {occur: [] for occur in range(len(nums), 0, -1)}

        # occur_hash = {
        #     6: [],
        #     5: [],
        #     4: [],
        #     3: [],
        #     2: [],
        #     1: [],
        # }

        num_occur = {}
        for num in nums:
            num_occur[num] = num_occur.get(num, 0) + 1

        # num_occur = {
        #     1: 3,
        #     2: 2,
        #     3: 1,
        # }

        for num, occur in num_occur.items():
            occur_hash[occur].append(num)

        # occur_hash = {
        #     6: [],
        #     5: [],
        #     4: [],
        #     3: [1],
        #     2: [2],
        #     1: [1],
        # }

        res = []
        for num_arr in occur_hash.values():
            if num_arr and k > 0:

                # if k > len(num_arr), the whole num in num_arr needed to be appended
                if k > len(num_arr):
                    res += num_arr

                    # cuz already taken number of k nums from num_arr
                    k -= len(num_arr)  

                else:
                    # take the rest k nums from num_arr
                    res += num_arr[:k]
                    return res