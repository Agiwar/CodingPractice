from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True
        
        prereqs_of = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs_of[course].append(prereq)
        
        awaiting_courses = set()
        
        def can_take_course(course: int) -> bool:
            if course in awaiting_courses:
                return False
            
            elif not prereqs_of[course]:
                return True
            
            awaiting_courses.add(course)
            for prereq in prereqs_of[course]:
                if not can_take_course(prereq):
                    return False
            
            awaiting_courses.remove(course)
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
