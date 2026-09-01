import heapq


class KthLargest:
    """
    to get the k-th largest number is controlling the min heap size,
        the invariant is the heap always holds the k largest numbers seen so far,
        so the heap's minimum, heap[0], is exactly the k-th largest

    at first, heapify the input nums, heapify doesn't sort the array,
        it only makes every parent <= its children, so only heap[0] is guaranteed
        to be the minimum, the rest stays unordered,
        then pop (len(nums) - k) times to shrink the heap down to size k

    for each add, push the new value first,
        if the size grows over k, pop the minimum away,
        so the heap stays at size k and heap[0] is still the k-th largest

    time: __init__ is O(n + (n - k) * log n), cuz heapify is O(n)
            and each of the (n - k) pops costs O(log n),
            add is O(log k), one push and at most one pop on a heap of size k,
            and reading heap[0] is O(1),
            n is the length of nums (duplicates included)
    space: O(k), the heap never keeps more than k numbers,
            no matter how long the stream goes
    """
    
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
        


def test_KthLargest():
    # LeetCode Example 1
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

    # LeetCode Example 2 — heavy duplicates
    obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert obj.add(2) == 7
    assert obj.add(10) == 7
    assert obj.add(9) == 7
    assert obj.add(9) == 8

    # Edge cases

    # Empty initial nums with k = 1 — the stream fills itself up
    obj = KthLargest(1, [])
    assert obj.add(-3) == -3
    assert obj.add(-2) == -2
    assert obj.add(-4) == -2
    assert obj.add(0) == 0
    assert obj.add(4) == 4

    # Initial nums shorter than k — only valid once k elements exist
    obj = KthLargest(2, [1])
    assert obj.add(2) == 1
    assert obj.add(3) == 2

    # k equals len(nums)
    obj = KthLargest(4, [4, 5, 8, 2])
    assert obj.add(3) == 3
    assert obj.add(10) == 4

    # All identical values — duplicates each count as their own element
    obj = KthLargest(2, [5, 5, 5])
    assert obj.add(5) == 5
    assert obj.add(1) == 5

    # Values below the current kth must not change the answer
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(1) == 4
    assert obj.add(0) == 4

    # Two instances must not share state (guards against class-level mutables)
    a = KthLargest(1, [1])
    b = KthLargest(1, [100])
    assert a.add(2) == 2
    assert b.add(3) == 100

    print("All tests passed")


if __name__ == "__main__":
    test_KthLargest()
