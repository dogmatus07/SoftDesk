# SoftDesk Support API
## Description
SoftDesk Support est une API construite avec Django et Django Rest Framework pour la gestion de projets, de contributeurs, de problèmes (issues) et de commentaires dans un environnement de support technique.

## Prérequis
* Python 3.12
* Pipenv pour la gestion des environnements virtuels
* Django 5.1.1
* Django Rest Framework 3.15.2
* JWT pour l'authentification
* Drf-yasg (Redoc / Swagger)

Les dépendances du projet se trouvent dans le fichier requirements.txt.

Dépendances principales :

* Django Rest Framework
* Simple JWT pour l'authentification
* Ruff pour le linting

### Modèles de données

#### Custom User
Le modèle CustomUser étend le modèle d'utilisateur par défaut de Django avec des champs supplémentaires tels que l'âge, le consentement et les préférences de communication.

#### Project
Représente un projet avec un titre, une description, un type (back-end, front-end, iOS, Android), et l'auteur du projet.

#### Contributor
Permet de gérer les contributeurs à un projet, chaque utilisateur ne pouvant contribuer qu'à un seul projet à la fois.

#### Issue
Le modèle Issue représente un problème lié à un projet, avec des priorités (basse, moyenne, haute), des étiquettes (bug, fonctionnalité, tâche), et un statut (à faire, en cours, terminé).

#### Comment
Le modèle Comment permet aux utilisateurs de commenter des problèmes spécifiques.

### Points de terminaison (API Endpoints)
Voici un résumé des principaux points de terminaison de l'API :

* /projects/ : Liste des projets et création de nouveaux projets.
* /projects/{id}/ : Détails, mise à jour ou suppression d'un projet.
* /projects/{project_id}/issues/ : Liste et création de problèmes pour un projet spécifique.
* /issues/{id}/ : Détails, mise à jour ou suppression d'un problème.
* /comments/ : Liste et création de commentaires.
* /comments/{id}/ : Détails, mise à jour ou suppression d'un commentaire.
* /swagger/ : Documentation API, permet de tester les différents endpoints et d'effectuer des opérations CRUD

**Les points de terminaison nécessitent une authentification via JWT.**

## Etapes d'installation et de configuration
1. Clonez le dépôt Git

```
git clone https://github.com/dogmatus07/SoftDesk.git
```

2. Accédez au répertoire du projet

```
cd SoftDesk
```

3. Créez un nouvel environnement virtuel

```
python3.12 -m venv env
```

4. Activez l'environnement virtuel

```
source env/bin/activate
```

5. Installez pipenv

```
apt install pipenv
```

6. Installez les dépendances
Utilisez pipenv pour installer les packages requis depuis le fichier requirements.txt

```
pipenv install
pip install -r requirements.txt
```

7. Installez setuptools (si nécessaire)
Si nécessaire, installez setuptools pour éviter les erreurs de dépendance

```
pip install setuptools
```

8. Effectuez les migrations
Exécuter les commandes suivantes pour appliquer les migrations de la base de données : 

```
python manage.py makemigrations
python manage.py migrate
```

9. Créez un super utilisateur
Définissez un compte administrateur pour accéder à l'interface d'administration : 

```
python manage.py createsuperuser
```

10. Configurez ALLOWED_HOSTS dans settings.py (si nécessaire)
Si vous accédez au projet depuis un hôte externe, ajoutez-le dans la configuration

```
cd softdesk
nano settings.py
```

Dans settings.py, modifiez la partie ALLOWED_HOSTS

```
ALLOWED_HOSTS = ['*']
```

Sauvegardez puis retourner au répertoire principal

```
cd ..
```

11. Peuplez la base de données

Toujours dans le répertoire du projet, exécutez le script de peuplement pour avoir des données initiales : 

```
python manage.py runscript api.scripts.populate_data
```

12. Lancez et testez le serveur

```
python manage.py runserver

ou 

python manage.py runserver votre_serveur_externe:8000
```

13. Accédez à la documentation Swagger
Rendez-vous sur Swagger pour interagir avec l'API

```
http://votre_serveur:8000/swagger/
```

## Test des ENDPOINTS
14. Authentification avec Token
Pour obtenir un token d'accès et de rafraîchissement, connectez-vous avec les identifiants de démo :

- Utilisateur : userX (où X est le numéro de l'utilisateur, ex. user1)
- Mot de passe : DevSoftD3sk)

### Instructions
Dans Swagger : 
- Accédez à la section Token.
- Cliquez sur Try it out et saisissez les identifiants.
- Récupérez le token d'accès.

Autorisation : 
- En haut de Swagger, cliquez sur Authorize.
- Dans la boîte de dialogue, entrez : Bearer <votre_token> (sans les chevrons).
- Cliquez sur Authorize puis Close.

Vous êtes maintenant prêt à tester les différents endpoints de l’API.



