import math
import os
import time
import tkinter as tk
from tkinter import *

font_courier10B = "Courier 10 bold"
font_courier12B = "Courier 12 bold"
font_courier18B = "Courier 18 bold"
font_courier22B = "Courier 22 bold"

entrySize = 15


# Helper Method(s)
def convertTimeToSeconds(num, time_str):
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


def convertSecondsToTime(seconds):

    hours = seconds // (60*60)
    seconds -= (60*60)*hours

    minutes = seconds // 60
    seconds -= 60 * minutes

    # print(hours, "hour(s)")
    # print(minutes, "minute(s)")
    # print(seconds, "second(s)")

    return [hours, minutes, seconds]


def timedShutdown():

    # Creates Window
    win = tk.Tk()
    win.title('TIMED SHUTDOWN')
    win.geometry("300x100")
    # win.geometry("500x500")
    win.eval('tk::PlaceWindow . center')

    total_time = IntVar(win, 0)

    # Zeros for Entry Defaults
    zero_text1 = StringVar(win, "0")
    zero_text2 = StringVar(win, "0")
    zero_text3 = StringVar(win, "0")

    # Hours
    label_Hours = StringVar(win, "Enter Hours: ")
    label_Hours_Dir = Label(win, textvariable=label_Hours, font=font_courier12B)
    label_Hours_Dir.grid(row=1, column=1)

    hr_ = Entry(win, textvariable=zero_text1, width=entrySize, font=font_courier10B)
    hr_.grid(row=1, column=2)

    # Minutes
    label_Minutes = StringVar(win, "Enter Minutes: ")
    label_Minutes_Dir = Label(win, textvariable=label_Minutes, font=font_courier12B)
    label_Minutes_Dir.grid(row=2, column=1)

    min_ = Entry(win, textvariable=zero_text2, width=entrySize, font=font_courier10B)
    min_.grid(row=2, column=2)

    # Seconds
    label_Seconds = StringVar(win, "Enter Seconds: ")
    label_Seconds_Dir = Label(win, textvariable=label_Seconds, font=font_courier12B)
    label_Seconds_Dir.grid(row=3, column=1)

    sec_ = Entry(win, textvariable=zero_text3, width=entrySize, font=font_courier10B)
    sec_.grid(row=3, column=2)

    def TotalSeconds():

        seconds_int = int(sec_.get())
        minutes_float = float(min_.get())
        hours_float = float(hr_.get())

        seconds_converted = convertTimeToSeconds(seconds_int, "seconds")
        minutes_converted = convertTimeToSeconds(minutes_float, "minutes")
        hours_converted = convertTimeToSeconds(hours_float, "hours")

        result = seconds_converted + minutes_converted + hours_converted
        print("Total Seconds:", result)
        total_time.set(result)
        win.destroy()

    button = tk.Button(win, text="Timed Shutdown", command=TotalSeconds)
    button.grid(row=4, column=2)

    win.mainloop()
    return int(total_time.get())


def timer(total_time):
    from tkinter import messagebox

    # creating Tk window
    root = Tk()

    early_exit = BooleanVar(root, False)

    # setting geometry of tk window
    root.geometry("500x125")
    root.eval('tk::PlaceWindow . center')

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            early_exit.set(True)

    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    root.title("Time Counter")

    times = convertSecondsToTime(total_time)

    # Declaration of variables
    hour = StringVar(root, str(times[0]))
    minute = StringVar(root, str(times[1]))
    second = StringVar(root, str(times[2]))

    # Label
    label = Label(root, textvariable=StringVar(root, "TIME LEFT UNTIL SHUTDOWN"), font=font_courier22B)
    label.grid(row=0, column=1)

    # Use of Entry class to take input from the user
    hourEntry = Entry(root, width=3, font=font_courier18B,
                      textvariable=hour)
    hourEntry.grid(row=1, column=0)

    minuteEntry = Entry(root, width=3, font=font_courier18B,
                        textvariable=minute)
    minuteEntry.grid(row=1, column=1)

    secondEntry = Entry(root, width=3, font=font_courier18B,
                        textvariable=second)
    secondEntry.grid(row=1, column=2)

    text = Label(root, textvariable=StringVar(root, "Exit this window to cancel Timed Shutdown"), font=font_courier12B)
    text.grid(rows=2, column=1)

    def submit():
        temp = total_time
        root.protocol("WM_DELETE_WINDOW", on_closing)

        while temp > -1:

            if bool(early_exit.get()):
                return

            mins, secs = divmod(temp, 60)

            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if temp == 0:
                print("TIMER EXITED, SHUTTING DOWN IN 5 SECONDS")
                os.system("shutdown -s -t 5")
                # messagebox.showinfo("Time Countdown", "Time's up ")

            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
    submit()

    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()


if __name__ == '__main__':

    # convertTime(3600.9, "seconds")
    # convertTime(60, "minutes")
    # convertTime(1.5, "hours")
    timer(timedShutdown())

