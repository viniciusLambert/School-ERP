from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from Users.models import User

class Order(models.Model):
    comment = models.CharField(_('comment'), max_length=200, null=True, blank=True)
    rating = models.IntegerField(_('rating'), null=True, blank=True)
    deliveryForecast = models.DateTimeField(_('deliveryForecast'), null=True, blank=True)
    ordered = models.DateTimeField(_('ordered'), null=True, blank=True)
    printing = models.DateTimeField(_('printing'), null=True, blank=True)
    finished = models.DateTimeField(_('finished'), null=True, blank=True)
    delivered = models.DateTimeField(_('delivered'), null=True, blank=True)
    canceled = models.DateTimeField(_('canceled'), null=True, blank=True)
    cancelId = models.CharField(_('cancelId'), max_length=30, null=True, blank=True)
    paymentLink = models.CharField(_('paymentLink'), max_length=300, null=True, blank=True)
    totalValue = models.FloatField(_('totalValue'), default=0.0)
    status = models.CharField(_('status'), max_length=30, null=True, blank=True)
    paymentType = models.CharField(_('paymentType'), max_length=30, default='money')
    trelloCardId = models.CharField(_('trelloCardId'), max_length=40, null=True, blank=True)

    usable = models.BooleanField(_('usable'))

    class Meta:
        ordering = ['id']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        db_table = "order"

    def __str__(self):
        return '#' + str(self.id) + ' - ' + self.user.name


class Alunos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matricula = models.CharField(_('matricula'), max_length=10)

    class Meta:
        ordering = ['id']
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = "alunos"

    def __str__(self):
        return '#' + str(self.id)


class Disciplinas(models.Model):
    nome = models.CharField(_('nome'), max_length=200, null=True, blank=True)
    codigo = models.CharField(_('codigo'), max_length=10, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplina"
        db_table = "disciplinas"

    def __str__(self):
        return '#' + str(self.id)


class Professores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['id']
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        db_table = "professores"

    def __str__(self):
        return '#' + str(self.id)

class Turmas(models.Model):
    nome = models.CharField(_('nome'), max_length=200, null=True, blank=True)
    professor = models.OneToOneField(Professores, on_delete=models.SET_NULL, null=True)
    disciplina = models.OneToOneField(Disciplinas, on_delete=models.SET_NULL, null=True)
    alunos = alunos = models.ManyToManyField(Alunos)

    class Meta:
        ordering = ['id']
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        db_table = "turmas"

    def __str__(self):
        return '#' + str(self.id)


