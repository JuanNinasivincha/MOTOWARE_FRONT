from django.conf import settings

import requests

dominio = getattr(settings, 'API_URL', 'https://tesis-motoware-back.onrender.com/')
url = f"{dominio}/m6"

headers = {'Content-type': 'application/json; charset=UTF-8'}

def get_repuestos_all(request, search):
    """Obtener todos los proyectos"""
    headers['Authorization'] = f"Bearer {request.session['token']}"
    r = None
    try:
        r = requests.get(f'{url}/consultar_repuestos', allow_redirects=False, headers=headers)
           
        r.raise_for_status()

        data= r.json()

        return data['repuestos']
    except requests.exceptions.RequestException:
        errors = 'Internal server error'

      