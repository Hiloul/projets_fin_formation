# Ajouter des fonctionnalités de décodage pour décoder les messages codés
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

def decoder_msg(message, decalage):
    return generer_code(message, - decalage)

while True:
    # Tant que
    message_original = input("Veuillez entrer le message à coder: ")
    decalage = int(input("Combien de lettres de décalages voulez-vous ? "))
    message_code = generer_code(message_original, decalage)
    choix_action = input("Voulez-vous décoder (O) la phrase ? ")

    if choix_action.upper() == "O":
        message_decode = decoder_msg(message_code, decalage)
        print("Message original :", message_original)
        print("Message codé     :", message_code)
        print("Message décodé   :", message_decode)
    else:
        print("Message original :", message_original)
        print("Message codé     :", message_code)

    choix = input("Voulez-vous coder un autre message ? (Oui/Non) ")
    if choix.lower() != "oui":
        break
