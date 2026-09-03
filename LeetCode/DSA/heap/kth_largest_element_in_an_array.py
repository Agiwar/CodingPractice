import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        kth largest = the smallest of the k largest, so keep exactly the k largest
            in a min heap and the root is the answer. duplicates occupy separate
            ranks, no special handling.

        heapify all n in place, then pop until size is k — each pop evicts the
            current minimum, which can never be among the k largest.
            read the root without popping, so the heap is left holding the k largest

        contract: this mutates the caller's list. nums is heapified and then drained
            down to k elements, so after the call it is neither the original list
            nor sorted. leetcode allows this, it hands over a throwaway list and
            calls once, but the caller cannot reuse nums afterwards —
            a second call on the same list returns a wrong answer rather than raising

        time: O(n + (n - k) * log n), n is len(nums),
                heapify O(n), then (n - k) pops each O(log n) on a heap of size <= n,
                reading the root is O(1).
                worst at k = 1, nearly everything is popped,
                best at k = n, nothing is popped

        space: O(1) extra, heapify is in place on the input,
                O(n) extra if the input must be preserved, via min_heap = list(nums)

        alternatives:
            push-one-by-one size-k min heap: O(n log k) time, O(k) space,
                never touches the input, and it streams.
                dominates the list(nums) copy on both space and safety,
                wins outright when k << n
            quickselect: O(n) average, O(n^2) worst without a random pivot,
                in place, batch only — the true optimum;
                partition on a pivot, recurse into the side holding index n - k
        """
        
        min_heap = nums
        heapq.heapify(min_heap)
        
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return min_heap[0]


findKthLargest = Solution().findKthLargest


def test_findKthLargest():
    # LeetCode Example 1
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    # LeetCode Example 2
    assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    # Edge cases

    # Single element
    assert findKthLargest([1], 1) == 1

    # k = 1 is the max, k = len(nums) is the min
    assert findKthLargest([3, 2, 1], 1) == 3
    assert findKthLargest([3, 2, 1], 3) == 1

    # All identical — duplicates each count as their own element
    assert findKthLargest([2, 2, 2, 2], 2) == 2

    # Duplicates straddling the kth position — no dedup allowed
    assert findKthLargest([1, 2, 2, 3], 2) == 2

    # Negative values
    assert findKthLargest([-1, -1, -2], 2) == -1


    print("All tests passed")


if __name__ == "__main__":
    test_findKthLargest()
