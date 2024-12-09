from typing import List


class Solution1:
    # Use bubble sort to sort all meetings by its start time.
    # time = O(n^2)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        
        if n in {0, 1}:
            return True
        
        while n > 1:
            need_to_swap = False
            
            for i in range(1, n):
                if intervals[i - 1][0] > intervals[i][0]:
                    need_to_swap = True
                    intervals[i - 1], intervals[i], intervals[i], intervals[i - 1]
            
            if not need_to_swap:
                break
            
            n -= 1
        
        return (
            all(intervals[i - 1][1] <= intervals[i][0] for i in range(1, len(intervals)))
        )


class Solution2:
    # time = O(n * log n)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x[0])
        
        return (
            all(intervals[i - 1][1] <= intervals[i][0] for i in range(1, len(intervals)))
        )


class Solution3:
    # Use set() to store the meeting time which is occupied.
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        
        time_occupied = set()
        for meeting in intervals:
            for meeting_time in range(meeting[0], meeting[1]):
                if meeting_time not in time_occupied:
                    time_occupied.add(meeting_time)
                
                else:
                    return False  # The meeting time has been occupied.
        
        return True