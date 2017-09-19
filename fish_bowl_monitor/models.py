from django.db import models

# Create your models here.


class TankTemp(models.Model):
    date_time_stamp = models.DateTimeField()
    temperature_data = models.IntegerField()
