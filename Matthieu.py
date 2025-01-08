import time 
import datetime

def regler_heure(heure, minutes, secondes):
    # On utilise un tuple directement et on vérifie la validité des valeurs
    return (heure if 0 <= heure < 24 else None,
            minutes if 0 <= minutes < 60 else None,
            secondes if 0 <= secondes < 60 else None)

def incrementer_secondes(heure, minutes, secondes):
    while True:
        # Affiche l'heure actuelle sous forme (heure, minutes, secondes)
        print(f"Heure actuelle: {heure:02d}:{minutes:02d}:{secondes:02d}")
        
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

# Exemple d'utilisation
heure = int(input("Entrez l'heure (0-23) : "))
minutes = int(input("Entrez les minutes (0-59) : "))
secondes = int(input("Entrez les secondes (0-59) : "))

# Lancer l'incrémentation continue des secondes
incrementer_secondes(heure, minutes, secondes)

