from django.db import models

# Create your models here.


class TankTemp(models.Model):
    date_time_stamp = models.DateTimeField(auto_now_add=True)
    temperature_data = models.FloatField()
    weather_data_temp = models.FloatField(blank=True, null=True)
