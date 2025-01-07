import datetime
from time import sleep

class GrannyClock :
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.correcting_time()

    def display_time(self, AMPM):
        """
        displays clock according to time format
        AMPM enables to choose between 12 hours display and 24 hours display
        """
        clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))
        if AMPM :
            if self.hours == 0 :
                hours = 12
                clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(hours, self.minutes, self.seconds))
                clock = str(clock)
                clock += " AM"
            elif self.hours == 12 :
                hours = 12
                clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(hours, self.minutes, self.seconds))
                clock = str(clock)
                clock += " PM"
            elif self.hours >= 1 and self.hours < 12 :
                clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))
                clock = str(clock)
                clock += " AM"
            elif self.hours >= 13 and self.hours <= 23 :
                hours = self.hours % 12
                clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(hours % 12, self.minutes, self.seconds))
                clock = str(clock)
                clock += " PM"

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

    # boolean used to choose between 12hours and 24hours display
    AMPM = False
    print("Voulez-vous un affichage 12 heures ? o/n")
    affichage = input()
    if affichage == "o" or affichage == "O" :
        AMPM = True


    while True :
        granny_clock.display_time(AMPM)
        sleep(1)
        granny_clock.seconds += 1
        granny_clock.correcting_time()

main()
