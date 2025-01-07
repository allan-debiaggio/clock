import datetime
from time import sleep

def display_time(hours, minutes, seconds):
    clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
    print(clock)

def main():

    hours = int(input())
    minutes = int(input())
    seconds = int(input())

    while True :
        display_time(hours, minutes, seconds)
        sleep(1)
        seconds += 1
        if seconds >= 60 :
            seconds = seconds % 60
            minutes += 1
            if minutes >= 60 :
                minutes = minutes % 60
                hours += 1
                if hours >= 24 :
                    hours = hours % 24
                    minutes = minutes % 60
                    seconds = seconds % 60


main()
