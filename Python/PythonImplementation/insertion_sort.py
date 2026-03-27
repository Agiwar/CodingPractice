class Solution:
    """
    insertion sort is determine what value needed to be inserted at the current position
    if there's only one num in array, that guarantee this array is already sorted,
    so the position pointer starts at index 1 (second position),
    and then define another pointer to represent position's sub-pointer,
    use this sub-pointer to make sure all nums before num at position pointer are sorted
    
    time = O(n^2), O(n) for best case
    space = O(1), in-place manipulation
    """
    
    def insertion_sort(self, arr: list[int]) -> list[int]:
        for i in range(1, len(arr)):
            j = i - 1
            
            while j >= 0 and arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
        
        return arr


insertion_sort = Solution().insertion_sort

def test_insertion_sort():
    # Basic cases
    assert insertion_sort([2, 3, 4, 1, 6]) == [1, 2, 3, 4, 6]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Edge cases
    assert insertion_sort([1]) == [1]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]

    print("All tests passed")

if __name__ == "__main__":
    test_insertion_sort()
