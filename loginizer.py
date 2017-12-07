user_pass = input("Please choose a password")
import time
time.sleep(1)
login = input("Would you like to login? : (Yes / No)")

def go_login():
    login_1 = input("Please Enter your password")
    if (login_1 == user_pass):
        print("Acess Granted")

def wrongpass():
    print("Wrong Password")
    time.sleep(2)
    
def trials():
    trial = 1
    while trial <= 3:
        login_1 = input("Please Enter your password")
        trial += 1
        if (login_1 == user_pass):
            print("Acess Granted")
            break
        wrongpass()
        print("You are not Authorized")

def dont_login():
    print("Thank you have a good day")
 
if (login == "Yes") or (login == "YES") or (login == "yes"):
    trials()
elif (login == "No") or (login == "NO") or (login == "no"):
    dont_login()
    time.sleep(5)
else:
    print("Thank you, have a good time, please keep your password safe")
    time.sleep(5)
    
        

time.sleep(5)

