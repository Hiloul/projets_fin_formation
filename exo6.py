# Projet : Application de codage de messages
# 1. Saisie du message : L'utilisateur peut saisir le message qu'il souhaite coder.
# 2. Saisie du décalage : L'utilisateur peut spécifier le décalage souhaité pour 
# ++ Le décalage détermine le nombre de positions à déplacer pour obtenir version codée.
# 3. Codage du message : Le programme utilise la fonction "generer_code"
# 4. Affichage du résultat : Le programme affiche à l'utilisateur le message 
# original ainsi que le message codé correspondant.
# 5. Après chaque codage, le programme demande s'il souhaite coder une autre phrase. 
# Si la réponse est "Non", le programme se termine, 
# sinon, il redemande de saisir une nouvelle phrase.
# 6. Sortie de l'application : Une fois que l'utilisateur a terminé de coder les 
# phrases et a répondu "Non" à la demande de codage supplémentaire, le programme 
# affiche un message de remerciement et se termine.
def generer_code(message, decalage):
    message_code = ""
    for lettre in message:
        if lettre.isalpha():
            if lettre.islower():
                code = ord(lettre) - ord('a')
                code_decale = (code + decalage) % 26
                lettre_code = chr(code_decale + ord('a'))
            else:
                code = ord(lettre) - ord('A')
                code_decale = (code + decalage) % 26
                lettre_code = chr(code_decale + ord('A'))
        else:
            lettre_code = lettre
        message_code += lettre_code
    return message_code

while True:
    # Tant que
    message_original = input("Veuillez entrer le message à coder: ")
    decalage = int(input("Combien de lettres de décalages voulez-vous ? "))
    
    message_code = generer_code(message_original, decalage)
    print("Message original :", message_original)
    print("Message codé     :", message_code)

    choix = input("Voulez-vous coder un autre message ? (Oui/Non) ")
    if choix.lower() != "oui":
        break