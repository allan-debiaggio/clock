# Function 1 : Display time
# Function 2 : Set time
# Function 3 : Set Alarm
# Function 4 opt : AM / PM Time
# Function 5 opt : Sleep time until user input
# Datetime object is really useful, should use it

from datetime import datetime, timedelta
import time
import os

current_time = None
user_alarm = None

def menu():
    global current_time
    try:
        while True:
            select = input("Menu: \n Enter 1 for the clock, 2 for setting time, 3 for setting an alarm, 6 to quit: ")
            if select == "1":
                display_time()
            elif select == "2":
                set_time()
            elif select == "3":
                set_alarm()
            elif select == "6":
               print("Exiting clock program.")
               break
            else:
                print("I did not understand your request.")
            quit
    except KeyboardInterrupt:
        print("\nExiting clock program.")

def display_time():
    global current_time
    global user_alarm
    try:
        if current_time is None:
            current_time = datetime.now()
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Current Time:", current_time.strftime("%H:%M:%S"))
            
            # Check for alarm
            if user_alarm and current_time.strftime("%H:%M:%S") == user_alarm:
                print("ALARM! DINNNNG DINNNNG!")
                user_alarm = None  # Reset alarm after it rings
            
            time.sleep(1)
            current_time += timedelta(seconds=1)  # Increments current time
    except KeyboardInterrupt:
      print("Going back to menu...")

def set_time():
    global current_time
    try:
        user_time = input("Enter the time to start the clock (HH:MM:SS): ")
        current_time = datetime.strptime(user_time, "%H:%M:%S")
        print("Time set successfully!")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    except KeyboardInterrupt:
        menu()

def set_alarm():
    global user_alarm
    try:
        user_alarm = input("Enter the time you want the alarm to ring (HH:MM:SS): ")
        print(f"Alarm set for {user_alarm}.")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    except KeyboardInterrupt:
        menu()

menu()