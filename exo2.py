# 1. demander à l'utilisateur de définir l'heure de l'alarme au format HH:MM. 
# 2. Il vérifie ensuite si l'heure est valide et la stocke dans une variable.
# 3. Entre dans une boucle qui vérifie si l'heure actuelle > ou = à l'heure de l'alarme. 
# 4. L'alarme atteinte, déclenche une alarme sonore en jouant un fichier audio.
# 5. L'alarme déclenchée , demande à l'user s'il souhaite activer la fonction snooze. 
# 6. Si "oui", l'alarme est retardée de 5 minutes la fonction snooze est activée.
# 7. Continue à vérifier l'heure actuelle et à déclencher l'alarme 
# 8. Jusqu'à ce que l'user choisisse de ne pas activer la fonction snooze.
# ++ modules os pour effectuer des opérations système.

import datetime
import time
import winsound
import os

def check_alarm(heure_entree):
    heure_alarme = datetime.datetime.strptime(heure_entree, "%H:%M").time()

    while True:
        heure_actuelle = datetime.datetime.now().time()

        if heure_actuelle >= heure_alarme:
            cocorico()
            break

        time.sleep(1)

def reveil_matin(heure_entree):
    heure_actuelle = datetime.datetime.now()
    print(heure_actuelle)
    heure_convertie = datetime.datetime.strptime(heure_entree, "%H:%M")
    alarme = heure_actuelle - heure_convertie
    print(alarme)

def cocorico():
    reveil_matin(heure_entree)
    fichier_son = os.path.join(os.getcwd(), 'sons', 'son.wav')
    winsound.PlaySound(fichier_son, winsound.SND_FILENAME)

def snooze():
    print("Fonction snooze activée.")
    time.sleep(2)  # 15 minutes = 900 secondes
    cocorico()

heure_entree = input("Veuillez régler l'alarme au format (HH:MM): ")
heure_valide = True

try:
    datetime.datetime.strptime(heure_entree, "%H:%M")
except ValueError:
    heure_valide = False

if heure_valide:
    check_alarm(heure_entree)
else:
    print("Heure invalide. Veuillez entrer une heure au format HH:MM.")


while True:
    choix_snooze = input("Souhaitez-vous activer la fonction snooze ? (Oui/Non) ")
    if choix_snooze.lower() == "oui":
        snooze()
    else:
        print("N'oublies pas de te réveiller !")
        break

