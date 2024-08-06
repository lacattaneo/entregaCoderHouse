from django import forms
from .models import Estudiante

class FormularioCursoPython(forms.Form):
        nombre = forms.CharField(
            label="Nombre",
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
        
        apellido = forms.CharField(
            label="Apellido",
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
        
        email = forms.EmailField(
            label="Email",
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico'}))
        
        curso = forms.CharField(
            label="Curso",
            max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
        
    
    #esto es, pensandolo como una curso y no un estudiante
"""
    camada = forms.IntegerField(
        label="Camada",
        widget=forms.TextInput(attrs={'placeholder': 'Numero de Camada'}))"""