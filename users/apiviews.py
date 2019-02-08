from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST

from users.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


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



