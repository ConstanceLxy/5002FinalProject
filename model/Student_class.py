import math


# Just try to commit
class Student(object):

    def __init__(self, name='', id=0, subject_1=0.0, subject_2=0.0, subject_3=0.0):
        self.name = name
        self.id = id
        self.list_scores = [round(subject_1, 1), round(subject_2, 1), round(subject_3, 1)]
        self.list_grades = []
        self.variance = self.Variance()

    # sum
    def sum(self):
        sum = 0
        for score in self.list_scores:
            sum += score
        return sum

    # class to class(A,B,C,D)
    def grade(self):
        for score in self.list_scores:
            if score >= 90:
                self.list_grades.append('A')
            elif score >= 80:
                self.list_grades.append('B')
            elif score >= 70:
                self.list_grades.append('C')
            elif score >= 60:
                self.list_grades.append('D')
            else:
                self.list_grades.append('F')

    # variance
    def Variance(self):
        sum_squre = 0
        sum = 0
        for score in self.list_scores:
            sum += score
        average = sum / 3
        for score in self.list_scores:
            sum_squre += math.pow(score - average, 2)
        return round(sum_squre / 3, 2)
