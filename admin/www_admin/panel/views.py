from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.

TEMPLATE_DIRS = (

    'os.path.join(BASE_DIR,"templates")'

)

def index(request):
    return render(request , "index.html")


def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users }
    return render(request , "gestionar-usuarios/lista.html",datos)


def agregar(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('telefono') and request.POST.get('fecha_nacimiento'):
           user = Usuarios()
           user.nombre = request.POST.get('nombre')
           user.apellido = request.POST.get('apellido')
           user.correo =  request.POST.get('correo')
           user.telefono =  request.POST.get('telefono')
           user.fecha_nacimiento = request.POST.get('fecha_nacimiento')
           user.save()
           return redirect('listar')
    else :
        return render(request , "gestionar-usuarios/add.html")


def actualizar(request):
    if request.method == 'POST':
        if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('telefono') and request.POST.get('fecha_nacimiento'):
           user_id_old = request.POST.get('id')
           user_old = Usuarios()
           user_old = Usuarios.objects.get(id = user_id_old )

           user = Usuarios()
           user.id = request.POST.get('id')
           user.nombre = request.POST.get('nombre')
           user.apellido = request.POST.get('apellido')
           user.correo =  request.POST.get('correo')
           user.telefono =  request.POST.get('telefono')
           user.fecha_nacimiento = request.POST.get('fecha_nacimiento')
           user.fecha_registro = user_old.fecha_registro
           user.save()
           return redirect('listar')

    else: 
        users = Usuarios.objects.all()
        datos = {'usuarios': users }
        return render(request , "gestionar-usuarios/update.html",datos)


def eliminar(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            id_delete = request.POST.get('id')
            tupla = Usuarios.objects.get(id = id_delete)
            tupla.delete()
            return redirect('listar')
    else: 
        users = Usuarios.objects.all()
        datos = {'usuarios': users }
        return render(request , "gestionar-usuarios/eliminar.html",datos) 

