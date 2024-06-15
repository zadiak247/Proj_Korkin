"""
Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.
"""

from tkinter import *
from tkinter import ttk


def get_info():
    X = int(entry1.get())
    A = int(entry2.get())
    Y = int(entry3.get())
    Price = A / X
    Y_kg = Price * Y
    label["text"] = 'Один кг конфет стоит %.02F рублей.\n%d кг конфет стоит %.02f рублей.' % (Price, Y, Y_kg)
    # label["text"] = f'Один кг конфет стоит {Price} рублей.\n{Y} кг конфет стоит {Y_kg} рублей.'


root = Tk()
root.title("17.2")
# root.geometry("250x200")


label1 = ttk.Label(text='ввод числа Х (кол-во килограмм конфет):')
label1.pack()
entry1 = ttk.Entry()
entry1.pack()

label2 = ttk.Label(text='ввод А (стоимость X кг конфет):')
label2.pack()
entry2 = ttk.Entry()
entry2.pack()

label3 = ttk.Label(text='ввод У (кол-во килограмм конфет, цену которых необходимо найти):')
label3.pack()
entry3 = ttk.Entry()
entry3.pack()

btn = ttk.Button(text="Click", command=get_info)
btn.pack()

label = ttk.Label()
label.pack()

root.mainloop()
