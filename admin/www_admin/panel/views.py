from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseNotFound, JsonResponse
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

def listar_stock(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_stock'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'stock/listar_stock.html', {'datos': datos_api})





def registrarstock(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        idrepuesto= request.POST.get('idrepuesto')
        nombrerepuesto = request.POST.get('nombrerepuesto')
        cantidad = request.POST.get('cantidad')
        estados= request.POST.get('estados')
        ubicacion = request.POST.get('ubicacion')

        url_api_fastapi = 'https://tesis-back-motoware.onrender.com/registrar_stock/'
         
        data = {
            "id" : id,
            "idrepuesto": idrepuesto,
            "nombrerepuesto": nombrerepuesto ,
            "cantidad": cantidad,
            "estados": estados,
            "ubicacion": ubicacion,

        }
       
        response = requests.post(url_api_fastapi, json=data)
        print(f"Estado de respuesta de la API: {response.status_code}")
        print(f"Contenido de respuesta de la API: {response.content}")
        if response.status_code == 200:
           return redirect('listarstock')
        else:
           return render(request, "stock/listar_stock.html", {'error_message': 'Hubo un problema al registrar el stock.'})
    else:
        return render(request, "stock/add.html")
    
def listar_solicitudes(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_solicitudMecanico'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'gestionar-solicitudes/list.html', {'datos': datos_api})


def listar_salidas(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_salidas'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'movimientos/listamovimientos.html', {'datos': datos_api})

def registrarsalidas(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        idstock= request.POST.get('idstock')
        cantidadsaliente = request.POST.get('cantidadsaliente')
        ubicacionstock= request.POST.get('ubicacionstock')
        destino= request.POST.get('destino')
        detallecliente = request.POST.get('detallecliente')
        horasalida = request.POST.get('horasalida')
        idsolicitud = request.POST.get('idsolicitud')

        url_api_fastapi = 'https://tesis-back-motoware.onrender.com/registrar_salida'


        data = {
            "id" : id,
            "idstock": idstock,
            "cantidadsaliente": cantidadsaliente,
            "ubicacionstock": ubicacionstock,
            "destino": destino,
            "detallecliente": detallecliente,
            "horasalida": horasalida,
            "idsolicitud": idsolicitud

        }
        
        response = requests.post(url_api_fastapi, json=data)
        print(f"Estado de respuesta de la API: {response.status_code}")
        print(f"Contenido de respuesta de la API: {response.content}")
        if response.status_code == 200:
           return redirect('listarsalidas')
        else:
           return render(request, "movimientos/listamovimientos.html", {'error_message': 'Hubo un problema al registrar la salida.'})
    else:
        return render(request, "movimientos/realizarsalida.html")


def listar_repuestos(request):
    url_backend = 'https://tesis-back-motoware.onrender.com/consultar_repuesto'
    response = requests.get(url_backend)
    datos_api = response.json()
    return render(request, 'gestionar-repuestos/listar.html', {'datos': datos_api})



def registrarrepuesto(request):
    if request.method == 'POST':
        estado_input = request.POST.get('estado')
        if estado_input == 'True':
            estado = True
        else:
            estado = False
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        proveedor_id = request.POST.get('proveedor_id')
        pais_procedencia = request.POST.get('pais_procedencia')
        fecharegistro = request.POST.get('fecharegistro')
        estado = request.POST.get('estado')
        precio = request.POST.get('precio')
        etiqueta_nombre = request.POST.get('etiqueta_nombre')
        valores_atributos = request.POST.get('valores_atributos')
        codigoMarca = request.POST.get('codigoMarca')
        gradoViscosidad = request.POST.get('gradoViscosidad')
        tipoMotor = request.POST.get('gradoViscosidad')
        calidad = request.POST.get('tipoMotor')
        litros = request.POST.get('litros')

    

        valores_atributos = {
            "codigoMarca": codigoMarca,
            "gradoViscosidad": gradoViscosidad,
            "tipoMotor": tipoMotor,
            "calidad": calidad,
            "litros": litros,
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

from django.shortcuts import render, redirect
import requests

def actualizar_repuesto(request, repuesto_id):
   
    url_api_fastapi = f'https://tesis-back-motoware.onrender.com/repuestos/{repuesto_id}'
    response = requests.get(url_api_fastapi)
    
    if response.status_code == 200:
        repuesto = response.json()  
        if request.method == 'POST':
            estado_input = request.POST.get('estado')
            estado = True if estado_input == 'True' else False
            
            nombre = request.POST.get('nombre')
            proveedor_id = request.POST.get('proveedor_id')
            pais_procedencia = request.POST.get('pais_procedencia')
            fecharegistro = request.POST.get('fecharegistro')
            precio = request.POST.get('precio')
            etiqueta_nombre = request.POST.get('etiqueta_nombre')
            codigoMarca = request.POST.get('codigoMarca')
            gradoViscosidad = request.POST.get('gradoViscosidad')
            tipoMotor = request.POST.get('tipoMotor')
            calidad = request.POST.get('calidad')
            litros = request.POST.get('litros')
            
            valores_atributos = {
                "codigoMarca": codigoMarca,
                "gradoViscosidad": gradoViscosidad,
                "tipoMotor": tipoMotor,
                "calidad": calidad,
                "litros": litros,
            }
            
            data = {
                "id": repuesto_id, 
                "nombre": nombre,
                "proveedor_id": proveedor_id,
                "pais_procedencia": pais_procedencia,
                "fecharegistro": fecharegistro,
                "estado": estado,
                "precio": precio,
                "etiqueta_nombre": etiqueta_nombre,
                "valores_atributos": valores_atributos,
            }
            
           
            put_response = requests.put(url_api_fastapi, json=data)
            
            if put_response.status_code == 200:
                return redirect('listarrep')
            else:
                print(put_response.text)
                return render(request, "gestionar-repuestos/actualizar.html", {'error_message': 'Hubo un problema al actualizar el repuesto.'})
        
       
        return render(request, "gestionar-repuestos/actualizar.html", {'repuesto': repuesto})
    else:
        print(response.text)
        return render(request, "gestionar-repuestos/listar.html", {'error_message': 'No se pudo obtener el repuesto para actualizar.'})


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
    



