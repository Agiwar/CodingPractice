from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        to take a course, all its prereqs must be takeable too, any one fails then the course fails,
            so DFS down each course's prereq chain, in_progress holds the courses on the current chain,
            reaching a course that's still in progress means it loops back to itself, which is a cycle

        once a course passes, empty its prereqs to mark it done,
            so later checks return True right away, and each course is explored only once

        time = O(V + E), each course and each prereq edge visited once
        space = O(V + E), adjacency list, plus O(V) for in_progress and recursion depth
        """
        
        if not prerequisites:
            return True
        
        prereqs_of = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs_of[course].append(prereq)
        
        in_progress = set()
        
        def can_take_course(course: int) -> bool:
            if course in in_progress:
                return False
            
            elif not prereqs_of[course]:
                return True
            
            in_progress.add(course)
            for prereq in prereqs_of[course]:
                if not can_take_course(prereq):
                    return False
            
            in_progress.remove(course)
            prereqs_of[course] = []
            
            return True
        
        return all(can_take_course(course) for course in range(numCourses))


canFinish = Solution().canFinish

def test_canFinish():
    # LeetCode Example 1
    assert canFinish(2, [[1,0]]) is True

    # LeetCode Example 2
    assert canFinish(2, [[1,0],[0,1]]) is False

    # Edge cases
    # self-loop: smallest possible cycle
    assert canFinish(1, [[0,0]]) is False

    # 3-course cycle: longer than 2
    assert canFinish(3, [[0,1],[1,2],[2,0]]) is False

    # cycle among courses unreachable from course 0: must check every course
    assert canFinish(4, [[1,0],[2,3],[3,2]]) is False

    # diamond: shared prereq must not be flagged as a cycle
    assert canFinish(4, [[1,0],[2,0],[3,1],[3,2]]) is True

    print("All tests passed")

if __name__ == "__main__":
    test_canFinish()
