"""
    File name: opm_login.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/8/2020
    Date last modified: 3/26/2020
    Program version: 1.2.0
    Python Version: 3.8.1
"""

import sqlite3
from sqlite3 import Error
import sys
import getpass
import time
import os
from datetime import datetime

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
            now = datetime.now()
            datenow = now.strftime("%m/%d/%Y")
            timenow = now.strftime("%H:%M:%S")
            file = open("log/log.txt","a") 
            file.write("[{0}][{1}] Successful Login\n".format(datenow, timenow))
            file.close()
            print("open menu...")
            time.sleep(1)
            clear()
        else:
            print("login failed")
            now = datetime.now()
            datenow = now.strftime("%m/%d/%Y")
            timenow = now.strftime("%H:%M:%S")
            file = open("log/log.txt","a") 
            file.write("[{0}][{1}] Failed Login\n".format(datenow, timenow))
            file.close()
            os._exit(1)
    except Error as e:
        print(e)
    finally:
        db.close()
