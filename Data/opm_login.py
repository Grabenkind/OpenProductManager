"""
    File name: opm_login.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/8/2020
    Date last modified: 2/22/2020
    Program version: 1.1.0
    Python Version: 3.8.1
"""

import sqlite3
from sqlite3 import Error
import sys
import getpass
import time
import os

clear = lambda: os.system('cls')

def login_request():
    username = input("Username: ")
    password = getpass.getpass()
    clear()
    try:
        db = sqlite3.connect('users.db')
        c = db.cursor()
        command = '''SELECT * from users WHERE Username="%s" AND Password="%s"''' % (username, password)
        c.execute(command)
        if c.fetchone() is not None:
            print("login successful")
            print("open menu...")
            time.sleep(1)
            clear()
        else:
            print("login failed")
            os._exit(1)
    except Error as e:
        print(e)
    finally:
        db.close()