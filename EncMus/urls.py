from django.urls import path
from EncMus import Views
from .Views import *



urlpatterns = [
       path('', inicio), 
       path('musicos', musicos),
       path('bandas', bandas),
       path('barandpubs', barandpubs),
       path('salasensayo', salasensayo),
       path('productores', productores),
    ]
