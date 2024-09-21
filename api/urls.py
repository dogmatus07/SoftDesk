from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectDetailView,
    ContributorListView,
    ContributorDetailView,
    IssueListCreateView,
    IssueDetailView,
    CommentListCreateView,
    CommentDetailView,
)


urlpatterns = [
    # project urls
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<uuid:pk>/", ProjectDetailView.as_view(), name="project-detail"),

    # contributor urls
    path("contributors/", ContributorListView.as_view(), name="contributor-list-create"),
    path(
        "contributors/<uuid:pk>/", 
        ContributorDetailView.as_view(), 
        name="contributor-detail"),
    
    # issue urls
    path("issues/", IssueListCreateView.as_view(), name="issue-list-create"),
    path("issues/<uuid:pk>/", IssueDetailView.as_view(), name="issue-detail"),

    # comment urls
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<uuid:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
