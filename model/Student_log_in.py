import time
enterName = 0
enterPassword = 0
name1 = 'Teacher'
password1 = '5002111'
Time = 0
Try = 4
for i in range(5):
    # use for loop to enable people to enter username and password many times.
    if Try !=0:
        enterName = input("Username: ")
        if enterName == "Teacher":
            enterPassword = input("Password: ")
            if enterPassword == "5002111":
                for i in range(10):
                    time.sleep(0.05)
                    # We use time.sleep() to defer execution, in this way, we can imitate an old computer to login.
                    Time+=10
                    print("login...(",Time,"/100)")
                print("log in successfully")
                break
            else:
                print('Incorrect password. You can try', Try-1, 'more times.')
                # People can only try 4 times to enter password.
                Try-=1
        else:
            print('Incorrect username. You can try',Try-1, 'more times.')
            # People can only try 4 times to enter username.
            Try-=1
    else:
        print('No more chance.')
