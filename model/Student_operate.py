from Student_load import load
from Student_class import Student
# from Student_record import record
from model.Student_Search import *

"""
                   File Function Description
scores_divided[used in sort]        -return a list with all the students scores and sum
sort                  -sort by subject

change score          -change a specific student's specific score
insert                -insert a student's information
part_operate          -use in a terminal
"""



def scores_divided(students):
    list_Chinese = []
    list_Math = []
    list_English = []
    list_Total = []
    for student in students:
        list_Chinese.append(student.list_scores[0])
        list_Math.append(student.list_scores[1])
        list_English.append(student.list_scores[2])
        list_Total.append(student.sum())
    list = [list_Chinese, list_Math, list_English, list_Total]
    return list


def sort(students):
    def bubble(students, list):  #bubble sort
        choose_1 = 0
        try:
            choose_1 = int(input('up（1） down（2）：'))
        except:
            print('')
        if choose_1 == 1:
            for i in range(1, len(list)):
                for j in range(0, len(list) - i):
                    if list[j] > list[j + 1]:
                        students[j], students[j + 1] = students[j + 1], students[j]
                        list[j], list[j + 1] = list[j + 1], list[j]
        elif choose_1 == 2:
            for i in range(1, len(list)):
                for j in range(0, len(list) - i):
                    if list[j] < list[j + 1]:
                        students[j], students[j + 1] = students[j + 1], students[j]
                        list[j], list[j + 1] = list[j + 1], list[j]
        else:
            print('invalid input')

    def selection(students, list):  # choose sort
        choose_1 = 0
        try:
            choose_1 = int(input('up（1） down（2）：'))
        except:
            print('')
        if choose_1 == 1:
            for i in range(0, len(list)):
                num = i
                for j in range(i + 1, len(list)):
                    if list[num] > list[j]:
                        num = j
                if num != i:
                    students[i], students[num] = students[num], students[i]
                    list[i], list[num] = list[num], list[i]
        elif choose_1 == 2:
            for i in range(0, len(list)):
                num = i
                for j in range(i + 1, len(list)):
                    if list[num] < list[j]:
                        num = j
                if num != i:
                    students[i], students[num] = students[num], students[i]
                    list[i], list[num] = list[num], list[i]
        else:
            print('invalid input')

    choose = 0
    try:
        choose = int(input('sort by:Chinese（1） Math（2） English（3） Total（4）：'))
    except:
        print('')
    if choose == 1:
        list_scores_all = scores_divided(students)
        bubble(students, list_scores_all[0])
    elif choose == 2:
        list_scores_all = scores_divided(students)
        selection(students, list_scores_all[1])
    elif choose == 3:
        list_scores_all = scores_divided(students)
        bubble(students, list_scores_all[2])
    elif choose == 4:
        list_scores_all = scores_divided(students)
        selection(students, list_scores_all[3])
    else:
        print('invalid input')


def change_score(students):
    name = input('Please input name or id：')
    for student in students:
        if student.name == name or str(student.id) == name:
            subject = 0
            try:
                subject = int(input('You want to change：Chinese（1）Math（2）English（3）：'))
            except:
                print("")
            if subject == 1:
                try:
                    new_score = int(input('please input new score：'))
                    student.list_scores[0] = new_score
                except:
                    print('invalid input')
            elif subject == 2:
                try:
                    new_score = int(input('please input new score：'))
                    student.list_scores[1] = new_score
                except:
                    print('invalid input')
            elif subject == 3:
                try:
                    new_score = int(input('please input new score：'))
                    student.list_scores[2] = new_score
                except:
                    print('invalid input')
            else:
                print('invalid input')


def insert(students):
    name = input('name：')
    while True:
        try:
            id = int(input('id：'))
            Chinese = float(input('Chinese：'))
            Math = float(input('Math：'))
            English = float(input('English：'))
            break
        except:
            print('invalid input,please try again！')
    new_student = Student(name, id, Chinese, Math, English)
    students.append(new_student)

def printStudentInfo(students):
    for student in students:
        print(f"Student Name: {student.name}")
        print(f"Student ID:   {student.id}")
        print(f"Chinese: {student.list_scores[0]},   Math: {student.list_scores[1]},   English: {student.list_scores[2]}")
        print(f"Grades:  {student.list_grades[0]}             {student.list_grades[1]}                {student.list_grades[2]}")
        print("---------------------------------------------")






def part_operate(students):
    while True:
        print("""
                       
                 Initialize...................1
                 Change.......................2
                 Sort.........................3
                 Insert.......................4
                 Print All Information........5
                 Exit.........................6
                 Show Average Scores..........7
                 Show Variance................8
                 Show Median..................9

         """)
        choose = 0
        try:
            choose = int(input('please input 1-5 to begin what you want to do：'))
        except:
            print('')
        if choose == 1:
            record('operate', choose)
            students = load()
            print('initialize successfully！')
        elif choose == 2:
            record('operate', choose)
            change_score(students)
            print('update successfully！')
        elif choose == 3:
            record('operate', choose)
            sort(students)
            print('sorted successfully')
        elif choose == 4:
            record('operate', choose)
            insert(students)
            print('add successfully')
        elif choose == 5:
            printStudentInfo(students)
        elif choose == 6:
            record('operate', choose)
            return
        elif choose == 7:
            show_average(students, len(students))
        elif choose == 8:
            show_variance(students)
        elif choose == 9:
            show_median(students)
        else:
            print('invalid input,please try again！')


