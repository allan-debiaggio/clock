# Function 1 : Display time
# Function 2 : Set time
# Function 3 : Set Alarm
# Function 4 opt : AM / PM Time
# Function 5 opt : Sleep time until user input

from datetime import datetime
import time
import os

def menu () :
   try :
      select=input("Enter 1 for the clock, 2 for setting time and 3 for setting an alarm : ")
      if select == "1" :
         display_time()
      else :
         print("I did not understand your request")
   except KeyboardInterrupt :
      print("Exiting clock program")


def display_time() :
   try :
      while True :
         os.system("cls") 
         current_time=time.strftime("%H:%M:%S")
         print(current_time)
         time.sleep(1)
   except KeyboardInterrupt :
        print("Exiting clock program")

#def set_time() :


menu()