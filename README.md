# Fonctionnement_Github

Ce repository permet de tester les différentes fonctionnalités de GitHub lors de la gestion de version. On va créer une API REST simple pour pouvoir tester toutes ces options, telles que les commits, pull requests, etc...

1. Nous avons créé une branche de fonctionnalité appelée `dev`.
2. Nous allons apporter des modifications sur cette branche.
3. Nous commettons les changements localement avec des messages de commit clairs et descriptifs.
4. Nous poussons la branche `dev` vers le dépôt distant sur GitHub.
5. Nous créons une pull request pour demander la fusion des modifications de la branche `dev` dans la branche principale `master`.
6. Nous révisons la pull request, discutons des modifications et apportons des ajustements si nécessaire.
7. Une fois la pull request approuvée, nous fusionnons la branche `dev` avec la branche principale `master`.
8. Nous mettons à jour notre branche locale `master` avec les changements fusionnés depuis le dépôt distant.
9. Nous supprimons la branche `dev` à la fois localement et sur GitHub si elle n'est plus nécessaire.

## Grandes fonctionnalités GitHub en collaboration et gestion de version

### Commit
Un commit est une sauvegarde de l'état actuel du projet. Chaque commit enregistre les modifications apportées aux fichiers et ajoute un message décrivant ces modifications. Cela permet de suivre l'historique des changements et de revenir à une version précédente si nécessaire.

### Branche (Branch)
Une branche est une version parallèle du projet sur laquelle on peut travailler sans affecter la branche principale (souvent appelée `master` ou `main`). On utilise les branches pour développer de nouvelles fonctionnalités ou corriger des bugs de manière isolée. Une fois les changements terminés, on peut fusionner la branche avec la branche principale.

### Pull Request (PR)
Une pull request est une demande pour fusionner les changements d'une branche dans une autre branche (souvent la branche principale). Les pull requests permettent de revoir et de discuter des modifications avant de les intégrer au projet. Elles facilitent la collaboration en assurant que les modifications sont examinées et approuvées avant d'être fusionnées.

### Gitignore
Le fichier `.gitignore` est utilisé pour spécifier quels fichiers et répertoires Git doit ignorer. Cela inclut généralement les fichiers temporaires, les fichiers de configuration locaux et les fichiers générés automatiquement qui ne doivent pas être suivis par le contrôle de version.

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

## Vue d'ensemble de FastAPI
FastAPI est un framework web moderne asynchrone et rapide (haute performance) pour créer des API avec le language de prog Python. Il est conçu pour être facile à utiliser et très performant, ce qui en fait un choix populaire pour créer des API RESTful.

## Installation de FastAPI
Pour commencer avec FastAPI, on doit d'abord l'installer en utilisant pip :

```pip install fastapi```

On aura également besoin d'un serveur ASGI, comme Uvicorn, pour servir l'application FastAPI :

```pip install uvicorn```

## Création de la première application FastAPI
Créons une simple application FastAPI qui répond aux requêtes HTTP GET avec une charge utile JSON. Créons un nouveau fichier appelé ```main.py``` et ajoutons le code suivant :
```sh
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}
```
Pour exécuter cette application, utilisons Uvicorn depuis la ligne de commande :
```uvicorn main:app --reload```
Visitons ```http://localhost:8000``` dans le navigateur web, et on devrait voir la réponse JSON ```{"message": "Hello, World"}.```

## Gestion des paramètres de chemin
FastAPI permet de définir des paramètres de chemin dans les endpoints. Modifions l'exemple précédent pour accepter un paramètre de chemin pour l'ID d'un utilisateur :
```sh
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
```

Maintenant, lorsque nous visitons ```http://localhost:8000/users/123``` , nous recevons la réponse ```{"user_id": 123}```.

## Réception de données JSON dans les requêtes
FastAPI s'intègre parfaitement avec Pydantic pour gérer les données JSON dans les requêtes. Modifions l'exemple pour accepter une requête POST avec une charge utile JSON :
```sh
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
@app.post("/items/")
async def create_item(item: Item):
    return item
```

Lorsque nous envoyons une requête POST à ```http://127.0.0.1:8000/items/``` avec une charge utile JSON comme ```{"name": "item1", "description": "This is item 1"}```, nous recevons la même charge utile JSON en réponse.

## Conclusion
Dans ce tutoriel, nous avons couvert les bases de la création d'API RESTful avec FastAPI en Python. Nous avons appris à installer FastAPI, créer des points de terminaison d'API Rest asynchrone, gérer les paramètres de chemin et recevoir des données JSON dans les requêtes. La performance et la facilité d'utilisation de FastAPI en font un choix convaincant pour créer des API web modernes avec Python.



# Commandes Git Importantes

## Initialisation d'un Référentiel Local
Initialise un nouveau référentiel Git dans le répertoire courant

```git init```

## Ajout et Commit des Modifications
Ajoute tous le contenu(fichier,dossiers) du repertoire
```git add .```

Ajoute uniquement f1, f2 et f3

```git add f1 f2 f3```

