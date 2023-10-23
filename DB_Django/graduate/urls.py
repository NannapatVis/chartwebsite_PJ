from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('chart', views.chart,name='chartB1'),
    path('chartbar2', views.chartbar2,name='chartB2'),
    path('chartdo1', views.chartdo1,name='chartD1'),
    path('chartdo2', views.chartdo2,name='chartD2'),
    path('chartpo1', views.chartpo1,name='chartP1'),
    path('chartpo2', views.chartpo2,name='chartP2'),
    path('chartra1', views.chartra1,name='chartR1'),
    path('chartra2', views.chartra2,name='chartR2'),

]
