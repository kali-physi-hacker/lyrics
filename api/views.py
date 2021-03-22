from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from lyrics.models import Lyric
from .models import LyricSerializer


def test(request):
    template = ""
    context = {}
    return render(request=request, template_name=template, context=context)


@api_view(["GET"])
def lyric_detail(request, pk):
    try:
        lyric = Lyric.objects.get(pk=pk)
    except Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