### Ajoute tous les fichiers modifiés et nouveaux au suivi de Git
Crée un commit avec un message décrivant les modifications(ajout, maj, suppression)
un message clair, descriptif de l'action a faire est toujours important

```git commit -m "Message de commit"```

## Configuration du Référentiel Distant
La commande suivante ajoute une remote appelée origin qui pointe vers l'URL du dépôt GitHub, en utilisant le protocole HTTPS, moins securiser et a chaque fois il faut
preciser le nom d'utilisateur et le token

```git remote add origin https://github.com/nom-utilisateur/nom-repository.git```

La suivante ajoute aussi une remote origin, mais l’URL utilise le protocole SSH, Plus sécurisé.
Avant de pouvoir utiliser cette méthode, on doit avoir généré une paire de clés SSH (publique et privée) sur l'ordinateur en local et ajouté la clé publique au compte GitHub.
voici une page qui explique de maniere detaillee https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

```git remote add origin git@github.com:AhmedAbdoulahi/Fonctionnement_Github.git```

NB : Ajoute egalement un référentiel distant nommé ```origin``` que nous pourrons changer, par exemple on peut l'appeler ```origin1```

## Pousser les Modifications Locales vers le Référentiel Distant
Pousse les modifications de la branche locale vers la branche ```main``` du référentiel distant, il peut s'agir de ```master``` ou un autre branch

```git push -u origin main``` ou ```git push -u origin master```  ou ```git push -u origin autre-branch``` 


## Tirer les Modifications du Référentiel Distant
Récupère les modifications de la branche ```main``` du référentiel distant et les fusionne avec la branche locale, valable pour master et autres

```git pull origin main```

## Utilisation des Branches

### Créer et Changer de Branche
sur toute la suite notre branche s'appelle ```dev```
Avant de créer une branche avec la cmd ```git branch dev```, il faut s'assurer que cette branche n'existe pas déjà sur GitHub. 
En effet, si la branche dev existe déjà, on risque de provoquer des conflits ou d'écraser des modifications déjà présentes si on crée et pousse une nouvelle branche portant le même nom. 
Pour éviter cela, on peut d'abord récupérer la liste des branches distantes avec la cmd ```git fetch origin``` et vérifier avec la cmd ```git branch -r``` si la branche dev est déjà présente. 
Si elle existe, il suffit de se placer dessus en utilisant la cmd ```git checkout dev```, ce qui permet de récupérer et de travailler directement sur cette branche sans la recréer. 
En revanche, si la branche n'existe pas, on peut alors la créer localement avec la cmd ```git branch dev```, basculer dessus avec la cmd ```git checkout dev```, puis la pousser sur GitHub en exécutant la cmd ```git push -u origin dev```. Cette dernière commande lie la branche locale à la branche distante, facilitant les futures interactions(push,pull). `

### Fusionner une Branche
La fusion d'une branche intervient lorsqu'on souhaite intégrer les modifications d'une branche de développementpar exemple ```dev``` dans une branche principale ```master```. 
Par exemple, après avoir travaillé sur de nouvelles fonctionnalités ou corrections de bugs dans la branche ```dev```, on voudra à un moment les fusionner avec la branche ```master``` pour les intégrer à la version principale. 
Pour cela, on commence par se placer sur la branche ```master``` avec la cmd ```git checkout master```, ce qui fait en sorte que la branche master devienne la branche active. 
Ensuite, on utilise la cmd ```git merge dev``` pour fusionner les changements réalisés dans ```dev``` dans la branche ```master```. Ce processus est utile lorsque le développement sur une branche secondaire est terminé et qu'on est prêt à l'intégrer dans la branche principale.


## Pull Requests et Collaboration

### Tirer avec Git

La commande `git pull` est utilisée pour récupérer les dernières modifications d'une branche du dépôt distant GitHub et les intégrer dans la branche locale. Cela  permet de mettre à jour le code avec les modifications faites par d'autres développeurs avant de continuer le taf.

Il existe deux manières principales de tirer des modifications :

1. **Fusionner directement** :
   ```
   git pull origin dev
   ```
   Cette commande récupère les modifications de la branche `dev` du dépôt distant et les fusionne directement dans la branche locale. Si des modifications ont été faites à la fois localement et sur la branche distante, cela peut créer un "commit de fusion" pour combiner les changements.

2. **Tirer avec Rebase** :
   ```
   git pull origin dev --rebase
   ```
   Cette commande récupère les modifications de la branche `dev` du dépôt distant et les applique au-dessus des commits locaux. Cela évite les commits de fusion et garde un historique plus linéaire, ce qui peut rendre l'historique des changements plus clair.

### Résoudre les Conflits de Fusion

Lorsque qu'on fais un `git pull` avec rebase ou fusion, il peut arriver que des conflits apparaissent si les mêmes parties du code ont été modifiées à la fois localement et sur le dépôt distant. Voici comment résoudre ces conflits :

1. **Ajouter les fichiers résolus** :
   ```
   git add <fichiers_resolus>
   ```
   Après avoir résolu les conflits dans les fichiers, on dois les ajouter à l'index avec cette commande pour marquer les conflits comme résolus.

