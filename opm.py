"""
    File name: OPM.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/6/2020
    Date last modified: 2/23/2020
    Program version: 1.1.0
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
    print("| + - Increase product quantity        |")
    print("| - - Decrease product quantity        |")
    print("| p - product management               |")
    print("| u - user management                  |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

clear()
# if theres no user, create "root" user
opm_user.root()
# open login
opm_login.login_request()

while True:
    try:
        # open Main Menu
        main_menu()
        # enter a command from the Main Menu List
        inpt = str(input("> "))

        # execute command +
        if inpt == "+":
            # increase the quantity of a product
            opm_product.product_increase()
        
        # execute command -
        elif inpt == "-":
            # decrease the quantity of a product
            opm.product.product_decrease()
        
        # execute command p
        elif inpt == "p":
            # open Product Menu
            opm_product.product_menu()
            # enter a command from the Product Menu List
            inpt = str(input("> "))
            # execute command add
            if inpt == "add":
                # add a new product
                opm_product.product_add()
            # execute command del
            elif inpt == "del":
                # delete a product
                opm_product.product_del()
            # execute command edit
            elif inpt == "edit":
                # open Product Edit Menu
                opm_product.product_edit_menu()
                # enter a command from the Product Edit Menu List
                inpt = str(input("> "))
                # execute command n
                if inpt == "n":
                    # edit name of a product
                    opm_product.product_edit_name()
                # execute command b
                elif inpt == "b":
                    # edit brand of a product
                    opm_product.product_edit_brand()
                # execute command i
                elif inpt == "i":
                    # edit itemnumber of a product
                    opm_product.product_edit_itemno()
                # execute command p
                elif inpt == "p":
                    # edit price of a product
                    opm_product.product_edit_price()
                # execute command back
                elif inpt == "menu":
                    # open Product Management
                    opm_product.product_menu()
                # execute command exit
                elif inpt == "exit":
                    clear()
                    # exit
                    os._exit(1)
            # execute command back
            elif inpt == "menu":
                # open Main Menu
                main_menu()
            # execute command exit
            elif inpt == "exit":
                clear()
                # exit
                os._exit(1)

        # execute command u
        elif inpt == "u":
            # open User Menu
            opm_user.user_menu()
            # enter a command from the User Menu List
            inpt = str(input("> "))
            # execute command add
            if inpt == "add":
                # add a new user
                opm_user.user_add()
            # execute command del
            elif inpt == "del":
                # delete a user
                opm_user.user_add()
            # execute command edit
            elif inpt == "edit":
                # open User Edit Menu
                opm_user.user_edit_menu()
                # enter a command from the User Edit Menu List
                inpt = str(input("> "))
                # execute command n
                if inpt == "n":
                    # edit username
                    opm_user.user_edit_name()
                # execute command p
                elif inpt == "p":
                    # edit password
                    opm_user.user_edit_password()
                        # execute command back
                elif inpt == "menu":
                    # open User Menu
                    opm_user.user_menu()
                # execute command exit
                elif inpt == "exit":
                    clear()
                    # exit
                    os._exit(1)
            # execute command back
            elif inpt == "menu":
                # open Main Menu
                main_menu()
            # execute command exit
            elif inpt == "exit":
                clear()
                # exit
                os._exit(1)

        # execute command x
        elif inpt == "exit":
            clear()
            # exit
            os._exit(1)

    except:
        print("Error: ", sys.exc_info([0]))