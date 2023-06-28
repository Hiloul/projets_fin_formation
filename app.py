# Le projet consiste en la création d'une application web pour afficher une recette 
# 1. Le framework Flask pour gérer les requêtes HTTP et générer des réponses HTML.
# 2. L'application contient une seule route, définie pour l'URL racine "/". 
# 3. Accèder à cette URL, la fonction de vue "index()" est exécutée. Cette 
# 4. Elle prépare les info sur la recette (titre, liste ingrédients et instructions).
# 5. Vue utilise "render_template" pour générer une réponse HTML "recette.html". 
# 6. Titre, ingredients et instructions passées au template: affichées dynamiquement.
# 7. L'application est exécutée lorsque le fichier est exécuté directement, grâce à la 
# condition "if name == 'main':". Cela permet de lancer le serveur Flask et de rendre 
# l'application accessible via un navigateur web.
# En résumé, ce projet permet de créer une application web simple pour afficher 
# une recette de cuisine à partir d'un template HTML.
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Info recette
    titre = "Recette de l'omelette (encore)"
    ingredients = [
        "2 œufs", 
        "5g de beurre", 
        "15cl de lait", 
        "2 pincées de sel", 
        "2 pincées de poivre"]
    instructions = "1. Casser et mélangez les œufs dans un bol. \n2. Mélanger avec lait. \n3. Ajouter le sel et le poivre. \n4. Mettre le beurre dans une poele chaude. \n5. Verser le mélange et cuire pendant 2 minutes de chaques cotés. \n6. Et ne vous éttoufez pas :)"

    return render_template("/projet_fin_formation_Ramata_Hilel/recette.html", titre=titre, ingredients=ingredients, instructions=instructions)


if __name__ == "__main__":
    app.run()
