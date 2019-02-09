import re

from rest_framework import serializers
from rest_framework.fields import Field

from domain.models import Pager

class p_content(Field):
    def to_representation(self, value):
        result = re.findall('<p>(\w+)</p>', value)
        return ','.join(result) if ','.join(result).__len__() < 100 else ','.join(result)[:97] + '...'

    def to_internal_value(self, data):
        pass


class PageSerializer(serializers.ModelSerializer):
    content = p_content(source='p_content')
    class Meta:
        model=Pager
        fields= '__all__'