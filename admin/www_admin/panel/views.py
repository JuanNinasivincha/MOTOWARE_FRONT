from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios, NumPartes
from django.shortcuts import redirect
import requests

# Create your views here.

TEMPLATE_DIRS = (

    'os.path.join(BASE_DIR,"templates")'

)


def index(request):
    return render(request , "index_master.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users }
    return render(request , "gestionar-usuarios/lista.html",datos)


def listar_numero_partes(request):
    url_backend = 'https://tesis-motoware-back.onrender.com/consultar_número_de_Partes_especifico'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'gestionar-numero-partes/lista.html', {'datos': datos_api})

def listarrep(request):
    numpartes = NumPartes.objects.all()
    datos = {'Repuestos': numpartes }
    return render(request , "gestionar-repuestos/lista.html",datos)


def visualizarrep(request):
    numpartes = NumPartes.objects.all()
    datos = {'Repuestos': numpartes }
    return render(request, 'gestionar-repuestos/visualizar_detalles.html', datos)


def registrarrep(request):
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
        return render(request , "gestionar-repuestos/add.html")



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

from django.shortcuts import render, redirect
import requests

def agregarnumpartes(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        dientes = request.POST.get('dientes')
        aros = request.POST.get('aros')
        litros = request.POST.get('litros')
        fecharegistro = request.POST.get('fecharegistro')

        url_api_fastapi = 'https://tesis-motoware-back.onrender.com/registrar_número_de_Partes'
         
        data = {
            "ID" : id,
            "Nombre": nombre,
            "Dientes": dientes,
            "Aros": aros,
            "Litros": litros,
            "fechaRegistro": fecharegistro
        }
       
        response = requests.post(url_api_fastapi, json=data)
        if response.status_code == 200:
           return redirect('listarnum')
        else:
           return render(request, "gestionar-numero-partes/add.html", {'error_message': 'Hubo un problema al registrar el número de partes.'})
    else:
        return render(request, "gestionar-numero-partes/add.html")


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
    



