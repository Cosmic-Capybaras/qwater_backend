from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Location, Data, DataType, Status
from .serializers import LocationSerializer, DataSerializer, DataTypeSerializer, StatusSerializer, DataCreateSerializer


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


class LatestDataForLocation(APIView):
    def get(self, request, location_id, *args, **kwargs):
        try:
            location = Location.objects.get(id=location_id)
            latest_data = Data.objects.filter(location_id=location_id).latest('created_at')
            serializer = DataSerializer(latest_data)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response({"error": "No such location found"}, status=status.HTTP_404_NOT_FOUND)
        except Data.DoesNotExist:
            return Response({"error": "No data found for the given location"}, status=status.HTTP_404_NOT_FOUND)



class CreateData(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DataCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)