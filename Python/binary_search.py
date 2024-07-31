import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--sorted_arr", type=int, nargs="+")
    parser.add_argument("-t", "--target", type=int)
    args = parser.parse_args()
    return args


def binary_search(arr: List[int], target: int) -> int:
    # define two pointers L & R which are the leftmost & rightmost pointer of input sorted array
    L = 0
    R = len(arr) - 1

    # execute binary search to find out the index of target value
    while L <= R:
        # find out the middle pointer
        # m = (L + R) // 2
    
        # this is better formula to avoid integer overflow when L & R are both very large integer
        m = L + (R - L) // 2

        if arr[m] < target:
            L = m + 1
        elif arr[m] > target:
            R = m - 1
        else:
            return m

    return -1    


if __name__ == "__main__":
    args = argparse_list()
    arr = args.sorted_arr
    t = args.target

    target_index = binary_search(arr=arr, target=t)
    print(target_index)
