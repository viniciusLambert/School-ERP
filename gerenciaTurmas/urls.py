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
    path('minhasturmas/list/', views.minhas_turmas, name='minhas_turmas'),
    path('turmas/<int:id>/', views.turma_detail, name='turma_detail'),

    path('alunos/<int:id>/', views.alunos_detail, name='alunos_detail'),

    path('avaliacao/<int:id>/', views.avaliacao_detail, name='avaliacao_detail'),
    path('avaliacao/new', views.avaliacao_new, name='avaliacao_new'),

]