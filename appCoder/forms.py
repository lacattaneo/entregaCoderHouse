from django import forms

class FormularioCurso(forms.Form):
    #especificar campos
    nombre = forms.CharField(
        label="Curso",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del Curso'}))
    
    camada = forms.IntegerField(
        label="Camada",
        widget=forms.TextInput(attrs={'placeholder': 'Numero de Camada'}))
