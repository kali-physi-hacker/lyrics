from django.urls import path
from .views import lyric_detail

from .views import test

urlpatterns = [
    path("/test/", test, name="test"),
    path("/api/lyric/<int:id>/", views.lyric_detail),
    ]
