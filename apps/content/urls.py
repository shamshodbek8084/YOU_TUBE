from django.urls import path
from .views import (CreateVideo, DeleteVideoView, UpdateVideoView,
    RetrieveVideoView,
    ListVideoView,
    LikeToVideoView,
    CreatePlaylistView,
    ListPlaylistView,
    Video_all_comment,
)

urlpatterns = [
    path("create_video/", CreateVideo.as_view(), name="create_video"),
    path("delete_video/<int:pk>", DeleteVideoView.as_view(), name="delete_video"),
    path("update_video/<int:pk>", UpdateVideoView.as_view(), name="update_video"),
    path("list-video/<int:pk>", ListVideoView.as_view(), name="update_video"),
    path("like-video/", LikeToVideoView.as_view(), name="like_video"),
    path("create_playlist/", CreatePlaylistView.as_view(), name="create_playlist"),
    path("List_playlist/<int:id>", ListPlaylistView.as_view(), name="List_playlist"),
    path("video_all_comment/<int:id>", Video_all_comment.as_view(), name="video_all_comment"),
]