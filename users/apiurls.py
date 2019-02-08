from django.urls.conf import include

from users import apiviews as views
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


route = DefaultRouter()
route.register('', views.UserAPIView, basename='st')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('',include(route.urls))
]
