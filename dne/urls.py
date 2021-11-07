"""dne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from . import converters
from cars.views import CarsListView, CarsAddFormView, CarsPerYearListView, ManufacturersListView, ManufacturersFormView, ManufacturersPerCountryListView, HomeTemplateView

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('api/cars/', CarsListView.as_view(), name='cars-list'),
    path('api/cars/create/', CarsAddFormView.as_view(), name='cars-create'),
    path('api/cars/<yyyy:year>/',
         CarsPerYearListView.as_view(), name='cars-per-year-list'),
    path('api/manufacturers/', ManufacturersListView.as_view(),
         name='manufacturers-list'),
    path('api/manufacturers/create/', ManufacturersFormView.as_view(),
         name='manufacturers-create'),
    path('api/manufacturers/<str:country>/',
         ManufacturersPerCountryListView.as_view(), name='manufacturers-per-country-list')
]
