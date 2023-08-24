from rest_framework import serializers
from AppAGRI.models import CapSol, CapSol2, batvanne, CapNPK, ValveFlow

class capsolSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapSol
        fields = '__all__'
        
class capsol2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CapSol2
        fields = '__all__'
        
class batvannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = batvanne
        fields = '__all__'

# ********************************************************************************************
class capnpkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapNPK
        fields = '__all__'
class valveFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValveFlow
        fields = '__all__'