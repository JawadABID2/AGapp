from django.urls import path 
from . import  views
urlpatterns = [
    # path('devices/sensor/<str:id>', views.diagramms, name = 'sensors'),
    path('', views.v_Overview, name='overview'),
    path('devices/', views.v_Devices, name='devices'),
    path('devices/actuators/<str:id>', views.v_Actuator, name='actuators'),
]