"""
Importing the necessary modules from the rest_framework and api app
"""

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from api.models import Project, Contributor, Issue, Comment
from .permissions import IsActiveUser
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
    UserSerializer,
)


# User Delete View


class UserDeleteView(generics.DestroyAPIView):
    """
    Delete a user instance RGPD compliant
    """

    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.delete()


# user profile view


class UserProfile(APIView):
    """
    Retrieve the user profile
    """

    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


# Project views
@method_decorator(cache_page(60 * 15), name="dispatch")
class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects or create a new project
    """

    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        """
        Return a list of projects that the user is a contributor to
        """
        return Project.objects.all().order_by("-created_time")

    def perform_create(self, serializer):
        """
        Create a new project and add the current user as the author
        """
        project = serializer.save(author_user=self.request.user)
        Contributor.objects.create(
            project=project, user=self.request.user, role="Author"
        )
        cache.clear()


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project instance
    """

    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)

    def perform_update(self, serializer):
        project = self.get_object()
        if project.author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à modifier ce projet.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à supprimer ce projet.")
        instance.delete()


@method_decorator(cache_page(60 * 15), name="dispatch")
class ContributorListView(generics.ListCreateAPIView):
    """
    List all contributors or add a new contributor
    """

    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        """
        Return a list of contributors for the project specified by the project id in the url
        """
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        """
        Add a new contributor to the project specified by the project id in the url
        """
        project_id = self.kwargs["project_id"]
        project = get_object_or_404(Project, id=project_id)

        user = serializer.validated_data["user"]

        # check if the user is already a contributor to the project
        if Contributor.objects.filter(project=project, user=user).exists():
            raise serializers.ValidationError(
                "Cet utilisateur est déjà un contributeur de ce projet"
            )

        # if the user is not already a contributor, save it
        serializer.save(project=project, user=user)
        cache.clear()


@method_decorator(cache_page(60 * 15), name="dispatch")
class ContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contributor instance
    """

    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        """
        Return a list of contributors for the project specified by the project id in the url
        """
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project_id=project_id)


@method_decorator(cache_page(60 * 15), name="dispatch")
class IssueListCreateView(generics.ListCreateAPIView):
    """
    List all issues or create a new issue
    """

    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        """
        Return a list of issues that the user is a contributor to
        """
        project_id = self.kwargs["project_id"]
        return Issue.objects.filter(
            project_id=project_id, project__contributors__user=self.request.user
        )

    def perform_create(self, serializer):
        """
        Create a new issue and add the current user as the author
        """
        project_id = self.kwargs["project_id"]
        project = Project.objects.get(id=project_id)
        serializer.save(author_user=self.request.user, project=project)
        cache.clear()
        return super().perform_create(serializer)


@method_decorator(cache_page(60 * 15), name="dispatch")
class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an issue instance
    """

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        return (
            Issue.objects.filter(project__contributors__user=self.request.user)
            .select_related("author_user", "assignee")
            .prefetch_related("comments")
        )

    def perform_update(self, serializer):
        if self.get_object().author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à effectuer cette action")
        serializer.save()
        cache.clear()

    def perform_destroy(self, instance):
        if instance.author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à effectuer cette action")
        instance.delete()
        cache.clear()


@method_decorator(cache_page(60 * 15), name="dispatch")
class CommentListCreateView(generics.ListCreateAPIView):
    """
    List all comments or create a new comment
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]

    def get_queryset(self):
        """
        Return a list of comments that the user is a contributor to
        """
        issue_id = self.request.query_params.get("issue_id")
        project_id = self.request.query_params.get("project_id")
        queryset = Comment.objects.all()

        if project_id and issue_id:
            queryset = queryset.filter(issue__project_id=project_id, issue_id=issue_id)
        elif project_id:
            queryset = queryset.filter(issue__project_id=project_id)
        elif issue_id:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset.order_by("-created_time")

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)
        cache.clear()


@method_decorator(cache_page(60 * 15), name="dispatch")
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    lookup_field = "uuid"

    def get_queryset(self):
        return Comment.objects.all()

    def perform_update(self, serializer):
        if self.get_object().author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à effectuer cette action")
        serializer.save()
        cache.clear()

    def perform_destroy(self, instance):
        if instance.author_user != self.request.user:
            raise PermissionDenied("Vous n'êtes pas autorisé à effectuer cette action")
        instance.delete()
        cache.clear()
