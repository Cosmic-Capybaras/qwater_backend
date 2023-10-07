from django.db import models
from django.utils import timezone


class Location(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()


class Status(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class DataType(models.Model):
    name = models.CharField(max_length=255)


class Data(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    test_date = models.DateTimeField(default=timezone.now)


class DataValue(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)
    string_value = models.CharField(max_length=255, null=True, blank=True)
