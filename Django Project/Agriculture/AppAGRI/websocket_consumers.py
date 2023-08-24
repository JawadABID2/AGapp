from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import importlib
import json
from AppAGRI.models import Mqtt_Channel
import os

def pushDB(modelClassName, data : dict):
    model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
    modelClass = getattr(model_path, modelClassName)
    modelObj = modelClass()
    for field in data.keys() :
        if hasattr(modelObj, field) :
            setattr(modelObj, field, data[field])      
    modelObj.save()

def getRow(modelClassName, condition:dict):
    """Condition is the dict value that contain the fields in key and their value to match in the database"""
    model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
    modelClass = getattr(model_path, modelClassName)
    try :
        data = modelClass.objects.get(**condition)
        return data
    except : 
        return None

def delRow(modelClassName, condition:dict):
    row = getRow(modelClassName, condition)
    if(row != None):
        _delete = lambda _row : _row.delete()
        _delete(row)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_add)("mqtt.group", self.channel_name)
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        rcv_data = json.loads(text_data)
        if('type' in rcv_data.keys()):
            mqtt_channel_name = Mqtt_Channel.objects.get(mqtt_channel_id = os.environ.get('MQTT_KEY', 'PRIMARY_KEY_IN_DB')).channel_name
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.send)(mqtt_channel_name, rcv_data)
        
        if('DnameBFlow' in rcv_data.keys()):
            print(rcv_data)
            delRow(rcv_data['DnameBFlow'], {'Id' : 0})
            pushDB(rcv_data['DnameBFlow'], {'Id' : 0, 'Flow' : rcv_data['Flow']})
            
        # insert = {
        #     'channel_name' : 'custom',
        #     'field1' : 'cust',
        #     'field2' : 12
        # }
        # pushDB("Mqtt_Channel", insert)
        
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)('mqtt.group', {
        #     'type' : 'mqtt.send.message',
        #     'message' : text_data
        # })
    
    def client_message(self, event):
        print("In websocket from mqtt consumer :\n" ,event)
        
    def mqtt_send_message(self, event):
        print("In websocket from client consumer :\n" , event)

