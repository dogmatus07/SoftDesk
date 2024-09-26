"""
Importing the necessary modules from the rest_framework and api app
"""
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from api.models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)


# Project views
class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects or create a new project
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Return a list of projects that the user is a contributor to
        """
        return Project.objects.filter(contributors__user=self.request.user)


    def perform_create(self, serializer):
        """
        Create a new project and add the current user as the author
        """
        project = serializer.save(author_user=self.request.user)
        Contributor.objects.create(
            project=project,
            user=self.request.user,
            role="Author"
            )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project instance
    """
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)


class ContributorListView(generics.ListCreateAPIView):
    """
    List all contributors or add a new contributor
    """
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Contributor.objects.filter(project_id=project_id)

class ContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contributor instance
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]


class IssueListCreateView(generics.ListCreateAPIView):
    """
    List all issues or create a new issue
    """
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Return a list of issues that the user is a contributor to
        """
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(
            project_id=project_id,
            project__contributors__user=self.request.user)
    

    def perform_create(self, serializer):
        """
        Create a new issue and add the current user as the author
        """
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)
        serializer.save(author_user=self.request.user, project=project)
        return super().perform_create(serializer)


class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an issue instance
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListCreateView(generics.ListCreateAPIView):
    """
    List all comments or create a new comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Return a list of comments that the user is a contributor to
        """
        return Comment.objects.filter(issue__project__contributors__user=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
