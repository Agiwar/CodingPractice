import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_arr", type=int, nargs="+")
    args = parser.parse_args()
    return args


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2

    left_half = arr[:m]
    right_half = arr[m:]

    return merge_sort(left_half), merge_sort(right_half)


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_arr

    arr_sort = merge_sort(arr)
    print(arr_sort)
