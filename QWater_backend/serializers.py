from rest_framework import serializers
from .models import Location, Status, DataType, Data, DataValue


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class DataValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataValue
        fields = '__all__'
