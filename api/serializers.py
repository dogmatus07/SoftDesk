from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Contributor, Issue, Comment


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


# Serializer for the Project model
class ProjectSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user", "created_time"]


class ContributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ["id", "user", "role"]


class IssueSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)
    assignee = UserSerializer()

    class Meta:
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


class CommentSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "uuid", "description", "author_user", "issue", "created_time"]
