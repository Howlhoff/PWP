from django import forms
from .models import *

class formPerfil(forms.ModelForm):
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    imagen=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = perfil
        fields = ['ciudad','pais','descripcion','imagen']
    def __init__(self, *args,**kwargs):
        super(formPerfil,self).__init__(*args,**kwargs)

class formUser(forms.ModelForm):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','email']
    def __init__(self, *args,**kwargs):
        super(formUser,self).__init__(*args,**kwargs)