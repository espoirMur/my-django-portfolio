import json
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework.views import status
from apis.music.models import Song
from .serializers import SongsSerializer


class BaseviewTestCase(APITestCase):
    client = APIClient()
    urls = 'apis.music.urls'

    @staticmethod
    def create_song(title='', artist=''):
        if title and artist:
            Song.objects.create(title=title, artist=artist)

    def setup(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseviewTestCase):

    def test_get_all_songs(self):
        """
        This test ensures that all Song added in the setUp method
        exist when we make a GET request to the Song/ endpoint
        """
        response = self.client.get(
            reverse(
                "songs-all",
                kwargs={
                    'version': 'v1'}))
        expected = Song.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostSongTest(BaseviewTestCase):

    def test_create_valid_song(self):
        valid_song = {'title': '48H Gecoco', 'artist': 'JB Mpianna'}
        response = self.client.post(reverse('songs-crud', kwargs={
            'version': 'v1',
            'pk': 1}), data=json.dumps(
            valid_song), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_song(self):
        invalid_song = {'title': '', 'artist': 'JB Mpianna'}
        response = self.client.post(
            reverse(
                'songs-crud',
                kwargs={
                    'version': 'v1',
                    'pk': 1}),
            data=json.dumps(invalid_song),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