2. **Continuer le Rebase** :
   ```
   git rebase --continue
   ```
   Si on utilise `git pull` avec `--rebase` et que des conflits sont survenus, après les avoir résolus et ajoutés, on dois continuer le processus de rebase avec cette commande.

Ces étapes permettent de gérer les conflits de manière ordonnée et de maintenir un historique clair des modifications.


## Voir ce qui est Local et qui n'est pas Poussé

```
git status
```
Affiche le statut des fichiers dans le répertoire de travail et l'index. On peut voir les fichiers modifiés, ajoutés ou supprimés qui sont prêts à être commités ou qui nécessitent encore des actions.

```
git log origin/main..HEAD
```
Affiche les commits locaux qui n'ont pas encore été poussés vers le référentiel distant. Cela permet de voir les changements locaux qui ne sont pas encore disponibles pour les autres développeurs.

## Différence entre les Référentiels Local et Distant

### Référentiel Local
Le référentiel local est la copie du projet qui réside sur notre machine. Toutes les modifications que l'on fait se trouvent dans ce référentiel avant d'être poussées vers le référentiel distant. Cela inclut les commits, les branches locales et les modifications non encore committées.

### Référentiel Distant
Le référentiel distant est une copie du projet hébergée sur une plateforme en ligne comme GitHub. Il permet de collaborer avec d'autres développeurs en partageant les modifications et en suivant l'historique du projet. Les modifications doivent être poussées vers ce référentiel pour être accessibles aux autres contributeurs.

# Autres Commandes Utiles

## Statut du Référentiel
```
git status
```
Affiche le statut des fichiers dans le répertoire de travail et l'index. C'est utile pour voir les fichiers modifiés, ajoutés ou supprimés avant de les ajouter à l'index ou de les committer.

## Log des Commits
```
git log
```
Affiche l'historique des commits. On peut voir les messages de commit, les identifiants de commit et les changements apportés au fil du temps.

## Cloner un Référentiel
```
git clone https://github.com/nom-utilisateur/nom-repository.git
```
Clone un référentiel distant dans un répertoire local. Cela crée une copie complète du projet pour travailler en local.

## Ignorer des Fichiers avec .gitignore
Crée un fichier `.gitignore` pour spécifier les fichiers et répertoires que Git doit ignorer. Cela inclut généralement les fichiers temporaires, les fichiers de configuration locaux, et les fichiers générés automatiquement.

Exemple de fichier `.gitignore` :

```
# Ignorer les fichiers de configuration locaux
config.py

# Ignorer les fichiers d'IDE, par exemple vscode
.vscode/

# Ignorer les fichiers temporaires
*.log
*.tmp

# Ignorer les répertoires générés
/dist
/build
```

Ces commandes couvrent les aspects essentiels de l'utilisation de Git pour la gestion de version et la collaboration. Elles permettent de suivre les modifications, de collaborer avec d'autres développeurs, et de gérer les branches et les conflits.

# Exemple Pratique

## Initialiser un nouveau projet
```
git init
```

## Ajouter un fichier README.md et le committer
```
echo "# Mon Projet" > README.md
git add README.md
git commit -m "Ajout du fichier README.md"
```

## Configurer le référentiel distant et pousser les modifications
```
git remote add origin https://github.com/ton-utilisateur/ton-repository.git
git push -u origin main
```
## Créer une nouvelle branche pour une fonctionnalité

Pour créer une nouvelle branche et y passer directement, on utilise la commande suivante :

```
git checkout -b fonctionnalite
```

Cette commande crée une nouvelle branche appelée `fonctionnalite` et change immédiatement le contexte de travail vers cette branche. Cela permet de commencer à travailler sur de nouvelles fonctionnalités sans affecter la branche principale `master` par exemple.

**NB :** Avant d'utiliser `git checkout -b`, il est essentiel de s'assurer que la branche `fonctionnalite` n'existe pas déjà. Si la branche existe déjà, la commande échouera et affichera une erreur. On peut vérifier l'existence des branches locales avec :

```
git branch
```

Si la branche existe déjà et qu'on souhaite simplement y passer, on utilise plutôt :

```
git checkout fonctionnalite
```

Cette commande change le contexte de travail vers la branche existante `fonctionnalite` sans la recréer.


## Apporter des modifications et les committer
```
echo "print('Hello, world!')" > hello.py
git add hello.py
git commit -m "Ajout du script hello.py"
```

## Pousser la branche de fonctionnalité vers le référentiel distant
```
git push -u origin fonctionnalite
```

## Créer une pull request sur GitHub pour fusionner la branche fonctionnalite dans main

### Tirer les dernières modifications de main
```
git checkout main
git pull origin main
```

### Fusionner la branche fonctionnalite dans main après avoir approuvé la pull request
```
git merge fonctionnalite
```

### Pousser les modifications fusionnées vers le référentiel distant
```
git push origin main
```

### Supprimer la branche de fonctionnalité locale
```
git branch -d fonctionnalite
```

### Supprimer la branche de fonctionnalité distante
```
git push origin --delete fonctionnalite
```
