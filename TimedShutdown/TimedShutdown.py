import math
import os
import sys
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Fonts
font_courier10B = "Courier 10 bold"
font_courier12B = "Courier 12 bold"
font_courier18B = "Courier 18 bold"
font_courier22B = "Courier 22 bold"

# Entry Box size
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
        result = int(result * (60 * 60))
        # print("{} {} = {} Seconds".format(num, time_str, result))

    return result


def convertSecondsToTime(seconds):
    hours = seconds // (60 * 60)
    seconds -= (60 * 60) * hours

    minutes = seconds // 60
    seconds -= 60 * minutes

    # print(hours, "hour(s)")
    # print(minutes, "minute(s)")
    # print(seconds, "second(s)")

    return [hours, minutes, seconds]


def timedShutdown():

    # Create and Setup Window
    window = tk.Tk()
    window.title('TIMED SHUTDOWN')
    window.geometry("300x100")
    window.resizable(width=False, height=False)
    window.eval('tk::PlaceWindow . center')

    # Local Variable(s)
    total_time = IntVar(window, 0)

    # Zeros for Entry Defaults
    zero_text1 = StringVar(window, "0")
    zero_text2 = StringVar(window, "0")
    zero_text3 = StringVar(window, "0")

    # Hours
    label_Hours = StringVar(window, "Enter Hours: ")
    label_Hours_Dir = Label(window, textvariable=label_Hours, font=font_courier12B)
    label_Hours_Dir.grid(row=1, column=1)

    hr_ = Entry(window, textvariable=zero_text1, width=entrySize, font=font_courier10B)
    hr_.grid(row=1, column=2)

    # Minutes
    label_Minutes = StringVar(window, "Enter Minutes: ")
    label_Minutes_Dir = Label(window, textvariable=label_Minutes, font=font_courier12B)
    label_Minutes_Dir.grid(row=2, column=1)

    min_ = Entry(window, textvariable=zero_text2, width=entrySize, font=font_courier10B)
    min_.grid(row=2, column=2)

    # Seconds
    label_Seconds = StringVar(window, "Enter Seconds: ")
    label_Seconds_Dir = Label(window, textvariable=label_Seconds, font=font_courier12B)
    label_Seconds_Dir.grid(row=3, column=1)

    sec_ = Entry(window, textvariable=zero_text3, width=entrySize, font=font_courier10B)
    sec_.grid(row=3, column=2)

    def TotalSeconds():
        try:
            seconds_int = float(sec_.get())
            minutes_float = float(min_.get())
            hours_float = float(hr_.get())

            seconds_converted = convertTimeToSeconds(seconds_int, "seconds")
            minutes_converted = convertTimeToSeconds(minutes_float, "minutes")
            hours_converted = convertTimeToSeconds(hours_float, "hours")

            result = seconds_converted + minutes_converted + hours_converted
            # print("Total Seconds:", result)
            total_time.set(result)
            window.destroy()

        except:
            messagebox.showinfo("ERROR", "USER DID NOT ENTER A VALID TIME TO SHUTDOWN, ABORTING PROGRAM")
            window.destroy()
            sys.exit()

    button = tk.Button(window, text="Timed Shutdown", command=TotalSeconds)
    button.grid(row=4, column=2)

    window.mainloop()
    return int(total_time.get())


# https://www.geeksforgeeks.org/create-countdown-timer-using-python-tkinter/
def timer(total_time):

    # Creating and setting geometry of tk window
    window = Tk()
    window.geometry("500x125")
    window.resizable(width=False, height=False)
    window.eval('tk::PlaceWindow . center')

    # Local Variables
    early_exit = BooleanVar(window, False)
    no_entry = BooleanVar(window, False)

    # Set's No_Entry boolean to True if no time was entered in first window
    if total_time <= 0:
        no_entry.set(True)
        messagebox.showinfo("ERROR", "USER DID NOT ENTER A TIME TO SHUTDOWN, ABORTING PROGRAM")
        window.destroy()
        sys.exit()

    # Toggles Early Exit Boolean to True
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
            early_exit.set(True)

    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    window.title("Shutdown Countdown")

    # Convert seconds into Hours, Minutes, Seconds for timer
    times = convertSecondsToTime(total_time)

    # Declaration of variables
    hour = StringVar(window, str(times[0]))
    minute = StringVar(window, str(times[1]))
    second = StringVar(window, str(times[2]))

    # Label
    label = Label(window, textvariable=StringVar(window, "TIME LEFT UNTIL SHUTDOWN"), font=font_courier22B)
    label.grid(row=0, column=1)

    # Use of Entry class to take input from the user
    hourEntry = Entry(window, width=3, font=font_courier18B, textvariable=hour)
    hourEntry.grid(row=1, column=0)

    minuteEntry = Entry(window, width=3, font=font_courier18B, textvariable=minute)
    minuteEntry.grid(row=1, column=1)

    secondEntry = Entry(window, width=3, font=font_courier18B, textvariable=second)
    secondEntry.grid(row=1, column=2)

    text = Label(window, textvariable=StringVar(window, "Exit this window to cancel Timed Shutdown"), font=font_courier12B)
    text.grid(rows=2, column=1)

    def countdown():
        time_left = total_time
        window.protocol("WM_DELETE_WINDOW", on_closing)

        while time_left > -1:

            # Exit early from window
            if bool(early_exit.get()):
                sys.exit()

            # Convert Time Left to hours, minutes, seconds
            min_, secs = divmod(time_left, 60)
            hours = 0
            if min_ > 60:
                hours, min_ = divmod(min_, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(min_))
            second.set("{0:2d}".format(secs))

            window.update()
            time.sleep(1)

            time_left -= 1
            if time_left <= 0:
                os.system("shutdown -s -t 5")
                window.destroy()

    countdown()
    window.mainloop()


if __name__ == '__main__':
    timeEntered = timedShutdown()
    timer(timeEntered)
