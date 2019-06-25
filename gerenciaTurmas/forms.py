from django import forms
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
    password = forms.CharField(widget=forms.PasswordInput)
    model = User
    widgets = {
        'password': forms.PasswordInput(),
    }
    class Meta:
        model = User
        fields = ('email',)


class AvaliacaoForm(forms.ModelForm):
    questoes = forms.ModelMultipleChoiceField(queryset=Questoes.objects.all(), required=False,)

    class Meta:
        model = Avaliacao
        fields = ('nome',)


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


class ResolucaoForm(forms.ModelForm):

    class Meta:
        model = Resolucao
        fields = ()

    def __init__(self, data, respostas, *args, **kwargs):
        self.respostas = respostas
        count = 1
        for resposta in respostas:
            field_name = "questao_%d" % resposta.questao.pk
            choices = [
                ('1', resposta.questao.alternativa1),
                ('2', resposta.questao.alternativa2),
                ('3', resposta.questao.alternativa3),
                ('4', resposta.questao.alternativa4),
            ]
            field_label = str(count) + ' - ' + resposta.questao.enunciado
            count += 1
            self.base_fields.update(
                {
                    field_name: forms.ChoiceField(
                        label=field_label,
                        required=True,
                        choices=choices,
                        widget=forms.RadioSelect
                    )
                }
            )

        return super(ResolucaoForm, self).__init__(data, *args, **kwargs)

    def save(self, *args, **kwargs):
        respostas = self.respostas
        res = super(ResolucaoForm, self).save(*args, **kwargs)
        res.respostas = respostas
        return res
    
    # def is_valid(self):
    #     res = super(ResolucaoForm, self).is_valid()
    #     ##Remover, feito apenas para testes
    #     if self.errors.get('__all__')[
    #             0] == ('Resolução with this Aluno and ' +
    #                   'Avaliacao already exists.'):
    #         self.errors = False
    #         return True
    #     return res
