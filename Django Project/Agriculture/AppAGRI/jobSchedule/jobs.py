import requests

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

import importlib
import os

DEV_EUI_VALVE = "2ee5270e481778fb"

def getValveFlow() :
    model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
    modelClass = getattr(model_path, 'ValveFlow')
    try :
        data = modelClass.objects.get(Id=0)
        return float(data.Flow)
    except : 
        return None
    
def getMqttChannelName() :
    model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
    modelClass = getattr(model_path, 'Mqtt_Channel')
    try :
        data = modelClass.objects.get(mqtt_channel_id = os.environ.get('MQTT_KEY', 'PRIMARY_KEY_IN_DB')).channel_name
        return str(data)
    except : 
        return None

def getET0():
    url = f"https://wsensa.pythonanywhere.com/api/list"
    result = requests.get(url)
    print("***###***###***###***###***###***###***###***###***###***###***###***###***###***###***###***###***")
    print(result.json()['data'][0])
    flow = getValveFlow()
    print(flow)
    mqtt_channel_name = getMqttChannelName()
    print(mqtt_channel_name)
    eto = result.json()['data'][0]['value']
    duration = (100 * eto) / flow
    rcv_data = {
        'type' : 'LoRaWAN.downlink',
        'devEui' : DEV_EUI_VALVE,
        'data' : {
            'command' : 0xA0,
            'duration' : duration*1000,
            'duration_bytes' : 3
        }
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(mqtt_channel_name, rcv_data)
    print("***###***###***###***###***###***###***###***###***###***###***###***###***###***###***###***###***")
        
def start():
    ET0 = CronTrigger(
		year="*", month="*", day="*", hour="12", minute="5", second="00"
	)
    
    scheduler = BackgroundScheduler()
    scheduler.start()
    
    scheduler.add_job(getET0, trigger=ET0)
    
    scheduler.print_jobs()