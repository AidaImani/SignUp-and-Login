from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verify_id = models.UUIDField()
    verify = models.BooleanField(default=False)

