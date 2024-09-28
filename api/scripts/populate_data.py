import os
import django

# run the script independently
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SoftDesk.settings")
django.setup()

from django.contrib.auth import get_user_model
from api.models import Project, Contributor, Issue, Comment


User = get_user_model()


def run():
    """
    Function to populate the database with dummy data
    """
    # create users
    user1, created = User.objects.get_or_create(
        first_name = "Franck",
        last_name = "Kouassi",
        username = "user1",
        password = "DevSoftD3sk)",
        age=26, consent = True,
        can_be_contacted = True,
        can_data_be_shared = True
        )

    user2, created = User.objects.get_or_create(
        first_name = "Sylvie",
        last_name = "Mehdi",
        username = "user2",
        password = "DevSoftD3sk)",
        age = 18, consent = True,
        can_be_contacted = True,
        can_data_be_shared = True
    )

    user3, created = User.objects.get_or_create(
        first_name = "Antoine",
        last_name = "Thibault",
        username = "user3",
        password = "DevSoftD3sk)",
        age = 13, consent = True,
        can_be_contacted = True,
        can_data_be_shared = True
    )

    user4, created = User.objects.get_or_create(
        first_name = "Olivier",
        last_name = "Gérard",
        username = "user4",
        password = "DevSoftD3sk)",
        age = 32, consent = True,
        can_be_contacted = True,
        can_data_be_shared = True
    )

    user5, created = User.objects.get_or_create(
        first_name = "Stéphane",
        last_name = "Schmitt",
        username = "user5",
        password = "DevSoftD3sk)",
        age = 41, consent = True,
        can_be_contacted = True,
        can_data_be_shared = True
    )

    # create projects
    project1 = Project.objects.create(
        title = "Projet Libra",
        description = "Projet de gestion de bibliothèque",
        type = "BACK_END",
        author_user = user1
    )

    project2 = Project.objects.create(
        title = "Projet E-commerce",
        description = "Projet de vente en ligne",
        type = "FRONT_END",
        author_user = user2
    )

    project3 = Project.objects.create(
        title = "Projet de gestion de stock",
        description = "Projet de gestion de stock",
        type = "IOS",
        author_user = user3
    )

    project4 = Project.objects.create(
        title = "Projet d'application mobile",
        description = "Application mobile de Fitness",
        type = "ANDROID",
        author_user = user4
    )

    project5 = Project.objects.create(
        title = "Projet de conception web",
        description = "Conception du site artisan paysager",
        type = "BACK_END",
        author_user = user5
    )

    # create contributors
    Contributor.objects.create(
        project = project1,
        user = user1,
        role = "Author"
    )
    Contributor.objects.create(
        project = project2,
        user = user2,
        role = "Author"
    )
    Contributor.objects.create(
        project = project3,
        user = user3,
        role = "Author"
    )
    Contributor.objects.create(
        project = project4,
        user = user4,
        role = "Author"
    )
    Contributor.objects.create(
        project = project5,
        user = user5,
        role = "Author"
    )
    
    # create issues
    issue1 = Issue.objects.create(
        title = "Problème de connexion",
        description = "Impossible de se connecter à l'application",
        priority = "HIGH",
        tag = "BUG",
        status = "TO_DO",
        project = project1,
        assignee = user1,
        author_user = user1

    )

    issue2 = Issue.objects.create(
        title = "Problème de paiement",
        description = "Impossible de payer en ligne",
        priority = "MEDIUM",
        tag = "BUG",
        status = "IN_PROGRESS",
        project = project2,
        assignee = user2,
        author_user = user2
    )

    issue3 = Issue.objects.create(
        title = "Problème de stock",
        description = "Le stock est vide",
        priority = "HIGH",
        tag = "BUG",
        status = "TO_DO",
        project = project3,
        assignee = user3,
        author_user = user3
    )

    issue4 = Issue.objects.create(
        title = "Problème d'authentification",
        description = "Impossible de s'authentifier à l'application",
        priority = "HIGH",
        tag = "BUG",
        status = "TO_DO",
        project = project4,
        assignee = user4,
        author_user = user4
    )

    issue5 = Issue.objects.create(
        title = "Problème de design au niveau du header",
        description = "Le design du header est à revoir",
        priority = "MEDIUM",
        tag = "BUG",
        status = "IN_PROGRESS",
        project = project5,
        assignee = user5,
        author_user = user5
    )

    # create comments
    Comment.objects.create(
        description = "Le problème est résolu",
        issue = issue1,
        author_user = user1
    )

    Comment.objects.create(
        description = "Le problème est en cours de résolution",
        issue = issue2,
        author_user = user2
    )

    Comment.objects.create(
        description = "Ajout de stock effectué",
        issue = issue3,
        author_user = user3
    )

    Comment.objects.create(
        description = "La connexion est résolue",
        issue = issue4,
        author_user = user4
    )

    Comment.objects.create(
        description = "Le design du header est en cours de modification",
        issue = issue5,
        author_user = user5
    )

    print("Database populated successfully")