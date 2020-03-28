"""
    File name: OPM.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/6/2020
    Date last modified: 3/26/2020
    Program version: 1.2.0
    Python Version: 3.8.1
"""

from Data import opm_login
from Data import opm_product
from Data import opm_user
import sys
import os

clear = lambda: os.system('cls')

def main_menu():
    clear()
    print("------------- [ MAIN MENU ] ------------")
    print("| \u001b[32m+\u001b[0m - \u001b[32mIncrease product quantity\u001b[0m        |")
    print("| \u001b[31m-\u001b[0m - \u001b[31mDecrease product quantity\u001b[0m        |")
    print("| p - product management               |")
    print("| u - user management                  |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

clear()

# START
# if theres no user, create "root" user
opm_user.root()

# create log Folder
if not os.path.exists('log'):
    os.mkdir('log')

# open login
opm_login.login_request()

while True:
    try:
        # open Main Menu
        main_menu()
        inpt = str(input("> "))

        # Increase product quantity
        if inpt == "+":
            opm_product.product_increase()

        # Decrease product quantity
        elif inpt == "-":
            opm.product.product_decrease()
        
        # open product menu
        elif inpt == "p":
            opm_product.product_menu()
            inpt = str(input("> "))
            if inpt == "add":
                opm_product.product_add()
            elif inpt == "del":
                opm_product.product_del()
            elif inpt == "edit":
                opm_product.product_edit_menu()
                inpt = str(input("> "))
                if inpt == "n":
                    opm_product.product_edit_name()
                elif inpt == "b":
                    opm_product.product_edit_brand()
                elif inpt == "i":
                    opm_product.product_edit_itemno()
                elif inpt == "p":
                    opm_product.product_edit_price()
                elif inpt == "menu":
                    opm_product.product_menu()
                elif inpt == "exit":
                    clear()
                    os._exit(1)
            elif inpt == "menu":
                main_menu()
            elif inpt == "exit":
                clear()
                os._exit(1)

        # open user menu
        elif inpt == "u":
            opm_user.user_menu()
            inpt = str(input("> "))
            if inpt == "add":
                opm_user.user_add()
            elif inpt == "del":
                opm_user.user_add()
            elif inpt == "edit":
                opm_user.user_edit_menu()
                inpt = str(input("> "))
                if inpt == "n":
                    opm_user.user_edit_name()
                elif inpt == "p":
                    opm_user.user_edit_password()
                elif inpt == "menu":
                    opm_user.user_menu()
                elif inpt == "exit":
                    clear()
                    os._exit(1)
            elif inpt == "menu":
                main_menu()
            elif inpt == "exit":
                clear()
                os._exit(1)

        # exit program
        elif inpt == "exit":
            clear()
            os._exit(1)

    except:
        print("Error: ", sys.exc_info([0]))
