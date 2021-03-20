from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Lyric(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    composer = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
