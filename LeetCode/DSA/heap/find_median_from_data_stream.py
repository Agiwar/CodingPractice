import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """
        split the stream into two halves,
            max_heap holds the smaller half (negated cuz heapq is min-heap only),
            min_heap holds the larger half,
            so the median only depends on the tops of both heaps

        push the new num into max_heap first,
            if it is bigger than min_heap's top then the order is broken,
            cuz max_heap's top is exactly that new num, move it over to min_heap,
            after the move the size gap can be 2, so move one element back,
            keep the gap <= 1 so findMedian can just read the tops

        time = O(log n), push and pop on heaps
        space = O(n), store every num across two heaps
        """

        heapq.heappush(self.max_heap, -num)
        
        if self.min_heap and self.min_heap[0] < -self.max_heap[0]:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        """
        odd count means the extra element sits on the bigger heap, so its top is the median,
        even count means both halves are equal, so average the two tops

        time = O(1), only peek the tops
        space = O(1)
        """

        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


def test_median_finder():
    # LeetCode example
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    # Edge: single element
    mf = MedianFinder()
    mf.addNum(7)
    assert mf.findMedian() == 7.0

    # Edge: descending inserts, input is not pre-sorted
    mf = MedianFinder()
    for num in [3, 2, 1]:
        mf.addNum(num)
    assert mf.findMedian() == 2.0
    mf.addNum(0)
    assert mf.findMedian() == 1.5

    # Edge: all duplicates
    mf = MedianFinder()
    for _ in range(4):
        mf.addNum(5)
    assert mf.findMedian() == 5.0

    # Edge: negatives, and even count averaging across zero
    mf = MedianFinder()
    mf.addNum(-5)
    mf.addNum(5)
    assert mf.findMedian() == 0.0
    mf.addNum(-1)
    assert mf.findMedian() == -1.0

    # Edge: median stays correct after every insert
    mf = MedianFinder()
    expected = [6.0, 6.5, 6.0, 4.0, 5.0, 5.5, 6.0, 6.5, 6.0, 5.5]
    for num, want in zip([6, 7, 2, 1, 5, 9, 10, 8, 3, 4], expected):
        mf.addNum(num)
        assert mf.findMedian() == want

    print("All tests passed")


if __name__ == "__main__":
    test_median_finder()
