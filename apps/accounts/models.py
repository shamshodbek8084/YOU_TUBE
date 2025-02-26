from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.


class Channel(BaseModel):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='channel')
    icon = models.ImageField(upload_to='channel/', blank=True, null=True)
    desc = models.TextField()
    banner = models.ImageField(upload_to='channel_banner/', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followed_channels', blank=True)

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

    def __str__(self):
        return self.name

