
from . import apiviews



from django.urls import path

urlpatterns = [
    path('', apiviews.MusicAPIView.as_view()),
]
