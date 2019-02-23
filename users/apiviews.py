from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from users.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rest_framework_simplejwt.views import TokenObtainPairView

class UserAPIView(ViewSet):

    @action(detail=False, methods=['GET'])
    def check(self, request):
        username = request.query_params.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'code': 400, 'data': '用户名已经存在'})
        else:
            return Response({'code': 200, 'data': 'ok11'})

    @action(detail=False, methods=['GET'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            if User.objects.get(username=username).check_password(password):
               pass
        return Response('ok')

    @action(detail=False, methods=['POST'])
    def regsiter(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response('用户名已存在', status=HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()

            return Response('注册成功')


class MyTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        serializer.validated_data['username'] = serializer.user.username
        serializer.validated_data['user_id'] = serializer.user.id
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

