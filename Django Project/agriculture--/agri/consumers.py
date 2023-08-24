from mqttasgi.consumers import MqttConsumer
import json
from channels.generic.websocket import WebsocketConsumer
from agri.models import Valve, NPK, MoistureTempEcSensor, Devices 
from asgiref.sync import async_to_sync
# t = TestEnv.objects.values_list('date', flat=True)
# temp = TestEnv.objects.values_list('temperature', flat=True)
# print(t)
# print("\n")
# print(t)
# temperature = []
# def test() :
#     for i in temp:
#       temperature.append(i.temperature)
# test() 
# print(temperature)

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
       pass
    def receive(self, text_data):
        pass

    def chat_message(self, event):
        args = event['handler_args']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message_value':args['data'],
            'src' : args['id_src']
        }))

class MyMqttConsumer(MqttConsumer):
    devices_list = []
    async def connect(self):
        print('New MQTT connexion')
        await self.subscribe('application/367c9132-5f89-442e-b606-e4e7a3bdb833/device/+/event/up', 2)

       
    async def receive(self, mqtt_message):
        infs = json.loads(mqtt_message['payload'])
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', infs["deviceInfo"]["devEui"])
        print('And QOS:', mqtt_message['qos'])

        await self.store_device(infs["deviceInfo"]["devEui"])

    async def store_device_info(self, dev_eui):
        # Assuming you have a model class named "Device" to store the device information
        device = Device(dev_eui)
        # Perform any additional processing or storage operations here
        # For example, you could save the device to a database or perform some other action
        await device.save()
            







    async def disconnect(self):
        await self.unsubscribe('application/367c9132-5f89-442e-b606-e4e7a3bdb833/device/+/event/up')
