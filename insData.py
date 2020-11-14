#!/usr/bin/python3

import sqlite3
database = "data.db"
def InsertTableData():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("""INSERT INTO SUPPLIER VALUES("s1", "Smith", 20, "London")""")
    c.execute("""INSERT INTO SUPPLIER VALUES("s2", "Jones", 10, "Paris")""")
    c.execute("""INSERT INTO SUPPLIER VALUES("s3", "Blake", 30, "Paris")""")
    c.execute("""INSERT INTO SUPPLIER VALUES("s4", "Clark", 20, "London")""")
    c.execute("""INSERT INTO SUPPLIER VALUES("s5", "Adams", 30, NULL)""")

    conn.commit()
    conn.close()
