from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from cars.forms import CarsForm, ManufacturersForm
from cars.models import Car, Manufacturer

class HomeTemplateView(TemplateView):
    """Default Home view"""
    template_name = 'home.html'

class CarsListView(ListView):
    """List view for cars"""
    model = Car
    template_name = 'cars.html'
    context_object_name = 'car_objects'


class CarsAddFormView(FormView):
    """Form view for cars"""
    form_class = CarsForm
    template_name = 'cars_add_form.html'
    success_url = '/api/cars/'


class CarsPerYearListView(ListView):
    """List view for cars per year"""
    model = Car
    template_name = "cars_per_year.html"
    context_object_name = 'car_objects'

    def get_queryset(self):
        self.year = self.kwargs['year']
        return super(CarsPerYearListView, self).get_queryset().filter(prod_date__year=self.year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.year
        return context


class ManufacturersListView(ListView):
    """List view for manufacturers"""
    model = Manufacturer
    template_name = 'manufacturers.html'
    context_object_name = 'manufacturer_objects'


class ManufacturersPerCountryListView(ListView):
    """List view for manufacturers per country"""
    model = Manufacturer
    template_name = "manufacturers_per_country.html"
    context_object_name = 'manufacturer_objects'

    def get_queryset(self):
        self.country = self.kwargs['country']
        return super(ManufacturersPerCountryListView, self).get_queryset().filter(country=self.country)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = self.country
        return context


class ManufacturersFormView(FormView):
    """Form view for manufacturers"""
    form_class = ManufacturersForm
    template_name = 'manufacturers_form.html'
    success_url = '/api/manufacturers/'
