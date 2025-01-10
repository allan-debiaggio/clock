import datetime
from time import sleep
from os import system


class GrannyClock :
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.correcting_custom_time()

    def display_custom_time(self, AMPM):
        """
        Used only for custom time

        displays clock according to time format
        AMPM enables to choose between 12 hours display and 24 hours display
        """
        clock = datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))
        if AMPM :
            if self.hours == 0 :
                clock = str(datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(12, self.minutes, self.seconds))) + " AM"
            elif self.hours == 12 :
                clock = str(datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(12, self.minutes, self.seconds))) + " PM"
            elif self.hours >= 1 and self.hours < 12 :
                clock = str(datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours, self.minutes, self.seconds))) + " AM"
            elif self.hours >= 13 and self.hours <= 23 :
                clock = str(datetime.time.fromisoformat("{:02}:{:02}:{:02}".format(self.hours % 12, self.minutes, self.seconds))) + " PM"

        print(clock)

    def correcting_custom_time(self):
        """
        Used only with custom time

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
    
    def check_alarm(self, autre):
        if self.hours == autre.hours and self.minutes == autre.minutes and self.seconds == autre.seconds :
            print("C'est l'heure !")

def menu(AMPM, custom_time, granny_clock, granny_alarm, alarm, finished):

    """
    features a general menu for the clock
    1 : use system clock to set the time
    2 : use user input clock to set the time
    3 : set the alarm time
    4 : switching between 12 hours display and 24 hours displays
    6 : turning off the clock
    """

    print("Menu de l'horloge.\nQue voulez-vous faire ?")
    print("Tapez 1 pour initialiser l'horloge")
    print("Tapez 2 pour régler l'heure")
    print("Tapez 3 pour régler l'alarme")
    print("Tapez 4 pour basculer en affichage 12h ou affichage 24h")
    print("Tapez 6 pour arrêter l'horloge")
    menu = input()

    while menu not in ["1", "2", "3", "4", "6"]:
        print("Veuillez renter un nombre : 1 ou 2 ou 3 ou 4 ou 6")
        menu = input()    

    if menu == "1":
        custom_time = False
    elif menu == "2" :
        custom_time = True
        hours = int(input("rentrez le nombre d'heures\n"))
        minutes = int(input("rentrez le nombre de minutes\n"))
        seconds = int(input("rentrez le nombre de secondes\n"))
        granny_clock = GrannyClock(hours, minutes, seconds)
    elif menu == "3":
        alarm = True
        hours = int(input("rentrez le nombre d'heures\n"))
        minutes = int(input("rentrez le nombre de minutes\n"))
        seconds = int(input("rentrez le nombre de secondes\n"))
        granny_alarm = GrannyClock(hours, minutes, seconds)
    elif menu == "4" :
        print("Tapez 1 pour affichage 12h")
        print("Tapez 2 pour affichage 24h")
        format_heure = input()
        if format_heure == "1":
            AMPM = True
        elif format_heure == "2":
            AMPM = False
    elif menu == "6":
        return (None, None, None, None, None, True)

    return (AMPM, custom_time, granny_clock, granny_alarm, alarm, finished)


def program_run(AMPM, custom_time, granny_clock, granny_alarm, alarm, finished):

    try :

        fonctions = menu(AMPM, custom_time, granny_clock, granny_alarm, alarm, finished)
        AMPM = fonctions[0]
        custom_time = fonctions[1]
        granny_clock = fonctions[2]
        granny_alarm = fonctions[3]
        alarm = fonctions[4]
        finished = fonctions[5]

        while True :

            if finished :
                return

            if custom_time :
                granny_clock.display_custom_time(AMPM)
                granny_clock.seconds += 1
                granny_clock.correcting_custom_time()
        
            else :
                horloge = datetime.datetime.now()
                formatted=""
                if AMPM :
                    formatted = horloge.strftime("%I:%M:%S %p")
                else :
                    formatted = horloge.strftime("%H:%M:%S")
                print(formatted)

            if alarm :
                if not custom_time :
                    granny_clock = GrannyClock(  int(horloge.strftime("%H")), int(horloge.strftime("%M")), int(horloge.strftime("%S")) )
                granny_clock.check_alarm(granny_alarm)

            sleep(1)
            system("clear")

    except KeyboardInterrupt :
        program_run(AMPM, custom_time, granny_clock, granny_alarm, alarm, finished)


def main():

    granny_alarm = None
    granny_clock = None

    # boolean used to turn off the clock - breaking the while True loop
    finished = False

    # boolean used to check wether we use an alarm, or not
    alarm = False

    # boolean used to check wether we use time system or custom time
    custom_time = False

    # boolean used to choose between 12hours and 24hours display
    AMPM = False

    program_run(AMPM, custom_time, granny_clock, granny_alarm, alarm, finished)


main()
