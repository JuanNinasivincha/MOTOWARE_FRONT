
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
    path('agregarprov', views.registrarproveedor, name = "agregarprov"),

    path('listarrep', views.listar_repuestos, name = "listarrep"),
    path('agregarrep', views.registrarrepuesto, name = "agregarrep"),
    path('actualizarrepuesto/<int:repuesto_id>/', views.actualizar_repuesto, name="actualizarrepuesto"),

    path('listarstock', views.listar_stock, name = "listarstock"),
    path('agregarstock', views.registrarstock, name = "agregarstock"),


    path('listarsolicitudes', views.listar_solicitudes, name= "listarsolicitudes"),


    path('listarsalidas', views.listar_salidas, name = "listarsalidas"),
    path('agregarsalida', views.registrarsalidas, name = "agregarsalida")

]