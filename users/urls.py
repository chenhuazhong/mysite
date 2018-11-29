from django.contrib.auth import login, logout

from users import views



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', views.userLogin),
    path('regisite/', views.registe),
    path('logout/', views.userLogout),
    path('center/', views.userinfo),

    # path('login/', login),
]
