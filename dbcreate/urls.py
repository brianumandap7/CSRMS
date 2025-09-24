from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import gdb, rodb, classdb, sevdb, tlpdb, statdb, iprdb

urlpatterns = [
    path('gdb/', views.gdb.as_view(), name='gdb'),
    path('rodb/', views.rodb.as_view(), name='rodb'),
    path('respdb/', views.respdb.as_view(), name='respdb'),
    path('classdb/', views.classdb.as_view(), name='classdb'),
    path('sevdb/', views.sevdb.as_view(), name='sevdb'),
    path('tlpdb/', views.tlpdb.as_view(), name='tlpdb'),
    path('statdb/', views.statdb.as_view(), name='statdb'),
    path('iprdb/', views.iprdb.as_view(), name='iprdb'),
]

