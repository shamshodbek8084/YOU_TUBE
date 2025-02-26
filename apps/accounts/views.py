from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .serializers import ChannelSerializer
from .models import Channel 

# Create your views here.
class CreateChannel(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        try:
            channel = request.user.channel
            if channel:
                data = {
                    "status" : False,
                    "msg" : "Bu foydalanuvchida kanal mavjud!"
                    
                }
                return Response(data=data)
        except Exception as ex:
            pass
        data = request.POST.copy()
        data['user'] = request.user.id 

        serializer = ChannelSerializer(data = request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        channel = serializer.save()
        channel.user = request.user
        channel.save()
        r_data = {
            "status" : True,
            "msg" : "kanal yaratildi",
            "data" : serializer.data
        }
        return Response(data=r_data)

class DeleteChannel(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        channel = get_object_or_404(Channel, id=pk)
        if channel.user == request.user:
            channel.delete()
            data = {
                'status' : True,
                'msg' : "Kanal o'chirildi"
            }
            return Response(data)
        else:
            data = {
                'status' : False,
                'msg' : "Kanal sizga tegishli emas"
            }
            return Response(data) 

class GetChannel(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):

        channel = request.user.channel
        serializer = ChannelSerializer(instance = channel)

        data = {
            'status' : True,
            'data' : serializer.data
        }

        return Response(data=data)