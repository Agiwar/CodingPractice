import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--given_color", type=int, nargs="+")
    return parser.parse_args()


def sort_colors(nums: List[int]) -> None:
    """
    use bucket sort, 
    the time and space complexity are O(N) and O(1) respectively
    """
    counts = [0] * 3  # three colors

    for n in nums:
        counts[n] += 1
    
    i = 0
    for n in range(3):  # three colors
        for _ in range(counts[n]):
            nums[i] = n
            i += 1
    
    return nums


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_color

    print(sort_colors(arr))
