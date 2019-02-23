from rest_framework import serializers

from music.models import MusicModel


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicModel
        fields = ('id', 'name', 'music', 'description', 'create_time')