from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from .permissions import IsHasChannel, IsOwner
from rest_framework.views import APIView
from .serializers import VideoSerializer
from rest_framework.response import Response
from .models import Video
# Create your views here.

class CreateVideo(APIView):
    permission_classes = [IsAuthenticated, IsHasChannel]
    serializer_class = VideoSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        video = serializer.save()
        channel = request.user.channel
        video.author = channel
        video.save()
        data = {
            "status" : True,
            "msg" : "Video yaratildi",
            "data" : self.serializer_class(instance = video, context = {"request" : request}).data
        }
        return Response(data=data)

class DeleteVideoView(DestroyAPIView):
    permission_classes = [IsHasChannel, IsOwner]
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active = True)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs) 
        data = {
            "status" : True,
            "msg" : "Video o'chirildi"

        }
        return Response(data=data)

class UpdateVideoView(UpdateAPIView):
    permission_classes = [IsHasChannel, IsOwner]
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active = True) 

class RetrieveVideoView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()  


class ListVideoView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = VideoSerializer
    queryset = Video.objects.all() 


