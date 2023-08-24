from django.contrib import admin
from .models import Devices, MoistureTempEcSensor, NPK, Valve

# Register your models here.

admin.site.register(Valve)
admin.site.register(Devices)
admin.site.register(MoistureTempEcSensor)
admin.site.register(NPK)