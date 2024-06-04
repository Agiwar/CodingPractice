import argparse
from typing import List

# remove duplicates from a sorted array my_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# use one pointer to indicate the number of non-duplicated element in array
# use another pointer to go through entire array to check whether the current elelment is duplicated or not.


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("sorted_array", type=int, nargs="+")
    args = parser.parse_args()
    return args


def remove_duplicates(arr: List[int]) -> int:
    # the first element must be unique
    # so the pointer we use to indicate duplicated or not can be started from second position
    
    L = 1
    for R in range(L, len(arr)):
        if arr[R - 1] != arr[R]:
            arr[L] = arr[R]
            L += 1
    return L


if __name__ == "__main__":
    args = argparse_list()
    sorted_array = args.sorted_array
    num_nonduplicated_ellement = remove_duplicates(sorted_array)

    # given 0 0 1 1 1 2 2 3 3 4, you may get 5
    print(num_nonduplicated_ellement)
