# DJANGO CORE IMPORTS
from django.urls import (include, path)

# THIRD-PARTY IMPORTS
from rest_framework import routers

# URBVAN IMPORTS
from .api.viewsets import (
    LineView,
    LineDetailView,
    RouteView,
    RouteDetailView,
)


urlpatterns_lines = ([
    path('lines/',LineView.as_view(), name='lines-list'),  # NOQA
    path('lines/<str:pk>/', LineDetailView.as_view(), name='lines-detail'),  # NOQA
    path('routes/', RouteView.as_view(), name='routes-list'),  # NOQA
    path('routes/<str:pk>/', RouteDetailView.as_view(), name='routes-detail'),  # NOQA
], 'lines')
