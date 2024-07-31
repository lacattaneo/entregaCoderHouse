from django.urls import path, include
from appCoder import views


urlpatterns = [
    path('',views.inicio),
    path('cursos/',views.curso),
    path('profesores/',views.profesores),
    path('estudiantes/',views.estudiantes),
    path('entregables/',views.entregables),
]