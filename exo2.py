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

# Input pour récuperer l'heure à laquelle le reveil sonnera
heure_entree=input("Veuillez régler l'alarme au format (HH:MM): ")
# Convertir en heure datetime pour le calcul
heure_convertie = datetime.datetime.strptime(heure_entree, "%H:%M")
# Try / except pour verifier la validité de l'heure et gestion d'erreurs
heure_valide = True
try:
    datetime.datetime.strptime(heure_entree, "%H:%M")
except ValueError:
            heure_valide = False


# Variable pour récuperer l'heure actuelle (import datetime)
heure_actuelle = datetime.datetime.now()
print(heure_actuelle)

def cocorico():
# Lancer le son à partir de l'url du fichier
    winsound.PlaySound('sons/son.wav', winsound.SND_FILENAME)	

def snooze():
    # Fonction pour retarder l'alarme
    print("Fonction snooze activée.")
    time.sleep(3) 

choix_snooze = input("Souhaitez-vous activer la fonction snooze ? (Oui/Non) ")
if choix_snooze.lower() == "oui":
    snooze()
else:
    pass


