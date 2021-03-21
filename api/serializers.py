from rest-framework import serializers

from .models import Lyric

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['id', 'title', 'discription', 'content', 'author', 'composer', 'dated_created']
