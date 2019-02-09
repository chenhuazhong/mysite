from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from page import apiviews

route = DefaultRouter()
route.register('', apiviews.PageAPIView)


urlpatterns = [
    path('', include(route.urls)),
    # path('page/<int:pk>/', views.detail),
    # path('page/<int:pk>/comment/', views.comment),
    # path('login/', login),
]


