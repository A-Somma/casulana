__author__ = 'Somma'
import IntervalsMenuInterface
from tkinter import messagebox
from datetime import datetime

date = datetime.now()
year = date.year

if year ==2016:

    root = IntervalsMenuInterface.tkinter.Tk()
    app = IntervalsMenuInterface.IntervalMenuInterface(master=root)
    app.mainloop()
else:
    messagebox.showerror(title="Error", message="Program is out of date! \n \n Please contact support at :\n casulana.aide@gmail.com")

