#import modules
 
from tkinter import *
import os
import re

# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("750x350")
 
    global legal_name
    global username
    global password
    global birthyear
    global legal_name_entry
    global username_entry
    global password_entry
    global birthyear_entry
    legal_name = StringVar()
    username = StringVar()
    password = StringVar()
    birthyear = StringVar()
 
    Label(register_screen, text = "Please enter details below\n This step is not required if you already have an account!", bg = "green").pack()
    Label(register_screen, text = "").pack()

    legal_name_lable = Label(register_screen, text="What's your name?")
    legal_name_lable.pack()
    legal_name_entry = Entry(register_screen, textvariable=legal_name)
    legal_name_entry.pack()

    birthyear_lable = Label(register_screen, text="What is your birthyear?")
    birthyear_lable.pack()
    birthyear_entry = Entry(register_screen, textvariable=birthyear)
    birthyear_entry.pack()

    username_lable = Label(register_screen, text="\nUsername * (must be valid\ni.e. JohnDoe1@yahoo.com) ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="\nPassword * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width = 10, height = 1, bg="white", command = lambda: [email_validation()]).pack()

    Button(register_screen, text="Back", width = 5, command = lambda: [main_screen.destroy(), main_account_screen()]).place(x = 50, y = 50)
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("750x350")
    Label(login_screen, text="Please enter valid email and password \n This will give you full access to the application!").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height = 1, command = login_verify).pack()
    Button(login_screen, text="Back", width = 5, command = lambda: [main_screen.destroy(), main_account_screen()]).place(x = 50, y = 50)


def app_screen():
    global app_screen
    global choice_ver

    choice_ver = IntVar()

    global choice_entry

    app_screen = Toplevel(login_screen)
    app_screen.title("Application homepage")
    app_screen.geometry("750x350")
    Label(app_screen, text="Welcome!").pack()
    Label(app_screen, text="").pack()
 
    Label(app_screen, text="Press Button or Enter Corresponding Number to Access Feature").pack()
    
    Label(app_screen, text="").pack()
    Button(app_screen, text="1) Status Updates - Share status with friends and family!", width=44, height = 1, command = share_status).pack()
    Label(app_screen, text="").pack()

    #COMMAND NEEDS TO BE CHANGED
    Button(app_screen, text="2) Status Pictures - Share pics with friends and family!", width=44, height = 1, command = share_status).pack()
    
    
    Label(app_screen, text="").pack()

    Label(app_screen, text="Navigate using numbers").pack()

    choice_entry = Entry(app_screen, textvariable=choice_ver, width = 3)
    choice_entry.pack()
    Label(app_screen, text="").pack()

    Button(app_screen, text="Go!", width = 3, height = 1, command = choice_verify).pack()
    
    Button(app_screen, text="Sign Out\nand Exit", width = 9, height = 3, command = lambda: [login_screen.destroy(), login_screen, main_screen.destroy()]).place(x = 50, y = 50)
 
# Implementing event on register button

def share_status():
    global share_screen
    share_screen = Toplevel(app_screen)
    share_screen.title("Share Status")
    share_screen.geometry("750x350")
    Label(share_screen, text="Share your thoughts! - FEATURE TO BE IMPLEMENTED SOON").pack()
    Label(share_screen, text="").pack()
 
    Button(share_screen, text="Back", width = 5, command = lambda: [share_screen.destroy(), app_screen]).place(x = 50, y = 50)

 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    legal_name_info = legal_name.get()
    birthyear_info = birthyear.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(legal_name_info + "\n")
    file.write(birthyear_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    legal_name_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success - Press Back to go to Homepage", fg="green", font=("calibri", 11)).pack()
    
 
def choice_verify():
    choice1 = choice_entry.get()
    
    if choice1 == "1":
        share_status()

    #elif choice == "2":
       # share_pics

    else:
        Label(app_screen, text="Invalid Entry", fg="red", font=("calibri", 11)).pack()
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

"""
def import_legal_name():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            
            sent_name = verify[2]
            sent_name = bytes(sent_name, 'utf-8')
            return sent_name
        else:
            password_not_recognised()
 
    else:
        user_not_found()
"""

 
# Designing popup for login success
 
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x250")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command= lambda: [main_screen.withdraw(), login_screen.withdraw(), delete_login_success(), app_screen()]).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("300x250")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for register invalid email
def invalid_registration_email():
    global email_invalid_screen
    email_invalid_screen = Toplevel(register_screen)
    email_invalid_screen.title("Try again")
    email_invalid_screen.geometry("300x250")
    Label(email_invalid_screen, text="Invalid Email Format").pack()
    Button(email_invalid_screen, text="OK", command = lambda: [delete_email_invalid_screen, register_screen.destroy(), register()]).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("300x250")
    Label(user_not_found_screen, text="Credentials do not match any in our system").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def email_validation():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    # pass the regular expression
    # and the string into the fullmatch() method

    if(re.fullmatch(regex, username_entry.get())):
        register_user()
    else:
        invalid_registration_email()

 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_email_invalid_screen():
    email_invalid_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("750x350")
    main_screen.title("Account Login")
    Label(text="Friends and Family <3", bg="green", width="300", height="2", font=("Times New Roman", 15)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 