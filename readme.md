# SoftDesk Support API
## Description
SoftDesk Support est une API construite avec Django et Django Rest Framework pour la gestion de projets, de contributeurs, de problèmes (issues) et de commentaires dans un environnement de support technique.

## Prérequis
* Python 3.11+
* Pipenv pour la gestion des environnements virtuels
* Django 5.1.1
* Django Rest Framework 3.15.2
* JWT pour l'authentification
* Drf-yasg (Redoc / Swagger)

Les dépendances du projet se trouvent dans le fichier requirements.txt et peuvent être installées avec :

```
pipenv install
```
Dépendances principales :

* Django Rest Framework
* Simple JWT pour l'authentification
* Ruff pour le linting

## Installation
1. Clonez ce dépôt

```
git clone https://github.com/dogmatus07/SoftDesk.git
```

2. Accédez au répertoire du projet

```
cd softdesk
```

3. Activez l'environnement virtuel avec Pipenv

```
pipenv shell
```

4. Installez les dépendances du projet

```
pipenv install
```

5. Configurez la base de données et effectuez les migrations

```
python manage.py makemigrations
python manage.py migrate
```

6. Créez un super utilisateur pour accéder à l'admin Django

```
python manage.py createsuperuser
```

7. Lancez le serveur local

```
python manage.py runserver
```

## Modèles de données

### Custom User
Le modèle CustomUser étend le modèle d'utilisateur par défaut de Django avec des champs supplémentaires tels que l'âge, le consentement et les préférences de communication.

### Project
Représente un projet avec un titre, une description, un type (back-end, front-end, iOS, Android), et l'auteur du projet.

### Contributor
Permet de gérer les contributeurs à un projet, chaque utilisateur ne pouvant contribuer qu'à un seul projet à la fois.

### Issue
Le modèle Issue représente un problème lié à un projet, avec des priorités (basse, moyenne, haute), des étiquettes (bug, fonctionnalité, tâche), et un statut (à faire, en cours, terminé).

### Comment
Le modèle Comment permet aux utilisateurs de commenter des problèmes spécifiques.

## Points de terminaison (API Endpoints)
Voici un résumé des principaux points de terminaison de l'API :

* /projects/ : Liste des projets et création de nouveaux projets.
* /projects/{id}/ : Détails, mise à jour ou suppression d'un projet.
* /projects/{project_id}/issues/ : Liste et création de problèmes pour un projet spécifique.
* /issues/{id}/ : Détails, mise à jour ou suppression d'un problème.
* /comments/ : Liste et création de commentaires.
* /comments/{id}/ : Détails, mise à jour ou suppression d'un commentaire.

**Les points de terminaison nécessitent une authentification via JWT.**

## Script de population des données
Le script populate_data.py permet de remplir la base de données avec des données de test, comme des utilisateurs, des projets, des contributeurs, des problèmes et des commentaires.

Se rendre dans api > scripts

```
cd api/scripts
```

Exécutez le script avec :

```
python populate_data.py
```