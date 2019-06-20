from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('disciplina/<int:id>/', views.disciplina_detail, name='disciplina_detail'),
    path('disciplina/new', views.disciplina_new, name='disciplina_new'),
    path('disciplina/<int:id>/edit/', views.disciplina_edit, name='disciplina_edit'),
]