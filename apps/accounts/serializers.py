from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Channel
from django.contrib.auth.models import User

class ChannelSerializer(ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    class Meta:
        model = Channel
        fields = ['name', 'id', 'user', 'icon', 'desc', 'banner', 'followers_count']

# Obunachilar sonini ko'rsatadi
    @staticmethod
    def get_followers_count(obj):
        return obj.followers.all().count()
    

# class RegisterSerializer(ModelSerializer):
#     password = serializers.CharField(write_only = True)
#     def create(self, validated_data):
        

#         return user

