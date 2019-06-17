from django.urls import path
from .views import ListSongs, SongDetails, SongDetailSimple

urlpatterns = [
    path('songs/', ListSongs.as_view(), name='songs-all'),
    path('songs/<int:pk>/', SongDetailSimple.as_view(), name='songs-crud'),
]
