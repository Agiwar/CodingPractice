from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        intervals[i] means the ith meeting, no need to attend 1st first, and then 2nd meeting etc,
            can attend 2nd, then 1st for example,
            as long as the current meeting's start is strictly earlier than the others' start,
            and current meeting's end is earlier or equal to next meeting's start,
            if no interval, return false cuz no any meetings can attend,
            if there's just one meeting, return true, definitely can attend

        cuz not strictly attend 1st, 2nd, then 3rd, etc meetings, so doing sort these meetings first,
            and compare their start and end time to determine if all meetings can be attended.

        time = O(n * log n), n is interval.length
        space = O(1)
        """

        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda x: x[0])

        return all(
            intervals[i - 1][1] <= intervals[i][0]
            for i in range(1, len(intervals))
        )


canAttendMeetings = Solution().canAttendMeetings

def test_canAttendMeetings():
    # LeetCode examples
    assert canAttendMeetings([[0,30],[5,10],[15,20]]) == False
    assert canAttendMeetings([[7,10],[2,4]]) == True

    # Edge cases
    assert canAttendMeetings([]) == True
    assert canAttendMeetings([[0, 1]]) == True
    assert canAttendMeetings([[1, 2], [0, 1]]) == True
    assert canAttendMeetings([[0, 1], [2, 3], [4, 5]]) == True
    assert canAttendMeetings([[4, 5], [2, 3], [0, 1]]) == True
    assert canAttendMeetings([[3, 5], [1, 3], [0, 1]]) == True
    assert canAttendMeetings([[3, 5], [1, 4], [0, 1]]) == False
    assert canAttendMeetings([[3, 6], [4, 8], [5, 10]]) == False
    assert canAttendMeetings([[3, 6], [7, 14], [15, 30]]) == True


    print("All tests passed")

if __name__ == "__main__":
    test_canAttendMeetings()
