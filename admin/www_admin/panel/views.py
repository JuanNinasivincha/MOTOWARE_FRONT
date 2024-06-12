from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseNotFound
from .models import Usuarios, NumPartes
from django.shortcuts import redirect
import requests


TEMPLATE_DIRS = (

    'os.path.join(BASE_DIR,"templates")'

)

def redirect_to_login(request):
    return redirect('login')


def login(request):
    return render(request , "registration/login.html")

def index(request):
    return render(request , "index_master.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users }
    return render(request , "gestionar-usuarios/lista.html",datos)


def listar_proveedores(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_proveedor'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'gestionar-proveedores/lista.html', {'datos': datos_api})

def registrarproveedor(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre= request.POST.get('nombre')
        ruc = request.POST.get('ruc')
        gmail = request.POST.get('gmail')
        númerocontacto= request.POST.get('númerocontacto')
        estado = request.POST.get('estado')

        url_api_fastapi = 'https://tesis-back-motoware.onrender.com/registrar_proveedor'
         
        data = {
            "id" : id,
            "nombre": nombre,
            "ruc": ruc ,
            "gmail": gmail,
            "númerocontacto": númerocontacto,
            "estado": estado,

        }
       
        response = requests.post(url_api_fastapi, json=data)
        if response.status_code == 200:
           return redirect('listarproveedores')
        else:
           return render(request, "gestionar-proveedores/lista.html", {'error_message': 'Hubo un problema al registrar el proveedor.'})
    else:
        return render(request, "gestionar-proveedores/add.html")





def listar_repuestos(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_repuesto'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'gestionar-repuestos/listar.html', {'datos': datos_api})



def registrarrepuesto(request):
    if request.method == 'POST':
        
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        proveedor_id = request.POST.get('proveedor_id')
        pais_procedencia = request.POST.get('pais_procedencia')
        fecharegistro = request.POST.get('fecharegistro')
        estado = request.POST.get('estado')
        precio = request.POST.get('precio')
        etiqueta_nombre = request.POST.get('etiqueta_nombre')
        valores_atributos = request.POST.get('valores_atributos')
        atributo1 = request.POST.get('atributo1')
        atributo2 = request.POST.get('atributo2')
        valores_atributos = {
            "atributo1": atributo1,
            "atributo2": atributo2
        }
        
        url_api_fastapi  = 'https://tesis-back-motoware.onrender.com/repuestos/'
       


        data = {
            "id": id,
            "nombre": nombre,
            "proveedor_id": proveedor_id,
            "pais_procedencia": pais_procedencia,
            "fecharegistro": fecharegistro,
            "estado": estado,
            "precio": precio,
            "etiqueta_nombre": etiqueta_nombre,
            "valores_atributos": valores_atributos,
        }
        

        response = requests.post(url_api_fastapi, json=data)
        if response.status_code == 200:
            return redirect('listarrep')
        else:
            print(response.text)  
            return render(request, "gestionar-repuestos/listar.html", {'error_message': 'Hubo un problema al registrar el repuesto.'})
    else:
        return render(request, "gestionar-repuestos/add.html")


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
    



