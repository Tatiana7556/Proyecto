from django import forms
from django import forms

class RegFrom(forms.Form):
    nombre= forms.CharField(max_length=100)
    correo= forms.CharField(max_length=120)
    Telefono= forms.IntegerField()
    Mensaje= forms.CharField(max_length=150)