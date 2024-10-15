import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_arr", type=int, nargs="+")
    return parser.parse_args()


def merge_sort(arr: List[int]) -> List[int]:
    # check whether sub-array is individual or not
    if len(arr) <= 1:
        return arr

    # find out the middle point of array to copy left & right sub-array
    m = len(arr) // 2

    left_half = arr[:m]
    right_half = arr[m:]

    # recursion for left & right half sub-array until getting individual
    merge_sort(left_half)
    merge_sort(right_half)

    # three pointers:
    # i: left half
    # j: right half
    # k: the entire array
    i = j = k = 0

    # put the smaller value from either left_half or right_halt into arr
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # check whether there's left_half left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # check whether there's right_half left
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_arr

    arr_sort = merge_sort(arr)
    print(arr_sort)
