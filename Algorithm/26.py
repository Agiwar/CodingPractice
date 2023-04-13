# Use two pointer:
# One goes through the entire array,
# the other is used to indicate the position where we wanna put the non-duplicated element.

from typing import Tuple


def remove_duplicate(arr: list) -> Tuple[int, list]:
    L = 1

    for R in range(1, len(arr)):
        if arr[R] != arr[R - 1]:
            arr[L] = arr[R]
            L += 1

    return L, arr
