from django.urls import path
from .views import lyric_detail, lyrics_list


urlpatterns = [path("lyric/<int:id>/", lyric_detail), path("lyrics/", lyrics_list, name="lyrics_list")]
