# Le projet consiste à développer une application de chiffrement de messages en 
# utilisant un décalage alphabétique. Voici les principales caractéristiques du projet :
# L'application permet de saisir un message texte.
# Le message texte est ensuite codé en remplaçant chaque lettre alphabétique 
# par une autre lettre décalée dans l'alphabet.
# Le décalage est spécifié par l'utilisateur.
# Les lettres minuscules et majuscules sont traitées séparément.
# Les caractères non alphabétiques restent inchangés dans le message codé.
# Le message codé est affiché à l'utilisateur.
# Pour réaliser ce projet, une fonction generer_code(message, decalage) est utilisée. 
# Cette fonction prend en paramètres le message à coder et le décalage à appliquer. 
# Elle itère sur chaque lettre du message et effectue les opérations suivantes :
# Vérifie si la lettre est alphabétique.
# Si la lettre est en minuscule, calcule le code de la lettre en utilisant 
# l'ordre Unicode des lettres minuscules de 'a' à 'z'.
# Si la lettre est en majuscule, calcule le code de la lettre en utilisant 
# l'ordre Unicode des lettres majuscules de 'A' à 'Z'.
# Ajoute la lettre codée au message codé.
# Si la lettre n'est pas alphabétique, l'ajoute telle quelle au message codé.
# À la fin de la fonction, le message codé est retourné.
# Dans ce projet un message original est défini, un décalage de 3 est spécifié, 
# puis la fonction generer_code() est appelée avec ces valeurs. Le message original 
# et le message codé sont ensuite affichés à l'aide de la fonction print().

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

# Définition du message original et du décalage
message_original = input("alors?")
decalage = 3

message_code = generer_code(message_original, decalage)

print("Message original :", message_original)
print("Message codé     :", message_code)
