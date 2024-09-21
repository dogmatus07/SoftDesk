from rest_framework import generics, permissions
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .models import Project, Contributor, Issue, Comment


# Project views
class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects or create a new project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project instance
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContributorListView(generics.ListCreateAPIView):
    """
    List all contributors or add a new contributor
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment instance
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

