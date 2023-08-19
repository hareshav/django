from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .services import global_choice,local_choice
# from django.db import models
# Create your models here.
class LocalService(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False)
    name=models.CharField(max_length=100,blank=False)    
    x_cood=models.FloatField(blank=False,default=None)
    y_cood=models.FloatField(blank=False,default=None)
    services=models.CharField(max_length=100,choices=local_choice,blank=False)
    from_time=models.TimeField(blank=True,default=None)
    to_time=models.TimeField(blank=True,default=None)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    AbstractBaseUser.password="haresh"
    def __str__(self):
        return str(self.id)
class RemoteService(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        return str(self.id)
        
class UserModels(AbstractUser):
    onservicelocal=models.ForeignKey(LocalService, on_delete=models.CASCADE,unique=False,null=True,default=None)
    localServiceFrom=models.TimeField(blank=True,default=None,null=True)
    localServiceDuration=models.IntegerField(blank=True,default=None,null=True)
    onserviceglobal=models.ForeignKey(RemoteService, on_delete=models.CASCADE,unique=False,null=True,default=None)
    globalServiceFrom=models.TimeField(blank=True,default=None,null=True)
    globalServiceDuration=models.IntegerField(blank=True,default=None,null=True)
    x_cood=models.FloatField(blank=False,default=None,null=True)
    y_cood=models.FloatField(blank=False,default=None,null=True)

