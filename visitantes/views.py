from django.shortcuts import render
from gestao.models import cursos,Funcionario,Noticias,Galeria,quadro_de_honra
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    data = {}
    data['cursos'] = cursos.objects.all()
    data['funcionarios'] = Funcionario.objects.all()
    data['noticias'] = Noticias.objects.all()
    data['acima'] = Galeria.objects.filter(painel='Acima')
    data['abaixo'] = Galeria.objects.filter(painel='Abaixo')
    data['Principal'] = Galeria.objects.filter(painel='Principal')
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    return render(request,'home.html',data)

def instituicao(request):
    data = {}
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    data['cursos'] = cursos.objects.all()
    return render(request,'listar/liceu.html',data)

def home2(request):
    return render(request,'home22.html')

def detalhes_curso(request,pk):
    data = {}
    data['curso'] = get_object_or_404(cursos,pk=pk)
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    data['cursos'] = cursos.objects.all()
    return render(request,'listar/detalhes_curso.html',data)

def detalhes_funcionario(request,pk,disc,direccao):
    data = {}
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    data['cursos'] = cursos.objects.all()
    data['disc'] = disc
    data['direccao'] = direccao
    data['funcionario'] = get_object_or_404(Funcionario,pk=pk)
    return render(request,'listar/detalhes_f.html',data)

def direccao(request):
    data = {}
    data['direccao'] = True
    data['cursos'] = cursos.objects.all()
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    data['funcionarios'] = Funcionario.objects.all()
    return render(request,'listar/quem.html',data)

def docentes(request):
    data = {}
    data['cursos'] = cursos.objects.all()
    data['quadro_de_honra1'] = quadro_de_honra.objects.all()
    data['professores'] = Funcionario.objects.filter(funcao='Professor(a)').order_by('nome_completo')
    return render(request,'listar/quem.html',data)

def Quadro_de_honra(request):
    data = {}
    data['cursos'] = cursos.objects.all()
    data['quadro_de_honra'] = quadro_de_honra.objects.filter().order_by('-media_obtida')
    data['quadro_de_honra1'] = True
    return render(request,'listar/quadro.html',data)

def Quadro_de_honra2(request,pk):
    data = {}
    data['cursos'] = cursos.objects.all()
    data['quadro_de_honra1'] = True
    data['alunod'] = get_object_or_404(quadro_de_honra,pk=pk)
    return render(request,'listar/quadro.html',data)

def noticia(request,pk):
    data = {}
    data['cursos'] = cursos.objects.all()
    data['quadro_de_honra1'] = quadro_de_honra.objects.filter().order_by('-media_obtida')
    data['noticia'] = get_object_or_404(Noticias,pk=pk)
    return render(request,'listar/noticia.html',data)

@csrf_exempt
def entrar(request):
    if request.method=='POST':
        username = request.POST['utilizador']
        password = request.POST['senha']
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            messages.success(request, 'Seja Bem-vindo')
            return HttpResponseRedirect('dashboard')
        else:
            messages.error(request, "Por favor introduza o utilizador e palavra passe corretos!")
            return HttpResponseRedirect('/')