from django.db import models

# Create your models here.


class Mqtt_Channel(models.Model):
    mqtt_channel_id = models.CharField(primary_key=True, max_length= 128)
    channel_name = models.CharField(max_length=128)
    
class vann(models.Model):
    dt=models.DateTimeField(auto_now=True, null=True)
    onoff = models.BooleanField()

    def __str__(self):
        return str(self.onoff)

    def save(self, *args, **kwargs):
        msg=self.onoff
        super(vann, self).save(*args, **kwargs)

        # client.publish("vanne", str(msg))

        # import paho.mqtt.client as mqtt

        # client1 = mqtt.Client()
        # client = mqtt.Client()
        # client1.disconnect()
        # client1.connect("broker.hivemq.com", 1883, 80)
        # client.connect("broker.hivemq.com", 1883, 80)
        # print("..................")
        # print("self :", self.onoff)
        # if (self.onoff == False):
        #     client.publish("test", "0")
        #     print("off")
        # elif (self.onoff == True):
        #     client1.publish("test1","1")  # publish the message typed by the user# publish the message typed by the user
        #     print("on")
        # #client1.disconnect() #disconnect from server
        
class batvanne(models.Model):
    bat = models.FloatField( null=True)
    dt = models.DateTimeField(auto_now=True, null=True)
    
class CapSol(models.Model):
    devId = models.IntegerField()
    Temp = models.FloatField( null=True)
    Hum = models.FloatField( null=True)
    Ec = models.FloatField( null=True)
    Sal = models.FloatField( null=True)
    Bat = models.FloatField( null=True)
    dt = models.DateTimeField(auto_now=True, null=True)
    time=models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.dt)
    # def save(self, *args, **kwargs):
    #     now = datetime.datetime.now()
    #     print("created ...... capteur de sol ",now)

class CapSol2(models.Model):
    devId = models.IntegerField()
    Temp = models.FloatField( null=True)
    Hum = models.FloatField( null=True)
    Ec = models.FloatField( null=True)
    Sal = models.FloatField( null=True)
    Bat = models.FloatField( null=True)
    dt = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.dt)
    
class Data(models.Model):
    ID_Device = models.IntegerField()
    Temp = models.FloatField(null=True)
    Hum = models.FloatField(null=True)
    Ray = models.FloatField(null=True)
    Wind_Speed = models.FloatField(null=True)
    Rain = models.FloatField(null=True)
    Time_Stamp = models.DateTimeField(auto_now_add=True)
    Bat = models.FloatField(null=True)
    alt = models.FloatField(null=True)
    pr = models.FloatField(null=True)
    d = models.FloatField(null=True)
    i = models.IntegerField(null=True)
    def __str__(self):
        return str(self.d) + str(self.Time_Stamp)
    #
    # def save(self, *args, **kwargs):
    #     now = datetime.datetime.now()
    #     x=now.time.strftime("%H:%M:%S")
    #     if not Data.objects.filter(Time_Stamp__date= now.date,Time_Stamp__time=x).exists():
    #         print("not exist ....")
    #
    #     else:
    #         print("data exist ")
    # def save(self, *args, **kwargs):
    #     now = datetime.datetime.now()
    #     print("created ......Weather station ",now)

class ValveFlow(models.Model):
    Id = models.IntegerField(primary_key=True)
    Flow = models.FloatField()
    
    def __str__(self) -> str:
        return "Flow"
# *********************************************************************************
class CapNPK(models.Model):
    devId = models.IntegerField()
    Azoute = models.FloatField( null=True)
    Phosphore = models.FloatField( null=True)
    Potassium = models.FloatField( null=True)
    Bat = models.FloatField( null=True)
    dt = models.DateTimeField(auto_now=True, null=True)
    time=models.TimeField(auto_now=True)


    def __str__(self):
        return str(self.dt)
