#!/usr/bin/python3

import sqlite3
database = "data.db"
def InsertTableData():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    try:
        c.execute("""INSERT INTO SUPPLIER VALUES("s1", "Smith", 20, "London")""")
        c.execute("""INSERT INTO SUPPLIER VALUES("s2", "Jones", 10, "Paris")""")
        c.execute("""INSERT INTO SUPPLIER VALUES("s3", "Blake", 30, "Paris")""")
        c.execute("""INSERT INTO SUPPLIER VALUES("s4", "Clark", 20, "London")""")
        c.execute("""INSERT INTO SUPPLIER VALUES("s5", "Adams", 30, NULL)""")

        c.execute("""INSERT INTO PART VALUES("p1", "Nut", "Red", 12, "London")""")
        c.execute("""INSERT INTO PART VALUES("p2", "Bolt", "Green", 17, "Paris")""")
        c.execute("""INSERT INTO PART VALUES("p3", "Screw", NULL, 17, "Rome")""")
        c.execute("""INSERT INTO PART VALUES("p4", "Screw", "Red", 14, "London")""")
        c.execute("""INSERT INTO PART VALUES("p5", "Cam", "Blue", 12, "Paris")""")
        c.execute("""INSERT INTO PART VALUES("p6", "Cog", "Red", 19, "London")""")

        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p1", 300, .005)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p2", 200, .009)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p3", 400, .004)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p4", 200, .009)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p5", 100, .01)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s1", "p6", 100, .01)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s2", "p1", 300, .006)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s2", "p2", 400, .004)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s3", "p2", 200, .009)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s3", "p3", 200, NULL)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s4", "p2", 200, .008)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s4", "p3", NULL, NULL)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s4", "p4", 300, .006)""")
        c.execute("""INSERT INTO SHIPMENT VALUES("s4", "p5", 400, .003)""")
    except:
        return

    conn.commit()
    conn.close()
