import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-arr", "--given_arr", type=int, nargs="+")
    return parser.parse_args()


def bucket_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    # suppose arr = [4, 2, 2, 8, 3, 3, 1]

    # get min & max value of input array to specify dataset range
    min_val = min(arr)
    max_val = max(arr)

    # while dataset range is determined, we can create the number of buckets
    num_of_buckets = (max_val - min_val) + 1  # +1 means both ended value of array needed to be included

    # initialize frequency of each value in array, [0, 0, 0, 0, 0, 0, 0, 0]
    counts_each_value_in_array = [0] * num_of_buckets

    # put counts of each value from array into the bucket
    for value in arr:
        counts_each_value_in_array[value - min_val] += 1  # results becomes [1, 2, 2, 1, 0, 0, 0, 1]
    
    # fill each bucket in the original array
    # index i means the position index of array
    i = 0
    for n in range(len(counts_each_value_in_array)):
        for _ in range(counts_each_value_in_array[n]):
            arr[i] = n + min_val
            i += 1

    return arr


if __name__ == "__main__":
    args = argparse_list()
    arr = args.given_arr

    arr_sort = bucket_sort(arr)
    print(arr_sort)