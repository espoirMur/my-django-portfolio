from rest_framework import serializers
from apis.music.models import Song


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artist')
