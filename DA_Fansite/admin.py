from django.contrib import admin

# Register your models here.
from .models import Personagem, Classe, ReferenciasPersonagem

@admin.register(Personagem)
class AdminPersonagem(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'raca','idade', 'data_criacao']
    ordering = ['idade']

@admin.register(Classe)
class AdminClasse(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'tipo', 'quantidade_especializacoes']
    ordering = ['nome']

@admin.register(ReferenciasPersonagem)
class AdminReferencias(admin.ModelAdmin):
    list_display = ['nome', 'personagem', 'link', 'classe', 'data_atualizacao']
    ordering = ['personagem']
    list_filter = ['classe']