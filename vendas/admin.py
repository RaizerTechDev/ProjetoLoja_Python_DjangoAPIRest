### Depois do models registrar aqui no admin

from django.contrib import admin
from .models import Categoria, Produto, Avaliacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   list_display = ('descricao', 'criacao', 'atualizacao')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'avaliador', 'email', 'nota')







