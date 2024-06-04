import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_array", type=int, nargs="+")
    parser.add_argument("given_value", type=int)
    args = parser.parse_args()
    return args

def remvoe_element(arr: List[int], val=int) -> int:
    # since the all elements in array may be equal to val
    # so the pointer L is started from zero (remove all occurrences)
    L = 0
    for R in range(0, len(arr)):
        if arr[R] != val:
            arr[L] = arr[R]
            L += 1
    return L


if __name__ == "__main__":
    args = argparse_list()
    given_arr = args.given_array
    given_val = args.given_value
    num_after_remove_occurrences = remvoe_element(arr=given_arr, val=given_val)

    # given 0 1 2 2 3 0 4 2, you may get 5
    print(num_after_remove_occurrences)
