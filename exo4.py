# Projet : Affiche un compteur et offre un cadeau de fidélité à 
# l'utilisateur tous les dix achats jusqu'au trentième achat. 
# 1. Le compteur est initialisé à 0 et affiché dans un label. 
# 2. À chaque clic sur le bouton "Incrémenter", le compteur est incrémenté de 1
# 3. Cadeau de fidélité : tout les 10 un cadeau de fidélité est offert à l'utilisateur. 
# 4. L'image du cadeau est affichée à l'aide du module PIL (Pillow)
# 5. Après chaque cadeau, passe à l'image suivante dans la liste. 
# 6. Lorsque la dernière image (30 clique) est atteinte, reste sur la dernière image 
# ++ L'application présente une fenêtre de (400x350) 
# ++ Le titre de la fenêtre indique clairement la fonctionnalité du programme.
# ++Assurez-vous de placer les images de cadeaux (cadeau.jpg, cadeau2.jpg, cadeau3.jpg)

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
image_cadeau2 = Image.open("images/Cadeau2.png")
image_cadeau3 = Image.open("images/Cadeau3.png")

# Taille
nouvelle_largeur = 150
nouvelle_hauteur = 125

# Redimensionnement
image_redimensionnee = image_cadeau.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)
image_tk = ImageTk.PhotoImage(image_redimensionnee)
image_redimensionnee2 = image_cadeau2.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)
image_tk2 = ImageTk.PhotoImage(image_redimensionnee2)
image_redimensionnee3 = image_cadeau3.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)
image_tk3 = ImageTk.PhotoImage(image_redimensionnee3)
# Compteur
compteur = tk.IntVar()
compteur.set(0)
label_compteur = tk.Label(root, textvariable=compteur, font=("Arial", 24))

# Variable pour afficher image 
etiquette = tk.Label(root, image=image_tk)
# etiquette.pack()
etiquette2 = tk.Label(root, image=image_tk2)
# etiquette2.pack()
etiquette3 = tk.Label(root, image=image_tk3)
# etiquette3.pack()
    
def quit_button_click():
    if messagebox.askyesno("Quitter", "En êtes vous sur(e)?"):
        root.destroy()

# def incrementer_button():
#     if compteur:
#         compteur.set(compteur.get() + 1)
#     elif compteur == 10:
#         etiquette.pack()
#     elif compteur == 20:
#         etiquette2.pack()
#     elif compteur == 30:
#         etiquette3.pack()

def incrementer_button():
    while compteur:
        compteur.set(compteur.get() + 1)

        break


# Placement compteur dans la fenêtre
label_compteur.pack()

increment_button = tk.Button(root, text="Incrémenter", command=incrementer_button)
increment_button.pack()

quit_button = tk.Button(root, text="Quitter", command=quit_button_click)
quit_button.pack(side="bottom")

root.mainloop()



