"""
    File name: opm_user.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/6/2020
    Date last modified: 2/22/2020
    Program version: 1.2.0
    Python Version: 3.8.1
"""

import sqlite3
from sqlite3 import Error
import os
import getpass
import time

clear = lambda: os.system('cls')

def root():
    db = sqlite3.connect('users.db')
    c = db.cursor()
    command = '''SELECT * from users WHERE Username="root" AND Password="!root"'''
    c.execute(command)
    if c.fetchone() is None:
        try:
            db = sqlite3.connect('users.db')
            command = """CREATE TABLE IF NOT EXISTS users(
                        Username TEXT PRIMARY KEY,
                        Password TEXT
                    );"""
            c = db.cursor()
            c.execute(command)
            command = """INSERT INTO users (Username, Password)
                        VALUES ("root", "!root");"""
            c.execute(command)
            db.commit()
        except Error as e:
            print(e)
        finally:
            db.close()

def user_menu():
    clear()
    print("---------- [ USER MANAGEMENT ] ---------")
    print("| add - ADD a user                     |")
    print("| del - DELETE a user                  |")
    print("| edit - EDIT a user                   |")
    print("| menu - open main menu                |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

def user_add():
    clear()
    username = "none"
    password = "none"

    username = str(input("Username: "))
    password = getpass.getpass()

    try:
        db = sqlite3.connect('users.db')
        command = """CREATE TABLE IF NOT EXISTS users(
                    Username TEXT PRIMARY KEY,
                    Password TEXT
                );"""
        c = db.cursor()
        c.execute(command)
        command = """INSERT INTO users (Username, Password)
                    VALUES ("%s", "%s");""" % (username, password)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def user_del():
    try:
        clear()
        username = "none"
        print("Which user should be deleted?")
        username = int(input("Username: "))

        db = sqlite3.connect('users.db')
        c = db.cursor()
        command = """DELETE FROM users WHERE Username = %s;""" % username
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def user_edit_menu():
    clear()
    print("------------ [ EDIT USER ] -------------")
    print("| n - EDIT name of a user              |")
    print("| p - EDIT password of a user          |")
    print("| menu - open main menu                |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

def user_edit_name():
    try:
        clear()
        username = None
        newusername = None
        print("Which user should be edited?")
        username = str(input("Username: "))
        clear()
        print("Enter new username")
        newusername = str(input("Username: "))

        db = sqlite3.connect('users.db')
        c = db.cursor()
        command = """UPDATE users SET Username = "%s"
        WHERE Username = "%s";""" % (newusername, username)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def user_edit_password():
    clear()
    username = input("Username: ")
    password = getpass.getpass()
    clear()
    try:
        db = sqlite3.connect('users.db')
        c = db.cursor()
        command = '''SELECT * from users WHERE Username="%s" AND Password="%s"''' % (username, password)
        c.execute(command)
        if c.fetchone() is not None:
            clear()
            print("Enter new password")
            newpassword = getpass.getpass()
            db = sqlite3.connect('users.db')
            c = db.cursor()
            command = """UPDATE users SET Password = "%s"
            WHERE Username = "%s";""" % (newpassword, username)
            c.execute(command)
            db.commit()
        else:
            print("wrong username or password")
            time.sleep(1)
            clear()
    except Error as e:
        print(e)
    finally:
        db.close()
