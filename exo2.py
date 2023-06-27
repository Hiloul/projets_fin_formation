import datetime
import time
import winsound
import os


heure_alarme=input("veuillez régler l'alarme au format (HH:MM): ")
heure_entree = input(f"Voulez vous régler le reveil pour {heure_alarme}?")
# Il vérifie ensuite si l'heure est valide et la stocke dans une variable.
# le programme entre dans une boucle qui vérifie en permanence si l'heure actuelle dépasse ou égale à l'heure de l'alarme
heure_actuelle = datetime.datetime.now()

print(heure_actuelle)
# Test 5 minute
# time.sleep(300)
print("2 seconde")

# Return immediately, allowing sounds to play asynchronously.
winsound.SND_ASYNC