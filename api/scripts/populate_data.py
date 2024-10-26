import os
import sys
import django
from django.contrib.auth import get_user_model
from api.models import Project, Contributor, Issue, Comment

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

# run the script independently
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "softdesk.settings")
django.setup()

User = get_user_model()


def run():
    """
    Function to populate the database with dummy data
    """
    # create users

    user_data = [
        ("Franck", "Kouassi", "user1", 26),
        ("Sylvie", "Mehdi", "user2", 18),
        ("Antoine", "Thibault", "user3", 13),
        ("Olivier", "Gérard", "user4", 32),
        ("Stéphane", "Schmitt", "user5", 41),
        ("Jean", "Dupont", "user6", 25),
        ("Marie", "Durand", "user7", 30),
        ("Paul", "Lefevre", "user8", 22),
        ("Sophie", "Lemoine", "user9", 19),
        ("Luc", "Martin", "user10", 28),
        ("Julie", "Michelet", "user11", 35),
        ("Pierre", "Descartes", "user12", 40),
        ("Marie", "Smith", "user13", 50),
        ("Albert", "Gérard", "user14", 60),
        ("Jeanne", "Muguet", "user15", 42),
        ("Stéphane", "Schmitt", "user16", 41),
        ("Steve", "Roberto", "user17", 38),
        ("Sylvie", "Mehdi", "user18", 18),
        ("Antoine", "Thibault", "user19", 24),
        ("Martin", "Weber", "user20", 32),
    ]

    for first_name, last_name, username, age in user_data:
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "consent": True,
                "can_be_contacted": True,
                "can_data_be_shared": True,
            },
        )

        if created:
            user.set_password("DevSoftD3sk)")
            user.save()

    # retrieve users
    user1 = User.objects.get(username="user1")
    user2 = User.objects.get(username="user2")
    user3 = User.objects.get(username="user3")
    user4 = User.objects.get(username="user4")
    user5 = User.objects.get(username="user5")
    user6 = User.objects.get(username="user6")
    user7 = User.objects.get(username="user7")
    user8 = User.objects.get(username="user8")
    user9 = User.objects.get(username="user9")
    user10 = User.objects.get(username="user10")
    user11 = User.objects.get(username="user11")
    user12 = User.objects.get(username="user12")
    user13 = User.objects.get(username="user13")
    user14 = User.objects.get(username="user14")
    user15 = User.objects.get(username="user15")
    user16 = User.objects.get(username="user16")
    user17 = User.objects.get(username="user17")
    user18 = User.objects.get(username="user18")
    user19 = User.objects.get(username="user19")
    user20 = User.objects.get(username="user20")

    # create projects

    project_data = [
        ("Projet Libra", "Projet de gestion de bibliothèque", "BACK_END", user1),
        ("Projet E-commerce", "Projet de vente en ligne", "FRONT_END", user2),
        ("Projet Stockify", "Projet de gestion de stock", "IOS", user3),
        ("Projet FitApp", "Application mobile de Fitness", "ANDROID", user4),
        ("Projet Artisan Paysager", "Conception du site Monjardin", "BACK_END", user5),
        ("Projet E-commerce", "Projet de vente en ligne", "FRONT_END", user6),
        (
            "Projet Electronique",
            "Projet de conception backend site électronique",
            "BACK_END",
            user7,
        ),
        (
            "Projet Site Web Corporate",
            "Création de site web pour une agence digitale",
            "FRONT_END",
            user8,
        ),
        (
            "Projet de gestion d'animalerie",
            "Projet de gestion de stock pour une animalerie",
            "IOS",
            user9,
        ),
        (
            "Projet d'application comptabilité",
            "Application mobile de comptabilité",
            "ANDROID",
            user10,
        ),
        (
            "Projet d'application mobile pour fleuriste",
            "Application mobile pour un fleuriste",
            "ANDROID",
            user11,
        ),
        (
            "Projet de rebranding site existant",
            "Rebranding d'un site existant",
            "FRONT_END",
            user12,
        ),
        (
            "Projet de gestion financière",
            "Projet de gestion financière pour un magasin",
            "BACK_END",
            user13,
        ),
        (
            "Projet d'application mobile pour un restaurant",
            "Application mobile pour un restaurant",
            "ANDROID",
            user14,
        ),
        (
            "Projet de conception de site web avec réservation",
            "Conception de site web avec réservation hôtel",
            "FRONT_END",
            user15,
        ),
        (
            "Projet de gestion d'actions en bourse",
            "Projet de gestion d'actions en bourse",
            "BACK_END",
            user16,
        ),
        (
            "Projet d'application IOS pour un transporteur",
            "Application IOS pour un transporteur",
            "IOS",
            user17,
        ),
        (
            "Projet d'amélioration site web restaurateur",
            "Amélioration site web restaurateur",
            "FRONT_END",
            user18,
        ),
        (
            "Projet de gestion de stock pour une pharmacie",
            "Projet de gestion de stock pour une pharmacie",
            "IOS",
            user19,
        ),
        (
            "Projet de conception de site web pour un hôtel",
            "Conception de site web pour un hôtel",
            "FRONT_END",
            user20,
        ),
    ]

    for title, description, type, author_user in project_data:
        Project.objects.get_or_create(
            title=title,
            defaults={
                "description": description,
                "type": type,
                "author_user": author_user,
            },
        )

    # retrieve projects
    project1 = Project.objects.get(title="Projet Libra")
    project2 = Project.objects.get(title="Projet E-commerce")
    project3 = Project.objects.get(title="Projet Stockify")
    project4 = Project.objects.get(title="Projet FitApp")
    project5 = Project.objects.get(title="Projet Artisan Paysager")
    project6 = Project.objects.get(title="Projet E-commerce")
    project7 = Project.objects.get(title="Projet Electronique")
    project8 = Project.objects.get(title="Projet Site Web Corporate")
    project9 = Project.objects.get(title="Projet de gestion d'animalerie")
    project10 = Project.objects.get(title="Projet d'application comptabilité")
    project11 = Project.objects.get(title="Projet d'application mobile pour fleuriste")
    project12 = Project.objects.get(title="Projet de rebranding site existant")
    project13 = Project.objects.get(title="Projet de gestion financière")
    project14 = Project.objects.get(
        title="Projet d'application mobile pour un restaurant"
    )
    project15 = Project.objects.get(
        title="Projet de conception de site web avec réservation"
    )
    project16 = Project.objects.get(title="Projet de gestion d'actions en bourse")
    project17 = Project.objects.get(
        title="Projet d'application IOS pour un transporteur"
    )
    project18 = Project.objects.get(title="Projet d'amélioration site web restaurateur")
    project19 = Project.objects.get(
        title="Projet de gestion de stock pour une pharmacie"
    )
    project20 = Project.objects.get(
        title="Projet de conception de site web pour un hôtel"
    )

    # create contributors

    contributor_data = [
        ("project1", user1, "Author"),
        ("project2", user2, "Author"),
        ("project3", user3, "Author"),
        ("project4", user4, "Author"),
        ("project5", user5, "Author"),
    ]

    for project, user, role in contributor_data:
        Contributor.objects.get_or_create(
            project=project, user=user, defaults={"role": role}
        )

    # retrieve contributors
    contributor1 = Contributor.objects.get(project=project1, user=user1)
    contributor2 = Contributor.objects.get(project=project2, user=user2)
    contributor3 = Contributor.objects.get(project=project3, user=user3)
    contributor4 = Contributor.objects.get(project=project4, user=user4)
    contributor5 = Contributor.objects.get(project=project5, user=user5)

    # create issues
    # args = title, description, priority, tag, status, project, author_user, assignee
    issue_data = [
        (
            "Problème de connexion",
            "Impossible de se connecter à l'application",
            "HIGH",
            "BUG",
            "TO_DO",
            project1,
            user1,
            user1,
        ),
        (
            "Problème de paiement",
            "Impossible de payer en ligne",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project2,
            user2,
            user2,
        ),
        (
            "Problème de stock",
            "Le stock est vide",
            "HIGH",
            "BUG",
            "TO_DO",
            project3,
            user3,
            user3,
        ),
        (
            "Problème d'authentification",
            "Impossible de s'authentifier à l'application",
            "HIGH",
            "BUG",
            "TO_DO",
            project4,
            user4,
            user4,
        ),
        (
            "Problème de design au niveau du header",
            "Le design du header est à revoir",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project5,
            user5,
            user5,
        ),
        (
            "Problème de connexion",
            "Impossible de se connecter à l'application",
            "HIGH",
            "BUG",
            "TO_DO",
            project6,
            user6,
            user6,
        ),
        (
            "Souci au niveau de JWT",
            "Problème de JWT",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project7,
            user7,
            user7,
        ),
        (
            "Problème installation Tailwind",
            "NPM à vérifier",
            "HIGH",
            "BUG",
            "TO_DO",
            project8,
            user8,
            user8,
        ),
        (
            "Base de données non accessible",
            "Problème de connexion à la base de données",
            "HIGH",
            "BUG",
            "TO_DO",
            project9,
            user9,
            user9,
        ),
        (
            "Plan comptable non conforme",
            "Problème de plan comptable",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project10,
            user10,
            user10,
        ),
        (
            "Système de paiement Stripe non fonctionnel",
            "Problème de paiement",
            "HIGH",
            "BUG",
            "TO_DO",
            project11,
            user11,
            user11,
        ),
        (
            "Logo à refaire selon nouveau charte graphique",
            "Problème de logo",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project12,
            user12,
            user12,
        ),
        (
            "Programme d'évaluation forex non fonctionnel",
            "Problème de programme forex",
            "HIGH",
            "BUG",
            "TO_DO",
            project13,
            user13,
            user13,
        ),
        (
            "Système de réservation de table à vérifier",
            "Problème de réservation",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project14,
            user14,
            user14,
        ),
        (
            "Système de booking de vols non fonctionnel",
            "Problème de booking",
            "HIGH",
            "BUG",
            "TO_DO",
            project15,
            user15,
            user15,
        ),
        (
            "Affichage des actions disponibles à revoir",
            "Problème d'affichage",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project16,
            user16,
            user16,
        ),
        (
            "Système de suivi de colis à mettre en place",
            "Problème de suivi de colis",
            "HIGH",
            "BUG",
            "TO_DO",
            project17,
            user17,
            user17,
        ),
        (
            "Version mobile du site à revoir",
            "Problème de version mobile",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project18,
            user18,
            user18,
        ),
        (
            "Différence de stocks entre le site et la pharmacie",
            "Problème de stock",
            "HIGH",
            "BUG",
            "TO_DO",
            project19,
            user19,
            user19,
        ),
        (
            "Système de réservation de chambre à vérifier",
            "Problème de réservation",
            "MEDIUM",
            "BUG",
            "IN_PROGRESS",
            project20,
            user20,
            user20,
        ),
    ]

    issues = []

    for (
        title,
        description,
        priority,
        tag,
        status,
        project,
        author_user,
        assignee,
    ) in issue_data:
        issue, created = Issue.objects.get_or_create(
            title=title,
            defaults={
                "description": description,
                "priority": priority,
                "tag": tag,
                "status": status,
                "project": project,
                "author_user": author_user,
                "assignee": assignee,
            },
        )

        # add issues into the list
        issues.append(issue)

    # create comments
    # args = description, issue, author_user

    comments_data = [
        ("Le problème est résolu", issues[0], user1),
        ("Le problème est en cours de résolution", issues[1], user2),
        ("Ajout de stock effectué", issues[2], user3),
        ("La connexion est résolue", issues[3], user4),
        ("Le design du header est en cours de modification", issues[4], user5),
        ("Le problème est résolu", issues[5], user6),
        ("Le problème est en cours de résolution", issues[6], user7),
        ("Ajout de stock effectué", issues[7], user8),
        ("La connexion au BDD est résolue", issues[8], user9),
        ("Investigation en cours", issues[9], user10),
        ("API Stripe en cours de vérification", issues[10], user11),
        ("Logo en cours de modification", issues[11], user12),
        ("Programme forex en cours de vérification", issues[12], user13),
        ("Système de paiement en cours de vérification", issues[13], user14),
        ("Système de réservation en cours de vérification", issues[14], user15),
        ("Système de booking non valide, recherche alternative", issues[15], user16),
        (
            "Affichage des actions en cours de modification, voir GitHub Repo Forex",
            issues[16],
            user17,
        ),
        ("Système de suivi de colis en cours de développement", issues[17], user18),
        ("Version mobile en cours, push bientôt", issues[18], user19),
        ("Différence de stock en cours d'investigation", issues[19], user20),
    ]

    for description, issue, author_user in comments_data:
        Comment.objects.get_or_create(
            description=description,
            defaults={"issue": issue, "author_user": author_user},
        )

    print("Database populated successfully")


if __name__ == "__main__":
    run()
