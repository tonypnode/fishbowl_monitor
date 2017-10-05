from django.shortcuts import render, redirect
from fish_bowl_monitor.models import TankTemp
from rest_framework.views import APIView
from rest_framework.response import Response


def fish_home_chart(request):
    check_db = TankTemp.objects.latest('date_time_stamp')
    oldest = TankTemp.objects.earliest('date_time_stamp')
    return render(request, 'chart.html', {
        'current_tank_temp': check_db.temperature_data,
        'earliest_tank_temp': oldest.temperature_data,
        'earliest_date': oldest.date_time_stamp,
    })


def fish_home(request):
    check_db = TankTemp.objects.latest('date_time_stamp')
    oldest = TankTemp.objects.earliest('date_time_stamp')
    return render(request, 'home.html', {
        'current_tank_temp': check_db.temperature_data,
        'earliest_tank_temp': oldest.temperature_data,
        'earliest_date': oldest.date_time_stamp,
        }
    )


def add_records():
    for idx in range(0, 2000):
        print("hello?!?!")
        TankTemp.objects.create(temperature_data=0, weather_data_temp=0)


def set_up_db(request):
    add_records()
    # return redirect(f'/')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, reqest):
        # Petty sure this can get cleaned up, but I need to get some reps in before it's clear how
        total = TankTemp.objects.all().count()
        qset = TankTemp.objects.filter().order_by('date_time_stamp').values_list('date_time_stamp', 'temperature_data', 'weather_data_temp')[total - 1440:total:60]
        labels = []
        default_data = []
        outside_temp = []
        for stuff in qset:
            default_data.append(stuff[1])
            dtg = stuff[0].strftime("%b %d %Y %H:%m")
            labels.append(dtg)
            outside_temp.append(stuff[2])

        data = {
            'labels': labels,
            'default_data': default_data,
            'outside_temp': outside_temp,
        }
        return Response(data)
