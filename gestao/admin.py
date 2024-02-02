from django.contrib import admin
from .models import Funcionario,cursos,Noticias,Galeria,quadro_de_honra,Provincias,Municipios
# Register your models here.
admin.site.register(cursos)
admin.site.register(Funcionario)
admin.site.register(Noticias)
admin.site.register(Galeria)
admin.site.register(quadro_de_honra)
admin.site.register(Municipios)
admin.site.register(Provincias)