# Importation de la classe FastAPI depuis le module fastapi
from fastapi import FastAPI

# Création d'une instance de l'application FastAPI
app = FastAPI()

# Définition d'une route GET pour la racine ("/")
# La fonction est asynchrone (async) ce qui permet de gérer les requêtes de manière non bloquante
@app.get("/")
async def read_root():
    # Retourne un message JSON
    return {"message": "Hello, World"}

# Définition d'une route GET avec un paramètre de chemin (user_id)
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    # Retourne un JSON avec l'ID de l'utilisateur
    return {"user_id": user_id}

# FastAPI s'intègre parfaitement avec Pydantic pour gérer les données JSON dans les requêtes.
# Modifions notre exemple pour accepter une requête POST avec une charge utile JSON :

# Importation de BaseModel depuis Pydantic pour la validation des données
from pydantic import BaseModel

# Définition d'un modèle de données avec Pydantic
class Item(BaseModel):
    name: str  # Le nom de l'item, une chaîne de caractères
    description: str = None  # La description de l'item, optionnelle

# Définition d'une route POST pour créer un item
@app.post("/items/")
async def create_item(item: Item):
    # Retourne les données de l'item en JSON
    return item
