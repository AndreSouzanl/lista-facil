
from django.urls import path

from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("novo/", views.criar_produto, name="criar"),
]
