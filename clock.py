from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title('Clock')

def clock():
    time = strftime('%I:%M:%S %p')
    label.config(text=time)
    label.after(1000, clock)

label = Label(window, font = ('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')

clock()

mainloop()