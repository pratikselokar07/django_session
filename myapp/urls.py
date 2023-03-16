from django import views
from django.urls import path

from .views import *

urlpatterns = [
    path('set',setsession, name='set'),
    path('get',getsession, name='get'),
    path('delete',deletesession, name='delete'),
    
]
