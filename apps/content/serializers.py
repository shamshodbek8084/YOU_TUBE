from rest_framework import serializers
from .models import Video, Comment, Playlist
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
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video', 'user', 'text']

class CommentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'user', 'text']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['author', 'videos', 'title']
    

