from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        if intervals.length is one, directly return 1, and there must be at least one meeting room required
            regardless of conflict occurrence, and if current meeting's end is equal to next one's,
            can use the same room, cuz people are gone when current meeting ended,
            assume at this time, next meeting's people can enter the room

        the main idea the code is observe the dependency of each meeting's time duration,
            to correctly check each meeting start & end, need to sort,
            if each meeting's start & end time has no conflict with next one,
            which means no need to occupy another meeting room,
            if conflict occurred, another meeting rooms required, depends on how many conflicts there are

        time = O(n * log n), n is intervals.length
        space = O(1)
        """

        if (n := len(intervals)) == 1:
            return 1

        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        res, ct = 0, 0
        s, e = 0, 0

        while s < n:
            if starts[s] < ends[e]:
                ct += 1
                s += 1

            else:
                ct -= 1
                e += 1

            res = max(res, ct)

        return res



minMeetingRooms = Solution().minMeetingRooms

def test_minMeetingRooms():
    # LeetCode examples
    assert minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert minMeetingRooms([[7,10],[2,4]]) == 1

    # Edge cases
    assert minMeetingRooms([[1, 3], [2, 6], [8, 10], [15, 18]]) == 2
    assert minMeetingRooms([[1, 4], [4, 5]]) == 1
    assert minMeetingRooms([[4, 7], [1, 4]]) == 1
    assert minMeetingRooms([[0, 1]]) == 1
    assert minMeetingRooms([[0, 1], [1, 2]]) == 1
    assert minMeetingRooms([[0, 1], [0, 2], [0, 3]]) == 3
    assert minMeetingRooms([[1, 10], [2, 3]]) == 2
    assert minMeetingRooms([[3, 4], [4, 8], [8, 9]]) == 1
    assert minMeetingRooms([[3, 4], [2, 8], [8, 9]]) == 2
    assert minMeetingRooms([[3, 4], [2, 8], [4, 9]]) == 2
    assert minMeetingRooms([[3, 4], [2, 8], [1, 9]]) == 3


    print("All tests passed")

if __name__ == "__main__":
    test_minMeetingRooms()
