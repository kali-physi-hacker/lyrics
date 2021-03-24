from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lyrics.models import Lyric
from lyrics.serializers import LyricSerializer


@api_view(["GET"])
def lyrics_list(request):  # new
    if request.method == "GET":
        # get lyrics from model
        lyrics = Lyric.objects.all()
        # serialize info
        serializer = LyricSerializer(lyrics, many=True)
        # return info
        return Response(data=serializer.data, status=status.HTTP_200_OK)
