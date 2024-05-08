
from django.urls import path,include

from django import views 
from. import views 


urlpatterns = [

    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.index,name = "index"),
    path('listar',views.listar,name = "listar"),
    path('agregar',views.agregar,name = "agregar"),
    path('actualizar',views.actualizar,name = "actualizar"),
    path('eliminar',views.eliminar,name = "eliminar"),


    path('listarnum',views.listar_numero_partes,name = "listarnum"),
    path('agregarnum',views.agregarnumpartes,name = "agregarnum"),

    path('listarrep',views.listarrep,name = "listarrep"),
    path('visualizarrep',views.visualizarrep,name = "visualizarrep"),
    path('registrarrep',views.registrarrep,name = "registrarrep"),

    



]