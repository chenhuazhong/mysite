from rest_framework.response import Response
from rest_framework.views import APIView

from domain.models import DomanModel
from domain.serializers import DomanSerializer


class DomanAPIView(APIView):

    def get(self, request):
        query_set = DomanModel.objects.all()[:4]
        serializer = DomanSerializer(query_set, many=True)
        print(serializer.data)
        return Response(serializer.data)