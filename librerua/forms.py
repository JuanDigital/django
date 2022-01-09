from django import forms
from .models import alumnos

class almForm(forms.ModelForm):
    class Meta:
        model= alumnos
        fields='__all__'

