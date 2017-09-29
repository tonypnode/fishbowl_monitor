from django.core.management.base import BaseCommand, CommandError
from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData

"""
I was really hoping to be able to have django run this in the background, but
I don't think that's possible. I looked at asynio and generators, but I don't
think those are going to work. So, looks like I will do more 
"""


class Command(BaseCommand):
    help = 'Recurring posting of temp to database, runs forever'

    def handle(self, *args, **kwargs):
        tank_temp = TempData()
        read_out = tank_temp.read_temp()
        print(read_out)
        TankTemp.objects.create(temperature_data=read_out)
        self.stdout.write('tem- = %s' % read_out)



