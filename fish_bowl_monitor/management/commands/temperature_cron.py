from django.core.management.base import BaseCommand
from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData

"""
This is only to manually run the cron. The cron is in and works just fine.
"""


class Command(BaseCommand):
    help = 'Manually post current temp to db and delete the oldest entry'

    def handle(self, *args, **kwargs):
        tank_temp = TempData()
        read_out = tank_temp.read_temp()
        TankTemp.objects.create(temperature_data=read_out)
        rm = TankTemp.objects.earliest('date_time_stamp')
        rm.delete()



