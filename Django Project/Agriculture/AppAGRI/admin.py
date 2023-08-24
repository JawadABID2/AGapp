from django.contrib import admin
from AppAGRI.models import batvanne, CapSol2, Mqtt_Channel, Data, CapSol, vann, ValveFlow, CapNPK

# Register your models here.

admin.site.register(vann)
admin.site.register(batvanne)
admin.site.register(CapSol)
admin.site.register(CapSol2)
admin.site.register(Data)
admin.site.register(Mqtt_Channel)
admin.site.register(ValveFlow)
admin.site.register(CapNPK)
