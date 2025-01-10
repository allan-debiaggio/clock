from datetime import datetime, timedelta
import time
import os
import threading

current_time = None
user_alarm = None
AMPM = None
stop_clock = False
clock_thread = None


def menu():
    global current_time
    global AMPM
    global stop_clock
    global clock_thread
    try:
        while True:
            print("\nMenu:")
            print("1. Display time")
            print("2. Set time")
            print("3. Set alarm")
            print("4. Time mode (12h / 24h)")
            print("5. Sleep mode")
            print("6. Quit")
            select = input("Enter your choice: ")

            if select == "1":
                display_time()
            elif select == "2":
                set_time()
            elif select == "3":
                set_alarm()
            elif select == "4":
                time_format()
            elif select == "5" :
                sleep_mode()
            elif select == "6":
                stop_clock_thread()
                print("Exiting clock program.")
                break
            else:
                print("Invalid option. Please try again.")
    except KeyboardInterrupt:
        stop_clock_thread()
        print("\nExiting clock program.")


def background_clock():
    global current_time
    global user_alarm
    global stop_clock

    if current_time is None:
        current_time = datetime.now()

    while not stop_clock:
        current_time += timedelta(seconds=1)
        # Check for alarm
        if user_alarm and current_time.strftime("%H:%M:%S") == user_alarm:
            print("\nALARM! DRINNNNG DRINNNNG!")
            user_alarm = None  # Reset alarm after it rings
        time.sleep(1)


def display_time():
    global current_time
    try:
        while True:
            os.system("cls")  # Clear the console
            if AMPM is None or not AMPM:
                print("Current Time:", current_time.strftime("%H:%M:%S"))
            else:
                print("Current Time:", current_time.strftime("%I:%M:%S %p"))
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReturning to menu...")


def set_time(): 
    global current_time
    try:
        user_time = input("Enter the time to start the clock (HH:MM:SS): ")
        current_time = datetime.strptime(user_time, "%H:%M:%S")
        print("Time set successfully!")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    except KeyboardInterrupt:
        print("Going back to menu...")


def set_alarm(): 
    global user_alarm
    try:
        user_alarm = input("Enter the time you want the alarm to ring (HH:MM:SS): ")
        print(f"Alarm set for {user_alarm}.")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    except KeyboardInterrupt:
        print("Going back to menu...")


def time_format():
    global AMPM
    try:
        choice = input("Select 1 for 24-hour format or 2 for 12-hour format: ")
        if choice == "1":
            AMPM = False
            print("Switched to 24-hour format.")
        elif choice == "2":
            AMPM = True
            print("Switched to 12-hour format.")
        else:
            print("Invalid choice.")
    except KeyboardInterrupt:
        print("Going back to menu...")


def stop_clock_thread():
    global stop_clock
    global clock_thread
    stop_clock = True
    if clock_thread is not None:
        clock_thread.join()  # Wait for the thread to finish before exiting


def sleep_mode():
    global stop_clock
    global clock_thread
    choice = input("Type 1 to enter sleep mode and 2 to reactivate the clock: ")
    if choice == "1":
        stop_clock = True
    elif choice == "2":
        stop_clock = False
        if clock_thread is None or not clock_thread.is_alive():  # Start a new thread if necessary
            clock_thread = threading.Thread(target=background_clock, daemon=True)
            clock_thread.start()
    else:
        print("I didn't understand your request.")


# Start the clock in a separate thread
stop_clock = False
clock_thread = threading.Thread(target=background_clock, daemon=True) #Daemon used to make the thread close
# when the main program exits 
clock_thread.start()

menu()
