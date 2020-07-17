import re
import random


def menu():
    input("Hello!! \nplease enter to continue")

    global page

    def page():

        a = input("1.login \n2.Sign up \n3.password recovery \n4.quit \nplease use the number \n== ")

        if a == "1":
            login()

        elif a == "2":
            signup()

        elif a == "3":
            r_passw()

        elif a == "4":
            exit()

        else:
            print("\ntry again!!\n")
            page()

    page()


def login():
    def isAuthorized():
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        with open("user_pass.txt", "r") as f:
            for line in f:
                loginInfo = line.strip().split(",")
                if username == loginInfo[0] and password == loginInfo[1]:
                    return True
            return False

    if isAuthorized():
        input("Authorized \t Press any key to continue: ")
        exit()
    else:
        print("please try again")
        login()


def signup():
    def look():
        global username, password

        username = input(str("please enter your username: ")).strip()
        password = input(str("please enter your password: ")).strip()

        with open("user_pass.txt", "r") as f:
            for line in f:
                login_info = line.strip().split(",")
                if username == login_info[0]:
                    return True
            return False

    if look():
        global in_menu

        def passw():
            print("\nThe username already exist\n")

            with open("user_pass.txt", "r") as f:
                for line in f:
                    login_info = line.strip().split(",")
                    if password == login_info[1]:
                        return True
                return False

        if passw():
            print("your password must be unique")
            menu()

        else:
            pass



    else:

        def pas():
            with open("user_pass.txt", "r") as f:
                for line in f:
                    login_info = line.strip().split(",")
                    if password == login_info[1]:
                        return True
                return False

        if pas():
            print("the password already exist")
            signup()

        else:
            q = True

            while q:
                if len(password) < 6:
                    print("your password must be more than 6 characters")
                    signup()
                elif not re.search("[a-z]", password):
                    print("your password must have some small letter characters")
                    signup()
                elif not re.search("[0-9]", password):
                    print("your password must have 1 or more number")
                    signup()
                elif not re.search("[A-Z]", password):
                    print("your password must have some big letter character")
                    signup()
                elif not re.search("[$#@!£%^&*€]", password):
                    print("your password must have special character")
                    signup()
                elif re.search("\s", password):
                    print("your password shouldn't have any spaces")
                else:
                    print("Valid Password")
                    q = False

                    f = open("user_pass.txt", "a")
                    f.write("\n")
                    f.write(username)
                    f.write(",")
                    f.write(password)
                    f.close()
                    print("your username is " + username, " and your password is " + password)
                    print("\n")
                    print("you are successfully logged in\n")
                    recovery()
                    page()
    look()


def recovery():
    f = open(username + "_recovery.txt", "a")
    f.write("\n")
    f.write(username)
    f.close()
    for i in range(0, 5):
        print("please enter 5 recovery question and password")
        print("\n")
        a = input(str("recovery question "))
        b = input("password: ")
        f = open(username + "_recovery.txt", "a")
        f.write(",")
        f.write(a)
        f.write(",")
        f.write(b)
        f.close()
        print("you password has been successfully created")


def r_passw():
    def checker():
        global us
        us = input("please enter your username to view your password ")

        with open(us + "_recovery.txt", "r") as f:
            for line in f:
                login_info = line.strip().split(",")
                if us == login_info[0]:
                    return True
            return False

    if checker():
        po = 0
        fp = open(us + '_recovery.txt')
        words = [word.strip() for line in fp.readlines() for word in line.split(',') if word.strip()]

        ww = words[1], words[3], words[5], words[7], words[9]
        we = words[2], words[4], words[6], words[8], words[10]

        for i in range(1, 3):

            q = random.choice(ww)
            a = input(q + " ")

            if q == words[1]:
                if a == words[2]:
                    print("you got it")
                    po = po + 1
                else:
                    print("you got it wrong")

            elif q == words[3]:
                if a == words[4]:
                    print("you got it")
                    po = po + 1
                else:
                    print("you got it wrong")
                    menu()

            elif q == words[5]:
                if a == words[6]:
                    print("you got it")
                    po = po + 1
                else:
                    print("no you got it wrong")
                    menu()

            elif q == words[7]:
                if a == words[8]:
                    print("you got it")
                    po = po + 1

                else:
                    print("you got it wrong")
                    menu()

            elif q == words[9]:
                if a == words[10]:
                    print("you got it right")
                    po = po + 1

                else:
                    print("you got it wrong")
                    menu()

            else:
                print("you are not authorised to see the password")
                menu()

        if po == 2:
            with open("user_pass.txt", "r") as s:
                for line in s:
                    login_in = line.strip().split(",")
                    if us == login_in[0]:
                        print("you can see the password now")
                        print(login_in[1])

        else:
            print("authentication failed")
            menu()



    else:
        print("authentication failed, sorry we can't show you the password")
        menu()


menu()
