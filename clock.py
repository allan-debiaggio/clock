import datetime
from time import sleep

class GrannyClock :
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.correcting_time()

    def display_time(self):
        clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))
        print(clock)

    def correcting_time(self):
        """
        Makes sure number of seconds is < 60,
        number of minutes < 60 and number of hours < 24.
        Number of minutes is incremented when number of seconds reaches 60
        Number of hours is incremented when number of minutes reaches 60
        Number of seconds and minutes is set to 0 when number of hours reaches 24
        """
        if self.seconds >= 60 :
            self.seconds = self.seconds % 60
            self.minutes += 1
            if self.minutes >= 60 :
                self.minutes = self.minutes % 60
                self.hours += 1
                if self.hours >= 24 :
                    self.hours = self.hours % 24
                    self.minutes = self.minutes % 60
                    self.seconds = self.seconds % 60

def main():
    hours = int(input("rentrez le nombre d'heures\n"))
    minutes = int(input("rentrez le nombre de minutes\n"))
    seconds = int(input("rentrez le nombre de secondes\n"))
    granny_clock = GrannyClock(hours, minutes, seconds)

    while True :
        granny_clock.display_time()
        sleep(1)
        granny_clock.seconds += 1
        granny_clock.correcting_time()

main()
