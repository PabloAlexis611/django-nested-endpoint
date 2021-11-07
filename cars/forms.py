from django.forms import ModelForm
from django.forms.widgets import DateInput
from cars.models import Car, Manufacturer


class CarsForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'prod_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }

class ManufacturersForm(ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'
        widgets = {
            'creation_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }
