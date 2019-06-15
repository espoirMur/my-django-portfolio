from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework.views import status
from apis.music.models import Songs
from .serializers import SongsSerializer


class BaseviewTestCase(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title='', artist=''):
        if title and artist:
            Songs.objects.create(title=title, artist=artist)

    def setup(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseviewTestCase):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        response = self.client.get(
            reverse(
                "songs-all",
                kwargs={
                    'version': 'v1'}))
        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
