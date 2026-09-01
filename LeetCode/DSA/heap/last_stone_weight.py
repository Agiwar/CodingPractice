import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        heapq is a min heap only, so negate every weight on the way in to fake a
            max heap, then pop gives the most negative one, which is the heaviest stone,
            and the arithmetic still holds in negated space,
            e.g. -8 and -7 pop out, (-8) - (-7) = -1, which is the weight 1 stone,
            so only the final answer needs to be negated back

        each round pops the two heaviest stones,
            if they are equal both are destroyed and nothing goes back to the heap,
            otherwise push their difference back so it can compete again,
            the loop stops when fewer than 2 stones are left

        time: O(n * log n), n is stones.length,
                the negation is O(n) and heapify is O(n),
                each round removes 2 stones and pushes back at most 1,
                so the size drops by at least 1 per round and the loop runs O(n) times,
                and each round costs O(log n) for the two pops and the one push,
                so total is O(n) + O(n) + O(n * log n) = O(n * log n)
        space: O(n) for the negated list,
                heapify is in-place so it only adds O(1),
                so total is O(n)
        """
        
        if len(stones) == 1:
            return stones[0]
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) // 2:
            y, x = (heapq.heappop(stones) for _ in range(2))
            
            if y != x:
                heapq.heappush(stones, y - x)
        
        return -stones[0] if stones else 0


lastStoneWeight = Solution().lastStoneWeight


def test_lastStoneWeight():
    # LeetCode Example 1
    assert lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

    # LeetCode Example 2
    assert lastStoneWeight([1]) == 1

    # Edge cases

    # Equal pair annihilates — nothing left, so 0
    assert lastStoneWeight([2, 2]) == 0

    # Two stones leave their difference
    assert lastStoneWeight([3, 7]) == 4

    # Odd count of identical stones — one survives
    assert lastStoneWeight([5, 5, 5]) == 5

    # The difference must be pushed back and re-compete:
    # 10,9 -> 1, then 3,2 -> 1, then 1,1 -> 0
    assert lastStoneWeight([9, 3, 2, 10]) == 0

    # Heaviest pair cancels first, then the remainder smashes
    assert lastStoneWeight([10, 4, 2, 10]) == 2

    # Max constraint values
    assert lastStoneWeight([1000, 1]) == 999

    print("All tests passed")


if __name__ == "__main__":
    test_lastStoneWeight()
