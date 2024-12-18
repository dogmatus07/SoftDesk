"""
Import the models from the api app and register them with the admin site.
"""

from django.contrib import admin
from .models import (
    CustomUser,
    Project,
    Contributor,
    Issue,
    Comment,
)


# register models
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
