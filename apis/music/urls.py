from django.urls import path
from .views import ListSongs, SongDetails

urlpatterns = [
    path('songs/', ListSongs.as_view(), name='songs-all'),
    path('songs/<int:pk>/', SongDetails.as_view(), name='songs-crud'),
]
