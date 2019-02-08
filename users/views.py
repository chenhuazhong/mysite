import json
import time

from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from users.models import User
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View



def userLogin(request):

    mobile = json.loads(request.body.decode('utf-8')).get('mobile')
    print(mobile)
    try:
        user = User.objects.get(mobile=mobile)
    except User.DoesNotExist as e:
        return  JsonResponse({'code': 400, 'message': '用户名不存在'})
    else:
        password = json.loads(request.body.decode('utf-8')).get('password')

        if not user.check_password(password):
            return JsonResponse({'code': 400, 'message': '密码错误'})
        tt = login(request=request, user=user)
        print(tt)
        return JsonResponse({'code': 200, 'data':{'user_id': user.id, 'user': user.username, 'img': user.ater_img.name}})

def registe(request):
    mobile = json.loads(request.body.decode('utf-8')).get('mobile')
    password = json.loads(request.body.decode('utf-8')).get('password')
    if mobile is None or password is None:
        return JsonResponse({'code': 400, 'message': '手机号或者密码不能为空'})
    if User.objects.filter(mobile=mobile).count() > 0:
        return JsonResponse({'code': 400, 'message': '用户名已经存在'})
    user = User()
    user.username = mobile
    user.mobile = mobile
    user.set_password(password)
    user.save()
    login(request, user)
    return JsonResponse({'code': 200, 'data': {'user_id': user.id, 'username': user.username, 'userimg': user.ater_img.name}})


#
def userLogout(request):
    user = request.user
    if not  user.is_authenticated:
        return JsonResponse({'code': 400,'message': '匿名用户'})
    else:
        tt =logout(request)
        print(tt)
        return JsonResponse({'code': 200, 'message': 'logout'})


def userinfo(request):
    return render(request, 'userinfo.html')



def test1(request):
    test = settings.TEST
    print(request.GET.get('t'))
    time.sleep(10)
    return HttpResponse(test)


