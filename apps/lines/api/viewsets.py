# THIRD-PARTY IMPORTS
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import mixins

# URBVAN IMPORTS
from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDeleteView,
)
from urbvan_framework.authentication import CustomTokenAuthentication
from urbvan_framework.permissions import IsManagerOrReadOnly
from .serializers import (
    LineModelSerializer,
    RouteModelSerializer,
)
from ..models import (
    LineModel,
    RouteModel,
)
from .schemas import LineSchema, RouteSchema


class LineView(ListCreateView):

    queryset = LineModel.objects.get_queryset().order_by('id')
    schema_class = LineSchema
    serializer_class = LineModelSerializer


class LineDetailView(RetrieveUpdateDeleteView):
    '''
        A viewset for retrieve, update and delete a Line
        @author Christian Buendia
    '''
    queryset = LineModel.objects.get_queryset().order_by('id')
    schema_class = LineSchema
    serializer_class = LineModelSerializer
    permission_classes = (IsManagerOrReadOnly, )


class RouteView(ListCreateView):

    queryset = RouteModel.objects.get_queryset().order_by('id')
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer


class RouteDetailView(RetrieveUpdateDeleteView):
    '''
        A viewset for retrieve, update and delete a Route
        @author Christian Buendia
    '''
    queryset = RouteModel.objects.get_queryset().order_by('id')
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer
    permission_classes = (IsManagerOrReadOnly, )
