import heapq


class Solution:
    def _get_point_distance(self, point: list[int, int]) -> list[int, list[int, int]]:
        return [sum(pt ** 2 for pt in point), point]
    
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        create a min heap, each node is [distance, point],
            where distance is the distance between this point and the origin.

        to get the k points closest to the origin,
            just min heap pop k times

        create a helper function to get distance between point and origin,
            helper function returns the distance first, then the point coordinate,
            so the heap orders by distance

        time: O(n + k * log n), O(n) to build the distance list,
                O(n) to heapify it in place, O(log n) for each heappop, k times.
                the k * log n term does not collapse into O(n),
                n is total number of points
        space: O(n) for the heap, which holds one entry per point,
                output doesn't count
        """
        
        min_heap = [self._get_point_distance(point) for point in points]
        heapq.heapify(min_heap)

        return [heapq.heappop(min_heap)[1] for _ in range(k)]


kClosest = Solution().kClosest


def normalize(points: list[list[int]]) -> list[list[int]]:
    # the answer may be returned in any order
    return sorted(points)


def test_kClosest():
    # LeetCode Example 1
    assert normalize(kClosest([[1, 3], [-2, 2]], 1)) == normalize([[-2, 2]])

    # LeetCode Example 2
    assert normalize(kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == normalize(
        [[3, 3], [-2, 4]]
    )

    # Edge cases

    # Single point, k = 1
    assert normalize(kClosest([[5, 5]], 1)) == normalize([[5, 5]])

    # k equals len(points) — everything comes back
    assert normalize(kClosest([[1, 1], [2, 2]], 2)) == normalize([[1, 1], [2, 2]])

    # A point sitting on the origin is the closest possible
    assert normalize(kClosest([[0, 0], [1, 1]], 1)) == normalize([[0, 0]])

    # Negative coordinate — distance is squared, not raw (9 < 25)
    assert normalize(kClosest([[-5, 0], [3, 0]], 1)) == normalize([[3, 0]])

    # Tie in distance, but unambiguous at k = 2 (dists 1, 1, 4)
    assert normalize(kClosest([[1, 0], [-1, 0], [0, 2]], 2)) == normalize(
        [[1, 0], [-1, 0]]
    )

    # Large coordinates — guards against float/sqrt precision shortcuts
    assert normalize(kClosest([[10000, 10000], [1, 1]], 1)) == normalize([[1, 1]])

    print("All tests passed")


if __name__ == "__main__":
    test_kClosest()
