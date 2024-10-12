from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, Contributor, Issue, Comment


# Serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'age',
            'consent',
            'can_be_contacted',
            'can_data_be_shared'
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
    author_user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user', 'created_time']


# Serializer for contributor model
class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Contributor
        fields = ['user', 'role']


# Serializer for issue model
class IssueSerializer(serializers.ModelSerializer):
    author_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    assignee = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

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
    
    def validate_assignee(self, value):
        """
        Check if the assignee is a contributor to the project
        """
        project = self.initial_data.get('project')
        if not Contributor.objects.filter(project=project, user=value).exists():
            raise serializers.ValidationError(
                "L'utilisateur n'est pas un contributeur du projet"
                )
        return value


# Serializer for comment model
class CommentSerializer(serializers.ModelSerializer):
    author_user = UserSerializer(read_only=True)
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'uuid', 'description', 'author_user', 'issue', 'created_time']
