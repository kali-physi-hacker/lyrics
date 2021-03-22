from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
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
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return JsonResponse(serializer.data)
