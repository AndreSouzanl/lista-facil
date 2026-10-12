from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CadastroUsuarioForm


def cadastrar(request):
    if request.user.is_authenticated:
        return redirect("produtos:lista")

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            messages.success(
                request,
                "Conta criada com sucesso! Bem-vindo ao ListaFácil.",
            )

            return redirect("produtos:lista")
    else:
        form = CadastroUsuarioForm()

    return render(
        request,
        "usuarios/cadastro.html",
        {"form": form},
    )
