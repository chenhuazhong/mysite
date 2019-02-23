from django.urls.conf import include

from users import apiviews as views, apiviews
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)


route = DefaultRouter()
route.register('', views.UserAPIView, basename='st')

urlpatterns = [
    path('login/', apiviews.MyTokenObtainPairView.as_view(), name='login'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('',include(route.urls))
]
