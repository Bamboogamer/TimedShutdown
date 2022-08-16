import math
import os
import time
import tkinter as tk
from tkinter import *

# Helper Method(s)
def convertTime(num, time_str):
    time_str = time_str.lower()
    result = num

    if time_str in ["second", "seconds", "sec", "s"]:
        result = math.ceil(result)
        # print("{} {} = {} Seconds".format(num, time_str, result))

    elif time_str in ["minute", "minutes", "min", "m"]:
        result *= 60
        result = int(result)
        # print("{} {} = {} Seconds".format(num, time_str, result))

    elif time_str in ["hour", "hours", "hr", "h"]:
        result = int(result * (60*60))
        # print("{} {} = {} Seconds".format(num, time_str, result))

    return result


def timedShutdown():

    # Creates Window
    win = tk.Tk()
    win.title('TIMED SHUTDOWN')
    win.geometry("300x100")
    win.eval('tk::PlaceWindow . center')

    # Zeros for Entry Defaults
    zero_text1 = StringVar(win, "0")
    zero_text2 = StringVar(win, "0")
    zero_text3 = StringVar(win, "0")

    # Hours
    label_Hours = StringVar(win, "Enter Hours: ")
    label_Hours_Dir = Label(win, textvariable=label_Hours)
    label_Hours_Dir.grid(row=1, column=1)

    hr_ = Entry(win, textvariable=zero_text1, width=30)
    hr_.grid(row=1, column=2)

    # Minutes
    label_Minutes = StringVar(win, "Enter Minutes: ")
    label_Minutes_Dir = Label(win, textvariable=label_Minutes)
    label_Minutes_Dir.grid(row=2, column=1)

    min_ = Entry(win, textvariable=zero_text2, width=30)
    min_.grid(row=2, column=2)

    # Seconds
    label_Seconds = StringVar(win, "Enter Seconds: ")
    label_Seconds_Dir = Label(win, textvariable=label_Seconds)
    label_Seconds_Dir.grid(row=3, column=1)

    sec_ = Entry(win, textvariable=zero_text3, width=30)
    sec_.grid(row=3, column=2)

    def PrintTotalSeconds():

        seconds_int = int(sec_.get())
        minutes_float = float(min_.get())
        hours_float = float(hr_.get())

        seconds_converted = convertTime(seconds_int, "seconds")
        minutes_converted = convertTime(minutes_float, "minutes")
        hours_converted = convertTime(hours_float, "hours")

        result = seconds_converted + minutes_converted + hours_converted
        print("Total Seconds:", result)

        # win.destroy()

    button = tk.Button(win, text="Timed Shutdown", command=PrintTotalSeconds)
    button.grid(row=4, column=2)

    win.mainloop()


if __name__ == '__main__':

    # convertTime(3600.9, "seconds")
    # convertTime(60, "minutes")
    # convertTime(1.5, "hours")
    timedShutdown()

