import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_array", type=int, nargs="+")
    parser.add_argument("given_value", type=int)
    return parser.parse_args()


def remove_element(arr: List[int], val=int) -> int:
    # since the all elements in array may be equal to val
    # so the pointer L is started from zero (remove all occurrences)
    L = 0
    for R in range(len(arr)):
        if arr[R] != val:
            arr[L] = arr[R]
            L += 1
    return L


if __name__ == "__main__":
    args = argparse_list()
    given_arr = args.given_array
    given_val = args.given_value
    num_after_remove_occurrences = remove_element(arr=given_arr, val=given_val)

    # given 0 1 2 2 3 0 4 2, you may get 5
    print(num_after_remove_occurrences)



def get_non_targeted_num_occur(nums: list[int], val: int) -> int:
    # nums = [2, 3, 2, 1, 5, 3, 3]
    # val = 3
    # expected k = 4, nums = [2, 2, 1, 5]
    
    # len(nums) = 0 >> 0
    # len(nums) = 1 and nums[0] = val >> 0

    if not nums:
        return 0

    k = 0
    for idx in range(len(nums)):
        if nums[idx] != val:
            nums[k] = nums[idx]
            k += 1

    return k
