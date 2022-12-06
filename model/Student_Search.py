"""
                 Function Description
show_scores(students)       -print specific student's score
show_average(students,num)  -print average scores from the whole class
show_rank(students)         -print specific student rank
show_variance(students)     -print students scores variance from low to high
show_highest(students)      -print the highest score for three subjects

grades_divided(students)    -return students' grades in default order        [to continue]
show_grade(students)        -print the number of people in each grade for the three subjects

"""

def show_scores(students,ID):
    flag = 0
    for student in students:
        if student.name == ID or str(student.id) == ID:
            print(f"Chinese :{student.list_scores[0]:.2f},math:{student.list_scores[1]:.2f},English:{student.list_scores[2]:.2f},Total:{student.sum():.2f}")
            flag = 1
            break
    if flag == 0:
        print("no this student")
        return

def show_average(students,num):
    def average(list,num):
        sum = 0
        for i in list:
            sum += i
        return sum / num

    # save every subject scores
    list_Chinese = []
    list_Math = []
    list_English = []

    for student in students:
        list_Chinese.append(student.list_scores[0])
        list_Math.append(student.list_scores[1])
        list_English.append(student.list_scores[2])

    ave = [] #save every subject's average
    ave.append(int(average(list_Chinese,num)))
    ave.append(int(average(list_Math,num)))
    ave.append(int(average(list_English,num)))
    print('Average Scores: ')
    print('Chinese: ' + str(ave[0]))
    print('English: ' + str(ave[1]))
    print('Math:    ' + str(ave[2]))
    return ave

def show_rank(students, NameId):
    list_Chinese = []
    list_Math = []
    list_English = []
    list_sum = []
    for student in students:
        list_Chinese.append(student.list_scores[0])
        list_Math.append(student.list_scores[1])
        list_English.append(student.list_scores[2])
        list_sum.append(student.sum())

    list_Chinese.sort(reverse=True)  # sort,down
    list_Math.sort(reverse=True)
    list_English.sort(reverse=True)
    list_sum.sort(reverse=True)
    rank = []
    flag = 0
    for student in students:
        if student.name == NameId or str(student.id) == NameId:
            rank.append(list_Chinese.index(student.list_scores[0]))
            rank.append(list_Math.index(student.list_scores[1]))
            rank.append(list_English.index(student.list_scores[2]))
            rank.append(list_sum.index(student.sum()))
            flag = 1
            break
    if flag == 0:
        print('no this student')
        return
    print(f"Chinese：{rank[0] + 1},Math：{rank[1] + 1},English：{rank[2] + 1},Total：{rank[3] + 1}")

def show_variance(students):
    name = []
    variance = []
    for student in students:
        if student.list_scores[0] == -1 or student.list_scores[1] == -1 or student.list_scores[2] == -1:
            continue
        name.append(student.name)
        variance.append(student.Variance())
    dict_0 = dict(zip(name,variance)) #make 2 lists into a dic with zip
    dict_1 = sorted(dict_0.items(),key = lambda x:x[1])
    for i in dict_1:
        print(i)
def show_highest(students):
    list_Chinese = []
    list_Math = []
    list_English = []
    for student in students:
        list_Chinese.append(student.list_scores[0])
        list_Math.append(student.list_scores[1])
        list_English.append(student.list_scores[2])
    list_Chinese.sort(reverse=True)
    list_Math.sort(reverse=True)
    list_English.sort(reverse=True)
    print('-------------------------------------------------------------')
    for student in students:
        if student.list_scores[0] == list_Chinese[0]:
            print(f"{student.name} get highest {list_Chinese[0]:.2f} in Chinese ")
    print('-------------------------------------------------------------')
    for student in students:
        if student.list_scores[1] == list_Math[0]:
            print(f"{student.name}get highest{list_Math[0]:.2f} in math")
    print('-------------------------------------------------------------')
    for student in students:
        if student.list_scores[2] == list_English[0]:
            print(f"{student.name}get highest{list_English[0]:.2f} in English")
    print('-------------------------------------------------------------')

