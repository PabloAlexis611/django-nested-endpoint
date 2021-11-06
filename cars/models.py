from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.TextChoices):
    WHITE = 'WHITE', _("White")
    BLACK = 'BLACK', _("Black")
    GRAY = 'GRAY', _("Gray")
    BLUE = 'BLUE', _("Blue")
    RED = 'RED', _("Red")


class Engine(models.TextChoices):
    V6 = 'V6', _("V6")
    V8 = 'V8', _("V8")
    V12 = 'V12', _("V12")


class Transmission(models.TextChoices):
    MANUAL = 'M', _("Manual")
    AUTOMATIC = 'A', _("Automatic")


class Drivetrain(models.TextChoices):
    AWD = 'AWD', _("All Wheel Drive")
    FWD = 'FWD', _("Front Wheel Drive")
    RWD = 'RWD', _("Rear Wheel Drive")


class Manufacturer(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    creation_date = models.DateField(
        _("Creation date"), auto_now=False, auto_now_add=False)
    country = models.CharField(_("Country"), max_length=50)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(_("Model"), max_length=50)
    color = models.CharField(_("Color"), max_length=5, choices=Color.choices)
    engine_type = models.CharField(
        _("Engine Type"), max_length=4, choices=Engine.choices)
    transmission_type = models.CharField(
        _("Transmission Type"), max_length=9, choices=Transmission.choices)
    drivetrain_type = models.CharField(
        _("Drivetrain Type"), max_length=3, choices=Drivetrain.choices)
    prod_date = models.DateField(
        _("Manafacturing date"), auto_now=False, auto_now_add=False)
