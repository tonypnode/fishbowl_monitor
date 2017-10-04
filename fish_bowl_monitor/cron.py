from fish_bowl_monitor.models import TankTemp
from fish_bowl_monitor.temperature_probe import TempData
from fish_bowl_monitor.open_weather import OpenWeather


def temperature_cron():
    opw = OpenWeather()
    tank_temp = TempData()
    read_out = tank_temp.read_temp()
    TankTemp.objects.create(temperature_data=read_out, weather_data_temp=opw.get_temp_data())
    rm = TankTemp.objects.earliest('date_time_stamp')
    rm.delete()

