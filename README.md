# Fonctionnement_Github
Ce repository permet de tester les differentes fonctionnalites de github lors d'une gestion de version. 
on va faire un API-REST simple pour pouvoir tester toutes ces options a savoir commit, gitignore, pullrequest etc....

1.on a créé une branche de fonctionnalité dev

on essaie de changer qqch puis faisons un pullrequest


## Grandes fonctionnalités GitHub en collaboration et gestion de version

### Commit
Un commit est une sauvegarde de l'état actuel du projet. Chaque commit enregistre les modifications apportées aux fichiers et ajoute un message décrivant ces modifications. Cela permet de suivre l'historique des changements et de revenir à une version précédente si nécessaire.

### Branche (Branch)
Une branche est une version parallèle du projet sur laquelle on peut travailler sans affecter la branche principale (souvent appelée master ou main). On utilise les branches pour développer de nouvelles fonctionnalités ou corriger des bugs de manière isolée. Une fois les changements terminés, on peut fusionner la branche avec la branche principale.

### Pull Request (PR)
Une pull request est une demande pour fusionner les changements d'une branche dans une autre branche (souvent la branche principale). Les pull requests permettent de revoir et de discuter des modifications avant de les intégrer au projet. Elles facilitent la collaboration en assurant que les modifications sont examinées et approuvées avant d'être fusionnées.

### Gitignore
Le fichier .gitignore est utilisé pour spécifier quels fichiers et répertoires Git doit ignorer. Cela inclut généralement les fichiers temporaires, les fichiers de configuration locaux et les fichiers générés automatiquement qui ne doivent pas être suivis par le contrôle de version.

### Merge
La fusion (merge) est le processus de combinaison des changements d'une branche dans une autre branche. Après avoir terminé le développement sur une branche de fonctionnalité, on peut fusionner cette branche dans la branche principale pour intégrer les nouvelles fonctionnalités ou corrections de bugs.

### Fork
Un fork est une copie personnelle d'un repository qui se trouve sur son propre compte GitHub. Les forks permettent de contribuer à des projets open source en copiant le repository, en apportant des modifications et en envoyant une pull request pour intégrer ces modifications dans le repository d'origine.

### Clone
Cloner un repository signifie créer une copie locale de ce repository sur son ordinateur. Cela permet de travailler sur le projet localement et de synchroniser les modifications avec le repository distant sur GitHub.

### Commit Message
Un message de commit est une courte description des modifications apportées dans ce commit. Des messages de commit clairs et descriptifs facilitent la compréhension de l'historique des modifications et la collaboration entre les membres de l'équipe.

En résumé, GitHub offre des outils puissants pour la gestion de version et la collaboration. Les commits, branches, pull requests et autres fonctionnalités permettent de gérer efficacement le développement de projets, de suivre les modifications et de collaborer avec d'autres développeurs.

# pratique

# Vue d'ensemble de FastAPI
FastAPI est un framework web moderne et rapide (haute performance) pour créer des API avec Python 3.7+ basé sur les hints de type standard de Python. Il est conçu pour être facile à utiliser et très performant, ce qui en fait un choix populaire pour créer des API RESTful.

## Installation de FastAPI
Pour commencer avec FastAPI, on doit d'abord l'installer en utilisant pip :
pip install fastapi
On aura également besoin d'un serveur ASGI, comme Uvicorn, pour servir l'application FastAPI :
pip install uvicorn

## Création de la première application FastAPI
Créons une simple application FastAPI qui répond aux requêtes HTTP GET avec une charge utile JSON. Créons un nouveau fichier appelé main.py et ajoutons le code suivant :
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

Pour exécuter cette application, utilisons Uvicorn depuis la ligne de commande :
uvicorn main:app --reload
Visitons http://127.0.0.1:8000 dans le navigateur web, et on devrait voir la réponse JSON {"message": "Hello, World"}.

## Gestion des paramètres de chemin
FastAPI permet de définir des paramètres de chemin dans les routes API. Modifions l'exemple précédent pour accepter un paramètre de chemin pour l'ID d'un utilisateur :
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
Maintenant, lorsque nous visitons http://127.0.0.1:8000/users/123, nous recevons la réponse {"user_id": 123}.

## Réception de données JSON dans les requêtes
FastAPI s'intègre parfaitement avec Pydantic pour gérer les données JSON dans les requêtes. Modifions l'exemple pour accepter une requête POST avec une charge utile JSON :
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
@app.post("/items/")
async def create_item(item: Item):
    return item
Lorsque nous envoyons une requête POST à http://127.0.0.1:8000/items/ avec une charge utile JSON comme {"name": "item1", "description": "This is item 1"}, nous recevons la même charge utile JSON en réponse.

## Conclusion
Dans ce tutoriel, nous avons couvert les bases de la création d'API RESTful avec FastAPI en Python. Nous avons appris à installer FastAPI, créer des points de terminaison d'API, gérer les paramètres de chemin et recevoir des données JSON dans les requêtes. La performance et la facilité d'utilisation de FastAPI en font un choix convaincant pour créer des API web modernes avec Python.


