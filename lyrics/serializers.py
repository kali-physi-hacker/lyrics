from rest_framework import serializers
from lyrics.models import Lyric


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ["title", "description", "content", "composer", "author"]
