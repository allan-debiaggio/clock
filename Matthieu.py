import time 
import datetime


def menu():
    while True:
        afficher_menu()  # Affiche les options du menu
        choix = input("Choisissez une option (1-3): ")

        if choix == "1":
            regler_heure_manuel()
        elif choix == "2":
            afficher_heure_actu()
        elif choix == "3":
            alarme()


def afficher_menu():
    print("=== MENU ===")
    print("1. Régler l'heure")
    print("2. Afficher l'heure actuelle")
    print("3. Alarme")

def regler_heure(heure, minutes, secondes):
    # On utilise un tuple directement et on vérifie la validité des valeurs
    return (heure if 0 <= heure < 24 else None,
            minutes if 0 <= minutes < 60 else None,
            secondes if 0 <= secondes < 60 else None)

def incrementer_secondes(heure, minutes, secondes):
    while True:
        # Affiche l'heure actuelle sous forme (heure, minutes, secondes)
        print(f"Heure actuelle: {heure:02d}:{minutes:02d}:{secondes:02d}",end="\r")
        
        # Incrémente les secondes
        secondes += 1
        
        # Gestion des dépassements de secondes
        if secondes == 60:
            secondes = 0
            minutes += 1
        
        # Gestion des dépassements de minutes
        if minutes == 60:
            minutes = 0
            heure += 1
        
        # Gestion des dépassements d'heure (24 heures)
        if heure == 24:
            heure = 0
        
        # Attendre une seconde avant de répéter l'incrémentation
        time.sleep(1)

def regler_heure_manuel() :
    # Exemple d'utilisation
    heure = int(input("Entrez l'heure (0-23) : "))
    minutes = int(input("Entrez les minutes (0-59) : "))
    secondes = int(input("Entrez les secondes (0-59) : "))
    # Lancer l'incrémentation continue des secondes
    incrementer_secondes(heure, minutes, secondes)



# heure système
def afficher_heure_actu():
    while True:
        heure_actuelle = datetime.datetime.now()
        format_heure_actuelle = heure_actuelle.strftime("%H:%M:%S")  # Date et heure actuelles
        print(f"\r{format_heure_actuelle}",end='',flush=True)
        time.sleep(1)
        

    
# Alarme
def alarme(heure, minutes, secondes):
    while True:
        heure = int(input("Entrez l'heure (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les secondes (0-59) : "))
        if alarme(heure, minutes, secondes) == regler_heure_manuel() :
            print("DRING DRING !!!")




