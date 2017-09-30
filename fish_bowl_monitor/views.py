from django.shortcuts import render
from fish_bowl_monitor.models import TankTemp


def fish_home(request):
    check_db = TankTemp.objects.latest('date_time_stamp')
    oldest = TankTemp.objects.earliest('date_time_stamp')
    return render(request, 'home.html', {
        'current_tank_temp': check_db.temperature_data,
        'earliest_tank_temp': oldest.temperature_data,
        'earliest_date': oldest.date_time_stamp,
        }
    )
