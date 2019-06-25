from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.init, name='init'),
    path('disciplina/list/', views.disciplina_list, name='disciplina_list'),
    path('disciplina/<int:id>/', views.disciplina_detail, name='disciplina_detail'),
    path('disciplina/new', views.disciplina_new, name='disciplina_new'),
    path('disciplina/<int:id>/edit/', views.disciplina_edit, name='disciplina_edit'),

    path('professores/list/', views.professores_list, name='professores_list'),
    path('professores/<int:id>/', views.professores_detail, name='professores_detail'),
    path('professores/new', views.professores_new, name='professores_new'),
    path('professores/<int:id>/edit/', views.professores_edit, name='professores_edit'),

    path('turmas/list/', views.turmas_list, name='turmas_list'),
    path('minhas_turmas/list/', views.minhas_turmas, name='minhas_turmas'),
    path('turmas/<int:id>/', views.turma_detail, name='turma_detail'),

    path('alunos/<int:id>/', views.alunos_detail, name='alunos_detail'),

    path('avaliacao/<int:id>/', views.avaliacao_detail, name='avaliacao_detail'),
    path('avaliacao/new/<int:disciplina_id>/', views.avaliacao_new, name='avaliacao_new'),
    path('avaliacao/<int:id>/edit/<int:disciplina_id>/', views.avaliacao_edit, name='avaliacao_edit'),
    path('avaliacao/delete/<int:id>/<int:did>/', views.avaliacao_delete, name='avaliacao_delete'),


    path('questao/<int:id>/', views.questao_detail, name='questao_detail'),
    path('questao/new/<int:avaliacao_id>/', views.questao_new, name='questao_new'),
    path('questao/<int:id>/edit/<int:disciplina_id>', views.questao_edit, name='questao_edit'),
    path('questao/delete/<int:id>/<int:qid>/', views.questao_delete, name='questao_delete'),

    path('resolucao/<int:avaliacao_id>/',
         views.resolucao_new, name='resolucao_new'),

    path('logout/', views.logout, name='logout'),

]
