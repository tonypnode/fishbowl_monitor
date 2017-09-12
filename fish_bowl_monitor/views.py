from django.http import HttpResponse

# Create your views here.


def fish_home(response):
    return HttpResponse('<html><title>Hello World</title><body>Yo</body></html>')
