from typing import List


def two_oldest_ages(ages: List[int]) -> List[int]:
    oldest = second_oldest = float("-inf")
    
    for age in ages:
        if age > oldest:
            second_oldest = oldest
            oldest = age
        elif age > second_oldest:
            second_oldest = age
    
    return [second_oldest, oldest]