from django.db import models
from django.contrib.auth.models import User

# Create your models here.
choices_estado = (
    ('Solteiro(a)','Solteiro(a)'),
    ('Casado(a)','Casado(a)'),
    ('Divorcio(a)','Divorcio(a)'),
)

choices_nivel_ac = (
    ('Técnico Médio','Técnico Médio'),
    ('Licenciado(a)','Licenciado(a)'),
    ('Mestre','Mestre'),
    ('Phd','Phd'),
)

choices_funcao = {
    ('Director','Director'),
    ('Subdirector Pedagógico','Subdirector Pedagógico'),
    ('Subdirector Administrativo','Subdirector Administrativo'),
    ('Chefe da Secretaria Geral','Chefe da Secretaria Geral'),
    ('Chefe da Secretaria Pedagógica','Chefe da Secretaria Pedagógica'),
    ('Coordenador(a) do Curso','Coordenador(a) do Curso'),
    ('Coordenador(a) de Disciplina','Coordenador(a) de Disciplina'),
    ('Professor(a)','Professor(a)'),
    ('Funcionário(a) Administrativo(a)','Funcionário(a) Administrativo(a)'),
    ('Funcionário(a) Auxiliar','Funcionário(a) Auxiliar'),
}
choices_categoria={
    ('Professor Auxiliar Do 1º Grau','Professor Auxiliar Do 1º Grau'),
    ('Professor Auxiliar Do 2º Grau','Professor Auxiliar Do 2º Grau'),
    ('Professor Auxiliar Do 3º Grau','Professor Auxiliar Do 3º Grau'),
    ('Professor Auxiliar Do 4º Grau','Professor Auxiliar Do 4º Grau'),
    ('Professor Auxiliar Do 5º Grau','Professor Auxiliar Do 5º Grau'),
    ('Professor Auxiliar Do 6º Grau','Professor Auxiliar Do 6º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 1.º Grau','Professor Do Ens. Prim. E Sec. Do 1º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 2.º Grau','Professor Do Ens. Prim. E Sec. Do 2º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 3.º Grau','Professor Do Ens. Prim. E Sec. Do 3º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 4.º Grau','Professor Do Ens. Prim. E Sec. Do 4º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 5.º Grau','Professor Do Ens. Prim. E Sec. Do 5º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 6.º Grau','Professor Do Ens. Prim. E Sec. Do 6º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 7.º Grau','Professor Do Ens. Prim. E Sec. Do 7º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 8.º Grau','Professor Do Ens. Prim. E Sec. Do 8º Grau'),
    ('Prof. Do Ens. Prim. E Sec. Do 9.º Grau','Professor Do Ens. Prim. E Sec. Do 9º Grau'),
    ('Professor Do Ens. Prim. E Sec. Do 10º Grau','Professor Do Ens. Prim. E Sec. Do 10º Grau'),
    ('Professor Do Ens. Prim. E Sec. Do 11º Grau','Professor Do Ens. Prim. E Sec. Do 11º Grau'),
    ('Professor Do Ens. Prim. E Sec. Do 12º Grau','Professor Do Ens. Prim. E Sec. Do 12º Grau'),
    ('Professor Do Ens. Prim. E Sec. Do 13º Grau','Professor Do Ens. Prim. E Sec. Do 13º Grau'),
}
class Funcionario(models.Model):
    foto = models.ImageField(upload_to='img', verbose_name="Foto Tipo Passe")
    arquivo = models.FileField(verbose_name='Bilhete de Identidade (Anexo)', upload_to='pdf')
    nAgente = models.CharField(max_length=9,verbose_name='Número de Agente', unique=True)
    nome_completo = models.CharField(max_length=150)
    estado_civil = models.CharField(choices=choices_estado, max_length=50)
    numero_do_bilhete = models.CharField(max_length=14,unique=True,verbose_name='Número do Bilhete')
    data_de_emissao = models.DateField()
    data_de_nascimento = models.DateField()
    local_de_nascimento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=100, verbose_name='Município')
    provincia = models.CharField(max_length=100, verbose_name='Província')
    residencia = models.CharField(max_length=100, verbose_name='Residência')
    contacto = models.CharField(max_length=18,unique=True)
    email = models.EmailField(unique=True)
    nivel_academico = models.CharField(max_length=100,choices=choices_nivel_ac)
    especialidade = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100, verbose_name='Instituição de formação')
    data_de_ingresso = models.DateField()
    categoria = models.CharField(max_length=150, choices=choices_categoria)
    funcao = models.CharField(choices=choices_funcao,max_length=32,verbose_name='Função')
    disciplina = models.CharField(max_length=300,verbose_name='Disciplina ou Curso', null=True)
    dados_academicos = models.TextField(default='nulo',verbose_name='Dados académicos (Colocar (nulo) caso não haver dados à declarar)')
    dados_profissionais = models.TextField(default='nulo', verbose_name='Dados profissionais (Colocar (nulo) caso não haver dados à declarar)')
    utilizador = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.nAgente,self.nome_completo)
    
