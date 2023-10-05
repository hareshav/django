from django.contrib import admin

# Register your models here.
from .models import UserModels,LocalService,RemoteService
# Register your models here.
admin.site.register(UserModels)
admin.site.register(LocalService)
admin.site.register(RemoteService)