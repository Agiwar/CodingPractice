"""
Insert Number in Fixed-Size Array

Given a fixed-size array arr, a number num, and an index i,
insert num at position i while maintaining the array's original size.
"""


def insert_num_fixed_arr_looping(
    arr: list[int] | None,
    num: int | None,
    i: int,
) -> list[int]:
    """
    time: O(n)
    space: O(1)
    
    In-place insertion, no extra space cost.
    """

    if not arr or num is None:
        return arr or []

    n = len(arr)
    if not (-n <= i < n):
        raise IndexError("Out of index.")

    elif 0 < i < n - 1:
        for idx in range(1, i + 1):
            arr[idx - 1] = arr[idx]

    elif -n < i < 0:
        for idx in range(-1, i, -1):
            arr[idx] = arr[idx - 1]

    arr[i] = num
    return arr


def insert_num_fixed_arr_slicing(
    arr: list[int] | None,
    num: int | None,
    i: int,
) -> list[int]:
    """
    time: O(n)
    space: O(n)
    
    Python evaluates RHS before LHS.
    The slice arr[1:i+1] must materialize into a temporary list
    before the assignment can occur.
    """

    if not arr or num is None:
        return arr or []

    n = len(arr)
    if not (-n <= i < n):
        raise IndexError("Out of index.")

    elif 0 < i < n - 1:
        arr[:i] = arr[1:i + 1]

    elif -n < i < -1:
        arr[i + 1:] = arr[i:-1]

    arr[i] = num
    return arr



def test_insert_num_fixed_arr():  # sourcery skip: use-contextlib-suppress
    num = 5
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, 0) == [5, -4, 2, 3]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, 1) == [-4, 5, 2, 3]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, 2) == [-4, 2, 5, 3]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, 3) == [1, -4, 2, 5]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, -1) == [1, -4, 2, 5]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, -2) == [1, -4, 5, 2]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, -3) == [1, 5, -4, 2]
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], num, -4) == [5, -4, 2, 3]
    assert insert_num_fixed_arr_slicing([], num, 1) == []
    assert insert_num_fixed_arr_slicing([1, -4, 2, 3], None, 1) == [1, -4, 2, 3]
    assert insert_num_fixed_arr_slicing([1], num, 0) == [num]

    try:
        insert_num_fixed_arr_slicing([1, -4, 2, 3], num, 4)
        assert False, "Out of index."
    except IndexError:
        pass

    try:
        insert_num_fixed_arr_slicing([1, -4, 2, 3], num, -5)
        assert False, "Out of index."
    except IndexError:
        pass

    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, 0) == [5, -4, 2, 3]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, 1) == [-4, 5, 2, 3]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, 2) == [-4, 2, 5, 3]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, 3) == [1, -4, 2, 5]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, -1) == [1, -4, 2, 5]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, -2) == [1, -4, 5, 2]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, -3) == [1, 5, -4, 2]
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], num, -4) == [5, -4, 2, 3]
    assert insert_num_fixed_arr_looping([], num, 1) == []
    assert insert_num_fixed_arr_looping([1, -4, 2, 3], None, 1) == [1, -4, 2, 3]
    assert insert_num_fixed_arr_looping([1], num, 0) == [num]

    try:
        insert_num_fixed_arr_looping([1, -4, 2, 3], num, 4)
        assert False, "Out of index."
    except IndexError:
        pass

    try:
        insert_num_fixed_arr_looping([1, -4, 2, 3], num, -5)
        assert False, "Out of index."
    except IndexError:
        pass


if __name__ == "__main__":
    test_insert_num_fixed_arr()
