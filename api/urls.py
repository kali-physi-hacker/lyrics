from django.urls import path
from .views import lyric_detail

from .views import test, lyrics_list


urlpatterns = [
    path("/lyric/<int:id>/", views.lyric_detail),
    path("/get/lyrics", lyrics_list, name="lyrics_list")
]

