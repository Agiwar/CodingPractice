from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        the main idea behind the code is doing while looping to check the first student is fit first sandwich or not,
            the relevant order of sandwiches is immutable (exclude the first sandwich consumed)
            if the student doesn't have their favorite sandwich, pop this student and append it in last position
            if student has sandwich, continue consuming until they don't
            pop first student and append student both takes O(1) time,
            but making sure all students they've seen the first sandwich, needs to traversing students
            edge case is students.length is one, if the only one student doesn't have their preferred sandwich,
            return 1 directly, on the other hand, if students and sandwiches are identical, return 0 directly

        time = O(n^2), n is student.length
        space = O(1)
        """
        
        if len(students) == 1 and students[0] != sandwiches[0]:
            return 1
        
        elif students == sandwiches:
            return 0
        
        idx = 0
        ct_students = len(students)
        seen = 0
        
        while idx < ct_students:
            sandwich = sandwiches[idx]
            
            if students[idx] != sandwich:
                seen += 1
                
                if seen == ct_students:
                    break
                
                students.append(students.pop(idx))  # pop(0) is O(n) time not O(1)
            
            else:
                students.pop(idx)
                sandwiches.pop(idx)
                ct_students -= 1
                seen = 0
        
        return ct_students


countStudents = Solution().countStudents

def test_countStudents():
    assert countStudents([1,1,0,0], [0,1,0,1]) == 0
    assert countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3

    # Edge cases
    assert countStudents([0], [0]) == 0
    assert countStudents([1], [1]) == 0
    assert countStudents([1], [0]) == 1
    assert countStudents([0, 0], [1, 1]) == 2
    assert countStudents([0, 0], [0, 1]) == 1
    assert countStudents([1, 1], [0, 1]) == 2
    assert countStudents([1, 1], [1, 0]) == 1
    assert countStudents([1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]) == 0
    assert countStudents([0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1]) == 2


    print("All tests passed")

if __name__ == "__main__":
    test_countStudents()
