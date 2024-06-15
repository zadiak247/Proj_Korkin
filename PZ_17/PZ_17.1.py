"""
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением
пакета tk. Получить интерфейс максимально приближенный к оригиналу
"""

from tkinter import *

root = Tk()
root.title("17.1")
root.geometry('350x520')


def close():
    root.destroy()
    root.quit()


# button = ttk.Button(root, text="Press Me", command=button_clicked())
# button.pack(fill=BOTH)

frame1 = Frame(root, bg='gray', bd=5)
frame2 = Frame(root, bg='silver', bd=30)


header_h = Label(root, width=30, height=1)
header = Label(root, width=30, height=1, bg='silver')

label_top = Label(frame1, text='Contact Us', width=17, height=1, font='arial 20', bg='gray')
# label_top.place(x=0, y=0)


label1 = Label(frame2, text='First Name', width=10, height=1, font='arial 12', bg='silver')
entry1 = Entry(frame2, borderwidth=1, width=20)

label2 = Label(frame2, text='Last Name', width=10, height=1, font='arial 12', bg='silver')
entry2 = Entry(frame2, borderwidth=1, width=20)
entry2.insert(0, 'Smith')

label3 = Label(frame2, text='Email', width=6, height=1, font='arial 12', bg='silver')
entry3 = Entry(frame2, borderwidth=1, width=20)
entry3.insert(0, 'Email address')

label4 = Label(frame2, text='Website', width=8, height=1, font='arial 12', bg='silver')
entry4 = Entry(frame2, borderwidth=1, width=20)
entry4.insert(0, 'www.example.com')

label5 = Label(frame2, text='Password', width=10, height=1, font='arial 12', bg='silver')
entry5 = Entry(frame2, borderwidth=1, width=20)
entry5.insert(0, '8-10 characters')

label6 = Label(frame2, text='Password Confirmation', width=20, height=1, font='arial 12', bg='silver')
entry6 = Entry(frame2, borderwidth=1, width=20)
entry6.insert(0, 'Type your password again')

button1 = Button(frame2, text='Sign Up', width=4, height=1)

header_h.pack(), header.pack(), frame1.pack(), frame2.pack(), label_top.pack(), label1.pack(anchor=W), entry1.pack(), label2.pack(anchor=W),\
    entry2.pack(), label3.pack(anchor=W), entry3.pack(), label4.pack(anchor=W), entry4.pack(), label5.pack(anchor=W),\
    entry5.pack(), label6.pack(anchor=W), entry6.pack(), button1.pack(anchor=W, pady=10)

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()

