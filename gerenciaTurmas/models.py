from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from Users.models import User

class Alunos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matricula = models.CharField(_('matricula'), max_length=10)

    class Meta:
        ordering = ['id']
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = "alunos"

    def __str__(self):
        return '#' + str(self.id) + " " + self.user.name + self.user.lastName


class Disciplinas(models.Model):
    nome = models.CharField(_('nome'), max_length=200, null=True, blank=True)
    codigo = models.CharField(_('codigo'), max_length=10, null=True, blank=True)
    cargaHoraria = models.IntegerField(_('cargaHoraria'), null=True, blank=True)
    class Meta:
        ordering = ['id']
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplina"
        db_table = "disciplinas"

    def __str__(self):
        return '#' + str(self.id) + " " + self.nome


class Professores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['id']
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        db_table = "professores"

    def __str__(self):
        return '#' + str(self.id) + " " + self.user.name + self.user.lastName

class Turmas(models.Model):
    nome = models.CharField(_('nome'), max_length=200)
    professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Alunos)

    class Meta:
        ordering = ['id']
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        db_table = "turmas"

    def __str__(self):
        return '#' + str(self.id)


class Questoes(models.Model):
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)

    nome = models.CharField(_('nome'), max_length=250)
    enunciado = models.CharField(_('enunciado'), max_length=250)
    alternativa1 = models.CharField(_('alternativa1'), max_length=250)
    alternativa2 = models.CharField(_('alternativa2'), max_length=250)
    alternativa3 = models.CharField(_('alternativa3'), max_length=250)
    alternativa4 = models.CharField(_('alternativa4'), max_length=250)
    correto = models.IntegerField(_('correto'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
        db_table = "questoes"

    def __str__(self):
        return '#' + str(self.id) + " " + self.enunciado + " " + self.nome


class Avaliacao(models.Model):
    nome = models.CharField(_('nome'), max_length=250)
    professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    questoes = models.ManyToManyField(Questoes)

    class Meta:
        ordering = ['id']
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        db_table = "avaliacao"

    def __str__(self):
        return '#' + str(self.id)


class Resolucao(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)

    class Meta:
        ordering = ['avaliacao']
        verbose_name = 'Resolução'
        verbose_name_plural = 'Resoluções'
        db_table = 'resolucao'

    def __str__(self):
        return self.avaliacao.nome + ' - ' + self.aluno.nome


class Resposta(models.Model):
    questao = models.ForeignKey(Questoes, on_delete=models.CASCADE)
    resolucao = models.ForeignKey(Resolucao, on_delete=models.CASCADE)
    alternativa_aluno = models.CharField(_('Resposta'), max_length=250)

    class Meta:
        ordering = ['questao']
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        db_table = 'resposta'

    def __str__(self):
        return self.questao.avaliacao.nome + '/' + self.questao.nome + ' = ' \
            + self.aluno.nome
