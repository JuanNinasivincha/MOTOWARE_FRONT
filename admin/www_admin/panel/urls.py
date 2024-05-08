
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

    path('listarreplit',views.listarreplit,name = "listarreplit"),
    path('listarreparos',views.listarreparos,name = "listarreparos"),
    path('listarrepgeneral',views.listarrepgeneral,name = "listarrep"),


    path('visualizarrepgeneral/<int:repuesto_id>',views.visualizarrep,name = "visualizarrepgeneral"),
    path('visualizarreparos/<str:repuesto_id>',views.visualizarreparos,name = "visualizarreparos"),
    #path('visualizarreplit/<int:repuesto_id>',views.visualizarrep,name = "visualizarrep"),

    path('registrarrep',views.registrarrep,name = "registrarrep")
    



]