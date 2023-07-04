from django.contrib import admin
from .models import UserModels,LocalService
# Register your models here.
admin.site.register(UserModels)
admin.site.register(LocalService)