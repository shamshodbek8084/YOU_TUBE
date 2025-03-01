from django.db import models

from apps.accounts.models import User, Channel
from apps.base.models import BaseModel

# Create your models here.
    
class Category(BaseModel):
    title = models.CharField(max_length=255, verbose_name='title')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Video(BaseModel):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField(verbose_name='description', null=True, blank=True)
    photo = models.ImageField(upload_to='videos', verbose_name='photo')
    file = models.FileField(upload_to='videos/', verbose_name='file')
    author = models.ForeignKey(Channel, on_delete=models.CASCADE, 
                               verbose_name='author', 
                               related_name='channel_videos',
                               null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, 
                                 verbose_name='category', related_name='category_videos')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title
    
class View(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name = 'video', related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'user', related_name='views')

    class Meta:
        verbose_name = 'View'
        verbose_name_plural = 'Views'

    def __str__(self):
        return f'{self.user} - {self.video}'
    
class Like(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='video', related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='likes')
    dislike = models.BooleanField(default=False, verbose_name='dislike')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f'{self.user} - {self.video}'
    
class Comment(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='video', related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='comment')
    text = models.TextField(verbose_name='comment')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user} - {self.video}'
    
class CommentLike(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='comment', related_name='comment_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='comment_likes')
    dislike = models.BooleanField(default=False, verbose_name='dislike')

    class Meta:
        verbose_name = 'CommentLike'
        verbose_name_plural = 'CommentLikes'

    def __str__(self):
        return f'{self.user} - {self.comment}'
    
class CommentComment(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='comment', related_name='comment_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', related_name='comment_comment')
    text = models.TextField(verbose_name='comment')

    class Meta:
        verbose_name = 'CommentComment'
        verbose_name_plural = 'CommentComments'

    def __str__(self):
        return f'{self.user} - {self.comment}'

class Playlist(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='author',
                               related_name='user_playlists')
    videos = models.ManyToManyField(Video, verbose_name='videos',
                                    related_name='video_playlists')
    title = models.CharField(max_length=256)


