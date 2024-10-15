import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("given_array", type=int, nargs="+")
    return parser.parse_args()


def concatenate_array(arr: List[int]) -> List[int]:
    # 1. python has built-in concatenation of arrays and strings
    # return arr + arr
    
    # 2. intuitively for loop
    # res = []
    # for _ in range(2):
    #     for num in arr:
    #         res.append(num)
    # return res
    
    # 3.
    arr_copy = arr.copy()
    arr_copy.extend(iter)
    # for item in arr:
    #     arr_copy.append(item)
    return arr_copy


if __name__ == "__main__":
    args = argparse_list()
    given_arr = args.given_array
    concatenation_of_arr = concatenate_array(given_arr)

    # given 1 2 1, you may get 1 2 1 1 2 1
    print(concatenation_of_arr)
