from Student_operate import *
from Student_save import *
from Student_log_in import *
import PySimpleGUI as sg
from model.Student_draw import *
from model.Student_load import load

students = load()
f = open('record.txt', 'w')
f.close()

layoutL = [
    [sg.T('SEARCH')],
    [sg.B('Show Scores  '), sg.B('Show Average'), sg.B('Show Rank')],
    [sg.B('Show Variance'), sg.B('Show Highest'), sg.B('Show All')],
]
layoutR = [
    [sg.T('OPERATE')],
    [sg.B('Change')],
    [sg.B('Sort')],
    [sg.B('Insert')]
]

layoutButtom = [
    [sg.T('Other')],
    [sg.B('Generate Report')],
    [sg.B('Save')],
    [sg.B('Exit')]
]

layout = [
    [sg.T(' Choose the File'), sg.In(), sg.FileBrowse()],
    [sg.T(' Select The Function you want')],
    [sg.Col(layoutL), sg.Col(layoutR)],
    [sg.Col(layoutButtom)],
    [sg.ML(size=(100, 20), reroute_stdout=True, write_only=False, reroute_cprint=True)],
    [sg.B('请输入一些内容'), sg.InputText()]
]

window = sg.Window('Student Score Management System', layout, resizable=True)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'Show Scores  ':
        NameId = sg.PopupGetText('please enter the student ID you want to find')
        show_scores(students, NameId)
        record('Show Scores')
        print('------------------------------------------------------------------------------------------------')
    if event == 'Show Average':
        show_average(students, len(students))
        record('Show Average')
        print('------------------------------------------------------------------------------------------------')
    if event == 'Show Rank':
        NameId = sg.PopupGetText('please enter the student ID you want to find')
        show_rank(students, NameId)
        record('Show Rank')
        print('------------------------------------------------------------------------------------------------')
    if event == 'Show Variance':
        show_variance(students)
        record('Show Variance')
        print('------------------------------------------------------------------------------------------------')
    if event == 'Show Highest':
        show_highest(students)
        record('Show Highest')
    if event == 'Show All':
        record('Show All')
        print_student_info(students)

    if event == 'Change':
        NameId = sg.PopupGetText('please enter the student ID you want to find')
        Subject = sg.PopupGetText('please enter the subject you want to change'
                                  '<Chinese:1>  <Math:2>  <English:3>')
        Score = sg.PopupGetText('please enter the new score')
        change_score(students, NameId, Subject, Score)
        xlsx_update(students)
        record('Change')
        print('update successfully！')
    if event == 'Sort':
        choose = sg.PopupGetText('you want to sort from up<1> or down<2>')
        chooseSubject = sg.PopupGetText('sort by:Chinese（1） Math（2） English（3） Total（4）：')
        sort(students, choose, chooseSubject)
        xlsx_update(students)
        record('Sort')
        print('sorted successfully')
    if event == 'Insert':
        newName = sg.PopupGetText('please enter the student name you want to add')
        newId = sg.PopupGetText('please enter the students id you want to add')
        newChinese = sg.PopupGetText('please enter the students Chinese score you want to add')
        newMath = sg.PopupGetText('please enter the students Math score you want to add')
        newEnglish = sg.PopupGetText('please enter the students English score you want to add')
        insert(students, newName, newId, newChinese, newMath, newEnglish)
        xlsx_update(students)
        record('Insert')
        print('add successfully')
    if event == 'Generate Report':
        report_generate(students)
        record('Generate Report')
    if event == 'Save':
        part_save(students)
        record('Save')
    if event == 'Exit':
        print('close')
        exit(0)

window.close()

