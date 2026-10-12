
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProdutoForm
from .models import Produto


@login_required
def lista(request):
    produtos = Produto.objects.filter(
        criado_por=request.user,
        status__in=[
            Produto.Status.ATIVO,
            Produto.Status.EDITADO,
            Produto.Status.FINALIZADO,
        ],
    )

    return render(
        request,
        "produtos/lista.html",
        {"produtos": produtos},
    )


@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.criado_por = request.user
            produto.save()

            messages.success(
                request,
                "Produto adicionado à sua lista com sucesso!",
            )

            return redirect("produtos:lista")
    else:
        form = ProdutoForm()

    return render(
        request,
        "produtos/formulario.html",
        {"form": form},
    )
