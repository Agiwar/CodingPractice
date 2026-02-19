from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass

canAttendMeetings = Solution().canAttendMeetings

def test_canAttendMeetings():
    assert canAttendMeetings([[0,30],[5,10],[15,20]]) == False
    assert canAttendMeetings([[7,10],[2,4]]) == True

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_canAttendMeetings()
