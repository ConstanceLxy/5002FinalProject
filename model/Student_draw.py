import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Student_class import Student
from Student_load import load
from model.Student_Search import *


def pie_district_chinese(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[0][0], show_scores_district(students)[0][1],
              show_scores_district(students)[0][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('Chinese Scores District')
    plt.show()


def pie_district_math(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[1][0], show_scores_district(students)[1][1],
              show_scores_district(students)[1][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('Math Scores District')
    plt.show()


def pie_district_english(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[2][0], show_scores_district(students)[2][1],
              show_scores_district(students)[2][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('English Scores District')
    plt.show()
