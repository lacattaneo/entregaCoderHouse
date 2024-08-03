from django.shortcuts import render, HttpResponse
from appCoder.models import Curso, Estudiante, Profesor, Entregable


def index(request):
    return render(request, "AppCoder/index.html")

def inicio2(request):
    return render(request, "AppCoder/inicio.html")


def curso(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")


def entregables(request):
    return render(request,"AppCoder/entregables.html")



def formularioCurso(request):
    if request.method == "POST":
        curso_nombre = request.POST["curso"]
        curso_camada = request.POST["camada"]
        nuevoCurso = Curso(nombre=curso_nombre, camada=curso_camada)
        nuevoCurso.save()
        return render(request, "AppCoder/index.html")
    return render(request,"AppCoder/formularioCurso.html")