def grades_divided(students):
    Chinese = []
    Math = []
    English = []
    list_all = [Chinese,Math,English]
    for student in students:
        student.grade()
        Chinese.append(student.list_grades[0])
        Math.append(student.list_grades[1])
        English.append(student.list_grades[2])
    return list_all

def show_grade(students):
    List_Chinese = [0,0,0,0,0]
    List_Math = [0,0,0,0,0]
    List_English = [0,0,0,0,0]
    list_all = grades_divided(students)
    Chinese = list_all[0]
    Math = list_all[1]
    English = list_all[2]
    def count(list_1,list_2):
        for i in list_2:
            if i == 'A': list_1[0]+=1
            elif i == 'B': list_1[1]+=1
            elif i == 'C': list_1[2]+=1
            elif i == 'D': list_1[3]+=1
            elif i == 'F': list_1[4]+=1
        return list_1
    List_Chinese = count(List_Chinese,Chinese)
    List_Math = count(List_Math,Math)
    List_English = count(List_English,English)
    print("Number of people for Chinese Grade: ")
    print('A: ' + str(List_Chinese[0]) + ' B: ' + str(List_Chinese[1]) + ' C: ' + str(List_Chinese[2]) + ' D: ' + str(List_Chinese[3]) +
          ' F: ' + str(List_Chinese[4]))
    print("------------------------------------------")
    print("Number of people for Math Grade: ")
    print('A: ' + str(List_Math[0]) + ' B: ' + str(List_Math[1]) + ' C: ' + str(List_Math[2]) + ' D: ' + str(List_Math[3]) +
          ' F: ' + str(List_Chinese[4]))
    print("------------------------------------------")
    print("Number of people for English Grade: ")
    print('A: ' + str(List_English[0]) + ' B: ' + str(List_English[1]) + ' C: ' + str(List_English[2]) + ' D: ' + str(List_English[3]) +
          ' F: ' + str(List_English[4]))
    print("------------------------------------------")

def show_median(students):
    Scores_Chinese = []
    Scores_Math = []
    Scores_English = []
    for student in students:
        if student.list_scores[0] == -1 or student.list_scores[1] == -1 or student.list_scores[2] == -1:
            continue
        Scores_Chinese.append(student.list_scores[0])
        Scores_Math.append(student.list_scores[1])
        Scores_English.append(student.list_scores[2])
        Scores_Chinese.sort()
        Scores_Chinese.sort()
        Scores_Chinese.sort()

    median = [Scores_Chinese[int((len(Scores_Chinese)-1)/2)], Scores_Math[int((len(Scores_Math)-1)/2)], Scores_English[int((len(Scores_English)-1)/2)]]
    return median
def show_scores_district(students):
    Chinese_90Above = 0
    Chinese_80Above = 0
    Chinese_80Below = 0

    Math_90Above = 0
    Math_80Above = 0
    Math_80Below = 0

    English_90Above = 0
    English_80Above = 0
    English_80Below = 0

    for student in students:
        if student.list_scores[0] > 90:
            Chinese_90Above += 1
        elif student.list_scores[0] > 80:
            Chinese_80Above += 1
        elif student.list_scores[0] < 80:
            Chinese_80Below += 1

        if student.list_scores[1] > 90:
            Math_90Above += 1
        elif student.list_scores[1] > 80:
            Math_80Above += 1
        elif student.list_scores[1] < 80:
            Math_80Below += 1

        if student.list_scores[2] > 90:
            English_90Above += 1
        elif student.list_scores[2] > 80:
            English_80Above += 1
        elif student.list_scores[2] < 80:
            English_80Below += 1

    chinese_district = [Chinese_90Above,Chinese_80Above,Chinese_80Below]
    math_district = [Math_90Above,Math_80Above,Math_80Below]
    english_district = [English_90Above,English_80Above,English_80Below]

    district = [chinese_district,math_district,english_district]

    return district

