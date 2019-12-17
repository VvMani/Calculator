from tkinter import *

root = Tk()
root.title("Calc")

# Entry widget
entry = Entry(root, width=60, border=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10,ipady=13)


# when button_click
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


# clear the text in entry widget
def button_clear():
    entry.delete(0, END)


# Addition button
def button_addition():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiply'
    f_num = float(first_number)
    entry.delete(0, END)


def button_division():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    entry.delete(0, END)


def button_backspace():
    current = entry.get()
    back = current[0:len(current) - 1]
    entry.delete(0, END)
    entry.insert(0, int(back))


def button_equal():
    second_num = entry.get()
    sec_num = int(second_num)
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + sec_num)
    elif math == "subtraction":
        entry.insert(0, f_num - sec_num)
    elif math == "multiply":
        entry.insert(0, f_num * sec_num)
    elif math == 'division':
        entry.insert(0, f_num / sec_num)


# define button
button_1 = Button(root, text="1", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click(0))
button_00 = Button(root, text="00", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click('00'))
button_dot = Button(root, text=".", padx=40, pady=20, border=5,fg="white", bg="grey", command=lambda: button_click('.'))


button_clear = Button(root, text="C", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_clear)
button_equal = Button(root, text="=", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_equal)
button_multiply = Button(root, text="*", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_multiply)
button_addition = Button(root, text="+", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_addition)
button_subtraction = Button(root, text="-", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_sub)
button_division = Button(root, text="/", padx=40, pady=20, border=5,fg="white", bg="grey", command=button_division)
button_back = Button(root, text="⌫", padx=36, pady=20, border=5,fg="white", bg="grey", command=button_backspace)

# Put the button on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_addition.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_equal.grid(row=5, column=3)
button_0.grid(row=5, column=0)
button_00.grid(row=5, column=1)
button_dot.grid(row=5,column=2)
button_clear.grid(row=1, column=1)
button_division.grid(row=1, column=3)
button_back.grid(row=1, column=2)

root.mainloop()
