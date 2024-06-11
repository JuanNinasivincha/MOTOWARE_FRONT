
from django.urls import path,include


from django import views 
from. import views 


urlpatterns = [


    path('', views.login, name = "login"),
    path('listar',views.listar,name = "listar"),
    path('agregar',views.agregar,name = "agregar"),
    path('actualizar',views.actualizar,name = "actualizar"),
    path('eliminar',views.eliminar,name = "eliminar"),
    path('login' , views.index , name = "index" ),


    path('listarprov',views.listar_proveedores,name = "listarproveedores"),
    path('agregarprov', views.registrarproveedor, name = "agregarprov")
    
    

]