from django import forms

from .models import Disciplinas
from Users.models import User

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplinas
        fields = ('nome', 'codigo','cargaHoraria',)



class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password',)



