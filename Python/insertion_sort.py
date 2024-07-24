import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--given_arr", type=int, nargs="+")
    args = parser.parse_args()
    return args


def insertion_sort(arr: List[int]) -> List[int]:
    # use i & j pointer to indicate the two values that we need to compare
    for i in range(1, len(arr)):
        j = i - 1

        # check whether two individual values in sub-array is ascending or not
        # if not, then do swap
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            # tmp = arr[j + 1]
            # arr[j + 1] = arr[j]
            # arr[j] = tmp

            j -= 1
        
    return arr


if __name__ == "__main__":
    args = argparse_list()
    given_arr = args.given_arr
    sorted_arr = insertion_sort(arr=given_arr)

    # given [2, 3, 4, 1, 6], you may get [1, 2, 3, 4, 6]
    print(sorted_arr)
