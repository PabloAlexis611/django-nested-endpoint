from django.urls import path
from .views import CarsListView, CarsAddFormView, CarsPerYearListView, ManufacturersListView, ManufacturersFormView, ManufacturersPerCountryListView, HomeTemplateView

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars-list'),
    path('cars/create/', CarsAddFormView.as_view(), name='cars-create'),
    path('cars/<yyyy:year>/',
         CarsPerYearListView.as_view(), name='cars-per-year-list'),
    path('manufacturers/', ManufacturersListView.as_view(),
         name='manufacturers-list'),
    path('manufacturers/create/', ManufacturersFormView.as_view(),
         name='manufacturers-create'),
    path('manufacturers/<str:country>/',
         ManufacturersPerCountryListView.as_view(), name='manufacturers-per-country-list')
]
