from django.shortcuts import render
from fish_bowl_monitor.models import TankTemp
# from fish_bowl_monitor.temperature_probe import TempData

# Create your views here.


def fish_home(request):
    check_db = TankTemp.objects.latest('date_time_stamp')
    return render(request, 'home.html', {'tank_temp': check_db.temperature_data})
