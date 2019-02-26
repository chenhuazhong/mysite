"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.static import serve
import users
from mysite import settings


urlpatterns = [
    path('V1/admin/', admin.site.urls),
    path('V1/user/', include('users.urls')),
    path('V1/', include('domain.urls')),
    path('V1/music/', include('music.urls')),
    path('V1/page/', include('page.urls')),
    path('V1/ckeditor/', include('ckeditor_uploader.urls')),
    path('API/user/', include('users.apiurls')),
    path('API/page/', include('page.apiurls')),
    path('API/doman/', include('domain.apiurls')),
    path('API/music/', include('music.apiurls'))
    # path('/static/.*', serve, {"document_root": settings.MEDIA_ROOT}),
    # path('static/media/(<str:path>.*)', page)

    # path('xadmin/', include(xadmin.site.urls)),
]
