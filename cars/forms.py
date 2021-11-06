from django.forms import ModelForm
from cars.models import Car, Manufacturer


class CarsForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class ManufacturersForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'
