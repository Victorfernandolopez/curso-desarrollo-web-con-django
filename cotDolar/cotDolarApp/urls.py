from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("cotizacion-dolar", views.cotizacion_dolar, name="cotizacion_dolar"),
    path("lista-de-cursos", views.cursos, name="cursos"),
    path("curso/<str:nombre_curso>", views.curso, name="curso")
    
]