# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet
from django.urls import path
from .views import music_list

router = DefaultRouter()
router.register(r'musics', MusicViewSet)

urlpatterns = [
  path('musics/', music_list, name='music-list'),
]
