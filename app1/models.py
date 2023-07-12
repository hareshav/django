from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# from django.db import models

# Create your models here.
class UserModels(AbstractUser):
    location=models.CharField(max_length=100,blank=True)
class LocalService(AbstractBaseUser):
    skill=(
        ('samayal','samayal'),
        ('carpenter','carpenter'),
        ('plumber','plumber'),
        ('Astronaut','Astronaut'),
        ('security','security'),
    )
    email = models.EmailField(blank=False)
    name=models.CharField(max_length=100,blank=False)    
    location=models.CharField(max_length=100,blank=False)
    services=models.CharField(max_length=100,choices=skill,blank=False)
    from_time=models.TimeField(blank=True,default=None)
    to_time=models.TimeField(blank=True,default=None)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    AbstractBaseUser.password="haresh"
    def __str__(self):
        return self.email
    
