from typing import List


def fill_none(input_list: List[int]) -> List[int]:
    if not input_list:
        return []

    input_list[0] = 0 if input_list[0] is None else input_list[0]

    for idx, value in enumerate(input_list):
        if value is None:
            input_list[idx] = input_list[idx - 1]

    return input_list