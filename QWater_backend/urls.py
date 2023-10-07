from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.LocationListCreate.as_view(), name='location-list-create'),
    path('data/', views.DataListCreate.as_view(), name='data-list-create'),
]
