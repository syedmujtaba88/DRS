from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):

    is_team_lead = models.BooleanField(default=False)

    def __str__(self):
        """Human readable return string."""
        return self.username
