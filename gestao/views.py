from django.shortcuts import render,redirect
from .models import cursos,Funcionario,Noticias,Galeria,quadro_de_honra
from .form import FunciForm,FunciForm2,FormCurso,FormNoticia,UtilizadorFormAdmin,FormHonra,AlterarPassForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@login_required(login_url='bloquear')
def dashboard(request):
    data = {}
    data['n_funcionarios'] = Funcionario.objects.all().count()
    data['funcionarios'] = Funcionario.objects.all()
    data['n_aniversariantes'] = 0
    for dados in data['funcionarios']:
        if dados.data_de_nascimento.day==date.today().day and dados.data_de_nascimento.month==date.today().month:
            data['n_aniversariantes']=data['n_aniversariantes']+1
    data['n_cursos'] = cursos.objects.all().count()
    data['n_utilizador'] = User.objects.all().count()
    data['n_noticias'] = Noticias.objects.all().count()
    data['n_galeria'] = Galeria.objects.all().count()
    data['n_quadro_de_honra'] = quadro_de_honra.objects.all().count()
    return render(request,'painel.html',data)

def bloquear(request):
    if request.user.is_authenticated:
        messages.error(request, "Utilizador sem Permissão para aceder esta funcionalidade")
        return HttpResponseRedirect('dashboard')
    else:
        messages.info(request, "Deve aceder esta página fazendo login com as suas credencias")
        return HttpResponseRedirect('/')
    
def terminar(request):
    logout(request)
    return HttpResponseRedirect('/')

#add
@method_decorator(csrf_exempt, name="dispatch")
class UserCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = UtilizadorFormAdmin
    success_url = reverse_lazy('add_user')
    success_message = 'Utilizador %(username)s registado!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Utilizador'
        context['btn'] = 'Registar Utilizador'
        context['link'] = 'q_utilizadores'
        return  context   

