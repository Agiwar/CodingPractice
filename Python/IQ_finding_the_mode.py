from collections import Counter
from typing import List


def mode(nums: List[int]) -> List[int]:
    nums_occur = dict(sorted(Counter(nums).items()))
    max_num_occur = max(nums_occur.values())

    res = []
    for num, occur in nums_occur.items():
        if occur == max_num_occur:
            res.append(num)
    
    return res