from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=300, height=200)
mile_input = Entry(width=7)
input.grid(row=0, column=1)


# label
Miles = Label(text='Miles')
Miles.grid(column=2, row=0)

equal = Label(text='is equal to')
equal.grid(row=1, column=0)

km = Label(text='km')
km.grid(row=1, column=2)

calc = Label(text='0')
calc.grid(row=1, column=1)


# button
def button_click():
    miles = float(mile_input.get())
    km = miles * 1.69
    calc.config(text=km)


button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)


window.mainloop()