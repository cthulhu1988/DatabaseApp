#!/usr/bin/python3
import sqlite3
import createTables as ct
import insertValues as iv
import insData as ins
from tkinter import *
database = "data.db"
root = Tk()
root.title("Database Entry System")
root.geometry("1000x800")

### Pull from imported modules
ct.createTables()
ins.InsertTableData()

def increaseStatus():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("UPDATE SUPPLIER set Status = Status * 1.1")
    c.execute("SELECT * FROM SUPPLIER")
    print(c.fetchall())
    conn.commit()
    conn.close()

def shipments_entry():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    mesg, fetch = iv.insertValues('SHIPMENT', shipment_sno_entry.get(), shipment_pno_entry.get(),
            shipment_qty_entry.get(),shipment_price_entry.get() )

    shipment_message.config(text = mesg)

    shipment_sno_entry.delete(0,END)
    shipment_pno_entry.delete(0,END)
    shipment_qty_entry.delete(0,END)
    shipment_price_entry.delete(0,END)
#############################################
def suppliers_entry():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    mesg,fetch = iv.insertValues('SUPPLIER', supplier_sno_entry.get(), supplier_sname_entry.get(),
            supplier_status_entry.get(),supplier_city_entry.get() )

    supplier_message.config(text = mesg)
    supplier_info.delete('1.0', END)
    supplier_info.insert(INSERT,fetch)

    supplier_sno_entry.delete(0,END)
    supplier_sname_entry.delete(0,END)
    supplier_status_entry.delete(0,END)
    supplier_city_entry.delete(0,END)
##########################################################
def parts_entry():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    mesg, fetch = iv.insertValues('PART', part_pno_entry.get(), part_pname_entry.get(),
            part_color_entry.get(), part_weight_entry.get() ,
            part_city_entry.get() )

    part_message.config(text = mesg)

    part_pno_entry.delete(0,END)
    part_pname_entry.delete(0,END)
    part_color_entry.delete(0,END)
    part_weight_entry.delete(0,END)
    part_city_entry.delete(0,END)
#################################################

supplier_info = Text(root, height = 6, width = 60)
supplier_info.grid(row=23, column=0, columnspan = 5, padx=0)
supplier_label = Label(root, text="Table Info")
supplier_label.grid(row=22, column=0, padx=0)

def populateText(mesg):
    supplier_info.delete('1.0', END)
    supplier_info.insert(INSERT,mesg)

def fetchSupplier():
    fetch = iv.getVal("SUPPLIER")
    print(fetch)
    populateText(fetch)
sup_button = Button(root, text="show Suppliers", command=fetchSupplier)
sup_button.grid(row = 30, column = 0, padx = (100,0))

def fetchPart():
    fetch = iv.getVal("PART")
    print(fetch)
    populateText(fetch)
part_button = Button(root, text="show Parts", command=fetchPart)
part_button.grid(row = 30, column = 1, padx = 0)


def fetchShip():
    fetch = iv.getVal("SHIPMENT")
    print(fetch)
    populateText(fetch)
ship_button = Button(root, text="show Shipments", command=fetchShip)
ship_button.grid(row = 30, column = 2, padx = 0)

status_button = Button(root, text="status x 10%", command=increaseStatus)
status_button.grid(row = 1, column = 6, padx = 20)

def getPart():
    matches = iv.getPartShipped("SHIPMENT", part_no_entry.get())
    part_no_info.delete('1.0', END)
    part_no_info.insert(INSERT,matches)
    part_no_entry.delete(0,END)

################# prompt user for part no:
part_no_button = Button(root, text="Enter Part No:", command=getPart)
part_no_button.grid(row = 2, column = 6, padx = 20, pady = 20)

part_no_entry = Entry(root, width=10)
part_no_entry.grid(row = 2, column = 7, padx = 5, pady = 20)

part_no_info= Text(root, height = 6, width = 30)
part_no_info.grid(row=3, column=6, columnspan = 3, padx=10)


