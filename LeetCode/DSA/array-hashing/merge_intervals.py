class Solution:
    def merge_checking_iteration(self, intervals: list[list[int]]) -> list[list[int]]:
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
    
    def merge_nested_while(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        instead of checking merged condition is true for each iteration,
        using the second while loop to auto checks merged condition is true until false,
        then directly move idx to the pt position, so it's one pass traversal.
        also in edge case, if there's just only one interval, the while loop can handle it,
        no need to early return, and note that the sorting applied one interval works O(1) time
        
        time = O(n * log n)
        space = O(n)
        """
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        n = len(intervals)
        
        idx = 0
        while idx < n:
            pt = idx + 1
            
            while pt < n and intervals[idx][1] >= intervals[pt][0]:
                max_end = max(intervals[idx][1], intervals[pt][1])
                intervals[idx] = [intervals[idx][0], max_end]
                pt += 1
            
            merged.append(intervals[idx])
            idx = pt
        
        return merged
    
    def merge_compare_last_interval(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        this solution is most common expected which only one for loop to iterate intervals,
        the key is that if just first interval or the last merged interval's end time
        is smaller than the current interval's end time, which has no overlap,
        otherwise, interval is overlapped, update the last merged interval's end time,
        which is according to the max end time of last merged interval's or current interval's
        
        time = O(n * log n)
        space = O(n)
        """
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
            

merge_checking_iteration = Solution().merge_checking_iteration
merge_nested_while = Solution().merge_nested_while
merge_compare_last_interval = Solution().merge_compare_last_interval

def test_merge():
    # LeetCode examples
    assert merge_checking_iteration([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_checking_iteration([[1,4],[4,5]]) == [[1,5]]
    assert merge_checking_iteration([[4,7],[1,4]]) == [[1,7]]
    
    assert merge_nested_while([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_nested_while([[1,4],[4,5]]) == [[1,5]]
    assert merge_nested_while([[4,7],[1,4]]) == [[1,7]]

    assert merge_compare_last_interval([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_compare_last_interval([[1,4],[4,5]]) == [[1,5]]
    assert merge_compare_last_interval([[4,7],[1,4]]) == [[1,7]]

    # Edge cases
    assert merge_checking_iteration([[0, 1]]) == [[0, 1]]
    assert merge_checking_iteration([[1, 1]]) == [[1, 1]]
    assert merge_checking_iteration([[0, 1], [1, 1]]) == [[0, 1]]
    assert merge_checking_iteration([[0, 1], [1, 2]]) == [[0, 2]]
    assert merge_checking_iteration([[0, 1], [2, 2], [3, 4]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_checking_iteration([[3, 4], [0, 1], [2, 2]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_checking_iteration([[3, 4], [0, 1], [2, 2], [4, 8], [8, 9]]) == [[0, 1], [2, 2], [3, 9]]
    assert merge_checking_iteration([[3, 3], [3, 3]]) == [[3, 3]]
    assert merge_checking_iteration([[3, 3], [2, 3], [1, 3]]) == [[1, 3]]
    assert merge_checking_iteration([[1, 10], [2, 3]]) == [[1, 10]]

    assert merge_nested_while([[0, 1]]) == [[0, 1]]
    assert merge_nested_while([[1, 1]]) == [[1, 1]]
    assert merge_nested_while([[0, 1], [1, 1]]) == [[0, 1]]
    assert merge_nested_while([[0, 1], [1, 2]]) == [[0, 2]]
    assert merge_nested_while([[0, 1], [2, 2], [3, 4]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_nested_while([[3, 4], [0, 1], [2, 2]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_nested_while([[3, 4], [0, 1], [2, 2], [4, 8], [8, 9]]) == [[0, 1], [2, 2], [3, 9]]
    assert merge_nested_while([[3, 3], [3, 3]]) == [[3, 3]]
    assert merge_nested_while([[3, 3], [2, 3], [1, 3]]) == [[1, 3]]
    assert merge_nested_while([[1, 10], [2, 3]]) == [[1, 10]]

    assert merge_compare_last_interval([[0, 1]]) == [[0, 1]]
    assert merge_compare_last_interval([[1, 1]]) == [[1, 1]]
    assert merge_compare_last_interval([[0, 1], [1, 1]]) == [[0, 1]]
    assert merge_compare_last_interval([[0, 1], [1, 2]]) == [[0, 2]]
    assert merge_compare_last_interval([[0, 1], [2, 2], [3, 4]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_compare_last_interval([[3, 4], [0, 1], [2, 2]]) == [[0, 1], [2, 2], [3, 4]]
    assert merge_compare_last_interval([[3, 4], [0, 1], [2, 2], [4, 8], [8, 9]]) == [[0, 1], [2, 2], [3, 9]]
    assert merge_compare_last_interval([[3, 3], [3, 3]]) == [[3, 3]]
    assert merge_compare_last_interval([[3, 3], [2, 3], [1, 3]]) == [[1, 3]]
    assert merge_compare_last_interval([[1, 10], [2, 3]]) == [[1, 10]]


    print("All tests passed")

if __name__ == "__main__":
    test_merge()
