from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "quantidade",
        "unidade",
        "status",
        "criado_por",
        "data_cadastro",
    )

    list_filter = ("status", "unidade")
    search_fields = ("nome", "descricao")
