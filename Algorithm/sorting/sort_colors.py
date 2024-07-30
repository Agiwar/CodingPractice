import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--given_color", type=int, nargs="+")
    args = parser.parse_args()
    return args


def sort_colors(nums: List[int]) -> None:
    counts = [0] * 3

    for n in nums:
        counts[n] += 1
    
    i = 0
    for n in range(len(counts)):
        for _ in range(counts[n]):
            nums[i] = n
            i += 1
    
    return nums


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_color

    print(sort_colors(arr))
