from django.shortcuts import render
from fish_bowl_monitor.models import TankTemp
# Create your views here.


def fish_home(request):
    tank_temp = TankTemp.objects.all().first()
    return render(request, 'home.html', {'tank_temp': tank_temp.temperature_data})
