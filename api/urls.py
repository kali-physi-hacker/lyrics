from django.urls import path

from .views import test , lyrics_list 

urlpatterns = [
    path("/test/", test, name="test"),\
    path("/getlyricslist/", lyrics_list, name="lyrics_list")

]
