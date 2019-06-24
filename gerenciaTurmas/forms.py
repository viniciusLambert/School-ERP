from django import forms

from .models import Disciplinas, Avaliacao, Questoes
from Users.models import User

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplinas
        fields = ('nome', 'codigo','cargaHoraria',)


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password',)


class AvaliacaoForm(forms.ModelForm):
    questoes = forms.ModelMultipleChoiceField(queryset=Questoes.objects.all())

    class Meta:
        model = Avaliacao
        fields = ('nome', )


class QuestaoForm(forms.ModelForm):

    class Meta:
        model = Questoes
        fields = (
            'disciplina',
            'nome',
            'enunciado',
            'alternativa1',
            'alternativa2',
            'alternativa3',
            'alternativa4',
            'correto'
        )
