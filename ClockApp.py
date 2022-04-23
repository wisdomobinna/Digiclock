from tkinter import Tk   
from tkinter import Label
import time

#tkinter is the standard GUI library for Python
#Label widget as part of the tkinter library is used to provide a single-line capiton for other widgets. 
#it can also contain images

masters =Tk()
masters.title("DigiClock")
clock = Label (masters, font=("Times New Roman", 70), bg="Black", fg="Cyan")
Label(masters, font=("Calibri", 25), text="Digital Clock", bg="black", fg="Cyan").pack()

#simple function to return time with format, timing and refreshing
#strftime makes it possible to specify a format string for a date object 
# in formatted string literals

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

clock.pack()
get_time()
masters.mainloop()

#mainloop function helps Tkinter to start running the application