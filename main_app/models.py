

from django.db import models
from django.contrib.auth.models import User

class MainForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields as per your requirements
