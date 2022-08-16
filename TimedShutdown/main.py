import math
import os
import tkinter as tk
from tkinter import *

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


def createWindow():
    win = tk.Tk()
    win.geometry("350x300")

    title = tk.Label(win, text="###", font="Courier 12 bold")
    title.grid(row=0, column=1)
    title = tk.Label(win, text="TIMED SHUTDOWN", font="Courier 12 bold")
    title.grid(row=0, column=2)
    title = tk.Label(win, text="###", font="Courier 12 bold")
    title.grid(row=0, column=3)

    label_Seconds = StringVar()
    label_Seconds.set("Enter Seconds: ")
    label_Seconds_Dir = Label(win, textvariable=label_Seconds)
    label_Seconds_Dir.grid(row=1, column=1)

    sec_ = Entry(win, width=30)
    sec_.grid(row=1, column=2)

    label_Minutes = StringVar()
    label_Minutes.set("Enter Minutes: ")
    label_Minutes_Dir = Label(win, textvariable=label_Minutes)
    label_Minutes_Dir.grid(row=2, column=1)

    min_ = Entry(win, width=30)
    min_.grid(row=2, column=2)

    label_Hours = StringVar()
    label_Hours.set("Enter Hours: ")
    label_Hours_Dir = Label(win, textvariable=label_Hours)
    label_Hours_Dir.grid(row=3, column=1)

    hr_ = Entry(win, width=30)
    hr_.grid(row=3, column=2)

    def PrintTotalSeconds():

        try:
            seconds_int = int(sec_.get())
        except:
            seconds_int = 0

        try:
            minutes_float = float(min_.get())
        except:
            minutes_float = 0

        try:
            hours_float = float(hr_.get())
        except:
            hours_float = 0

        seconds_converted = convertTime(seconds_int, "seconds")
        minutes_converted = convertTime(minutes_float, "minutes")
        hours_converted = convertTime(hours_float, "hours")

        time_in_seconds = seconds_converted + minutes_converted + hours_converted
        print("Total Seconds:", time_in_seconds)

        # win.destroy()

    button = tk.Button(win, text="Calculate", command=PrintTotalSeconds)
    button.grid(row=4, column=2)

    win.mainloop()


if __name__ == '__main__':

    # convertTime(3600.9, "seconds")
    # convertTime(60, "minutes")
    # convertTime(1.5, "hours")
    createWindow()

