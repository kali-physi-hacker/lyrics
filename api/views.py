from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from lyrics.models import Lyric
from lyrics.serializers import LyricSerializer

from django.http import HttpResponse, JsonResponse


def test(request):
    template = ""
    context = {}
    return render(request=request, template_name=template, context=context)


@api_view(["GET"])
def Get_LyricsList(request): # new 


    try :
        # first pick info from model
        lyrics = Lyric.objects.all()
    except Lyric.DoesNotExist:
        return HttpResponse(status=404)
        
        if request.method == "GET":
            # serialize info
            serializer = LyricSerializer(lyrics, many=True)
            # return info 
            return Response (serializer.data)



    
    # return info 
    # check if info can be gotten at once and serialized too

    
