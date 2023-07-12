from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .services import global_choice,local_choice
# from django.db import models
# Create your models here.
class UserModels(AbstractUser):
    location=models.CharField(max_length=100,blank=True)
class LocalService(AbstractBaseUser):
    email = models.EmailField(blank=False)
    name=models.CharField(max_length=100,blank=False)    
    location=models.CharField(max_length=100,blank=False,default=None)
    services=models.CharField(max_length=100,choices=local_choice,blank=False)
    from_time=models.TimeField(blank=True,default=None)
    to_time=models.TimeField(blank=True,default=None)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    AbstractBaseUser.password="haresh"
    def __str__(self):
        return self.email
class RemoteService(AbstractBaseUser):
    email = models.EmailField(blank=False)
    name=models.CharField(max_length=100,blank=False)    
    services=models.CharField(max_length=100,choices=global_choice,blank=False)
    from_time=models.TimeField(blank=True,default=None)
    to_time=models.TimeField(blank=True,default=None)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    AbstractBaseUser.password="haresh"
    def __str__(self):
        return self.email
    
