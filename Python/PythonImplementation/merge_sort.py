class Solution:
    def merge_sort(self, arr: list[int]) -> list[int]:
        if (n := len(arr)) <= 1:
            return arr
        
        m = n // 2
        arr_l = arr[:m]
        arr_r = arr[m:]
        
        self.merge_sort(arr_l)
        self.merge_sort(arr_r)
        
        i = j = k = 0
        while i < len(arr_l) and j < len(arr_r):
            if arr_l[i] <= arr_r[j]:
                arr[k] = arr_l[i]
                i += 1
            
            else:
                arr[k] = arr_r[j]
                j += 1
            
            k += 1
        
        while i < len(arr_l):
            arr[k] = arr_l[i]
            i += 1
            k += 1
        
        while j < len(arr_r):
            arr[k] = arr_r[j]
            j += 1
            k += 1
        
        return arr

merge_sort = Solution().merge_sort

def test_merge_sort():
    # Basic cases
    assert merge_sort([2, 3, 4, 1, 6]) == [1, 2, 3, 4, 6]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Edge cases
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]

    print("All tests passed")

if __name__ == "__main__":
    test_merge_sort()
