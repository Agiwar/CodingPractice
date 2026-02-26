from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        there's at least one meeting, directly return itself,
            if current meeting's end is equal to next one's start, it's overlap (meeting conflict)
            results are merge all conflict meetings along with non-conflict meetings

        the main idea behind code is figure out these meetings sequence,
            to check each one's start & end, so need to sort them,
            merge conditions are curr's end >= next's start,
            merged one has biggest end time, so if curr's end >= next's end, select curr's end,
            if after merged, merged still conflicts next one,
            need to merge them as well until there's no overlap

        time = O(n * log n), n is intervals.length
        space = O(n)
        """


        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        merged = []
        curr, next = 0, 1
        
        while next < len(intervals):
            if intervals[curr][1] >= intervals[next][0]:
                max_end = max(intervals[curr][1], intervals[next][1])
                intervals[curr] = [intervals[curr][0], max_end]
            
            else:
                merged.append(intervals[curr])
                curr = next
            
            next += 1
        
        merged.append(intervals[curr])
        
        return merged
            

merge = Solution().merge

def test_merge():
    # LeetCode examples
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([[4,7],[1,4]]) == [[1,7]]

    # Edge cases
    assert merge([[0, 1]]) == [[0, 1]]
    assert merge([[1, 1]]) == [[1, 1]]
    assert merge([[0, 1], [1, 1]]) == [[0, 1]]
    assert merge([[0, 1], [1, 2]]) == [[0, 2]]
    assert merge([[0, 1], [2, 2], [3, 4]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge([[3, 4], [0, 1], [2, 2]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge([[3, 4], [0, 1], [2, 2], [4, 8], [8, 9]]) == [[0, 1], [2, 2], [3, 9]]
    assert merge([[3, 3], [3, 3]]) == [[3, 3]]
    assert merge([[3, 3], [2, 3], [1, 3]]) == [[1, 3]]
    assert merge([[1, 10], [2, 3]]) == [[1, 10]]


    print("All tests passed")

if __name__ == "__main__":
    test_merge()
