from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Turmas,
    Alunos,
    Disciplinas,
    Professores,
    Avaliacao,
    Questoes,
    Resposta,
    Resolucao
)

from Users.models import User
from .forms import (
    DisciplinaForm,
    LoginForm,
    AvaliacaoForm,
    QuestaoForm,
    ResolucaoForm,
)

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
        if user.password == request.POST['password']:
            request.session['email'] = user.email
            request.session['type'] = user.type
            if (request.session.get('type') == 'Professor'):
                return render(request, 'gerenciaTurmas/init.html', {})
            else:
                user = User.objects.get(email=request.session.get('email'))
                aluno = Alunos.objects.get(user_id=user.id)
                turmas = Turmas.objects.filter(alunos__pk=aluno.id)
                return redirect('minhas_turmas')

    form = LoginForm()
    return render(request, 'gerenciaTurmas/login/login.html', {'form': form})


def disciplina_list(request):
    disciplina = Disciplinas.objects.all()
    return render(request,
                  'gerenciaTurmas/disciplinas_list.html',
                  {'disciplinas': disciplina}
                  )


def disciplina_detail(request, id):
    disciplina = get_object_or_404(Disciplinas, id=id)
    avaliacoes = Avaliacao.objects.filter(disciplina__pk=id)
    type = request.session.get('type')

    if(type == 'Aluno'):
        user = User.objects.get(email=request.session.get('email'))
        aluno = Alunos.objects.get(user_id=user.id)
        provas = 0
        nota = 0
        for avaliacao in avaliacoes:
            try:
                avaliacao.nota = Resolucao.objects.get(avaliacao__pk=avaliacao.id, aluno__pk=aluno.id).nota
            except Resolucao.DoesNotExist:
                avaliacao.nota = None
            if(avaliacao.nota != None):
                provas += 1
                nota += avaliacao.nota
        if(provas == 0):
            provas =1
        return render(request, 'gerenciaTurmas/disciplina_detail.html', {
            'disciplina': disciplina,
            'avaliacoes': avaliacoes,
            'type' : type,
            'media': nota/provas
        })
    return render(request, 'gerenciaTurmas/disciplina_detail.html', {
        'disciplina': disciplina,
        'avaliacoes': avaliacoes,
        'type': type,
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


def disciplina_edit(request, id):
    disciplina =  get_object_or_404(Disciplinas, id=id)
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            print('------------------------------', request.POST)
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
        notas = []
        situacao_alunos = []
        for turma in turmas:
            disciplina = get_object_or_404(Disciplinas, id=turma.disciplina.id)
            avaliacoes = Avaliacao.objects.filter(disciplina__pk=disciplina.id)

            n = 0
            q = 0
            for avaliacao in avaliacoes:
                try:
                    nota_aluno = Resolucao.objects.get(
                        avaliacao__pk=avaliacao.id,
                        aluno__pk=aluno.id).nota
                    n += nota_aluno
                    notas.append({
                        'disciplina': turma.disciplina.nome,
                        'avaliacao': avaliacao.id,
                        'nota': nota_aluno
                    })
                except Resolucao.DoesNotExist:
                    notas.append({
                        'disciplina': turma.disciplina.nome,
                        'avaliacao': avaliacao.id,
                        'nota': 'Tarefa Não Realizada'
                    })
                q += 1
            if (q == 0):
                q = 1
            media = n / q
            print(notas)
            situacao_alunos.append({
                'disciplina': turma.disciplina.nome,
                'media': media,
                'situacao': "aprovado" if media >= 6 else "reprovado"
                })

        type = request.session.get('type')
        return render(request, 'gerenciaTurmas/minhas_turmas.html',
                      {'avaliacao': avaliacao,
                       'type': type,
                       'notas': notas,
                       'situacao_alunos': situacao_alunos,
                       'turmas': turmas,
                       })
    else:
        user = User.objects.get(email=request.session.get('email'))
        professor = Professores.objects.get(user_id=user.id)
        turmas = Turmas.objects.filter(professor__pk=professor.id)


    return render(request, 'gerenciaTurmas/minhas_turmas.html',
                  {'turmas': turmas,
                   })


def turma_detail(request,id):
    turma = get_object_or_404(Turmas, id=id)
    return render(request, 'gerenciaTurmas/turma_detail.html', {'turma': turma})


def alunos_detail(request, id):
    aluno = get_object_or_404(Alunos, id=id)
    turmas = Turmas.objects.filter(alunos__pk=id)
    return render(request, 'gerenciaTurmas/alunos_detail.html', {'aluno': aluno, 'turmas': turmas})


def avaliacao_detail(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    turmas = Turmas.objects.filter(professor__pk = avaliacao.professor.id, disciplina__pk=avaliacao.disciplina.id)
    notas = []
    situacao_alunos = []
    for turma in turmas:
        disciplina = get_object_or_404(Disciplinas, id=turma.disciplina.id)
        avaliacoes = Avaliacao.objects.filter(disciplina__pk=disciplina.id)

        for aluno in turma.alunos.all():
            n = 0
            q = 0
            for avaliacao in avaliacoes:
                try:
                   nota_aluno = Resolucao.objects.get(
                        avaliacao__pk=avaliacao.id, aluno__pk=aluno.id).nota
                   n += nota_aluno
                   notas.append({
                       'aluno' : aluno.user.name,
                       'avaliacao' : avaliacao.id,
                       'nota' : nota_aluno
                   })
                except Resolucao.DoesNotExist:
                    notas.append({
                        'aluno': aluno.user.name,
                        'avaliacao': avaliacao.id,
                        'nota': 'Tarefa Não Realizada'
                    })
                q += 1
            if(q == 0):
                q = 1
            media = n/q

            situacao_alunos.append({
                'aluno': aluno.user.name,
                'media': media,
                'situacao' : "aprovado" if media >= 6 else "reprovado"
            })
    type = request.session.get('type')
    return render(request, 'gerenciaTurmas/avaliacao_detail.html',
                  {'avaliacao': avaliacao ,
                   'type':type ,
                   'nota' : notas,
                   'situacao_alunos': situacao_alunos,

                   })


def avaliacao_delete(request, id, did):
    disciplina = get_object_or_404(Disciplinas, id=did)
    type = request.session.get('type')
    avaliacao = get_object_or_404(Avaliacao, id=id)

    try:
        resolucao = Resolucao.objects.get(avaliacao__pk=avaliacao.id)
        avaliacoes = Avaliacao.objects.filter(disciplina__pk=did)
        return render(request, 'gerenciaTurmas/disciplina_detail.html', {
            'disciplina': disciplina,
            'avaliacoes': avaliacoes,
            'type': type
        })
    except Resolucao.DoesNotExist:
        avaliacao.delete()
        avaliacoes = Avaliacao.objects.filter(disciplina__pk=did)

        return render(request, 'gerenciaTurmas/disciplina_detail.html', {
            'disciplina': disciplina,
            'avaliacoes': avaliacoes,
            'type': type
        })

def questao_delete(request, id, qid):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    questao = get_object_or_404(Questoes, id = qid)
    avaliacao.questoes.remove(questao)
    type = request.session.get('type')
    return render(request, 'gerenciaTurmas/avaliacao_detail.html', {'avaliacao': avaliacao, 'type': type})


def avaliacao_new(request, disciplina_id):
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.nome = request.POST['nome']
            user = User.objects.get(email=request.session.get('email'))
            professor = Professores.objects.get(user=user)
            avaliacao.professor = professor
            disciplina = Disciplinas.objects.get(id=disciplina_id)
            avaliacao.disciplina = disciplina
            avaliacao.save()
            avaliacao.questoes.set(form.cleaned_data.get('questoes'))

        return redirect('avaliacao_detail', id=avaliacao.id)
    else:
        form = AvaliacaoForm()
        return render(
            request,
            'gerenciaTurmas/avaliacao_new.html',
            {
                'form': form,
             }
        )


def avaliacao_edit(request, id, disciplina_id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao.delete()
            avaliacao = form.save(commit=False)
            avaliacao.nome = request.POST['nome']
            user = User.objects.get(email=request.session.get('email'))
            professor = Professores.objects.get(user=user)
            avaliacao.professor = professor
            disciplina = Disciplinas.objects.get(id=disciplina_id)
            avaliacao.disciplina = disciplina
            avaliacao.save()
            avaliacao.questoes.set(form.cleaned_data.get('questoes'))

        return redirect('avaliacao_detail', id=avaliacao.id)
    else:
        form = AvaliacaoForm(instance=avaliacao)
        return render(
            request,
            'gerenciaTurmas/avaliacao_new.html',
            {
                'form': form,
             }
        )


def questao_detail(request, id):
    questao = get_object_or_404(Questoes, id=id)

    return render(request, 'gerenciaTurmas/questao_detail.html',
                  {'questao': questao})


def questao_new(request, avaliacao_id):
    if request.method == "POST":
        form = QuestaoForm(request.POST)
        if form.is_valid():
            avaliacao = Avaliacao.objects.get(id=avaliacao_id)
            questao = form.save(commit=False)
            questao.nome = request.POST['nome']
            questao.enunciado = request.POST['enunciado']
            questao.alternativa1 = request.POST['alternativa1']
            questao.alternativa2 = request.POST['alternativa2']
            questao.alternativa3 = request.POST['alternativa3']
            questao.alternativa4 = request.POST['alternativa4']
            questao.correto = request.POST['correto']
            questao.disciplina = avaliacao.disciplina
            questao.save()
            avaliacao.questoes.add(questao)
            avaliacao.save()


        return redirect('questao_detail', id=questao.id)
    else:
        form = QuestaoForm()
        return render(
            request,
            'gerenciaTurmas/questao_new.html',
            {
                'form': form,
            }
        )


def questao_edit(request, id, disciplina_id):
    questao = get_object_or_404(Questoes, id=id)
    if request.method == "POST":
        form = QuestaoForm(request.POST)
        if form.is_valid():
            questao = form.save(commit=False)
            questao.nome = request.POST['nome']
            questao.enunciado = request.POST['enunciado']
            questao.alternativa1 = request.POST['alternativa1']
            questao.alternativa2 = request.POST['alternativa2']
            questao.alternativa3 = request.POST['alternativa3']
            questao.alternativa4 = request.POST['alternativa4']
            disciplina = Disciplinas.objects.get(id=disciplina_id)
            questao.disciplina = disciplina
            questao.correto = request.POST['correto']
            questao.save()

        return redirect('questao_detail', id=questao.id)
    else:
        form = QuestaoForm(instance=questao)
        return render(
            request,
            'gerenciaTurmas/questao_new.html',
            {
                'form': form,
            }
        )


def resolucao_new(request, avaliacao_id):
    user = User.objects.get(email=request.session.get('email'))
    aluno = Alunos.objects.get(user_id=user.id)
    avaliacao = Avaliacao.objects.get(id=avaliacao_id)
    questoes = Questoes.objects.filter(avaliacao__pk=avaliacao_id)
    respostas = [Resposta(questao=questao) for questao in questoes]
    form = ResolucaoForm(
        initial=[{'aluno': aluno, 'avaliacao': avaliacao}],
        data={},
        respostas=respostas
    )
    if request.method == "POST":
        form = ResolucaoForm(request.POST, respostas=respostas)
        nota = 0.0
        if form.is_valid():
            resolucao = form.save(commit=False)
            for resposta in resolucao.respostas:
                resposta.alternativa_aluno = request.POST.get(
                    'questao_%d', resposta.questao.pk)

                if resposta.alternativa_aluno == resposta.questao.correto:
                    nota += 10/len(resolucao.respostas)

            resolucao.avaliacao = avaliacao
            resolucao.aluno = aluno
            resolucao.nota = nota
            resolucao.save()

            for resposta in resolucao.respostas:
                resposta.resolucao = resolucao
                resposta.save()
            return render(
                request,
                'gerenciaTurmas/resolucao_new.html', {'form': form,}
            )
        # return redirect()
    return render(
        request,
        'gerenciaTurmas/resolucao_new.html',
        {
            'form': form,
        }
    )
