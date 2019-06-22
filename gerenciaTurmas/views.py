from django.shortcuts import render, get_object_or_404, redirect
from .models import Turmas, Alunos, Disciplinas, Professores, Avaliacao

from Users.models import User
from .forms import DisciplinaForm, LoginForm

# Create your views here.

def init(request):
    print(request.session.get('email'))
    if(request.session.get('email') != None):
        return render(request, 'gerenciaTurmas/init.html', {})
    else:
        return redirect('login')

def login(request):
    if request.method == "POST":
        user = get_object_or_404(User, email=request.POST['email'])
        if(user.password == request.POST['password']):
            request.session['email'] = user.email
            request.session['type'] = user.type
            return render(request, 'gerenciaTurmas/init.html', {})

    form = LoginForm()
    return render(request, 'gerenciaTurmas/login/login.html', {'form': form})



def disciplina_list(request):
    disciplina = Disciplinas.objects.all()
    return render(request, 'gerenciaTurmas/disciplinas_list.html', {'disciplinas': disciplina})


def disciplina_detail(request, id):
    disciplina = get_object_or_404(Disciplinas, id=id)
    avaliacoes = Avaliacao.objects.filter(disciplina__pk=id)
    return render(request, 'gerenciaTurmas/disciplina_detail.html', {
        'disciplina': disciplina,
        'avaliacoes': avaliacoes,
    })

def disciplina_new(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
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


def professores_list(request):
    professores = Professores.objects.all()
    return render(request, 'gerenciaTurmas/professores_list.html', {'professores': professores})


def professores_detail(request, id):
    professor = get_object_or_404(Professores, id=id)
    turmas = Turmas.objects.filter(professor__pk=id)
    return render(request, 'gerenciaTurmas/professores_detail.html', {'professor': professor, 'turmas':turmas })


#nao feito
def professores_new(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.nome = request.POST['nome']
            disciplina.codigo = request.POST['codigo']
            disciplina.cagaHoraria = request.POST['cargaHoraria']
            disciplina.save()

        return redirect('disciplina_detail', id=disciplina.id)
    else:
        form = DisciplinaForm()
    return render(request, 'gerenciaTurmas/disciplina_edit.html', {'form': form})

#nao feito
def professores_edit(request,id):
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


def turmas_list(request):
    turmas = Turmas.objects.all()
    return render(request, 'gerenciaTurmas/turmas_list.html', {'turmas': turmas})


def minhas_turmas(request):
    if(request.session.get('type') == "Aluno"):
        user = User.objects.get(email =request.session.get('email'))
        aluno = Alunos.objects.get(user_id=user.id )
        turmas = Turmas.objects.filter(alunos__pk=aluno.id)
    else:
        user = User.objects.get(email=request.session.get('email'))
        professor = Professores.objects.get(user_id=user.id)
        turmas = Turmas.objects.filter(professor__pk=professor.id)
    return render(request, 'gerenciaTurmas/turmas_list.html', {'turmas': turmas})


def turma_detail(request,id):
    turma = get_object_or_404(Turmas, id=id)
    return render(request, 'gerenciaTurmas/turma_detail.html', {'turma': turma})

def alunos_detail(request, id):
    aluno = get_object_or_404(Alunos, id=id)
    turmas = Turmas.objects.filter(alunos__pk=id)
    return render(request, 'gerenciaTurmas/alunos_detail.html', {'aluno': aluno, 'turmas': turmas})

def avaliacao_detail(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    return render(request, 'gerenciaTurmas/avaliacao_detail.html', {'avaliacao': avaliacao})


