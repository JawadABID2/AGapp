from django.db import models






class Devices(models.Model):
    id = models.CharField(db_column='DeviceID', primary_key=True, max_length=255)
    device = models.CharField(db_column='Device', max_length=255, blank=True, null=True)

    


class MoistureTempEcSensor(models.Model):
    devEui = models.ForeignKey(Devices, on_delete=models.CASCADE, db_column='DeviceID',  blank=True, null=True)
    moisture : models.FloatField(db_column='Mosture',  blank=True, null=True)
    temp = models.FloatField(db_column='Temp',  blank=True, null=True)
    ec = models.FloatField(db_column='Ec',  blank=True, null=True)
    sal = models.FloatField(db_column='Sal',  blank=True, null=True)
    batt = models.FloatField(db_column='Batt',  blank=True, null=True)
    date = models.DateTimeField(db_column='Date',  blank=True, null=True)

    


class  NPK(models.Model):
    devEui = models.ForeignKey(Devices, on_delete=models.CASCADE, db_column='DeviceID',  blank=True, null=True)
    nitrogen  = models.FloatField(db_column='Nitrogen ',  blank=True, null=True)
    phosphorus  = models.FloatField(db_column='Phosphorus ',  blank=True, null=True)
    potassium  = models.FloatField(db_column='Potassium ',  blank=True, null=True)
    batt = models.FloatField(db_column='Batt',  blank=True, null=True)
    date = models.DateTimeField(db_column='Date',  blank=True, null=True)

    



class Valve(models.Model):
    devEui = models.ForeignKey(Devices, on_delete=models.CASCADE, db_column='DeviceID',  blank=True, null=True)
    batt = models.FloatField(db_column='Batt',  blank=True, null=True)
    date = models.DateTimeField(db_column='Date',  blank=True, null=True)

    



