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


class DataValueSerializer(serializers.ModelSerializer):
    data_type_name = serializers.StringRelatedField(source='data_type.name', read_only=True)

    class Meta:
        model = DataValue
        fields = ('data_type', 'data_type_name', 'value', 'string_value')


class DataSerializer(serializers.ModelSerializer):
    data_values = DataValueSerializer(many=True, read_only=True, source='datavalue_set')
    location_title = serializers.StringRelatedField(source='location.title', read_only=True)
    location_city = serializers.StringRelatedField(source='location.city', read_only=True)
    location_country = serializers.StringRelatedField(source='location.country', read_only=True)

    class Meta:
        model = Data
        fields = ('location', 'location_title', 'location_city', 'location_country', 'status', 'description', 'test_date', 'data_values')


class DataCreateSerializer(serializers.ModelSerializer):
    data_values = DataValueSerializer(many=True, write_only=True)

    class Meta:
        model = Data
        fields = ('location', 'status', 'description', 'test_date', 'data_values')

    def create(self, validated_data):
        data_values = validated_data.pop('data_values', [])
        data_instance = Data.objects.create(**validated_data)

        for dv in data_values:
            DataValue.objects.create(data=data_instance, **dv)

        return data_instance
