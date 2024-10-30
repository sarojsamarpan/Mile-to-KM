from tkinter import *


def calculate():
    miles = int(input.get())
    km = round(miles * 1.6, 2)
    answer.config(text=km)


window = Tk()

window.title("Mile to KM converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

input = Entry()
input.grid(column=1, row=0)

input_label = Label(text="Miles")
input_label.grid(column=2, row=0)

messaage = Label(text="is equal to")
messaage.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

unit = Label(text="KM")
unit.grid(column=2, row=1)

convert = Button(text="Calculate", command=calculate)
convert.grid(column=1, row=2)


window.mainloop()
