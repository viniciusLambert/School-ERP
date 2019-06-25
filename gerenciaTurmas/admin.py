# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Turmas, Alunos, Disciplinas, Professores, Questoes, \
    Avaliacao, Resolucao, Resposta


class ProfessoresAdmin(admin.ModelAdmin):

    list_display = ['id', 'user']
    search_fields = ['id' ,'user']


class AlunosAdmin(admin.ModelAdmin):

    list_display = ['id', 'user']
    search_fields = ['id' ,'user']

class TurmasAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome','disciplina', 'professor']
    search_fields = ['id' ,'disciplina', 'professor']

class DisciplinasAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'codigo']
    search_fields = ['id', 'nome', 'codigo']

class QuestoesAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'disciplina']
    search_fields = ['id', 'nome', 'disciplina']

class AvaliacaoAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'disciplina']
    search_fields = ['id', 'nome', 'disciplina']

class ResolucaoAdmin(admin.ModelAdmin):

    list_display = ['id', 'aluno', 'avaliacao']
    search_fields = ['id']

class RespostaAdmin(admin.ModelAdmin):

    list_display = ['id', 'questao']
    search_fields = ['id']

admin.site.register(Resolucao, ResolucaoAdmin)
admin.site.register(Resposta, RespostaAdmin)
admin.site.register(Professores, ProfessoresAdmin)
admin.site.register(Alunos, AlunosAdmin)
admin.site.register(Turmas, TurmasAdmin)
admin.site.register(Disciplinas, DisciplinasAdmin)
admin.site.register(Questoes, QuestoesAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
