from django import forms
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Perfil


class RegistroForm(UserCreationForm):

    direccion = forms.CharField(
        required=True
    )

    telefono = forms.CharField(
        max_length=9,
        required=True
    )

    edad = forms.IntegerField(
        min_value=18,
        max_value=100,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name',)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('direccion', 'telefono', 'edad', 'avatar')
