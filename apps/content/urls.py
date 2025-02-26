from django.urls import path
from .views import (CreateVideo, DeleteVideoView, UpdateVideoView,
    RetrieveVideoView,
    ListVideoView
)

urlpatterns = [
    path("create_video/", CreateVideo.as_view(), name="create_video"),
    path("delete_video/<int:pk>", DeleteVideoView.as_view(), name="delete_video"),
    path("update_video/<int:pk>", UpdateVideoView.as_view(), name="update_video"),
    path("list-video/<int:pk>", ListVideoView.as_view(), name="update_video"),
]