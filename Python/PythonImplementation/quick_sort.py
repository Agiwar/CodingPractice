class Solution:
    def quick_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        w_pt = 0

        for r_pt in range(len(arr) - 1):
            if arr[r_pt] < pivot:
                arr[w_pt], arr[r_pt] = arr[r_pt], arr[w_pt]
                w_pt += 1

        arr[-1] = arr[w_pt]
        arr[w_pt] = pivot

        left = self.quick_sort(arr[:w_pt])
        right = self.quick_sort(arr[w_pt + 1:])

        return left + [pivot] + right

quick_sort = Solution().quick_sort

def test_quick_sort():
    # Basic cases
    assert quick_sort([2, 3, 4, 1, 6]) == [1, 2, 3, 4, 6]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Edge cases
    assert quick_sort([1]) == [1]
    assert quick_sort([2, 1]) == [1, 2]
    assert quick_sort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]

    print("All tests passed")

if __name__ == "__main__":
    test_quick_sort()
