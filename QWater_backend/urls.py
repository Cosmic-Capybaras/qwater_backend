from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.LocationListCreate.as_view(), name='location-list-create'),
    path('data/', views.DataListCreate.as_view(), name='data-list-create'),
    path('data-types/', views.DataTypeListCreate.as_view(), name='data-type-list-create'),
    path('status/', views.StatusListCreate.as_view(), name='status-list-create'),
    path('latest-data/<int:location_id>/', views.LatestDataForLocation.as_view(), name='latest-data-for-location'),
    path('data/create/', views.CreateData.as_view(), name='data-create'),
]
