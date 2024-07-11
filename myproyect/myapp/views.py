
# Create your views here.
from django.http import HttpResponse,JsonResponse
import mysql.connector

config= {
    'user' : 'root',
    'password' : 'bautista2018',
    'database' : 'cafe',
    'host' : 'localhost'
}

def index(request):
    return HttpResponse("HOLA MUNDO!")

def acerca_de (request):
    return HttpResponse("¡curso de python y django!")

def index1 (request):
    return HttpResponse("<html>¡<strong>hola</strong>, <em>mundo</em>!</html>")

def productos (request):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT descripcion, precio from producto")
    html = """
        <html>
        <title>lista de cursos</title>
        <table style="border: 1px solid">
            <thead>
                <tr>
                    <th>Nombre_Producto</th>
                    <th>Precio</th>
                </tr>
            </thead>
    """
    for(nombre,precio) in cursor.fetchall():
        html +=f"""
            <tr>
                <td>{nombre}</td>
                <td>{precio}</td>
            </tr>
        """
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)

def empleados (request):
    conn = mysql.connector.connect(user='root', password='bautista2018', host='127.0.0.1',database='cafe', auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, apellido, sueldo FROM empleados")
    html = """
        <html>
        <title>empleados</title>
        <table style="border: 1px solid">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>apellido</th>
                    <th>sueldo</th>
                </tr>
            </thead>
    """
    for(nombre,apellido, sueldo) in cursor.fetchall():
        html +=f"""
            <tr>
                <td>{nombre}</td>
                <td>{apellido}</td>
                <td>{sueldo}</td>
            </tr>
        """
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)

def productosJson (request):
    conn = mysql.connector.connect(user='root', password='bautista2018', host='127.0.0.1',database='cafe', auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, apellido, sueldo FROM empleados")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response