@method_decorator(csrf_exempt, name="dispatch")
class Add_Funcionario(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FunciForm
    success_url = reverse_lazy('q_funcionarios')
    success_message = "Funcinário (%(nome_completo)s) registado!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Funcionário'
        context['btn'] = 'Registar Funcionário'
        context['link'] = 'q_funcionarios'
        return  context

@method_decorator(csrf_exempt, name="dispatch")
class Add_Funcionario2(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FunciForm2
    success_url = reverse_lazy('q_funcionarios')
    success_message = "Funcinário (%(nome_completo)s) registado!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Funcionário 2'
        context['btn'] = 'Registar Funcionário'
        context['link'] = 'q_funcionarios'
        return  context
    
@method_decorator(csrf_exempt, name="dispatch")
class Add_Curso(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FormCurso
    success_url = reverse_lazy('AddCurso')
    success_message = "Curso (%(nome_do_curso)s) registado"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Curso'
        context['btn'] = 'Registar Curso'
        context['link'] = 'q_cursos'
        return  context   
  
@method_decorator(csrf_exempt, name="dispatch")
class Add_noticias(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FormNoticia
    success_url = reverse_lazy('AddNoticia')
    success_message = "Notícia com titulo (%(titulo)s) registada"
    def form_valid(self, form):
        form.instance.utilizador = self.request.user
        url = super().form_valid(form)
        return url
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Notícia'
        context['btn'] = 'Registar Notícia'
        context['link'] = 'q_noticias'
        return  context   

@method_decorator(csrf_exempt, name="dispatch")
class Add_foto(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    model = Galeria
    fields = ['img','painel']
    template_name = 'form.html'
    success_url = reverse_lazy('Addfoto')
    success_message = "Fotografia adicionada à galeria"
    
    def form_valid(self, form):
        form.instance.utilizador = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Fotografia'
        context['btn'] = 'Adicionar Fotografia'
        context['link'] = 'q_galeria'
        return  context   

@method_decorator(csrf_exempt, name="dispatch")
class quadroHonra(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('bloquear')
    form_class = FormHonra
    template_name = 'form.html'
    success_url = reverse_lazy('AddquadroHonra')
    success_message = "Aluno foi registado na lista de destacados"
    
    def form_valid(self, form):
        form.instance.utilizador = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registar Aluno destacado'
        context['btn'] = 'Registar Aluno destacado'
        context['link'] = 'q_quadroH'
        return  context  
#edit
@method_decorator(csrf_exempt, name="dispatch")
class edit_Funcionario(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FunciForm
    success_url = reverse_lazy('q_funcionarios')
    success_message = 'Dados do Funcionário %(nome_completo)s actualizados!'
    
    def get_object(self, queryset=None):
        self.object = Funcionario.objects.get(pk=self.kwargs['fun_id'])
        return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar funcionário'
        context['link'] = 'q_funcionarios'
        context['btn'] = 'Actualizar dados'
        return  context
    
@method_decorator(csrf_exempt, name="dispatch")
class edit_Funcionario2(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FunciForm2
    success_url = reverse_lazy('q_funcionarios')
    success_message = 'Dados do Funcinário %(nome_completo)s actualizados!'
    
    def get_object(self, queryset=None):
        self.object = Funcionario.objects.get(pk=self.kwargs['fun_id'])
        return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar funcionário 2'
        context['link'] = 'q_funcionarios'
        context['btn'] = 'Actualizar dados'
        return  context

@method_decorator(csrf_exempt, name="dispatch")
class edit_curso(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FormCurso
    success_url = reverse_lazy('q_cursos')
    success_message = 'Dados do Curso %(nome_do_curso)s actualizados!'
    
    def get_object(self, queryset=None):
        self.object = cursos.objects.get(pk=self.kwargs['curso_id'])
        return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar dados do Curso'
        context['link'] = 'q_cursos'
        context['btn'] = 'Actualizar dados'
        return  context

@method_decorator(csrf_exempt, name="dispatch")
class EditUser(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    model = User
    fields = ['username','first_name','last_name','email']
    template_name = 'form.html'
    success_url = reverse_lazy('q_utilizadores')
    success_message = 'Dados do utilizador %(username)s actualizados!'

    def get_object(self, queryset=None):
       self.object = get_object_or_404(User, pk = self.kwargs['user_id'])
       return self.object
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualizar dados do Utilizador'
        context['link'] = 'q_utilizadores'
        context['btn'] = 'Actualizar dados'
        return context

@method_decorator(csrf_exempt, name="dispatch")
class edit_noticia(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = FormNoticia
    success_url = reverse_lazy('q_noticias')
    success_message = "Notícia com titulo (%(titulo)s) actualizada"
    
    def get_object(self, queryset=None):
        self.object = Noticias.objects.get(pk=self.kwargs['noti_id'])
        return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar dados da notícia'
        context['link'] = 'q_noticias'
        context['btn'] = 'Actualizar dados'
        return  context
    
@method_decorator(csrf_exempt, name="dispatch")
class edit_foto(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    model = Galeria
    fields = ['img','painel']
    template_name = 'form.html'
    success_url = reverse_lazy('q_galeria')
    success_message = "Fotografia actualizada"
    
    def get_object(self, queryset=None):
        self.object = Galeria.objects.get(pk=self.kwargs['foto_id'])
        return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar fotografia'
        context['link'] = 'q_galeria'
        context['btn'] = 'Actualizar'
        return  context

@method_decorator(csrf_exempt, name="dispatch")
class EditquadroHonra(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    model = quadro_de_honra
    fields = ['img','nome_do_aluno','idade','classe','curso','ano_lectivo','referencia','desc_notas','media_obtida']
    success_url = reverse_lazy('q_quadroH')
    success_message = "As alterações foram salvas"
    
    def get_object(self, queryset=None):
        self.object = quadro_de_honra.objects.get(pk=self.kwargs['alunod_id'])
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Aluno destacado'
        context['btn'] = 'Actualizar Aluno destacado'
        context['link'] = 'q_quadroH'
        return  context  
    
@method_decorator(csrf_exempt, name="dispatch")
class AlterarPassword(LoginRequiredMixin,SuccessMessageMixin,PasswordChangeView):
    login_url = reverse_lazy('bloquear')
    template_name = 'form.html'
    form_class = AlterarPassForm
    success_url = reverse_lazy('dashboard')
    success_message = 'Sua Palavra-Passe foi alterada'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Alterar Palavra Passe'
        context['btn'] = 'Salvar alterações'
        context['link'] = 'dashboard'
        return context

#View
@login_required(login_url='bloquear')
def q_cursos(request):
    data = {}
    data['titulo'] = 'Lista de Cursos'
    data['cursos'] = cursos.objects.all().order_by('nome_do_curso')
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def q_funcionarios(request):
    data = {}
    data['titulo'] = 'Lista de Funcionarios'
    data['funcionarios'] = Funcionario.objects.all().order_by('nome_completo')
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def q_utilizador(request):
    data = {}
    data['titulo'] = 'Lista de Utilizadores'
    data['utilizadores'] = User.objects.all().order_by('username')
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def q_noticia(request):
    data = {}
    data['titulo'] = 'Lista de Noticias'
    data['noticias'] = Noticias.objects.all().order_by('data')
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def q_galeria(request):
    data = {}
    data['titulo'] = 'Galeria'
    data['galeria'] = Galeria.objects.all()
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def Q_QuadroH(request):
    data = {}
    data['titulo'] = 'Quadro de Honra Admin'
    data['quadro_de_honra'] = quadro_de_honra.objects.all().order_by('-media_obtida')
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def Aniversariantes(request):
    data = {}
    data['titulo'] = 'Aniversariantes do dia '
    data['data'] = date.today()
    data['funcionari1'] = Funcionario.objects.filter()
    aniversariantes = []
    for dados in data['funcionari1']:
        if dados.data_de_nascimento.day==date.today().day and dados.data_de_nascimento.month==date.today().month:
            aniversariantes = dados
            data['aniversariantes'] = aniversariantes
    return render(request,'listar/listas.html',data)

@login_required(login_url='bloquear')
def d_funcionario_admin(request,fun_id):
    data = {}
    data['sessao'] = True
    data['funcionario'] = get_object_or_404(Funcionario,pk=fun_id)
    return render(request,'listar/detalhes_f2.html',data)

class perfil(LoginRequiredMixin, TemplateView):
     login_url = reverse_lazy('bloquear')
     template_name = 'listar/perfil.html'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['tempo_servico'] = relativedelta(date.today(), self.request.user.funcionario.data_de_ingresso)
         context['anos'] = context['tempo_servico'].years
         context['meses'] = context['tempo_servico'].months
         context['semanas'] = context['tempo_servico'].weeks
         context['dias'] = context['tempo_servico'].days
         return context
#eliminar
@login_required(login_url='bloquear')
def elim_curso(request,curso_id):
    curso = cursos.objects.get(pk=curso_id)
    curso.delete()
    messages.success(request,'Curso Eliminado')
    return HttpResponseRedirect('/q_cursos')

@login_required(login_url='bloquear')
def elim_f(request,fun_id):
    funcionario = Funcionario.objects.get(pk=fun_id)
    funcionario.delete()
    messages.success(request,'Funcionário Eliminado')
    return HttpResponseRedirect('/q_funcionarios')

@login_required(login_url='bloquear')
def elim_user(request,user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    messages.success(request,'Utilizador Eliminado')
    return HttpResponseRedirect('/q_utilizadores')

@login_required(login_url='bloquear')
def elim_noti(request,noti_id):
    noticia = Noticias.objects.get(pk=noti_id)
    noticia.delete()
    messages.success(request,'Notícia Eliminada')
    return HttpResponseRedirect('/q_noticias')

@login_required(login_url='bloquear')
def elim_foto(request,foto_id):
    foto = Galeria.objects.get(pk=foto_id)
    foto.delete()
    messages.success(request,'Foto Eliminada')
    return HttpResponseRedirect('/q_galeria')

@login_required(login_url='bloquear')
def elim_alunod(request,alunod_id):
    foto = quadro_de_honra.objects.get(pk=alunod_id)
    foto.delete()
    messages.success(request,'Aluno destacado Eliminado')
    return HttpResponseRedirect('/q_quadroH')