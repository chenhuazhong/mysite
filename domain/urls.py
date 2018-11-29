from django.contrib.auth import login

from domain import views



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('page/<int:pk>/', views.detail),
    path('page/<int:pk>/comment/', views.comment),
    # path('login/', login),
]
