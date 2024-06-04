import tkinter as tk
from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import openpyxl
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = tk.Tk()
root.title("Aplikasi Stok Obat")
root.geometry("1250x650+210+100")
root.config(bg=background)

file = pathlib.Path('data_obat.xlsx')
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Nama Obat"
    sheet['C1'] = "Golongan"
    sheet['D1'] = "Brand"
    sheet['E1'] = "Expired"
    sheet['F1'] = "Kemasan"
    sheet['G1'] = "Jumlah"
    sheet['H1'] = "Kode Obat"
    sheet['I1'] = "Distributor"
    sheet['J1'] = "Harga Beli"
    sheet['K1'] = "Harga Grosir"
    sheet['L1'] = "Harga Jual"

    file.save('data_obat.xlsx')

Label(root, text="Registrasi Obat Apotik", width=10, height=2, bg="#FFF0F5", fg="#808080", font='arial 20 bold').pack(side=TOP, fill=X)

# search box
search = StringVar()
Entry(root, textvariable=search, width=15, bd=2, font="arial 20").place(x=820, y=70)
imageicon3 = PhotoImage(file="search.png")
Srch = Button(root, text="Search", compound=LEFT, image=imageicon3, width=123, bg="#68ddfa", font="arial 13 bold")
Srch.place(x=1060, y=66)

# tombol update
imageicon4 = PhotoImage(file="loading.png")
update_button = Button(root, image=imageicon4, bg="#c36464")
update_button.place(x=110, y=64)

# registrasi dan tanggal
Label(root, text="Registration No:", font="arial 13", fg=framebg, bg=background).place(x=30, y=150)
Label(root, text="Tanggal:", font="arial 13", fg=framebg, bg=background).place(x=500, y=150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

today = date.today()
d1 = today.strftime("%d/%m/%y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)
Date.set(d1)

# detail barang
obj = LabelFrame(root, text="Detail Barang", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

# detail harga
obj2 = LabelFrame(root, text="Detail Harga", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj, text="Nama Obat", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj, text="Golongan", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj, text="Brand", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(obj, text="Expired", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj, text="Kemasan", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Label(obj, text="Jumlah", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font="arial 10")
name_entry.place(x=160, y=50)

radio = IntVar()
R1 = Radiobutton(obj, text="Biasa", variable=radio, value=1, bg=framebg, fg=framefg)
R1.place(x=150, y=100)
R2 = Radiobutton(obj, text="Keras", variable=radio, value=2, bg=framebg, fg=framefg)
R2.place(x=200, y=100)

Brand = StringVar()
brand_entry = Entry(obj, textvariable=Brand, width=20, font="arial 10")
brand_entry.place(x=160, y=150)

Exp = StringVar()
expired_entry = Entry(obj, textvariable=Exp, width=20, font="arial 10")
expired_entry.place(x=630, y=50)

Kemasan = StringVar()
kemasan_entry = Entry(obj, textvariable=Kemasan, width=20, font="arial 10")
kemasan_entry.place(x=630, y=100)

jumlah = Combobox(obj, values=list(range(1, 1001)), font="roboto 10", width=17, state="r")
jumlah.place(x=630, y=150)
jumlah.set("Select Jumlah")

Label(obj2, text="Kode Obat", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj2, text="Distributor", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj2, text="Harga Beli", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(obj2, text="Harga Grosir", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj2, text="Harga Jual", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)

Kode = StringVar()
kode_obat_entry = Entry(obj2, textvariable=Kode, width=20, font="arial 10")
kode_obat_entry.place(x=160, y=50)

Distributor = StringVar()
distributor_entry = Entry(obj2, textvariable=Distributor, width=20, font="arial 10")
distributor_entry.place(x=160, y=100)

Beli = IntVar()
harga_beli_entry = Entry(obj2, textvariable=Beli, width=20, font="arial 10")
harga_beli_entry.place(x=160, y=150)

Grosir = IntVar()
harga_grosir_entry = Entry(obj2, textvariable=Grosir, width=20, font="arial 10")
harga_grosir_entry.place(x=630, y=50)

Jual = IntVar()
harga_jual_entry = Entry(obj2, textvariable=Jual, width=20, font="arial 10")
harga_jual_entry.place(x=630, y=100)

# Add functionality for the buttons (search, update)
def search_record():
    # Implement search functionality here
    pass

def update_record():
    # Implement update functionality here
    pass

Srch.config(command=search_record)
update_button.config(command=update_record)

root.mainloop()