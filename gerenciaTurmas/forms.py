from django import forms

from .models import Disciplinas

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplinas
        fields = ('nome', 'codigo','cargaHoraria',)