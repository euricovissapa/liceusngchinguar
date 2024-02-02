from django.forms import fields,ModelForm
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime,date
from .models import Funcionario,cursos,Noticias,Galeria,quadro_de_honra

class UtilizadorFormAdmin(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100,label='Primeiro Nome')
    last_name = forms.CharField(max_length=100,label='Último Nome')
    class Meta():
        model = User
        fields = ['username','email','first_name','last_name']

class AlterarPassForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

class FunciForm(forms.ModelForm):
    disciplina = forms.CharField(required=False,help_text='Este campo deve ser preenchido apenas para professores e coordenadores')
    data_de_emissao = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)
    data_de_nascimento = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)
    data_de_ingresso = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)

    class Meta():
        model = Funcionario
        fields = '__all__'

    def clean_nAgente(self):
        agente = self.cleaned_data['nAgente']
        if len(agente)<8:
            raise ValidationError('O número de agente deve conter 9 dígitos')
        return agente

    def clean_data_de_nascimento(self):
        data_de_nascimento = self.cleaned_data['data_de_nascimento']
        anos = relativedelta(date.today(), data_de_nascimento)
        if anos.years < 18:
            raise ValidationError('Não é permitido neste ambiente funcionários menores de 18 anos de idade')
        return data_de_nascimento

    def clean_data_de_emissao(self):
        data_de_emissao = self.cleaned_data['data_de_emissao']
        if data_de_emissao > date.today():
            raise ValidationError('A data de emissão do B.I não podem ser superior a data actual')
        return data_de_emissao

    def clean_data_de_ingresso(self):
        data_de_ingresso = self.cleaned_data['data_de_ingresso']
        if data_de_ingresso > date.today():
            raise ValidationError('A data de ingresso não podem ser superior a data actual')
        return data_de_ingresso

    def clean_numero_do_bilhete(self):
        bi = self.cleaned_data['numero_do_bilhete']
        if len(bi)<14:
            raise ValidationError('O número de bilhete deve conter 14 carácteres')
        if bi[9].islower() or bi[10].islower():
            raise ValidationError('As letras "{}{}" devem ser todas maísculas'.format(bi[9],bi[10]))
        return bi

    def clean_contacto(self):
        contacto = self.cleaned_data['contacto']
        if len(contacto)<18:
            raise ValidationError('O número de telefone deve conter 9 dígitos')
        return contacto

class FunciForm2(forms.ModelForm):
    disciplina = forms.CharField(required=False,help_text='Este campo deve ser preenchido apenas para professores e coordenadores')
    data_de_emissao = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)
    data_de_nascimento = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)
    data_de_ingresso = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date',}),input_formats=('%Y-%m-%d',),)


    class Meta():
        model = Funcionario
        fields = ['foto','arquivo','nAgente','nome_completo','estado_civil','numero_do_bilhete','data_de_emissao','data_de_nascimento','local_de_nascimento','municipio','provincia','residencia','contacto','email','nivel_academico','especialidade','instituicao','data_de_ingresso','categoria','funcao','disciplina','dados_academicos','dados_profissionais']

    def clean_nAgente(self):
        agente = self.cleaned_data['nAgente']
        if len(agente)<8:
            raise ValidationError('O número de agente deve conter 9 dígitos')
        return agente

    def clean_data_de_nascimento(self):
        data_de_nascimento = self.cleaned_data['data_de_nascimento']
        anos = relativedelta(date.today(), data_de_nascimento)
        if anos.years < 18:
            raise ValidationError('Não é permitido neste ambiente funcionários menores de 18 anos de idade')
        return data_de_nascimento

    def clean_data_de_emissao(self):
        data_de_emissao = self.cleaned_data['data_de_emissao']
        if data_de_emissao > date.today():
            raise ValidationError('A data de emissão do B.I não podem ser superior a data actual')
        return data_de_emissao

    def clean_data_de_ingresso(self):
        data_de_ingresso = self.cleaned_data['data_de_ingresso']
        if data_de_ingresso > date.today():
            raise ValidationError('A data de ingresso não podem ser superior a data actual')
        return data_de_ingresso

    def clean_numero_do_bilhete(self):
        bi = self.cleaned_data['numero_do_bilhete']
        if len(bi)<14:
            raise ValidationError('O número de bilhete deve conter 14 carácteres')
        if bi[9].islower() or bi[10].islower():
            raise ValidationError('As letras "{}{}" devem ser todas maísculas'.format(bi[9],bi[10]))
        return bi

    def clean_contacto(self):
        contacto = self.cleaned_data['contacto']
        if len(contacto)<18:
            raise ValidationError('O número de telefone deve conter 9 dígitos')
        return contacto

class FormCurso(forms.ModelForm):
    class Meta:
        model = cursos
        fields = '__all__'


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['figura','titulo','texto']
    def clean_contacto(self):
        titulo = self.cleaned_data['titulo']
        if Noticias.objects.filter(titulo=titulo).exists():
            raise ValidationError('Já existe notícia com este titulo')
        return titulo

class FormHonra(forms.ModelForm):
    class Meta:
        model = quadro_de_honra
        fields = ['img','nome_do_aluno','idade','classe','curso','ano_lectivo','referencia','desc_notas','media_obtida']
    def clean(self):
        cl = self.cleaned_data['classe']
        c = self.cleaned_data['curso']
        a = self.cleaned_data['ano_lectivo']
        r = self.cleaned_data['referencia']
        if quadro_de_honra.objects.filter(classe=cl, curso=c, ano_lectivo=a,referencia=r).exists():
            raise ValidationError('Já existe um aluno no quadro de honra com os mesmos dados')
        return self.cleaned_data
