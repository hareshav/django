from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db import models

# Create your models here.
class UserModels(AbstractUser):
    location=models.CharField(max_length=100,blank=True)

