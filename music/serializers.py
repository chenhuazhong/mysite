from rest_framework import serializers

from music.models import MusicModel


class MusicSerializer(serializers.ModelSerializer):
    music_url = serializers.ReadOnlyField(source='music.name')
    class Meta:
        model = MusicModel
        fields = ('id', 'name', 'music', 'music_url', 'description', 'create_time')