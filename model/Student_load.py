import pandas as pd
from model.Student_class import Student


def load():
    data = pd.read_excel(r"D:\CodeHouse\PycharmProjects\5002FinalProject\model\Student_Scores.xlsx", skiprows=[0], converters={'Name': str, 'ID': int, 'Chinese': float, 'Math': float, 'English': float})
    # array to data array
    data_array = data.values
    # array to list
    students = []
    for data_list in data_array:
        student = Student(data_list[0],data_list[1],data_list[2],data_list[3],data_list[4])
    # list to student
        students.append(student)
    return students
