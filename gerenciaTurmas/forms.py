from django import forms
from django.forms import inlineformset_factory


from .models import (
    Disciplinas,
    Avaliacao,
    Questoes,
    Alunos,
    Resolucao,
    Resposta
)
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
            'nome',
            'enunciado',
            'alternativa1',
            'alternativa2',
            'alternativa3',
            'alternativa4',
            'correto'
        )


class RespostaForm(forms.ModelForm):

    class Meta:
        model = Resposta
        fields = (
            'resolucao',
            'alternativa_aluno',
            'questao'
        )


class ResolucaoForm(forms.ModelForm):

    class Meta:
        model = Resolucao
        fields = (
            'aluno',
            'avaliacao'
        )


RespostasFormSet = inlineformset_factory(
    Resolucao,
    Resposta,
    form=RespostaForm,
    extra=1
)
