from Student_load import load
from Student_Search import *
from Student_operate import part_operate
from Student_save import part_save
from Student_record import record
from Student_log_in import *
from model.Student_draw import report_generate

students = load()      #load
f = open('record.txt','w')
f.close()
while True:
    print("""
                Student score management System 
                Search.............1
                Operate............2
                Generate Report....3
                Save...............4
                Exit...............5
    """)
    choose = 0 
    try:
        choose = int(input('Please input num 1-4：'))
    except:
        print("")
    if choose == 1:
        record('system',choose)
        part_search(students)
    elif choose == 2:
        record('system',choose)
        part_operate(students)
    elif choose == 3:
        record('system', choose)
        report_generate(students)
    elif choose == 4:
        record('system',choose)
        part_save(students)
    elif choose == 5:
        record('system',choose)
        print('close')
        exit(0)
    else:
        print('Invalid input,please input again!')
