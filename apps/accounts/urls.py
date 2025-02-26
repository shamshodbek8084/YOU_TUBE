from django.urls import path
from .views import CreateChannel, DeleteChannel, GetChannel
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Token olish uchun
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Tokenni yangilash uchun
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create_channel/', CreateChannel.as_view(), name = 'createchannel'),
    path('delete_channel/<int:pk>', DeleteChannel.as_view(), name = 'deletechannel'),
    path('get_channel/', GetChannel.as_view(), name = 'getchannel'),
]

