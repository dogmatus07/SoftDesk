from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Contributor, Issue, Comment


# Serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# Serializer for project model
class ProjectSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user', 'created_time']


# Serializer for contributor model
class ContributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'role']


# Serializer for issue model
class IssueSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)
    assignee = UserSerializer()

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'priority',
            'tag',
            'status',
            'project',
            'author_user',
            'assignee',
            'created_time',
        ]


# Serializer for comment model
class CommentSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'uuid', 'description', 'author_user', 'issue', 'created_time']
