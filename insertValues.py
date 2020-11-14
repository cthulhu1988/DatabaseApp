#!/usr/bin/python3
import sys
import sqlite3
import traceback
database = "data.db"

def getVal(table):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("SELECT * FROM {}".format(table))
    fetch = (c.fetchall())
    return fetch
    conn.commit()
    conn.close()


def insertValues(table, *args):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    try:
        c.execute("INSERT INTO {} VALUES {}".format(table, args))
    except sqlite3.Error as er:
        err = ('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        conn.close()
        return "error",err

    c.execute("SELECT * FROM {}".format(table))
    fetch = (c.fetchall())
    conn.commit()
    conn.close()
    message = "Success"
    return message, fetch
