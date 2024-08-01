from django.urls import path, include
from appCoder import views


urlpatterns = [
    path('',views.inicio, name="inicio"), #primer view
    path('cursos/',views.curso, name="cursos"),
    path('profesores/',views.profesores, name="profesores"),
    path('estudiantes/',views.estudiantes, name="estudiantes"),
    path('entregables/',views.entregables, name="entregables"),
]