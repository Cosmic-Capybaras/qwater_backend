from rest_framework import generics
from .models import Location, Data
from .serializers import LocationSerializer, DataSerializer


class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DataListCreate(generics.ListCreateAPIView):
    queryset = Data.objects.all().order_by('-created_at')
    serializer_class = DataSerializer
