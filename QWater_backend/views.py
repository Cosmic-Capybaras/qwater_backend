from rest_framework import generics
from .models import Location, Data, DataType, Status
from .serializers import LocationSerializer, DataSerializer, DataTypeSerializer, StatusSerializer


class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DataListCreate(generics.ListCreateAPIView):
    queryset = Data.objects.all().order_by('-created_at')
    serializer_class = DataSerializer


class DataTypeListCreate(generics.ListCreateAPIView):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer


class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
