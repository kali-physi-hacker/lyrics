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


@api_view(["GET", "PUT"])
def lyric_detail(request, pk):
    try:
        lyric = Lyric.objects.get(pk=pk)
    except Lyric.DoesNotExist:
        return Response(
            data={"error": "Lyric not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = LyricSerializer(lyric, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
