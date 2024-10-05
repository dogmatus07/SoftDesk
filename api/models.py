"""
Import models, User and uuid
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Custom User model that extends the default User Model by Django
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    consent = models.BooleanField(default=False)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

class Project(models.Model):
    """
    class representing a Project
    """
    BACK_END = "BACK_END"
    FRONT_END = "FRONT_END"
    IOS = "IOS"
    ANDROID = "ANDROID"

    TYPE_CHOICES = [
        (BACK_END, "Back-end"),
        (FRONT_END, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Contributor(models.Model):
    """
    Class representing a Contributor
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="contributors"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default="Contributor")

    class Meta:
        """
        Define the unique_together attribute to ensure that
        a user can only be added to a project once.
        """
        unique_together = ("project", "user")

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"


class Issue(models.Model):
    """
    Define the Issue model with the following fields:
    - id: a UUID field that is the primary key.
    - title: a CharField with a maximum length of 255 characters.
    - description: a TextField.
    - priority: a CharField with a maximum length of 10 characters.
    It should have three choices: LOW, MEDIUM, and HIGH.
    - tag: a CharField with a maximum length of 10 characters.
    It should have three choices: BUG, FEATURE, and TASK.
    - project: a ForeignKey to the Project model with a CASCADE delete option.
    - author_user: a ForeignKey to the User model with a CASCADE delete option.
    - assignee: a ForeignKey to the User model with a CASCADE delete option.
    - created_time: a DateTimeField that is automatically set when an object is created.
    """

    # define the priority choices
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    PRIORITY_CHOICES = [(LOW, "Low"), (MEDIUM, "Medium"), (HIGH, "High")]

    # define the type choices
    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"

    TAG_CHOICES = [(BUG, "Bug"), (FEATURE, "Feature"), (TASK, "Task")]

    # define the status choices
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"

    STATUS_CHOICES = [
        (TODO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=TODO)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="issues_created"
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="issues_assigned"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """
    Define the Comment model with the following fields:
    - id: a UUID field that is the primary key.
    - description: a TextField.
    - author_user: a ForeignKey to the User model with a CASCADE delete option.
    - issue: a ForeignKey to the Issue model with a CASCADE delete option.
    - created_time: a DateTimeField that is automatically set when an object is created.
    """

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    description = models.TextField()
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uuid} - on {self.issue.title}"
