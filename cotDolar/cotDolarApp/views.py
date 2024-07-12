import sqlite3
from django.http import HttpResponseRedirect,HttpResponse, request
from django.shortcuts import render
def index(request):
    ctx = {"nombre" : "juan"}
    return render(request, "cotDolarApp/index.html",ctx)

def cotizacion_dolar(request):
    r = request.get("https://dolarapi.com/v1/dolares/blue")
    resultado = r.json()
    html = f"""
        <html>
        <title>Cotizacion del dolar</title>
        <p><strong>Compra</strong>: {resultado["Compra"]}</p>
        <p><strong>Venta</strong>: {resultado["Venta"]}</p>
        </html>
        """
    return HttpResponse(html)

def cursos (request):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    cursos = cursor.fetchall()
    conn.close()
    ctx = {"cursos": cursos}
    return render(request,"cotDolarApp/cursos.html", ctx)