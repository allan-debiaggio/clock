import time
import os

def display_time () :
   while True :
      os.system("cls")
      print(time.strftime("%H:%M:%S"))
      time.sleep(1)

display_time()