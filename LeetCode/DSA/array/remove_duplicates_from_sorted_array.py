import argparse
from typing import List

# remove duplicates from a sorted array my_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# use one pointer to indicate the number of non-duplicated element in array
# use another pointer to go through entire array to check whether the current elelment is duplicated or not.


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("sorted_array", type=int, nargs="+")
    return parser.parse_args()


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
    num_nonduplicated_element = remove_duplicates(sorted_array)

    # given 0 0 1 1 1 2 2 3 3 4, you may get 5
    print(num_nonduplicated_element)







def remove_duplicates_array(nums: list[int]) -> int:
    # nums is ordered, [1, 1, 2, 3, 3, 5]
    # expected k = 4, nums = [1, 2, 3, 5]

    # k >= 1, if k = 1, there must be a unique number in nums

    # time = O(n)
    # space = O(1)

    if k == 1:
        return k

    k = 1
    for idx in range(1, len(nums)):
        if nums[idx - 1] != nums[idx]:
            nums[k] = nums[idx]
            k += 1

    return k
            
