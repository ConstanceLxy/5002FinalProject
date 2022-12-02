import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Student_class import Student
from Student_load import load
from model.Student_Search import *
from docx import  Document
from docx.shared import Inches

def pie_district_chinese(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[0][0], show_scores_district(students)[0][1],
              show_scores_district(students)[0][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('Chinese Scores District')
    plt.savefig("Chinese_District.png")
    plt.show()


def pie_district_math(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[1][0], show_scores_district(students)[1][1],
              show_scores_district(students)[1][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('Math Scores District')
    plt.savefig("Math_District.png")
    plt.show()



def pie_district_english(students):
    labels = ['scores > 90', '80 < scores < 90', 'scores < 80']
    values = [show_scores_district(students)[2][0], show_scores_district(students)[2][1],
              show_scores_district(students)[2][2]]
    plt.pie(values, labels=labels, autopct="%.2f%%", labeldistance=1.12)
    plt.title('English Scores District')
    plt.savefig("English_District.png")
    plt.show()

def report_generate():
    document = Document()
    document.add_heading('Class Scores Report', 0)
    document.add_picture('Chinese_District.png', width=Inches(3))
    document.add_picture('English_District.png', width=Inches(3))
    document.add_picture('Math_District.png', width=Inches(3))
    document.add_page_break()
    document.save('demo.docx')





# def curve_distribute_chinese():

# def curve_distribute_math():
#
# def curve_distribute_english():
