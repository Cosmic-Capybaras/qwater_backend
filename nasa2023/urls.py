from django.contrib import admin
from django.urls import path
from QWater_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', views.LocationListCreate.as_view(), name='location-list-create'),
    path('data/', views.DataListCreate.as_view(), name='data-list-create'),
]
