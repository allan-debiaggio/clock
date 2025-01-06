import datetime

def display_time(hours, minutes, seconds):
    clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
    print(clock)

def main():

    hours = int(input())
    minutes = int(input())
    seconds = int(input())

    while True :
        display_time(hours, minutes, seconds)

main()
