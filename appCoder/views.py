from django.shortcuts import render, HttpResponse
from appCoder.models import Curso, Estudiante, Profesor, Entregable


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def curso(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")


def entregables(request):
    return render(request,"AppCoder/entregables.html")
