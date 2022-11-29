from Student_operate import *


# Read in the student info file
students = load()


# Grades every students
for student in students:
    student.grade()
#     print(student.name)
#     print(student.Variance())
#     print(student.sum())
#     print("-----------")
part_operate(students)
