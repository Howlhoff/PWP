from django import forms
from .models import *

class formComentario(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Escribe aqui!',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = comentario
        fields =['content']