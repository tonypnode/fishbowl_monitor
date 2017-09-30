from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData


def temperature_cron():
    tank_temp = TempData()
    read_out = tank_temp.read_temp()
    TankTemp.objects.create(temperature_data=read_out)
    rm = TankTemp.objects.earliest('date_time_stamp')
    rm.delete()

