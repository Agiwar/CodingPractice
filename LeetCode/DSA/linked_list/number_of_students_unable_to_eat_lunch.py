from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        the main idea behind the code is determine what student's preference is,
            how many "0" type students want "0" type sandwiches, and so on "1" type

            edge case is students.length is one,
            if the only one student doesn't have their preferred sandwich, return 1 directly,
            on the other hand, if students and sandwiches are identical, return 0 directly.

        cuz the students queue will continue looping until that student gets their sandwich,
            it's like a circular looping for students, so the order of students doesn't matter,
            sandwiches' order is immutable, but that's not important,
            calculate how many *1* type sandwich, and *0*'s,
            traversing the sandwiches categories, if the current can be taken in students whoever,
            subtract total number of students by 1, and so on,
            if traversal done, means everyone is happy,
            but if the current sandwich can't be taken from someone, exit looping directly,
            then the current number of students is answer

        time = O(m), m is sandwiches.length
        space = O(1), stud_types counter always has length 2 regardless of students.length
        """
        
        if len(students) == 1 and students[0] != sandwiches[0]:
            return 1
        
        elif students == sandwiches:
            return 0
        
        
        from collections import Counter
        
        
        stud_types = Counter(students)
        for sand in sandwiches:
            if sand not in stud_types or not stud_types[sand]:
                return sum(stud_types.values())
            
            stud_types[sand] -= 1
        
        return 0



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
