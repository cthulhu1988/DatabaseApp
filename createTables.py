#!/usr/bin/python3

import sqlite3

def createTables():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    ## Create Supplier table:
    c.execute("""
        CREATE TABLE IF NOT EXISTS SUPPLIER(
            Sno text PRIMARY KEY,
            Sname text NON NULL,
            Status Integer NON NULL,
            City text NON NULL

        )""")

    ## Create PART table:
    c.execute("""
        CREATE TABLE IF NOT EXISTS PART(
            Pno text PRIMARY KEY,
            Pname text,
            Color text,
            Weight Integer,
            City text
        )""")

    ## Create Shipment table:
    c.execute("""
        CREATE TABLE IF NOT EXISTS SHIPMENT(
            Sno text,
            Pno text,
            Qty Integer,
            Price Real,
            PRIMARY KEY(Sno, Pno),
            FOREIGN KEY(Sno) REFERENCES SUPPLIER(Sno),
            FOREIGN KEY(Pno) REFERENCES SUPPLIER(Pno)
        )""")


    conn.commit()
    conn.close()
