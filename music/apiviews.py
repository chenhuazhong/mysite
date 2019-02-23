from rest_framework.generics import ListAPIView

from music.models import MusicModel
from music.serializers import MusicSerializer


class MusicAPIView(ListAPIView):
    serializer_class = MusicSerializer
    queryset = MusicModel.objects.filter(is_delete=False).all()