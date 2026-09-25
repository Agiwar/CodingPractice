from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        postorder DFS from every course: a course is written only after all its
        prereqs are written. prereqs_of already points to prereqs, so no reverse.

        in_progress is the current chain; hitting a course in it is a cycle, return [].
        course_done is every course already written; hitting one means it's taken,
        skip it, no need to check it again.

        no early return for a course without prereqs, unlike 207: here every course
        has to be written, and an empty loop costs nothing.

        Time: O(V + E), each course and each edge is visited once.
        Space: O(V + E) for prereqs_of, plus O(V) for the sets and recursion depth.
        """
        
        if not prerequisites:
            return list(range(numCourses))
        
        prereqs_of = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs_of[course].append(prereq)
        
        in_progress = set()
        course_done = set()
        course_done_order = []
        
        def can_take_course(course: int) -> bool:
            if course in course_done:
                return True
            
            if course in in_progress:
                return False
            
            in_progress.add(course)
            
            for prereq in prereqs_of[course]:
                if not can_take_course(prereq):
                    return False
            
            course_done.add(course)
            course_done_order.append(course)
            
            in_progress.remove(course)
            
            return True
        
        return (
            course_done_order
            if all(can_take_course(course) for course in range(numCourses))
            else []
        )


findOrder = Solution().findOrder

def is_valid_order(num_courses: int, prerequisites: list[list[int]], order: list[int]) -> bool:
    position_of = {course: idx for idx, course in enumerate(order)}
    covers_every_course_once = sorted(order) == list(range(num_courses))
    return covers_every_course_once and all(
        position_of[prereq] < position_of[course] for course, prereq in prerequisites
    )

def test_findOrder():
    # LeetCode examples (any valid order is accepted)
    assert is_valid_order(2, [[1,0]], findOrder(2, [[1,0]]))
    assert is_valid_order(4, [[1,0],[2,0],[3,1],[3,2]], findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    assert findOrder(1, []) == [0]

    # Edge cases
    # no prereqs: every course must still appear
    assert is_valid_order(3, [], findOrder(3, []))

    # 2-course cycle
    assert findOrder(2, [[1,0],[0,1]]) == []

    # 3-course cycle
    assert findOrder(3, [[0,1],[1,2],[2,0]]) == []

    # cycle among courses unreachable from course 0: must check every course
    assert findOrder(4, [[1,0],[2,3],[3,2]]) == []

    # reversed chain (0 needs 1 needs 2 ...): only one valid order, guards prereq direction
    assert findOrder(5, [[0,1],[1,2],[2,3],[3,4]]) == [4,3,2,1,0]

    # disconnected components, both valid: order must cover both
    assert is_valid_order(5, [[1,0],[3,2],[4,3]], findOrder(5, [[1,0],[3,2],[4,3]]))

    print("All tests passed")

if __name__ == "__main__":
    test_findOrder()
