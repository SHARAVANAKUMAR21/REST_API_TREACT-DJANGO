from rest_framework import serializers
from .models import Dream

class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ['id', 'title', 'description', 'date_recorded', 'user']

class DreamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ['title', 'description', 'date_recorded']
