# DJANGO CORE IMPORTS
from django.db import models

# URBVAN IMPORTS
from apps.stations.models import StationModel
from apps.utils import create_id


class LineModel(models.Model):

    id = models.CharField(
        default=create_id('line_'),
        primary_key=True,
        max_length=30,
        unique=True
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Linea'
    
    def __str__(self):
        return self.name


class RouteModel(models.Model):

    id = models.CharField(
        default=create_id('route_'),
        primary_key=True,
        max_length=30,
        unique=True
    )
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ruta'

    def __str__(self):
        return self.line