class cursos(models.Model):
    figura = models.ImageField(upload_to='img')
    nome_do_curso = models.CharField(max_length=100,unique=True)
    sigla = models.CharField(max_length=20)
    perfil_de_entrada = models.TextField()
    perfil_de_saida = models.TextField()
    classe_10 = models.TextField(verbose_name='Disciplinas da 10ª Classe')
    classe_11 = models.TextField(verbose_name='Disciplinas da 11ª Classe')
    classe_12 = models.TextField(verbose_name='Disciplinas da 12ª Classe')
    duracao = models.CharField(max_length=10,verbose_name='Duração')
    total_disc = models.IntegerField(verbose_name='Total de Disciplinas do Curriculo')

    def __str__(self) -> str:
        return("{}".format(self.nome_do_curso))
    
class Noticias(models.Model):
    figura = models.ImageField(upload_to='img')
    titulo = models.CharField(max_length=500, unique=True)
    texto = models.TextField()
    data = models.DateTimeField(auto_now=True)
    utilizador = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ("{} - {}".format(self.titulo, self.data))

choices_painel = (
    ('Principal','Principal'),
    ('Acima','Acima'),
    ('Abaixo','Abaixo'),
)

class Galeria(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='Fotografia')
    painel = models.CharField(choices=choices_painel,max_length=20)
    utilizador = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ("{} - {}".format(self.img, self.painel))

class quadro_de_honra(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='Fotografia do aluno')
    nome_do_aluno = models.CharField(max_length=100)
    idade = models.CharField(max_length=20)
    classe = models.CharField(max_length=20,verbose_name='Classe que frequenta')
    curso = models.ForeignKey(cursos,on_delete=models.CASCADE, verbose_name='Curso que frequenta')
    ano_lectivo = models.CharField(max_length=20)
    choices_ref =   (
        ('Iº Trimestre','Iº Trimestre'),
        ('IIº Trimestre','IIº Trimestre'),
        ('IIIº Trimestre','IIIº Trimestre'),
        ('Anual','Anual'),
    )
    referencia = models.CharField(choices=choices_ref,max_length=20,verbose_name='Referência da avaliação')
    desc_notas = models.TextField(verbose_name='Descrição das notas')
    media_obtida = models.IntegerField(verbose_name='Média Obtida')
    data = models.DateTimeField(auto_now=True)
    utilizador = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return ("{} - {} - {} - {} - {}".format(self.nome_do_aluno, self.classe, self.curso, self.referencia, self.media_obtida))


class Provincias(models.Model):
    provincia = models.CharField(max_length=100, unique=True) 
    def __str__(self):
        return "{}".format(self.provincia)

class Municipios(models.Model):
    municipio = models.CharField(max_length=100,unique=True)
    Provincia = models.ForeignKey(Provincias, on_delete=models.PROTECT)
    def __str__(self):
        return "{}".format(self.municipio)

