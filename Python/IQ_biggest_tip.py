from typing import List


def most_tips(user_ids: List[int], tips: List[int]) -> int:
    user_tip_pairs = {}
    for user, tip in zip(user_ids, tips):
        user_tip_pairs[user] = user_tip_pairs.get(user, 0) + tip
    
    most_tips = max(user_tip_pairs.values())
    return next(user for user, tip in user_tip_pairs.items() if tip == most_tips)