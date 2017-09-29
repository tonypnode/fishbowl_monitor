# from django.core.management.base import BaseCommand, CommandError
from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData


def temperature_cron():
    tank_temp = TempData()
    read_out = tank_temp.read_temp()
    print(read_out)
    TankTemp.objects.create(temperature_data=read_out)



