import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--given_arr", type=int, nargs="+")
    args = parser.parse_args()
    return args


def quick_sort(arr: List[int], s: int, e: int) -> List[int]:
    # base case: the size of sub-array is zero or one
    # len(arr) <= 1: this condition doesn't change throughout the recursion
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]  # set pivot value is the mostright value of array
    left = s        # pointer for left side

    # go through the entire array to check each value is less than pivot value or not
    # if yes, swap the current value and the left pointer's value, and update left pointer
    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
    
    # move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sort the left & right sides
    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)

    return arr


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_arr

    arr_sort = quick_sort(
        arr=arr, 
        s=0, 
        e=len(arr) - 1,
    )
    print(arr_sort)
