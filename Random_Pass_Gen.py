#!/usr/bin/python
import random
import webbrowser
import time
__Author__ = "Andrew Lee Johnson"
__Copyright__ = "Copyright (C) 2017 Andrew Lee Johnson "
__About__ = "New Password Generater that save it to a text file"
__Notes__ = "Make it be able to encrypt or decrypt a file if he or she wants"
password = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+[]\;',./?><1234567890"
f = open('output.txt', 'w')
number = 10
random_value = random.sample(password, number)
random_value = random.sample(random_value, number)
random_value = "".join(random_value)


def password_gen():
    print(__Author__)
    print('''
       \|----------------------------------------------------------|/
       \|     Enter Your Choice:                                   |/
       \|       1) Print Password                                  |/
       \|       2) Save it to output.txt                           |/
       \|       3) Exit                                            |/
       \|----------------------------------------------------------|/
    ''')
    user = input("Enter Your Choice: ")

    if user == '1':
        time.sleep(2)
        print_password()
    elif user == '2':
        time.sleep(2)
        save_info()
    elif user == "Exit" or "exit" or '3':
        time.sleep(2)
        exit()
    else:
        time.sleep(2)
        print("Enter It Again Please")
        password_gen()


def print_password():
    random_value = random.sample(password, number)
    random_value = random.sample(random_value, number)
    random_value = "".join(random_value)
    print("**************", random_value, "**************")
    time.sleep(2)
    password_gen()


def save_info():
    random_value = random.sample(password, number)
    random_value = random.sample(random_value, number)
    random_value = "".join(random_value)
    random_value2 = random.sample(random_value, number)
    random_value2 = "".join(random_value2)
    a = random_value
    b = random_value2
    f.write('Password: ' + str(a))
    f.write('\nPassWord 2: ' + str(b))
    f.close()
    open_text_file()


def open_text_file():
    print("Do you want to open your file?")
    print('''
       \|---------------------------------|/
       \|     Enter Your Choice           |/
       \|       1) Yes                    |/
       \|       2) No                     |/
       \|---------------------------------|/  ''')
    user_input = input("Enter Your Choice Here: ")
    if user_input == '1':
        webbrowser.open("output.txt")
        password_gen()
    elif user_input == '2':
        password_gen()



password_gen()
