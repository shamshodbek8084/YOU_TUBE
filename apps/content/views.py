from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
# Create your views here.

class CreateVideo(APIView):
    permission_classes = []