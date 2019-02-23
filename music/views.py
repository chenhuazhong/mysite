from django.shortcuts import render

# Create your views here.


def music(request):
    user = request.user
    return render(request, 'music.html')

def lrc(request):
    return render(request, 'lrc.html')

