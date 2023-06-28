# Projet : Programme de compteur avec cadeau de fidélité
# Description : Ce projet consiste en la création d'une application graphique 
# utilisant Tkinter, qui affiche un compteur et offre un cadeau de fidélité à 
# l'utilisateur lorsque le compteur atteint 10. L'application présente une interface
# simple avec un label pour afficher le compteur et un bouton pour l'incrémenter.
# Fonctionnalités :
# 1. Le compteur est initialisé à 0 et affiché dans un label.
# 2. Chaque clic sur le bouton "Incrémenter", le compteur += 1 màj valeur affichée
# 3. Lorsque compteur == 10, un cadeau de fidélité est offert à l'user. 
# 4. L'image du cadeau (redimensionnée) affichée avec module PIL (Pillow) dans un label 
# 5. Fenêtre dimensions prédéfinies (400x350) avec utilisation intuitive.
# 6. L'user peut lancer l'app et observer le compteur affiché. 
# ++ image nommée "Cadeau.png" dans un dossier "images"
# ++ Le titre de la fenêtre est clair

from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Compteur Avec Cadeaux de Fidélité !")

# Définition de la taille initiale de la fenêtre
largeur = 400
hauteur = 350
root.geometry(f"{largeur}x{hauteur}")

# Charger l'image
image_cadeau = Image.open("images/Cadeau.png")

# Taille
nouvelle_largeur = 150
nouvelle_hauteur = 125

# Redimensionnement
image_redimensionnee = image_cadeau.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)
image_tk = ImageTk.PhotoImage(image_redimensionnee)

# Compteur
compteur = tk.IntVar()
compteur.set(0)
label_compteur = tk.Label(root, textvariable=compteur, font=("Arial", 24))

def quit_button_click():
    if messagebox.askyesno("Quitter", "En êtes vous sur(e)?"):
        root.destroy()

def incrementer_button():
    compteur.set(compteur.get() + 1)
    if compteur.get() == 10:
        # Afficher l'image du cadeau
        etiquette_cadeau = tk.Label(root, image=image_tk)
        etiquette_cadeau.pack(side="bottom")
        compteur.set(0)     

# Placement compteur dans la fenêtre
label_compteur.pack()

increment_button = tk.Button(root, text="Incrémenter", command=incrementer_button)
increment_button.pack()

quit_button = tk.Button(root, text="Quitter", command=quit_button_click)
quit_button.pack(side="bottom")

root.mainloop()



