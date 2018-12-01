from django.contrib.auth import authenticate
from django.http.response import HttpResponse, JsonResponse


def login_wrapper(fun):

    def wrapper(request, *args, **kwargs):
        user = request.user
        if user is not None and not user.is_anonymous:

            return fun(request, *args, **kwargs)
        else:
            return JsonResponse({'code': 403, 'message': '登录账号后访问'})
    return wrapper

