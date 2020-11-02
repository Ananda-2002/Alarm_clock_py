import datefinder
import winsound
import datetime
import subprocess
import webbrowser
import os


def alarm():
    hourA = int(input("Enter hour "))
    minA = int(input("Enter minute "))
    if hourA < 12:
        day_night = input("AM/PM? ")
        if day_night.lower() == "pm":
            hourA += 12
    print("Alarm set at ", hourA, ":", minA, day_night)
    while True:

        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound(
                    'audios\\alarm.wav', winsound.SND_LOOP)
            elif minA < datetime.datetime.now().minute:
                break


alarm()
