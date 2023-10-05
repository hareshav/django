from rest_framework import serializers
from .models import UserModels,RemoteService

class data(serializers.ModelSerializer):
    class Meta:
        model = RemoteService
        fields='__all__'