from django.shortcuts import render, HttpResponse, redirect
from appCoder.models import Curso, Estudiante, Profesor, Entregable
from appCoder.forms import FormularioCurso


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


#formularios

def formularioCurso(request):
    if request.method == "POST":
        miFormulario = FormularioCurso(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
            return redirect("index")
    else:
        miFormulario = FormularioCurso()  # Muestra un formulario vacío para construir el HTML
    
    return render(request, "AppCoder/formularioCurso.html", {"miFormulario": miFormulario})