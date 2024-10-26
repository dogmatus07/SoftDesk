"""
Import the path function from django.urls and the views from the api app.
"""

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
    UserProfile,
)


urlpatterns = [
    # profile urls
    path("profile/", UserProfile.as_view(), name="profile-detail"),
    # project urls
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    # contributor urls
    path(
        "projects/<int:project_id>/contributors/",
        ContributorListView.as_view(),
        name="contributor-list-create",
    ),
    path(
        "projects/<int:project_id>/contributors/<int:pk>/",
        ContributorDetailView.as_view(),
        name="contributor-detail",
    ),
    # issue urls
    path(
        "projects/<int:project_id>/issues/",
        IssueListCreateView.as_view(),
        name="issue-list-create",
    ),
    path(
        "projects/<int:project_id>/issues/<int:pk>/",
        IssueDetailView.as_view(),
        name="issue-detail",
    ),
    # comment urls
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
