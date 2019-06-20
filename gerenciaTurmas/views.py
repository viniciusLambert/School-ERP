from django.shortcuts import render, get_object_or_404, redirect
from .models import Turmas, Alunos, Disciplinas, Professores

from .forms import DisciplinaForm

# Create your views here.
def post_list(request):
    turmas = Turmas.objects.all()
    return render(request, 'gerenciaTurmas/post_list.html', {'turmas': turmas})


def disciplina_detail(request, id):
    disciplina = get_object_or_404(Disciplinas, id=id)
    return render(request, 'gerenciaTurmas/disciplina_detail.html', {'disciplina': disciplina})

def disciplina_new(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            print('------------------------------',request.POST)
            disciplina = form.save(commit=False)
            disciplina.nome = request.POST['nome']
            disciplina.codigo = request.POST['codigo']
            disciplina.cagaHoraria = request.POST['cargaHoraria']
            disciplina.save()

        return redirect('disciplina_detail', id=disciplina.id)
    else:
        form = DisciplinaForm()
    return render(request, 'gerenciaTurmas/disciplina_edit.html', {'form': form})


def disciplina_edit(request,id):
    disciplina =  get_object_or_404(Disciplinas, id=id)
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            print('------------------------------',request.POST)
            disciplina = form.save(commit=False)
            disciplina.nome = request.POST['nome']
            disciplina.codigo = request.POST['codigo']
            disciplina.cagaHoraria = request.POST['cargaHoraria']
            disciplina.save()

        return redirect('disciplina_detail', id=disciplina.id)
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'gerenciaTurmas/disciplina_edit.html', {'form': form})