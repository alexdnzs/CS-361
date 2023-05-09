#from LogReg import *
import os

def import_birthyear():
    username1 = input("What is the your username? ")
    password1 = input("What is your password? ")
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            
            birth_year = verify[3]
            #birth_year = bytes(birth_year, 'utf-8')
            #print(birth_year) - print statement used for debugging

            #Returns the year as bytes
            return birth_year
        else:
            print("No Matching User Found - Cannot Import Birthyear!")
