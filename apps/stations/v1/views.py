# coding: utf8
# THIRD-PARTY IMPORTS
from rest_framework import viewsets
from rest_framework import mixins

# URBVAN IMPORTS 
from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDeleteView,
)
from .schemas import (
    LocationSchema,
    StationSchema,
)
from .serializers import (
    LocationSerializer,
    StationSerializer,
)
from ..models import (
    LocationModel,
    StationModel,
)


class LocationView(ListCreateView):

    queryset = LocationModel.objects.get_queryset().order_by('id')
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationDetailView(RetrieveUpdateDeleteView):
    '''
        A viewset for retrieve, update and delete a Location
        @author Christian Buendia
    '''
    queryset = LocationModel.objects.get_queryset().order_by('id')
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationView(ListCreateView):

    queryset = StationModel.objects.get_queryset().order_by('id')
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationDetailView(RetrieveUpdateDeleteView):
    '''
        A viewset for retrieve, update and delete a Station
        @author Christian Buendia
    '''
    queryset = StationModel.objects.get_queryset().order_by('id')
    schema_class = StationSchema
    serializer_class = StationSerializer
