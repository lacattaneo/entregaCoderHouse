from django.shortcuts import render, HttpResponse
from appCoder.models import Curso, Estudiante, Profesor, Entregable

def curso(self):
    curso = Curso(nombre="Desarrollo web", camada="2002")
    curso.save()
    documentoDeTexto= f"-->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)