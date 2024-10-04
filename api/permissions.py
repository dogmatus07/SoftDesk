"""
This file contains the custom permissions for the API.
"""
from rest_framework.permissions import IsAuthenticated

class IsActiveUser(IsAuthenticated):
    """
    Allows access only to active users.
    """
    def has_permission(self, request, view):
        # Ensure that the user is active
        return super().has_permission(request, view) and request.user.is_active
