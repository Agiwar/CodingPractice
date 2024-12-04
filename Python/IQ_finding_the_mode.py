from collections import Counter
from typing import List


def mode1(nums: List[int]) -> List[int]:
    if not nums: return []
    
    num_occur = Counter(nums)
    max_num_occur = max(num_occur.values())
    
    return sorted(num for num, occur in num_occur.items() if occur == max_num_occur)