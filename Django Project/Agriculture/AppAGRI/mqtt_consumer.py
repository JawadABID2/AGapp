from mqttasgi.consumers import MqttConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
import importlib
import os
from base64 import b64encode
import json
#2ee5270e481778ff
DOWNLINK_TOPIC = "application/c09c71b9-c566-4f25-89e7-037d9cf185e2/device/2ee5270e481778fb/command/down"
DEV_EUI_SOL1 = "13e08e2951742243"
DEV_EUI_SOL2 = "6f8e5550f7ec89e9"
DEV_EUI_VALVE = "2ee5270e481778fb" 
DEV_EUI_NPK = "71ca6b16b8e4ac42"

def base64Cvrt(data:dict):
    _out = ""
    for key in data.keys():
        if key.split('_')[-1] == "bytes":
            continue
        n = 1
        n_key = key + "_bytes"
        if n_key in data.keys():
            n = data[n_key]
        out = hex(int(data[key]))[2:]
        if len(out) < 2*n :
            for _ in range(2*n - len(out)):
                out = '0' + out
        _out += out
    
    return b64encode(bytes.fromhex(_out)).decode()

class MqttChannelConsumer(MqttConsumer):
    async def connect(self):
        print("MQTT CONNECTION")
        await self.subscribe('application/c09c71b9-c566-4f25-89e7-037d9cf185e2/device/+/event/up', 2)
        # await self.subscribe('application/9e071e11-d8bd-4dad-b992-dac8d24ceba4/device/+/event/up', 3)
        # await self.subscribe('application', 2)     
        # channel_layer = get_channel_layer() 
        # await channel_layer.group_add("mqtt.group", self.channel_name) 
        
        await self.delRow("Mqtt_Channel", {"mqtt_channel_id" : os.environ.get('MQTT_KEY', 'PRIMARY_KEY_IN_DB')})  
        await self.pushDB("Mqtt_Channel", {
            "mqtt_channel_id" : os.environ.get('MQTT_KEY', 'PRIMARY_KEY_IN_DB'),
            "channel_name":self.channel_name
        }) 
                           

    async def receive(self, mqtt_message):
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', mqtt_message['payload'])
        
        # sol_table = {DEV_EUI_SOL1 : "CapSol", DEV_EUI_SOL2 : "CapSol2"}
        
        # db_data = {"devId":2, "Temp":29, "Hum":0, "Ec":0, "Sal":0, "Bat":3.7}
        # await self.pushDB(sol_table["13e08e2951742243"], db_data)
        
        tx_data = json.loads(mqtt_message['payload'])
        dev_eui = tx_data["deviceInfo"]["devEui"]
        payload_data = tx_data["object"]["bytes"]
        xpayload_data = [int(_byte) for _byte in payload_data]
        taille_xpayload_data = len(xpayload_data)
        sol_table = {DEV_EUI_SOL1 : "CapSol", DEV_EUI_SOL2 : "CapSol2"}
        print(dev_eui)
        print(xpayload_data)
        print(taille_xpayload_data)
        print(list(sol_table.keys()))
        if dev_eui in list(sol_table.keys()):
            if dev_eui == DEV_EUI_SOL1 :

                id_dev = 2
            else :
                id_dev = 3
            if taille_xpayload_data == 14:
                temp = (xpayload_data[0] * 256) + xpayload_data[1]
                temp = float(temp/100)
                
                hum = (xpayload_data[2] * 256) + xpayload_data[3]
                hum = float(hum/100)
                
                ec = (xpayload_data[4] * 256) + xpayload_data[5]
                ec = float(ec)
                
                sal = (xpayload_data[6] * 256) + xpayload_data[7]
                sal = float(sal)
                
                v_batt = (xpayload_data[8] * 256) + xpayload_data[9]
                v_batt = float(v_batt/100)
                
                deepsleep = (xpayload_data[13] << 24)  + (xpayload_data[12] << 16) + (xpayload_data[11] << 8) + (xpayload_data[10])
                print('deepsleep : ', deepsleep)
                
                db_data = {"devId":id_dev, "Temp":temp, "Hum":hum, "Ec":ec, "Sal":sal, "Bat":v_batt}
                await self.pushDB(sol_table[dev_eui], db_data)
            else :
                print("ya pas des données????!!!!")
                v_batt = (xpayload_data[0] * 256) + xpayload_data[1]
                v_batt = float(v_batt/100)
                print(v_batt)
                deepsleep = (xpayload_data[5] << 24)  + (xpayload_data[4] << 16) + (xpayload_data[3] << 8) + (xpayload_data[2])
                print('deepsleep : ', deepsleep)
                # db_data = {"devId":id_dev, "Bat":v_batt}
                
            
        if dev_eui == DEV_EUI_VALVE:
            v_batt = (xpayload_data[0] * 256) + xpayload_data[1]
            v_batt = float(v_batt/100)
            
            deepsleep = (xpayload_data[5] << 24)  + (xpayload_data[4] << 16) + (xpayload_data[3] << 8) + (xpayload_data[2])
            print('deepsleep ev : ', deepsleep)
            
            db_data = {"bat":v_batt}
            
            await self.pushDB("batvanne", db_data)
        if dev_eui == DEV_EUI_NPK:
            if taille_xpayload_data == 12:
                azt = (xpayload_data[0]*256) + xpayload_data[1]
                azt = float(azt)
                pho = (xpayload_data[2]*256) + xpayload_data[3]
                pho = float(pho)
                pot = (xpayload_data[4]*256) + xpayload_data[5]
                pot = float(pot)
                v_batt = (xpayload_data[6]*256) + xpayload_data[7]
                v_batt = float(v_batt/100)
                deepsleep = (xpayload_data[8]) + (xpayload_data[9] << 8) + (xpayload_data[10] << 16) + (xpayload_data[11] << 24)
                print("deepsleep : ", deepsleep)
                db_data = {"devId":4, "Azoute":azt, "Phosphore":pho, "Potassium":pot, "Bat":v_batt}
                await self.pushDB("CapNPK", db_data)
            else :
                print("ya pas des données????!!!!")
                v_batt = (xpayload_data[0] * 256) + xpayload_data[1]
                v_batt = float(v_batt/100)
                print(v_batt)
                deepsleep = (xpayload_data[5] << 24)  + (xpayload_data[4] << 16) + (xpayload_data[3] << 8) + (xpayload_data[2])
                print('deepsleep : ', deepsleep)
                # db_data = {"devId":4, "Bat":v_batt}
            


    async def disconnect(self):
        # await self.unsubscribe('application/367c9132-5f89-442e-b606-e4e7a3bdb833/device/+/event/up')
        await self.subscribe('application', 2)
        
    async def mqtt_send_message(self, event):
        print("In mqtt from client consumer :\n" , event)
        
    async def client_message(self, event):
        print("In mqtt from mqtt consumer :\n" ,event)
    
    async def LoRaWAN_downlink(self, event):
        print("In mqtt from mqtt consumer :\n" ,event)
        try :
            data = base64Cvrt(event['data'])
            message = {
                "devEui" : event['devEui'],
                "confirmed" : False,
                "fPort" : 1,
                "data" : data
            }
            await self.publish(DOWNLINK_TOPIC, json.dumps(message))
        except :
            print("error")

    @database_sync_to_async
    def getRow(self, modelClassName, condition:dict):
        """Condition is the dict value that contain the fields in key and their value to match in the database"""
        model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
        modelClass = getattr(model_path, modelClassName)
        try :
            data = modelClass.objects.get(**condition)
            return data
        except : 
            return None
    
    async def delRow(self, modelClassName, condition:dict):
        row = await self.getRow(modelClassName, condition)
        if(row != None):
            _delete = lambda _row : _row.delete()
            await database_sync_to_async(_delete)(row)
    
    @database_sync_to_async
    def pushDB(self, modelClassName, data : dict):
        model_path = importlib.import_module(os.environ.get('DATABASE_MODEL_MODULE', '.models'))
        modelClass = getattr(model_path, modelClassName)
        modelObj = modelClass()
        for field in data.keys() :
            if hasattr(modelObj, field) :
                setattr(modelObj, field, data[field])      
        print("****************** : ",modelObj)
        modelObj.save()