from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("empleados", views.empleados, name="empleados"),
    path("acerca_de", views.acerca_de, name="acerca_de"),
    path("empleados/Json", views.productosJson, name="productosJson"),
]