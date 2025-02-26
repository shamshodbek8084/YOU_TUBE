from rest_framework import serializers
from .models import Video
from apps.accounts.serializers import ChannelSerializer


class VideoSerializer(serializers.ModelSerializer):
    channel_name = serializers.SerializerMethodField("get_channel_name")
    class Meta:
        model = Video
        fields = ['title', 'description', 'author', 'photo', 'file', 'category', 'channel_name']
# id ning o'rniga nom qo'yib chiqaradi channel_name ga 
    
    def get_channel_name(self, obj):
        return ChannelSerializer(instance=obj.author,
                                 context = {"request" : self.context.get("request")}).data