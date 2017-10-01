from django.shortcuts import render
from fish_bowl_monitor.models import TankTemp
from rest_framework.views import APIView
from rest_framework.response import Response


def fish_home_chart(request):
    return render(request, 'chart.html')


def fish_home(request):
    check_db = TankTemp.objects.latest('date_time_stamp')
    oldest = TankTemp.objects.earliest('date_time_stamp')
    return render(request, 'home.html', {
        'current_tank_temp': check_db.temperature_data,
        'earliest_tank_temp': oldest.temperature_data,
        'earliest_date': oldest.date_time_stamp,
        }
    )


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, reqest):
        # Petty sure this can get cleaned up, but I need to get some reps in before it's clear how
        qset = TankTemp.objects.filter().order_by('date_time_stamp').values_list('date_time_stamp', 'temperature_data')[::150]
        labels = []
        default_data = []
        for stuff in qset:
            default_data.append(stuff[1])
            dtg = stuff[0].strftime("%d %H:%m")
            labels.append(dtg)

        data = {
            'labels': labels,
            'default_data': default_data,
        }
        return Response(data)
