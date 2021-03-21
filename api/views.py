from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Lyric
from .models import LyricSerializer


def test(request):
    template = ""
    context = {}
    return render(request=request, template_name=template, context=context)
    from django.shortcuts import render


@csrf_exempt
def lyric_detail(request, pk):
    try:
        lyric = Lyric.objects.get(pk=pk)
    except Lyric.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = LyricSerializer(lyric)
        return JsonResponse(serializer.data)
