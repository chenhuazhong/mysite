from rest_framework import serializers

from domain.models import DomanModel


class DomanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DomanModel
        fields = ('url', 'image', 'title', 'type', 'id')