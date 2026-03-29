class Solution:
    def bucket_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        
        min_num, max_num = min(arr), max(arr)
        bucket_ct = max_num - min_num + 1
        buckets = [0] * bucket_ct
        
        for num in arr:
            buckets[num - min_num] += 1
        
        w_pt = 0
        for ct in range(len(buckets)):
            for _ in range(buckets[ct]):
                arr[w_pt] = ct + min_num
                w_pt += 1
        
        return arr
        

bucket_sort = Solution().bucket_sort

def test_bucket_sort():
    # Basic cases
    assert bucket_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
    assert bucket_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bucket_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Edge cases
    assert bucket_sort([1]) == [1]
    assert bucket_sort([2, 1]) == [1, 2]
    assert bucket_sort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]

    print("All tests passed")

if __name__ == "__main__":
    test_bucket_sort()
