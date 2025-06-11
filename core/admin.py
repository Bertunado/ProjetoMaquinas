from django.contrib import admin
from .models import Peca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'adicionada_por', 'maquina','adicionada_em')  # campos para aparecer na lista do banco de dados