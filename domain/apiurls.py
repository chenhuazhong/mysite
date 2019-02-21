from django.urls.conf import path, include

from domain import apiviews

urlpatterns = [
    path('', apiviews.DomanAPIView.as_view()),
    # path('page/<int:pk>/', views.detail),
    # path('page/<int:pk>/comment/', views.comment),
    # path('login/', login),
]


