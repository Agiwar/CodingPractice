import argparse
from typing import List


def argparse_list() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-stu", "--students", type=int, nargs="+")
    parser.add_argument("-sand", "--sandwiches", type=int, nargs="+")
    args = parser.parse_args()
    return args


# first submission
# def count_students(students: List[int], sandwiches: List[int]) -> int:
#     if sum(students) == sum(sandwiches):
#         while students:
#             if students[0] == sandwiches[0]:
#                 students.pop(0)
#                 sandwiches.pop(0)
#             else:
#                 students.append(students.pop(0))
#         return 0
#     else:
#         ct = 0
#         while students:
#             if students[0] == sandwiches[0]:
#                 ct = 0
#                 students.pop(0)
#                 sandwiches.pop(0)
#             else:
#                 ct += 1
#                 if sandwiches[0] not in students and ct == len(students):
#                     return ct
#                 students.append(students.pop(0))


# second submission
# def count_students(students: List[int], sandwiches: List[int]) -> int:
#     ct = 0
#     while students:
#         if students[0] == sandwiches[0]:
#             ct = 0
#             students.pop(0)
#             sandwiches.pop(0)
#         else:
#             ct += 1
#             if sandwiches[0] not in students and ct == len(students):
#                 return ct
#             students.append(students.pop(0))
#     return ct


# third solution
def count_students(students: List[int], sandwiches: List[int]) -> int:
    if len(students) == 1 and students[0] != sandwiches[0]:
        return 0

    ct = 0
    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            ct = 0
        
        else:
            students.append(students.pop(0))
            ct += 1
            
            if ct == len(students):
                break
    
    return ct


if __name__ == "__main__":
    args = argparse_list()
    students = args.students
    sandwiches = args.sandwiches
    num_students_no_lunch = count_students(students=students, sandwiches=sandwiches)

    # given students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1]
    # you may get 3
    print(num_students_no_lunch)
