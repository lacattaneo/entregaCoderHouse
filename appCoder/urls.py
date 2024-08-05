from django.urls import path, include
from appCoder import views


urlpatterns = [
    path('',views.index, name="index"), #primer view
    path('inicio/',views.inicio2, name="inicio"),
    path('cursos/',views.curso, name="cursos"),
    path('profesores/',views.profesores, name="profesores"),
    path('estudiantes/',views.estudiantes, name="estudiantes"),
    path('entregables/',views.entregables, name="entregables"),
    path('formularioCursoPython/',views.formularioCursoPython, name = "formularioCursoPython"),
    path('busquedaEstudiante/', views.busquedaEstudiante, name="BusquedaEstudiante"),
    path('buscar/', views.buscar, name='buscar'),
]