from django.shortcuts import render
# from .models import TestEnv
import json

# def diagramms(request, id):
#     labels = TestEnv.objects.values_list('date', flat=True)
#     temperature = TestEnv.objects.values_list('temperature', flat=True)
#     humidity = TestEnv.objects.values_list('humidity',flat=True)
#     battery = TestEnv.objects.values_list('battery', flat=True)
#     CO2 = TestEnv.objects.values_list('co2', flat = True)
#     context = { 'context' : json.dumps({
#             'labels': list(map(str,labels)),
#             'temperature': list(temperature),
#             'humidity': list(humidity),
#             'battery' : list(battery),
#             'CO2' : list(CO2),
#         }), 
#         'data' : id,
    # }
    # return render(request, 'moisture_sensor.html', context)

def v_Overview(request):
    return render(request, 'overview.html' )

def v_Devices(request):
    return render(request, 'devices.html')

def v_Actuator(request, id):
    context = {
        "data" : id
    }
    return render(request, 'electrovanne.html', context=context)


