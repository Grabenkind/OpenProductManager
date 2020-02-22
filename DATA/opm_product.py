"""
    File name: opm_product.py
    Author: Steven Müller (Grabenkind)
    Date created: 2/7/2020
    Date last modified: 2/22/2020
    Program version: 1.0.0
    Python Version: 3.8.1
"""

import sqlite3
from sqlite3 import Error
import os

clear = lambda: os.system('cls')

def product_menu():
    clear()
    print("-------- [ PRODUCT MANAGEMENT ] --------")
    print("| add - ADD a product                  |")
    print("| del - DELETE a product               |")
    print("| edit - EDIT a product                |")
    print("| menu - open main menu                |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

def product_add():
    clear()
    name = None
    itemnumber = None
    price = None
    quantity = None

    name = str(input("Product Name: "))
    itemnumber = int(input("Item No.: "))
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    try:
        db = sqlite3.connect('products.db')
        command = """CREATE TABLE IF NOT EXISTS products(
                    ItemNo INTEGER PRIMARY KEY,
                    Name TEXT,
                    Price REAL,
                    Quantity INTEGER
                );"""
        c = db.cursor()
        c.execute(command)
        command = """INSERT INTO products (ItemNo,
                    Name, Price, Quantity)
                    VALUES (%d, "%s", %d, %d);""" % (itemnumber, name, price, quantity)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_del():
    try:
        clear()
        itemnumber = 0
        print("Which product should be deleted?")
        itemnumber = int(input("Item No.: "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """DELETE FROM products WHERE ItemNo = %d;""" % itemnumber
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_edit_menu():
    clear()
    print("----------- [ EDIT PRODUCT ] -----------")
    print("| n - EDIT name of a product           |")
    print("| i - EDIT item no. of a product       |")
    print("| p - EDIT price of a product          |")
    print("| menu - open main menu                |")
    print("| exit - exit program                  |")
    print("----------------------------------------")

def product_edit_name():
    try:
        clear()
        itemnumber = None
        newname = None
        print("Which product should be edited?")
        itemnumber = int(input("Item No.: "))
        clear()
        print("Enter new name")
        newname = str(input("Name: "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """UPDATE products SET Name = "%s"
        WHERE ItemNo = %d;""" % (newname, itemnumber)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_edit_itemno():
    try:
        clear()
        itemnumber = None
        newitemnumber = None
        print("Which product should be edited?")
        itemnumber = int(input("Item No.: "))
        clear()
        print("Enter new item no")
        newitemnumber = int(input("Item No.: "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """UPDATE products SET ItemNo = %d
        WHERE ItemNo = %d;""" % (newitemnumber, itemnumber)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_edit_price():
    try:
        clear()
        itemnumber = None
        newprice = None
        print("Which product should be edited?")
        itemnumber = int(input("Item No.: "))
        clear()
        print("Enter new price")
        newprice = float(input("Price: "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """UPDATE products SET Price = %d
        WHERE ItemNo = %d;""" % (newprice, itemnumber)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_increase():
    try:
        clear()
        itemnumber = None
        new = None
        print("Which product should be topped up?")
        itemnumber = int(input("Item No.: "))
        clear()
        print("Increase quantity by")
        new = int(input("> "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """UPDATE products SET Quantity = Quantity + %d
        WHERE ItemNo = %d;""" % (new, itemnumber)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()

def product_decrease():
    try:
        clear()
        itemnumber = None
        new = None
        print("Which product should be reduced?")
        itemnumber = int(input("Item No.: "))
        clear()
        print("decrease quantity by")
        new = int(input("> "))

        db = sqlite3.connect('products.db')
        c = db.cursor()
        command = """UPDATE products SET Quantity = Quantity - %d
        WHERE ItemNo = %d;""" % (new, itemnumber)
        c.execute(command)
        db.commit()
    except Error as e:
        print(e)
    finally:
        db.close()