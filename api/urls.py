from django.urls import path

from .views import test , Get_LyricsList 

urlpatterns = [
    path("/test/", test, name="test"),
    path("/getlyricslist/", Get_LyricsList, name="get_lyricslist")

]
