from typing import List


class Solution:
    # Use bubble sort to sort all meetings by its start time.
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