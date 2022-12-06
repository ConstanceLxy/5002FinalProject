import pandas as pd
import numpy as np
from Student_record import record


def save(students, position):
    choose = input('You want to choose：Chinese（1）Math（2）English（3）Total（4）：')
    list_choose = choose.split()
    list_choose = [int(x) for x in list_choose]
    labels = ['Chinese', 'Math', 'English', 'Total']
    labels_show = ['Name', 'ID']
    for i in list_choose:
        labels_show.append(labels[list_choose[i - 1] - 1])
    students_1 = np.asarray([labels_show])
    for student in students:
        data_student = [student.list_scores[0], student.list_scores[1], student.list_scores[2], student.sum()]
        data_student_show = [student.name, student.id]
        for i in list_choose:
            data_student_show.append(data_student[list_choose[i - 1] - 1])
        data_student_show = np.asarray([data_student_show])
        students_1 = np.append(students_1, data_student_show, axis=0)
    data = pd.DataFrame(students_1)
    data.to_excel(position, header=False, index=False)


def part_save(students):
    while True:
        print("""
                    Save     
                 Save.................1
                 Save as...............2
                 exit.................3
         """)
        choose = 0
        try:
            choose = int(input('please input 1-3：'))
        except:
            print('')
        if choose == 1:
            record('save', choose)
            position = 'Student_Scores.xlsx'
            save(students, position)
            print('save successfully！')
        elif choose == 2:
            record('save', choose)
            position = 'Student_Scores_1.xlsx'
            save(students, position)
            print('save successfully！')
        elif choose == 3:
            record('save', choose)
            return
        else:
            print('Wrong input,please try again!')
