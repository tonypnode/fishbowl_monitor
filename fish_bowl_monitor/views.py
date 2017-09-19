from django.shortcuts import render

# Create your views here.


def fish_home(request):
    return render(request, 'home.html')
