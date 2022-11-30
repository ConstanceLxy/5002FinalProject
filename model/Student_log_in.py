import time
answerName = 0
answerPassword = 0
name1 = 'Teacher'
password1 = '5002111'
Time = 0
Try = 4
for i in range(5):
    if Try !=0:
        answerName = input("Username: ")
        if answerName == 'Teacher':
            answerPassword = input("Password: ")
            if answerPassword == '5002111':
                for i in range(10):
                    time.sleep(0.1)
                    Time+=10
                    print("login...(",Time,"/100)")
                print("log in successfully")
                break
            else:
                print('Incorrect password. You can try', Try, 'more times.')
                Try-=1
        else:
            print('Incorrect username. You can try',Try, 'more times.')
            Try-=1
    else:
        print('No more chance.')