################ SUPPLIER ###########################################
sup_row=8
supplier_table = Label(root, text="Supplier Table").grid(row=(sup_row-1), column=0, padx=5)
# sno
supplier_sno_entry = Entry(root, width=10)
supplier_sno_entry.grid(row=sup_row, column=0, padx=5)
supplier_sno_label = Label(root, text="Sno").grid(row=(2+sup_row), column=0, padx=5)
# sname
supplier_sname_entry = Entry(root, width=10)
supplier_sname_entry.grid(row=sup_row, column=1, padx=5)
supplier_sname_label = Label(root, text="Sname").grid(row=(2+sup_row), column=1, padx=5)
# status
supplier_status_entry = Entry(root, width=10)
supplier_status_entry.grid(row=sup_row, column=2, padx=5)
supplier_status_label = Label(root, text="Status").grid(row=(2+sup_row), column=2, padx=5)
# city
supplier_city_entry = Entry(root, width=10)
supplier_city_entry.grid(row=sup_row, column=3, padx=5)
supplier_city_label = Label(root, text="City").grid(row=(2+sup_row), column=3, padx=5)

# supplier submit button
supplier_submit_button = Button(root, text="Supplier Entry Submit", command=suppliers_entry)
supplier_submit_button.grid(row=(sup_row+3), column=0, columnspan=4, padx=5, pady=5, ipadx=100)
# supplier message
supplier_message = Label(root, text="Normal")
supplier_message.grid(row=(4+sup_row), columnspan=6, padx=5)
#####################################################################################


################ SHIPMENT ###########################################
ship_row=14
shipment_table = Label(root, text="Shipment Table").grid(row=(ship_row-1), column=0, padx=5)
#sno
shipment_sno_entry = Entry(root, width=10)
shipment_sno_entry.grid(row=ship_row, column=0, padx=5)
shipment_sno_label = Label(root, text="Sno").grid(row=(2+ship_row), column=0, padx=5)
# pno
shipment_pno_entry = Entry(root, width=10)
shipment_pno_entry.grid(row=ship_row, column=1, padx=5)
shipment_pno_label = Label(root, text="Pno").grid(row=(2+ship_row), column=1, padx=5)
# QTY
shipment_qty_entry = Entry(root, width=10)
shipment_qty_entry.grid(row=ship_row, column=2, padx=5)
shipment_qty_label = Label(root, text="Qty").grid(row=(2+ship_row), column=2, padx=5)
# Price
shipment_price_entry = Entry(root, width=10)
shipment_price_entry.grid(row=ship_row, column=3, padx=5)
shipment_price_label = Label(root, text="Price").grid(row=(2+ship_row), column=3, padx=5)

# shipment submit button
shipment_submit_button = Button(root, text="Shipment Entry Submit", command=shipments_entry)
shipment_submit_button.grid(row=(ship_row+3), column=0, columnspan=4, padx=5, pady=5, ipadx=100)

shipment_message = Label(root, text="Normal")
shipment_message.grid(row=(4+ship_row), columnspan=6, padx=5)
#####################################################################################



################ PARTS ###########################################
parts_table = Label(root, text="Parts Table").grid(row=0, column=0, padx=5)

part_pno_entry = Entry(root, width=10)
part_pno_entry.grid(row=1, column=0, padx=5)
part_pno_label = Label(root, text="Pno").grid(row=2, column=0, padx=5)

part_pname_entry = Entry(root, width=10)
part_pname_entry.grid(row=1, column=1, padx=5)
part_pname_label = Label(root, text="Pname").grid(row=2, column=1, padx=5)

part_color_entry = Entry(root, width=10)
part_color_entry.grid(row=1, column=2, padx=5)
part_color_label = Label(root, text="Color").grid(row=2, column=2, padx=5)

part_weight_entry = Entry(root, width=10)
part_weight_entry.grid(row=1, column=3, padx=5)
part_weight_label = Label(root, text="Weight").grid(row=2, column=3, padx=5)

part_city_entry = Entry(root, width=10)
part_city_entry.grid(row=1, column=4, padx=5)
part_city_label = Label(root, text="City").grid(row=2, column=4, padx=5)

# parts submit button
parts_submit_button = Button(root, text="Parts Entry Submit", command=parts_entry)
parts_submit_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, ipadx=100)

part_message = Label(root, text="Normal")
part_message.grid(row=4, columnspan=6, padx=5)
###########################################################################################


root.mainloop()


    ## creates tables
    ## insert into
