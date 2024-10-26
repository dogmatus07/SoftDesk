from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, Contributor, Issue, Comment


class UserPublicSerializer(serializers.ModelSerializer):
    """
    Serializer no sensitive data for User Model
    """

    class Meta:
        """
        Meta class for user serializer no sensitive data
        """

        model = get_user_model()
        fields = ["id", "first_name"]


# Serializer for user model
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    """

    class Meta:
        """
        Meta class for user serializer
        """

        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "age",
            "consent",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate_age(self, value):
        """
        Check if the user is older than 15 years
        """
        if value < 15:
            raise serializers.ValidationError("Vous devez avoir plus de 15 ans")
        return value

    def create(self, validated_data):
        """
        Create a new user
        """
        user = get_user_model().objects.create_user(**validated_data)
        return user


# Serializer for project model
class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model
    """

    author_user = UserPublicSerializer(read_only=True)

    class Meta:
        """
        Meta class for project serializer
        """

        model = Project
        fields = ["id", "title", "description", "type", "author_user", "created_time"]


# Serializer for contributor model
class ContributorSerializer(serializers.ModelSerializer):
    """
    Serializer for contributor model
    """

    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        """
        Meta class for contributor serializer
        """

        model = Contributor
        fields = ["user", "role"]


# Serializer for issue model
class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer for issue model
    """

    author_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    assignee = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )

    class Meta:
        """
        Meta class for issue serializer
        """

        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "tag",
            "status",
            "project",
            "author_user",
            "assignee",
            "created_time",
        ]

    def validate_assignee(self, value):
        """
        Check if the assignee is a contributor to the project
        """
        project = self.initial_data.get("project")
        if not Contributor.objects.filter(project=project, user=value).exists():
            raise serializers.ValidationError(
                "L'utilisateur n'est pas un contributeur du projet"
            )
        return value


# Serializer for comment model
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comment model
    """

    author_user = UserPublicSerializer(read_only=True)
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        """
        Meta class for comment serializer
        """

        model = Comment
        fields = ["uuid", "description", "author_user", "issue", "created_time"]
