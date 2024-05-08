from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseNotFound
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

def listarreplit(request):
    url_backend = 'https://tesis-motoware-back.onrender.com/consultar_repuestoLitros'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request , "gestionar-repuestos/listarlitros.html", {'datos': datos_api})

def listarrepgeneral(request):
    url_backend = 'https://tesis-motoware-back.onrender.com/consultar_repuesto_especifico'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request , "gestionar-repuestos/listargeneral.html", {'datos': datos_api})


def listarreparos(request):
    url_backend = 'https://tesis-motoware-back.onrender.com/consultar_repuestoAros'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request , "gestionar-repuestos/listararos.html", {'datos': datos_api})

def visualizarreparos(request,repuesto_id):
    url_backend = f'https://tesis-motoware-back.onrender.com/obtener_repuestoAros/{repuesto_id}'
    try:
        response = requests.get(url_backend)
        repuesto_data = response.json()

    except requests.RequestException as e:
        print(f"Error al obtener los datos del repuesto: {e}")
        return HttpResponseNotFound("No se pudo obtener el repuesto. Por favor, inténtalo de nuevo más tarde.")
   
    if repuesto_data is None:
         return HttpResponseNotFound("No se encontró ningún repuesto con el ID proporcionado.")
    return render(request, 'gestionar-repuestos/visualizardetallesaro.html', {'repuesto_data' : repuesto_data})
    

def visualizarrep(request,repuesto_id):
  
    url_backend = f'https://tesis-motoware-back.onrender.com/obtener_repuesto_id/{repuesto_id}'
    try:
        response = requests.get(url_backend)
        repuesto_data = response.json()

    except requests.RequestException as e:
        print(f"Error al obtener los datos del repuesto: {e}")
        return HttpResponseNotFound("No se pudo obtener el repuesto. Por favor, inténtalo de nuevo más tarde.")
   
    if repuesto_data is None:
         return HttpResponseNotFound("No se encontró ningún repuesto con el ID proporcionado.")
    return render(request, 'gestionar-repuestos/visualizarrepgeneral.html', {'repuesto_data' : repuesto_data})

def visualizarreplit(request,repuesto_id):
    
    url_backend = f'https://tesis-motoware-back.onrender.com/obtener_repuestoLitros/{repuesto_id}'
    try:
        response = requests.get(url_backend)
        repuesto_data = response.json()

    except requests.RequestException as e:
        print(f"Error al obtener los datos del repuesto: {e}")
        return HttpResponseNotFound("No se pudo obtener el repuesto. Por favor, inténtalo de nuevo más tarde.")
   
    if repuesto_data is None:
         return HttpResponseNotFound("No se encontró ningún repuesto con el ID proporcionado.")
    return render(request, 'gestionar-repuestos/visualizardetallelitros.html', {'repuesto_data' : repuesto_data})


def registrarrep(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        partesLi= request.POST.get('partesli')
        codigoMarca = request.POST.get('codigoMarca')
        gradoViscosidad = request.POST.get('gradoViscosidad')
        tipoMotor = request.POST.get('tipoMotor')
        calidad = request.POST.get('calidad')
        Litros = request.POST.get('Litros')
        fechaRegistro = request.POST.get('fechaRegistro')
        Estado = request.POST.get('Estado')                            

        url_api_fastapi = 'https://tesis-motoware-back.onrender.com/registrar_repuestoLitros'
         
        data = {
            "ID" : ID,
            "partesLi": partesLi,
            "codigoMarca": codigoMarca ,
            "gradoViscosidad": gradoViscosidad,
            "tipoMotor": tipoMotor,
            "calidad": calidad,
            "Litros": Litros,
            "fechaRegistro": fechaRegistro,
            "Estado": Estado,

        }
       
        response = requests.post(url_api_fastapi, json=data)
        if response.status_code == 200:
           return redirect('listarlitros')
        else:
           return render(request, "gestionar-repuestos/listarlitros.html", {'error_message': 'Hubo un problema al registrar el repuesto litros.'})
    else:
        return render(request, "gestionar-repuestos/add.html")


def registrarreparo(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        partesAr= request.POST.get('partesAr')
        medidaA1 = request.POST.get('medidaA1')
        medidaA2 = request.POST.get('medidaA2')
        medidaA3= request.POST.get('medidaA3')
        codigoLlanta= request.POST.get('codigoLlanta')
        camara = request.POST.get('camara')
        fechaRegistro = request.POST.get('fechaRegistro')
        Estado = request.POST.get('Estado')                            

        url_api_fastapi = 'https://tesis-motoware-back.onrender.com/registrar_repuestoAros'
         
        data = {
            "ID" : ID,
            "partesAr": partesAr,
            "medidaA1": medidaA1 ,
            "medidaA2": medidaA2,
            "medidaA3": medidaA3,
            "codigoLlanta": codigoLlanta,
            "Camara": camara,
            "fechaRegistro": fechaRegistro,
            "Estado": Estado,

        }
       
        response = requests.post(url_api_fastapi, json=data)
        if response.status_code == 200:
           return redirect('listararos')
        else:
           return render(request, "gestionar-repuestos/listararos.html", {'error_message': 'Hubo un problema al registrar el repuesto litros.'})
    else:
        return render(request, "gestionar-repuestos/addaro.html")




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
    



