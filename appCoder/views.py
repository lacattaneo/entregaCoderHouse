from django.shortcuts import render, HttpResponse, redirect
from appCoder.models import Curso, Estudiante, Profesor, Entregable
from appCoder.forms import FormularioCursoPython


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

def formularioCursoPython(request):
    if request.method == 'POST':
        form = FormularioCursoPython(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            curso = form.cleaned_data['curso']

        Estudiante.objects.create(nombre=nombre, apellido=apellido, email=email, curso=curso)

        return redirect("index") # o usa redirect('nombre_de_la_url') para redirigir
    else:
        form = FormularioCursoPython()
    
    return render(request, 'AppCoder/formularioCursoPython.html', {'form': form})




def busquedaEstudiante(request):
    return render(request, "AppCoder/busquedaEstudiante.html")


def buscar(request):
    apellido = request.GET.get("apellido", "")

    if apellido:
        # Busca estudiantes que coincidan con el apellido
        estudiantes = Estudiante.objects.filter(apellido__icontains=apellido)
        if estudiantes.exists():
            respuesta = estudiantes
        else:
            respuesta = "No se encontraron estudiantes con ese apellido."
    else:
        respuesta = "No se ha proporcionado un apellido para buscar."

    return render(request, "AppCoder/busquedaEstudiante.html", {"respuesta": respuesta})