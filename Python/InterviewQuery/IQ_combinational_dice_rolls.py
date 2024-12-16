import itertools
import random
from typing import List, Tuple


def combinational_dice_rolls(n: int, m: int) -> List[Tuple[int]]:
    if n == 0:
        return []
    
    all_combinations = []
    for _ in range(m ** n):
        dice_roll = [0] * n
        
        for dice in range(n):
            dice_roll[dice] = random.choice(range(1, m + 1))
        
        all_combinations.append(dice_roll)
    
    return all_combinations


def combinational_dice_rolls(n: int, m: int) -> List[Tuple[int]]:
    return [] if n == 0 else list(itertools.product(range(1, m + 1), repeat=n))