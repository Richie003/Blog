from django.db import models

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(unique=True, max_length=225, default="", blank=False)