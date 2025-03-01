from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from .permissions import IsHasChannel, IsOwner
from rest_framework.views import APIView
from .serializers import VideoSerializer, CommentSerializer, CommentCommentSerializer, PlaylistSerializer
from rest_framework.response import Response
from .models import Video, Like, Comment, CommentLike, CommentComment, Playlist
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

class Video_all_comment(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        video = get_object_or_404(Video, id = pk)
        comment = Comment.objects.filter(video = video).select_related("user")
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)
    

class LikeToVideoView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        like = Like.objects.filter(video = request.data['video'], user = request.user).first()
        if like:
            if like.dislike == request.data.get("dislike"):
                like.delete()
                data = {
                    "status" : True,
                    "msg" : "Like o'chirildi"
                }
            else:
                like.dislike = request.data['dislike']
                like.save()
                data = {
                    "status" : True,
                    "msg" : "Like o'zgartirildi"
                }
        else:
            Like.objects.create(video = request.data['video'], 
                                user = request.user,
                                dislike = request.data['dislike'])
            data = {
                "status" : True,
                "msg" : "Like qo'yildi"
            }
        return Response(data=data)
    
class CommentVideo(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk):
        video = get_object_or_404(Video, id = pk)
        text = request.data.get("text")
        datas = {
            "status" : False,
            "msg" : "Komment matnini to'ldiring"
        }
        if text:
            comment = Comment.objects.create(video=video, user=request.user, text=text)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:   
            return Response(data=datas)

class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        dislike = request.data.get("dislike", False)

        like_obj = CommentLike.objects.filter(comment=comment, user=request.user).first()

        if like_obj:
           
            if like_obj.dislike == dislike:
                like_obj.delete()
                data = {
                "status" : True,
                "msg" : "Comment_like o'chirildi"
                }
                return Response(data=data)
            else:
                like_obj.dislike = dislike
                like_obj.save()
                data = {
                "status" : True,
                "msg" : "Comment_like o'zgartirlidi"
                }
                return Response(data=data)
        else:
            CommentLike.objects.create(comment=comment, user=request.user, dislike=dislike)
            data = {
                "status" : True,
                "msg" : "Commentga like quyildi"
            }
            return Response(data=data)        

class Comment_to_commentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        text = request.data.get("text")
        data = {
            "status" : False,
            "msg" : "Komment matni bo'sh"
        }
        if text:
            reply = CommentComment.objects.create(comment=comment, user=request.user, text=text)
            serializer = CommentCommentSerializer(reply)
            return Response(serializer.data)
        else:
            return Response(data=data)

# Playlist CRUD

class CreatePlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        title = request.data.get("title")
        video_ids = request.data.get("videos", [])

        if not title:
            data = {
                "status" : False,
                "msg" : "Playlist titleni kiriting"
            }
            return Response(data=data)

        playlist = Playlist.objects.create(author=request.user, title=title)
        
        if video_ids:
            videos = Video.objects.filter(id__in=video_ids)
            playlist.videos.set(videos)

        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)
    
class ListPlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if pk:
            playlist = get_object_or_404(Playlist, id=pk, author=request.user)
            serializer = PlaylistSerializer(playlist)
            return Response(serializer.data)
        playlists = Playlist.objects.filter(author=request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

