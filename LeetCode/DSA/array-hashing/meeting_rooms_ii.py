import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
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
        space = O(n)
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
    
    def minMeetingRooms_min_heap(self, intervals: list[list[int]]) -> int:
        """
        at first sort the intervals by start time, make sure what room is occupied first,
        when traversing intervals, put interval's end time to min-heap,
        the min-heap guarantees to show the minimum interval end time among all intervals when indexing zero,
        however, in order to get the minimum number of occupied rooms,
        need to check the current all room's smallest end time can be over before next interval's start time,
        if can, means the current occupied room can be freed up for next meeting usage,
        
        n = intervals.length which must be larger or equal to 1
        time: O(n * log n) where:
            sorting: O(n * log n)
            build min-heap by push/pop, occupied rooms is k, total is n, so O(n * log k)
                cuz k <= n is guaranteed, so O(n * log n)
            
        space: O(n), the worst case is all rooms are occupied
        """
        
        intervals.sort(key=lambda x: x[0])
        using_rooms = []
        
        for start, end in intervals:
            if using_rooms and using_rooms[0] <= start:
                heapq.heappop(using_rooms)
                
            heapq.heappush(using_rooms, end)
        
        return len(using_rooms)



minMeetingRooms = Solution().minMeetingRooms
minMeetingRooms_min_heap = Solution().minMeetingRooms_min_heap

def test_minMeetingRooms():
    # LeetCode examples
    assert minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert minMeetingRooms([[7,10],[2,4]]) == 1

    assert minMeetingRooms_min_heap([[0,30],[5,10],[15,20]]) == 2
    assert minMeetingRooms_min_heap([[7,10],[2,4]]) == 1

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

    assert minMeetingRooms_min_heap([[1, 3], [2, 6], [8, 10], [15, 18]]) == 2
    assert minMeetingRooms_min_heap([[1, 4], [4, 5]]) == 1
    assert minMeetingRooms_min_heap([[4, 7], [1, 4]]) == 1
    assert minMeetingRooms_min_heap([[0, 1]]) == 1
    assert minMeetingRooms_min_heap([[0, 1], [1, 2]]) == 1
    assert minMeetingRooms_min_heap([[0, 1], [0, 2], [0, 3]]) == 3
    assert minMeetingRooms_min_heap([[1, 10], [2, 3]]) == 2
    assert minMeetingRooms_min_heap([[3, 4], [4, 8], [8, 9]]) == 1
    assert minMeetingRooms_min_heap([[3, 4], [2, 8], [8, 9]]) == 2
    assert minMeetingRooms_min_heap([[3, 4], [2, 8], [4, 9]]) == 2
    assert minMeetingRooms_min_heap([[3, 4], [2, 8], [1, 9]]) == 3


    print("All tests passed")

if __name__ == "__main__":
    test_minMeetingRooms()
