from typing import List, Tuple


def rectangle_overlap(a: List[Tuple[int, int]], b: List[Tuple[int, int]]) -> bool:
    if not a or not b: return False

    a_min_x = min(x for x, _ in a)
    a_max_x = max(x for x, _ in a)
    a_min_y = min(y for _, y in a)
    a_max_y = max(y for _, y in a)

    return any(
        a_min_x <= b_x <= a_max_x and
        a_min_y <= b_y <= a_max_y
        for b_x, b_y in b
    )