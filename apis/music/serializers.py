from rest_framework import serializers
from apis.music.models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        field = ('title', 'artist')
