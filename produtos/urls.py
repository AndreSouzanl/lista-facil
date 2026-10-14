
from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("novo/", views.criar_produto, name="criar"),
    path("<int:produto_id>/editar/", views.editar_produto, name="editar"),
    path("<int:produto_id>/excluir/", views.excluir_produto, name="excluir"),
    path("<int:produto_id>/comprado/", views.alternar_comprado, name="comprado"),
    path("<int:produto_id>/reativar/",views.reativar_produto,name="reativar"),
]
