from django.shortcuts import render
from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData

# Create your views here.


def fish_home(request):
    tank_temp = TempData()
    read_out = tank_temp.read_temp()
    TankTemp.objects.create(temperature_data=read_out)
    check_db = TankTemp.objects.latest('date_time_stamp')
    return render(request, 'home.html', {'tank_temp': check_db.temperature_data})
