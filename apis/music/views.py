from rest_framework.response import Response
from .models import Song
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, status
from apis.music.models import Song
from .serializers import SongsSerializer


class ListSongs(generics.ListCreateAPIView):
    """
    provides a get all song method handler
    """
    queryset = Song.objects.all()
    serializer_class = SongsSerializer


class SongDetails(APIView):
    """
    RUD Endpoint for a song

    Args:
        APIView ([type]): [description]
    """

    def get_song(self, pk):
        try:
            song = Song.objects().get(pk=pk)
            return song
        except Song.DoesNotExist:
            raise Http404

    def get(self, pk, format=None):
        song = self.get_song(pk)
        serializer = SongsSerializer(song)
        return Response(serializer.data)

    def post(self, serializer, pk, version):
        song = self.request.data
        serializer = SongsSerializer(data=song)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, pk, format=None):
        song = self.get_song(pk)
        serializer = SongsSerializer(song, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format=None):
        song = self.get_song(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongDetailSimple(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer
