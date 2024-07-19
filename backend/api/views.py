# api/views.py
from urllib import response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializer

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

@api_view(['GET'])
def music_list(request):
    musics = [
        {"title": "Song 1", "file": "http://localhost:8000/media/https://pixabay.com/music/techno-trance-big-jason-slap-house-version-background-music-for-video-vlog-1minute-223905/"},
        {"title": "Song 2", "file": "http://localhost:8000/media/https://pixabay.com/music/upbeat-big-jason-slap-house-version-background-music-for-video-vlog-37-sec-223903/"},
     
    ]
    return response(musics)
