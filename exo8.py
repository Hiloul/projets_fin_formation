# Permettre à l'utilisateur de choisir d'autres méthodes de codage, en plus du décalage.
# Par exemple, nous pourrions choisir comme deuxième méthode, la méthode de substitution :
# 1. Saisissez le message à coder : Bonjour, comment ça va ?
# 2. Choisissez la méthode de codage (1: Décalage, 2: Substitution) : 2
# 3. Saisissez les substitutions (lettre:code), 'q' pour quitter : 
# a:t 
# b:o 
# c:p 
# d:q 
# q:z 
# r:x 
# s:y 
# t:m 
# u:n 
# v:r 
# w:s 
# x:u 
# y:v 
# z:w
# Résultat : Message original : Bonjour, comment ça va ? 
# Méthode de codage : Substitution Message codé : Tmnpurs, ynnpmu mè wu ?
# Haut du formulaire
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