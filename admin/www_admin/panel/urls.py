
from django.urls import path,include


from django import views 
from. import views 


urlpatterns = [


    path('', views.login, name = "login"),
    path('listar',views.listar,name = "listar"),
    path('agregar',views.agregar,name = "agregar"),#USUARIOS
    path('actualizar',views.actualizar,name = "actualizar"),#USUARIOS
    path('eliminar',views.eliminar,name = "eliminar"),#USUARIOS
    path('login' , views.index , name = "index" ),



    path('listarprov',views.listar_proveedores,name = "listarproveedores"),#PROVEEDORES
    path('agregarprov', views.registrarproveedor, name = "agregarprov"),#PROVEEDORES

    path('listarrep', views.listar_repuestos, name = "listarrep"),#REPUESTOS
    path('agregarrep', views.registrarrepuesto, name = "agregarrep"),#REPUESTOS
    path('actualizarrepuesto/<int:repuesto_id>/', views.actualizar_repuesto, name="actualizarrepuesto"),#REPUESTOS

    path('listarstock', views.listar_stock, name = "listarstock"),#STOCK
    path('agregarstock', views.registrarstock, name = "agregarstock"),#STOCK


    path('listarsolicitudes', views.listar_solicitudes, name= "listarsolicitudes"),#SOLICITUDES


    path('listarsalidas', views.listar_salidas, name = "listarsalidas"),#SALIDAS
    path('agregarsalida', views.registrarsalidas, name = "agregarsalida")#SALIDAS

]