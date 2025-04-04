import math
from typing import Dict, List

def compute_mean(nums: List) -> float:
    return sum(nums) / len(nums)


def compute_variance(nums: List) -> float:
    mu = compute_mean(nums)
    return compute_mean([(x - mu) ** 2 for x in nums])


def compute_stddev(nums: List) -> float:
    return math.sqrt(compute_deviation(nums))


def compute_deviation(list_numbers: List[Dict]) -> Dict[str, float]:    
    return {
        item.get("key"): compute_stddev(item.get("values"))
        for item in list_numbers
    }