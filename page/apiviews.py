from rest_framework import viewsets
from rest_framework import views
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from domain.models import Pager
from page.serializers import PageSerializer


class PageListAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView, viewsets.ViewSet):
    serializer_class = PageSerializer
    queryset = Pager.objects.filter(p_isdelete=False)
    pass

class PageAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    queryset = Pager.objects.all()